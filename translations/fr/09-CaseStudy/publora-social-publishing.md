# Étude de cas : Publication sur les réseaux sociaux depuis un agent avec un serveur MCP à distance

> **Avertissement :** Plusieurs services et projets open-source peuvent publier sur les réseaux sociaux, et une équipe pourrait également intégrer directement l'API de chaque réseau. Le scénario ci-dessous est fourni comme un exemple concret de la façon dont un **serveur MCP à distance capable d'écrire** peut être conçu et utilisé. Publora est un service commercial avec un niveau gratuit ; les modèles décrits ici s'appliquent à tout serveur MCP qui effectue des actions irréversibles au nom d'un utilisateur.

## Vue d'ensemble

Les agents sont bons pour rédiger du contenu et mauvais pour le diffuser. Un modèle peut écrire une annonce de communiqué en quelques secondes, puis le travail s’arrête : publier signifie une API par réseau, une application OAuth par réseau, et un ensemble différent de règles médias pour chacun. La plupart des équipes résolvent ce problème en copiant le texte manuellement dans un navigateur.

Cette étude de cas examine comment cette dernière étape est réalisée avec un serveur MCP à distance unique, et — plus utile pour toute personne construisant un tel serveur — les décisions de conception qu’un serveur **capable d’écrire** doit bien prendre. La lecture des données est indulgente. La publication ne l’est pas : un appel d’outil erroné est visible par un public et ne peut pas être annulé.

## Scénario

Une petite équipe de relations développeurs rédige des publications dans un agent (Claude, VS Code, Cursor — le client importe peu). Ils veulent que l’agent :

- voie quels comptes sociaux l’équipe a connectés,
- rédige une publication et la conserve comme brouillon pour approbation humaine,
- attache une image,
- la programme pour plusieurs réseaux à un moment choisi,
- et rapporte plus tard ses performances.

Crucialement, ils veulent que l’agent soit *incapable* de publier par accident pendant leurs expérimentations.

## Outils utilisés

