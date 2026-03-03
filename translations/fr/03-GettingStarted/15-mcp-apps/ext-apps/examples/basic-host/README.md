# Exemple : Hôte de base

Une implémentation de référence montrant comment construire une application hôte MCP qui se connecte à des serveurs MCP et affiche des interfaces utilisateur d'outils dans un bac à sable sécurisé.

Cet hôte de base peut également être utilisé pour tester des applications MCP pendant le développement local.

## Fichiers clés

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - Hôte UI React avec sélection d'outil, saisie de paramètres et gestion des iframes
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Proxy iframe externe avec validation de sécurité et relais bidirectionnel des messages
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Logique principale : connexion au serveur, appel d'outil et configuration d'AppBridge

## Commencer

```bash
npm install
npm run start
# Ouvrir http://localhost:8080
```

Par défaut, l'application hôte tentera de se connecter à un serveur MCP à `http://localhost:3001/mcp`. Vous pouvez configurer ce comportement en définissant la variable d'environnement `SERVERS` avec un tableau JSON d'URL de serveurs :

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Architecture

Cet exemple utilise un modèle de bac à sable double iframe pour une isolation sécurisée de l'interface utilisateur :

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Pourquoi deux iframes ?**

- L'iframe externe s'exécute sur une origine distincte (port 8081) empêchant l'accès direct à l'hôte
- L'iframe interne reçoit du HTML via `srcdoc` et est restreinte par des attributs sandbox
- Les messages passent par l'iframe externe qui les valide et les relaie bidirectionnellement

Cette architecture garantit que même si le code UI de l'outil est malveillant, il ne peut pas accéder au DOM de l'application hôte, aux cookies ou au contexte JavaScript.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source officielle. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->