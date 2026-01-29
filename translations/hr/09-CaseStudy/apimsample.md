# Studija slučaja: Izlaganje REST API-ja u API Managementu kao MCP poslužitelja

Azure API Management je usluga koja pruža Gateway iznad vaših API krajnjih točaka. Funkcionira tako da Azure API Management djeluje kao proxy ispred vaših API-ja i odlučuje što učiniti s dolaznim zahtjevima.

Korištenjem ove usluge dodajete niz značajki kao što su:

- **Sigurnost**, možete koristiti sve od API ključeva, JWT-a do upravljanog identiteta.
- **Ograničavanje brzine**, sjajna značajka koja omogućuje odlučivanje koliko poziva prolazi unutar određenog vremenskog razdoblja. Ovo osigurava da svi korisnici imaju dobro iskustvo i da vaša usluga nije preopterećena zahtjevima.
- **Skaliranje i balansiranje opterećenja**. Možete postaviti više krajnjih točaka za raspodjelu opterećenja i također odlučiti kako "balansirati opterećenje".
- **AI značajke poput semantičkog keširanja**, ograničenja tokena, praćenja tokena i još mnogo toga. Ovo su sjajne značajke koje poboljšavaju odzivnost i pomažu vam da pratite potrošnju tokena. [Pročitajte više ovdje](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Zašto MCP + Azure API Management?

Model Context Protocol brzo postaje standard za agentne AI aplikacije i način izlaganja alata i podataka na konzistentan način. Azure API Management je prirodan izbor kada trebate "upravljati" API-jima. MCP poslužitelji često se integriraju s drugim API-jima kako bi riješili zahtjeve za alatima, na primjer. Stoga kombinacija Azure API Managementa i MCP-a ima puno smisla.

## Pregled

U ovom konkretnom slučaju naučit ćemo kako izložiti API krajnje točke kao MCP poslužitelj. Na taj način, ove krajnje točke lako možemo učiniti dijelom agentne aplikacije, dok istovremeno koristimo značajke Azure API Managementa.

## Ključne značajke

- Odabirete metode krajnjih točaka koje želite izložiti kao alate.
- Dodatne značajke koje dobivate ovise o tome što konfigurirate u odjeljku s pravilima za vaš API. Ovdje ćemo pokazati kako možete dodati ograničavanje brzine.

## Preduvjet: uvoz API-ja

Ako već imate API u Azure API Managementu, odlično, možete preskočiti ovaj korak. Ako ne, pogledajte ovaj link, [uvoz API-ja u Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Izlaganje API-ja kao MCP poslužitelja

Za izlaganje API krajnjih točaka, slijedite ove korake:

1. Otvorite Azure Portal na sljedećoj adresi <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
   i idite na svoju instancu API Managementa.

1. U lijevom izborniku odaberite APIs > MCP Servers > + Create new MCP Server.

1. U odjeljku API odaberite REST API koji želite izložiti kao MCP poslužitelj.

1. Odaberite jednu ili više API operacija koje želite izložiti kao alate. Možete odabrati sve operacije ili samo određene.

    ![Odabir metoda za izlaganje](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Kliknite **Create**.

1. Idite na opciju izbornika **APIs** i **MCP Servers**, trebali biste vidjeti sljedeće:

    ![Prikaz MCP poslužitelja u glavnom prozoru](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP poslužitelj je kreiran i API operacije su izložene kao alati. MCP poslužitelj je naveden u odjeljku MCP Servers. Stupac URL prikazuje krajnju točku MCP poslužitelja koju možete koristiti za testiranje ili unutar klijentske aplikacije.

## Opcionalno: Konfiguriranje pravila

Azure API Management ima osnovni koncept pravila gdje postavljate različita pravila za svoje krajnje točke, poput ograničavanja brzine ili semantičkog keširanja. Ova pravila se pišu u XML formatu.

Evo kako možete postaviti pravilo za ograničavanje brzine vašeg MCP poslužitelja:

1. U portalu, pod APIs, odaberite **MCP Servers**.

1. Odaberite MCP poslužitelj koji ste kreirali.

1. U lijevom izborniku, pod MCP, odaberite **Policies**.

1. U uređivaču pravila dodajte ili uredite pravila koja želite primijeniti na alate MCP poslužitelja. Pravila su definirana u XML formatu. Na primjer, možete dodati pravilo za ograničavanje poziva na alate MCP poslužitelja (u ovom primjeru, 5 poziva po 30 sekundi po IP adresi klijenta). Evo XML-a koji će uzrokovati ograničavanje brzine:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Evo slike uređivača pravila:

    ![Uređivač pravila](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Isprobajte

Provjerimo radi li naš MCP poslužitelj kako je predviđeno.

Za ovo ćemo koristiti Visual Studio Code i GitHub Copilot u njegovom Agent modu. Dodati ćemo MCP poslužitelj u *mcp.json* datoteku. Na taj način, Visual Studio Code će djelovati kao klijent s agentnim mogućnostima, a krajnji korisnici će moći unijeti upit i komunicirati s poslužiteljem.

Evo kako dodati MCP poslužitelj u Visual Studio Code:

1. Koristite MCP: **Add Server naredbu iz Command Palette**.

1. Kada se zatraži, odaberite vrstu poslužitelja: **HTTP (HTTP ili Server Sent Events)**.

1. Unesite URL MCP poslužitelja u API Managementu. Primjer: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (za SSE krajnju točku) ili **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (za MCP krajnju točku), obratite pažnju na razliku između transporta `/sse` ili `/mcp`.

1. Unesite ID poslužitelja po vašem izboru. Ovo nije važna vrijednost, ali će vam pomoći da zapamtite što je ova instanca poslužitelja.

1. Odaberite želite li spremiti konfiguraciju u postavke radnog prostora ili korisničke postavke.

  - **Postavke radnog prostora** - Konfiguracija poslužitelja se sprema u .vscode/mcp.json datoteku dostupnu samo u trenutnom radnom prostoru.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    ili ako odaberete streaming HTTP kao transport, izgledat će malo drugačije:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Korisničke postavke** - Konfiguracija poslužitelja se dodaje u vašu globalnu *settings.json* datoteku i dostupna je u svim radnim prostorima. Konfiguracija izgleda slično sljedećem:

    ![Korisničke postavke](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Također trebate dodati konfiguraciju, zaglavlje kako biste osigurali pravilnu autentifikaciju prema Azure API Managementu. Koristi se zaglavlje pod nazivom **Ocp-Apim-Subscription-Key**.

    - Evo kako ga možete dodati u postavke:

    ![Dodavanje zaglavlja za autentifikaciju](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), ovo će uzrokovati prikazivanje upita za unos vrijednosti API ključa koji možete pronaći u Azure Portalu za vašu instancu Azure API Managementa.

   - Da biste ga dodali u *mcp.json*, možete ga dodati ovako:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### Korištenje Agent moda

Sada smo sve postavili u postavkama ili u *.vscode/mcp.json*. Isprobajmo.

Trebala bi se pojaviti ikona Alati, gdje su navedeni izloženi alati s vašeg poslužitelja:

![Alati s poslužitelja](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Kliknite ikonu alata i trebali biste vidjeti popis alata poput ovog:

    ![Alati](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Unesite upit u chat za pokretanje alata. Na primjer, ako ste odabrali alat za dobivanje informacija o narudžbi, možete pitati agenta o narudžbi. Evo primjera upita:

    ```text
    get information from order 2
    ```

    Sada će vam se prikazati ikona alata koja vas pita želite li nastaviti s pozivom alata. Odaberite da nastavite s pokretanjem alata, trebali biste vidjeti izlaz poput ovog:

    ![Rezultat upita](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **ono što vidite ovisi o alatima koje ste postavili, ali ideja je da dobijete tekstualni odgovor poput gore navedenog**

## Reference

Evo kako možete saznati više:

- [Vodič o Azure API Managementu i MCP-u](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python primjer: Sigurno udaljeni MCP poslužitelji koristeći Azure API Management (eksperimentalno)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratorij za autorizaciju MCP klijenta](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Korištenje Azure API Management ekstenzije za VS Code za uvoz i upravljanje API-jima](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registracija i otkrivanje udaljenih MCP poslužitelja u Azure API Centeru](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Sjajan repozitorij koji prikazuje mnoge AI mogućnosti s Azure API Managementom
- [AI Gateway radionice](https://azure-samples.github.io/AI-Gateway/) Sadrži radionice koristeći Azure Portal, što je sjajan način za početak evaluacije AI mogućnosti.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.