- [Publora MCP Server](https://github.com/publora/mcp-server) — un serveur MCP à distance (`streamable-http`) exposant des outils de publication, de programmation, de médias et d’analyse LinkedIn. Enregistré dans le registre MCP officiel sous `com.publora/mcp-server`.

## Flux de travail étape par étape

1. **Connecter le serveur.** Les clients qui utilisent OAuth complètent le flux d’autorisation par code avec PKCE via l’écran de consentement du serveur ; les clients qui ne le font pas, comme les CLI sans interface, utilisent une clé API Publora dans un header. Les deux méthodes sont supportées, et celle utilisée dépend du client, pas du serveur.
2. **Lister les connexions.** L’agent appelle `list_connections` et reçoit les comptes connectés avec leurs identifiants.
3. **Rédiger.** L’agent appelle `create_post` *sans* heure programmée. La publication est enregistrée comme brouillon — rien n’est publié.
4. **Attacher des médias.** Les URLs publiques d’image sont transmises dans le même appel ; le serveur les télécharge et les valide.
5. **Programmer.** Après approbation humaine, `update_post` passe le statut à programmé avec une heure au format ISO 8601.
6. **Mesurer.** Pour LinkedIn, `linkedin_post_stats` renvoie l’engagement une fois la publication en ligne.

## Exemple de prompt

```text
Which social accounts do I have connected?
Draft a post announcing our new changelog page, attach the screenshot at
https://example.com/changelog.png, and keep it as a draft — do not publish it.
Once I approve, schedule it to LinkedIn and Bluesky for tomorrow at 09:00 UTC.
```

## Diagramme Mermaid

```mermaid
flowchart TD
    A[Invite utilisateur dans un client MCP] --> B[Le client effectue OAuth avec le serveur]
    B --> C[list_connections]
    C --> D{Réseaux cibles connectés ?}
    D -- No --> E[L'agent rapporte ceux qui manquent]
    D -- Yes --> F[create_post sans scheduledTime -> brouillon]
    F --> G[L'humain révise le brouillon]
    G -- Approved --> H[update_post: status=scheduled]
    G -- Rejected --> I[delete_post]
    H --> J[Le serveur publie à l'heure prévue]
    J --> K[linkedin_post_stats pour engagement]
```

## Implémentation technique

Les leçons ci-dessous sont la partie transférable de cette étude de cas.

### Découverte ouverte, exécution authentifiée

`tools/list` est servi sans authentification ; chaque `tools/call` requiert un token
et renvoie sinon un `401` avec un header `WWW-Authenticate` pointant vers les
métadonnées de la ressource protégée. L’ancien endpoint du serveur répond aussi à une
requête non authentifiée `initialize` pour les clients en versions de protocole avant
`2026-07-28` ; les clients actuels n’utilisent pas cette poignée de main.

Cette séparation spécifique au serveur permet aux registres, catalogues et clients d’inspecter les noms,
schémas, et annotations des outils sans secret tout en empêchant l’exécution anonyme.
La découverte ouverte est un choix de déploiement, non une exigence MCP ; un
déploiement protégé peut aussi exiger une autorisation pour `tools/list`.

### Enregistrement : enregistrement dynamique des clients, et ce qui le remplace

Le serveur annonce `/.well-known/oauth-protected-resource` et `/.well-known/oauth-authorization-server`, et supporte le flux de code d’autorisation avec PKCE (`S256`), les tokens de rafraîchissement, et **l’enregistrement dynamique des clients**.

L’enregistrement dynamique a supprimé l’étape manuelle pour les clients hérités : sans lui,
chaque client avait besoin d’un `client_id` pré-émis par le fournisseur.

Considérez ceci comme un comportement de compatibilité plutôt que comme un modèle à copier. La révision `2026-07-28` de la spécification déprécie l’enregistrement dynamique au profit des Documents de Métadonnées Client, où le client héberge un document de métadonnées à une URL HTTPS stable et cette URL *est* le `client_id`. DCR continue à fonctionner pour l’instant, mais un serveur construit aujourd’hui devrait prévoir CIMD et garder DCR uniquement pour les clients plus anciens.

### Les annotations des outils ne sont pas une décoration

Chaque outil porte un `title` et les hints applicables : `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`.

Deux raisons pour les valoriser. Premièrement, les clients utilisent les hints pour décider ce qu’ils doivent confirmer avec l’utilisateur — un client peut exécuter automatiquement une consultation en lecture seule et s’arrêter pour approbation avant une suppression. La spécification précise que les annotations sont des hints non fiables, non un mécanisme d’autorisation : elles orientent ce qu’un client propose de faire, elles ne bloquent rien sur le serveur, qui doit toujours appliquer ses propres règles. Deuxièmement, les principaux annuaires de connecteurs *exigent* désormais ces annotations pour la revue ; un serveur dont les outils manquent de titres et de hints sera automatiquement rejeté, peu importe leur performance.

### Rendre les identifiants impossibles à inventer

Les identifiants des plateformes sont des chaînes opaques retournées par `list_connections`, et la description du schéma précise explicitement qu’ils doivent être copiés à l’identique et jamais devinés. Le serveur refuse tout autre cas.

Les modèles sont des devineurs habiles. Tout serveur capable d’écrire doit partir du principe qu’un identifiant sera finalement halluciné et faire échouer ce chemin fort et tôt, plutôt que d’agir sur une valeur plausible.

### Échouer avant la publication, avec un message exploitable

Certains réseaux refusent les publications en texte seul et exigent une image ou vidéo. Cela est validé lorsque la publication est programmée, et l’erreur mentionne la plateforme et l’exigence manquante.

Un agent peut récupérer d’un « Instagram exige un média — attachez une image ou une vidéo » sans aller-retour supplémentaire. Il ne peut pas récupérer d’un `400` générique.

### Rendre les nouvelles tentatives sûres

Les deux outils qui créent du contenu, `create_post` et `update_post`, acceptent une clé d’idépotence : la réutiliser avec la même requête rejoue la réponse originale au lieu de créer une seconde publication. Les environnements d’exécution d’agents réessaient sur timeout ; sans idépotence, une réponse lente devient une publication en double. Les autres outils d’écriture — suppressions, étapes média, réactions et commentaires LinkedIn — n’en prennent pas, donc un réessai là n’est pas automatiquement sûr. Il est utile de savoir quelles mutations sont protégées et lesquelles ne le sont pas.

### Fournir un moyen de tester sans rien publier


Le serveur accepte une cible réservée, `publora-playground`, qui est validée et reconnue comme une destination réelle puis rejetée — rien n'atteint un compte réel. Elle est décrite dans le schéma de l'outil lui-même, que tout client peut lire sans identifiants : le champ `platforms` de `create_post` la décrit comme "une cible de test de connexion qui ne nécessite aucune connexion réelle — le message est reconnu puis rejeté, rien n'est publié". Appelez-la en la passant comme unique entrée : `platforms: ["publora-playground"]`.

Cela s'est avéré être l’un des détails les plus utiles de toute la surface. Les réviseurs des annuaires de connecteurs, les contributeurs et l’intégration continue peuvent exercer le chemin d’écriture complet de bout en bout sans risque pour un véritable public. Tout serveur MCP avec des actions irréversibles bénéficie d'une cible no-op documentée.

## Résultats et Impact

- L’étape de publication est passée d’un navigateur à la même conversation où le contenu est écrit, et une habitude de brouillon en premier garde un humain dans la boucle. Soyez précis sur ce que cela signifie : un brouillon est une convention, pas une frontière. Le même identifiant peut planifier ou publier, donc toute personne nécessitant une véritable validation doit l’appliquer en dehors de la surface de l’outil — des identifiants séparés, ou une couche de politique devant le serveur.
- Les différences par réseau — exigences médias, hiérarchisation, contrôles de réponse — sont gérées une fois dans le serveur au lieu d’être répétées dans chaque agent qui s’y connecte.
- Le même serveur soutient plusieurs clients MCP sans identifiants pré-émis.
    Les clients actuels peuvent utiliser des Documents Métadonnées Client ; DCR reste une solution de secours
    pour les clients plus anciens.
- Les contraintes de conception ci-dessus ont été formées autant par les revues des annuaires de connecteurs que par les utilisateurs : annotations, OAuth et une cible de test sécurisée étaient chacune requises par au moins un d’entre eux.

## Références

- [Serveur Publora MCP (source)](https://github.com/publora/mcp-server)
- [Documentation Publora API et MCP](https://docs.publora.com)
- [Entrée registre MCP : `com.publora/mcp-server`](https://registry.modelcontextprotocol.io/v0/servers?search=com.publora/mcp-server)
- [Spécification MCP — Autorisation](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [Spécification MCP — Annotations d’outil](https://modelcontextprotocol.io/docs/concepts/tools)

## Prochaines étapes

- Prenez un serveur MCP que vous construisez et vérifiez ici les trois gains les moins coûteux : annotations sur chaque outil, une clé d’atomicité sur chaque écriture, et une cible no-op documentée.
- Essayez la séparation découverte ouverte : appelez `tools/list` sur un serveur distant public sans identifiants, puis appelez un outil et inspectez le défi `401`.
- Considérez ce que signifie "annuler" dans votre domaine. La publication a des brouillons et des suppressions ; si vos actions n’ont pas d’équivalent, la confirmation appartient à la conception de l’outil, pas à la demande.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->