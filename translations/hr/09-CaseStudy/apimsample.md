# Studija slučaja: Izložiti REST API u upravljanju API-jem kao MCP server

Azure API Management je usluga koja pruža Gateway iznad vaših API krajnjih točaka. Način rada je takav da Azure API Management djeluje kao proxy ispred vaših API-ja i može odlučiti što učiniti s dolaznim zahtjevima.

Korištenjem ove usluge dodajete čitav niz značajki poput:

- **Sigurnost**, možete koristiti sve od API ključeva, JWT do upravljanog identiteta.
- **Ograničenje brzine**, sjajna značajka koja omogućuje da odlučite koliko poziva prolazi u određenom vremenskom jedinicom. To pomaže osigurati da svi korisnici imaju izvrsno iskustvo, a također i da vaša usluga nije preopterećena zahtjevima.
- **Skaliranje i ravnoteža opterećenja**. Možete postaviti nekoliko krajnjih točaka za izjednačavanje opterećenja i također možete odlučiti kako "izjednačiti opterećenje".
- **AI značajke poput semantičkog keširanja**, ograničenja tokena, praćenja tokena i još mnogo toga. Ove su značajke izvrsne za poboljšanje odzivnosti kao i za praćenje potrošnje tokena. [Pročitajte više ovdje](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Zašto MCP + Azure API Management?

Model Context Protocol brzo postaje standard za agentne AI aplikacije i način izlaganja alata i podataka na dosljedan način. Azure API Management je prirodan izbor kada trebate "upravljati" API-jima. MCP serveri često se integriraju s drugim API-jima kako bi riješili zahtjeve prema nekom alatu, na primjer. Stoga kombinacija Azure API Managementa i MCP-a ima puno smisla.

## Pregled

U ovom specifičnom slučaju upotrebe naučit ćemo kako izložiti API krajnje točke kao MCP server. Time lako možemo učiniti te krajnje točke dijelom agentne aplikacije, istovremeno koristeći prednosti Azure API Managementa.

## Ključne značajke

- Odaberete metode krajnjih točaka koje želite izložiti kao alate.
- Dodatne značajke koje dobivate ovise o onome što konfigurirate u dijelu pravila za vaš API. Ovdje ćemo vam pokazati kako dodati ograničenje brzine.

## Predkorak: uvoz API-ja

Ako već imate API u Azure API Managementu, odlično, tada možete preskočiti ovaj korak. Ako ne, pogledajte ovu poveznicu, [uvoz API-ja u Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Izložite API kao MCP Server

Da biste izložili API krajnje točke, slijedite sljedeće korake:

1. Idite na Azure Portal na adresu <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
Navigirajte do instance upravljanja API-jem.

1. U lijevom izborniku odaberite APIs > MCP Servers > + Create new MCP Server.

1. U API-ju odaberite REST API koji želite izložiti kao MCP server.

1. Odaberite jedno ili više API operacija koje će biti izložene kao alati. Možete odabrati sve operacije ili samo određene operacije.

    ![Odaberite metode za izlaganje](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Odaberite **Create**.

1. Idite na opciju menija **APIs** i **MCP Servers**, trebali biste vidjeti sljedeće:

    ![Vidi MCP Server u glavnom prozoru](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP server je kreiran i API operacije su izložene kao alati. MCP server je naveden u panelu MCP Servers. Stupac URL prikazuje krajnju točku MCP servera koju možete pozvati za testiranje ili unutar klijentske aplikacije.

## Opcionalno: Konfigurirajte politike

Azure API Management ima osnovni koncept politika gdje postavljate različita pravila za vaše krajnje točke, kao što su ograničenje brzine ili semantičko keširanje. Te se politike pišu u XML-u.

Evo kako možete postaviti politiku za ograničenje brzine vašeg MCP servera:

1. U portalu, pod APIs, odaberite **MCP Servers**.

1. Odaberite MCP server koji ste stvorili.

1. U lijevom izborniku, pod MCP, odaberite **Policies**.

1. U uređivaču politika dodajte ili uredite politike koje želite primijeniti na alate MCP servera. Politike su definirane u XML formatu. Na primjer, možete dodati politiku za ograničenje poziva na alate MCP servera (u ovom primjeru, 5 poziva po 30 sekundi po IP adresi klijenta). Evo XML-a koji će to ograničiti:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Evo slike uređivača politika:

    ![Uređivač politika](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Isprobajte

Provjerimo radi li naš MCP Server kako je zamišljeno.

> [!NOTE]
> Azure API Management trenutno izlaže ovaj server putem Streamable
> HTTP `/mcp` krajnje točke. Stariji HTTP+SSE `/sse` transport je zastario i
> trebao bi se koristiti samo s naslijeđenim klijentima.

Za ovo ćemo koristiti Visual Studio Code i GitHub Copilot u Agent modu. Dodavat ćemo MCP server u *mcp.json* datoteku. Time će Visual Studio Code djelovati kao klijent s agentnim mogućnostima, a krajnji korisnici moći će unijeti prompt i komunicirati s navedenim serverom.

Pogledajmo kako dodati MCP server u Visual Studio Code:

1. Upotrijebite naredbu MCP: **Add Server iz Command Palette**.

1. Kada se zatraži, odaberite tip servera: **HTTP (HTTP ili Server Sent Events)**.

1. Unesite Streamable HTTP URL prikazan za MCP server u API Managementu.
    Na primjer:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Unesite ID servera po vlastitom izboru. Ovo nije važna vrijednost, ali pomoći će vam da zapamtite koja je to instanca servera.

1. Odaberite hoćete li spremiti konfiguraciju u postavke radnog prostora ili korisničke postavke.

  - **Postavke radnog prostora** - Konfiguracija servera se sprema u datoteku .vscode/mcp.json dostupnu samo u trenutnom radnom prostoru.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Korisničke postavke** - Konfiguracija servera se dodaje u globalnu datoteku *settings.json* i dostupna je u svim radnim prostorima. Konfiguracija izgleda otprilike ovako:

    ![Korisnička postavka](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Također morate dodati konfiguraciju, zaglavlje kako bi se pravilno autentificiralo prema Azure API Managementu. Koristi zaglavlje nazvano **Ocp-Apim-Subscription-Key**.

    - Evo kako ga možete dodati u postavke:

    ![Dodavanje zaglavlja za autentifikaciju](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), ovo će izazvati prikaz prompta koji će vas zatražiti da unesete vrijednost API ključa koju možete pronaći u Azure Portalu za vašu Azure API Management instancu.

   - Da biste ga dodali u *mcp.json* umjesto toga, možete ga dodati ovako:

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

### Koristite Agent mod

Sad smo sve postavili, bilo u postavkama ili u *.vscode/mcp.json*. Isprobajmo.

Trebao bi postojati ikona Alata ovako, gdje su navedeni izloženi alati vašeg servera:

![Alati s servera](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Kliknite ikonu alata i trebali biste vidjeti popis alata ovako:

    ![Alati](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Upišite prompt u chat da biste pozvali alat. Na primjer, ako ste odabrali alat za dobivanje informacija o narudžbi, možete upitati agenta o narudžbi. Evo primjera prompta:

    ```text
    get information from order 2
    ```

    Sada će vam biti prikazana ikona alata koja traži da nastavite s pozivanjem alata. Odaberite nastavak izvođenja alata, sada biste trebali vidjeti izlaz ovako:

    ![Rezultat iz prompta](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **ono što vidite gore ovisi o alatima koje ste postavili, ali ideja je da dobijete tekstualni odgovor kao gore**


## Reference

Evo kako možete saznati više:

- [Vodič o Azure API Management i MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python primjer: Sigurni udaljeni MCP serveri koristeći Azure API Management (eksperimentalno)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratorij za autorizaciju MCP klijenta](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Koristite Azure API Management ekstenziju za VS Code za uvoz i upravljanje API-jima](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrirajte i otkrijte udaljene MCP servere u Azure API Centeru](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Odličan repozitorij koji pokazuje mnoge AI mogućnosti s Azure API Managementom
- [AI Gateway radionice](https://azure-samples.github.io/AI-Gateway/) Sadrži radionice koristeći Azure Portal, što je izvrstan način za početak procjene AI mogućnosti.

## Što dalje

- Natrag na: [Pregled studija slučaja](./README.md)
- Sljedeće: [Azure AI Travel Agents](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->