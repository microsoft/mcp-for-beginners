Her er et eksempel som demonstrerer MCP App

## Installer 

1. Naviger til *mcp-app* mappen
1. Kjør `npm install`, dette skal installere frontend- og backend-avhengigheter

Verifiser at backend kompilerer ved å kjøre:

```sh
npx tsc --noEmit
```

Det skal ikke være noe output hvis alt er i orden.

## Kjør backend

> Dette krever litt ekstra arbeid hvis du bruker en Windows-maskin siden MCP Apps-løsningen bruker `concurrently` biblioteket som kjører, som du må finne et alternativ for. Her er den problematiske linjen i *package.json* i MCP App:

```json
"start": "concurrently \"cross-env NODE_ENV=development INPUT=mcp-app.html vite build --watch\" \"tsx watch main.ts\""
```

Denne appen har to deler, en backend-del og en host-del.

Start backend ved å kalle:

```sh
npm start
```

Dette skal starte backend på `http://localhost:3001/mcp`. 

> Merk, hvis du er i en Codespace, må du kanskje sette port-synlighet til offentlig. Sjekk at du kan nå endepunktet i nettleseren via https://<name av Codespace>.app.github.dev/mcp

## Valg -1 Test appen i Visual Studio Code

For å teste løsningen i Visual Studio Code, gjør følgende:

- Legg til en serveroppføring i `mcp.json` slik:

    ```json
    {
        "servers": {
            "my-mcp-server-7178eca7": {
                "url": "http://localhost:3001/mcp",
                "type": "http"
            }
        },
        "inputs": []
    }
    ```

1. Klikk på "start" knappen i *mcp.json*
1. Sørg for at et chatte-vindu er åpent og skriv `get-faq`, du skal se et resultat som dette:

    ![Visual Studio Code MCP Apps](../../../../../../translated_images/no/vscode-ui.f2771dcfce25ca0f.webp)

## Valg -2- Test appen med en host

Repoet <https://github.com/modelcontextprotocol/ext-apps> inneholder flere ulike hoster som du kan bruke for å teste MVP Apps.

Vi vil presentere to ulike alternativer her:

### Lokal maskin

- Naviger til *ext-apps* etter at du har klonet repoet.

- Installer avhengigheter

   ```sh
   npm install
   ```

- I et separat terminalvindu, naviger til *ext-apps/examples/basic-host*

    > hvis du er i Codespace, må du navigere til serve.ts på linje 27 og erstatte http://localhost:3001/mcp med din Codespace URL for backend, for eksempel https://psychic-xylophone-657rpjgvxpc5g64-3001.app.github.dev/mcp

- Kjør hosten:

    ```sh
    npm start
    ```

    Dette skal koble hosten til backend og du skal se appen kjøre slik:

    ![App kjører](../../../../../../translated_images/no/mcp-app.50dd20a779bea32f.webp)

### Codespace

Det krever litt ekstra arbeid for å få en Codespace-miljø til å fungere. For å bruke en host gjennom Codespace:

- Se *ext-apps* katalogen og naviger til *examples/basic-host*.
- Kjør `npm install` for å installere avhengigheter
- Kjør `npm start` for å starte hosten.

## Test ut appen

Prøv appen på følgende måte:

- Velg "Call Tool" knappen og du skal se resultatene som dette:

    ![Tool resultat](../../../../../../translated_images/no/tool-result.cfec4814ce8e0146.webp)

Flott, alt fungerer.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->