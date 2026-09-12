# MCP koreňové adresáre (zastaralá funkcia)

> [!WARNING]
> Koreňové adresáre sú zastarané od verzie MCP `2026-07-28`. V tejto revízii sú ponechané pre
> kompatibilitu a môžu byť odstránené v prvej revízii špecifikácie
> vydanej dňa alebo po 28. júli 2027. Nové implementácie by mali adresáre alebo súbory odovzdávať cez
> parametre nástroja, URI zdrojov alebo konfiguráciu servera.


## Prehľad

Koreňové adresáre umožňujú klientovi MCP oznámiť serveru, ktoré umiestnenia v súborovom systéme sú relevantné
pre aktuálnu požiadavku. Koreň obsahuje povinné URI začínajúce na `file://` a voliteľný
ľudsky čitateľný názov.

Koreňové adresáre sú informatívne tipy. Nie sú kontajnermi histórie konverzácie,
protokolovými reláciami ani mechanizmom kontroly prístupu. Protokol nevyžaduje,
aby server zostal v rámci uvedených koreňov.

## Výučbové ciele

Na konci tejto lekcie budete schopní:

- Vysvetliť, čo koreňové adresáre MCP predstavujú a čo nepredstavujú.
- Rozpoznať aktuálny viackrokový tok `roots/list`.
- Použiť bezpečnostné kontroly nezávisle od koreňov.
- Migráciu nových implementácií na podporované alternatívy.

## Dáta koreňov

Klient vracia každý koreň ako URI začínajúce `file://` s voliteľným zobrazovaným menom:

```json
{
  "roots": [
    {
      "uri": "file:///home/user/projects/weather-service",
      "name": "Weather Service"
    }
  ]
}
```

Klienti by mali sprístupňovať iba miesta schválené používateľom. Servery by mali výsledok vnímať
ako usmernenie o relevantných súboroch, nie ako dôkaz autorizácie.

## Tok MCP 2026-07-28

Klient, ktorý podporuje Koreňové adresáre, deklaruje túto schopnosť v každej požiadavke:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Počas spracovania požiadavky klienta môže server vrátiť
`InputRequiredResult` obsahujúci vstupnú požiadavku `roots/list`:

```json
{
  "resultType": "input_required",
  "inputRequests": {
    "workspaceRoots": {
      "method": "roots/list"
    }
  },
  "requestState": "opaque-state-from-server"
}
```

Klient zhromaždí schválené koreňové adresáre a zopakuje pôvodnú požiadavku s príslušnými `inputResponses` a nezmeneným `requestState`.
Tento viackrokový vzor udržiava protokol bezstavový; neexistuje handshake `initialize` alebo
protokolová relácia.


## Zastaralé správanie 2025-11-25

V MCP `2025-11-25` klienti oznamovali Koreňové adresáre počas inicializácie. Server mohol priamo
požiadať o `roots/list` a klient mohol poslať
`notifications/roots/list_changed`, keď sa jeho koreňové adresáre zmenili.

Tento životný cyklus je zastarané správanie. Nekombinujte jeho príklady inicializácie alebo
oznámení s implementáciou `2026-07-28`.

## Odporúčané náhrady

### Parametre nástroja

Vyjadrite povinný adresár alebo súbor explicitne v schéme nástroja:

```json
{
  "name": "analyze_project",
  "inputSchema": {
    "type": "object",
    "properties": {
      "projectDirectory": {
        "type": "string",
        "description": "Approved project directory to analyze"
      }
    },
    "required": ["projectDirectory"]
  }
}
```

### URI zdrojov

Použite zdroje MCP, ak server môže sprístupniť relevantné súbory cez stabilné
URI. To udržuje objavovanie a získavanie explicitné.

### Konfigurácia servera

Pri pevných nasadeniach nakonfigurujte povolené adresáre pri spustení servera.
To je často jasnejšie než ich zisťovanie počas volania nástroja.

## Bezpečnostné požiadavky

Nech si zvolíte ktorúkoľvek náhradu:

- Získajte súhlas používateľa pred sprístupnením umiestnení v súborovom systéme.
- Kanonizujte a validujte cesty, aby ste zabránili prechádzaniu mimo povolené miesta.
- Vynútite autorizáciu a sandboxing nezávisle od hodnôt koreňov.
- Skontrolujte oprávnenia pri prístupe k súboru, nielen pri jeho zoznamovaní.
- Vyhnite sa vracaniu citlivých ciest v logoch alebo chybových správach.

## Kľúčové závery

- Koreňové adresáre popisujú relevantné umiestnenia v súborovom systéme; neukladajú stav konverzácie.

- Koreňové adresáre sú usmernením, nie hranicou kontroly prístupu.
- MCP `2026-07-28` prenáša schopnosť pre každú požiadavku a používa
  `InputRequiredResult` pre `roots/list`.
- Nové implementácie by mali namiesto toho používať parametre nástroja, URI zdrojov alebo konfiguráciu
  servera.

## Dodatočné zdroje

- [Koreňové adresáre v MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Register zastaraných funkcií](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [Čo sa zmenilo v MCP: Špecifikácia 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->