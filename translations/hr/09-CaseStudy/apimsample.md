# Studija slučaja: Izložiti REST API u API Management kao MCP poslužitelj

Azure API Management je usluga koja pruža Gateway na vrhu vaših API krajnjih točaka. Način na koji funkcionira jest da Azure API Management djeluje poput proxyja ispred vaših API-ja i može odlučiti što učiniti s dolaznim zahtjevima.

Korištenjem toga dodajete cijeli niz funkcija poput:

- **Sigurnost**, možete koristiti sve od API ključeva, JWT do upravljane identitete.
- **Ograničenje brzine**, izvrsna je značajka mogućnost odlučivanja koliko poziva prođe u određenoj vremenskoj jedinici. To pomaže osigurati da svi korisnici imaju izvrsno iskustvo, a također i da vaša usluga nije preopterećena zahtjevima.
- **Skaliranje i uravnoteženje opterećenja**. Možete postaviti broj krajnjih točaka za raspodjelu opterećenja i također možete odlučiti kako "uravnotežiti opterećenje".
- **AI značajke poput semantičkog keširanja**, ograničenja tokena i nadzora tokena i još mnogo toga. Ovo su izvrsne značajke koje poboljšavaju odzivnost kao i pomažu u praćenju potrošnje tokena. [Pročitajte više ovdje](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Zašto MCP + Azure API Management?

Model Context Protocol brzo postaje standard za agentne AI aplikacije i način kako izložiti alate i podatke na konzistentan način. Azure API Management je prirodan izbor kada trebate "upravljati" API-jima. MCP poslužitelji često se integriraju s drugim API-jima kako bi riješili zahtjeve za alat, na primjer. Stoga kombinacija Azure API Managementa i MCP-a ima puno smisla.

## Pregled

U ovom specifičnom primjeru upotrebe naučit ćemo kako izložiti API krajnje točke kao MCP poslužitelj. Time možemo lako učiniti ove krajnje točke dijelom agentne aplikacije, a istovremeno iskoristiti značajke iz Azure API Managementa.

## Ključne značajke

- Odaberete metode krajnjih točaka koje želite izložiti kao alate.
- Dodatne značajke koje ćete dobiti ovise o tome što konfigurirate u odjeljku pravila za vaš API. No ovdje ćemo vam pokazati kako dodati ograničenje brzine.

## Prethodni korak: uvoz API-ja

Ako već imate API u Azure API Managementu, super, onda možete preskočiti ovaj korak. Ako ne, pogledajte ovaj link, [uvoz API-ja u Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Izložiti API kao MCP poslužitelj

Za izlaganje API krajnjih točaka slijedite ove korake:

1. Idite na Azure Portal i na sljedeću adresu <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
Idite na vašu instancu API Managementa.

1. U lijevom izborniku odaberite APIs > MCP Servers > + Create new MCP Server.

1. U API odaberite REST API koji želite izložiti kao MCP poslužitelj.

1. Odaberite jednu ili više API operacija koje želite izložiti kao alate. Možete odabrati sve operacije ili samo određene.

    ![Odaberite metode za izlaganje](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Odaberite **Create**.

1. Idite na opciju izbornika **APIs** i **MCP Servers**, trebali biste vidjeti sljedeće:

    ![Pogledajte MCP poslužitelj u glavnom prikazu](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP poslužitelj je kreiran i API operacije su izložene kao alati. MCP poslužitelj je naveden u MCP Servers panelu. Stupac URL prikazuje krajnju točku MCP poslužitelja koju možete pozvati za testiranje ili unutar klijentske aplikacije.

## Opcionalno: Konfigurirajte pravila

Azure API Management ima osnovni koncept pravila gdje postavljate različita pravila za vaše krajnje točke, poput ograničenja brzine ili semantičkog keširanja. Ta pravila se pišu u XML-u.

Evo kako konfigurirati pravilo za ograničenje brzine vašeg MCP poslužitelja:

1. U portalu, pod APIs, odaberite **MCP Servers**.

1. Odaberite MCP poslužitelj koji ste kreirali.

1. U lijevom izborniku, pod MCP, odaberite **Policies**.

1. U uređivaču pravila dodajte ili uredite pravila koja želite primijeniti na alate MCP poslužitelja. Pravila su definirana u XML formatu. Na primjer, možete dodati pravilo koje ograničava pozive na alate MCP poslužitelja (u ovom primjeru, 5 poziva na 30 sekundi po IP adresi klijenta). Evo XML koda koji će uzrokovati ograničenje brzine:

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

Provjerimo radi li naš MCP poslužitelj kako je zamišljeno.

> [!NOTE]
> Azure API Management trenutno izlaže ovaj poslužitelj putem Streamable
> HTTP `/mcp` krajnje točke. Stariji HTTP+SSE `/sse` transport je zastario i
> treba ga koristiti samo s naslijeđenim klijentima.

Za ovo ćemo koristiti Visual Studio Code i GitHub Copilot u njegovom Agent načinu rada. Dodati ćemo MCP poslužitelj u datoteku *mcp.json*. Time će Visual Studio Code djelovati kao klijent s agentnim sposobnostima, a krajnji korisnici će moći upisati upit i komunicirati s navedenim poslužiteljem.

Pogledajmo kako, dodati MCP poslužitelj u Visual Studio Code:

1. Koristite MCP: **Add Server naredbu iz Command Palette**.

1. Kada se zatraži, odaberite tip poslužitelja: **HTTP (HTTP ili Server Sent Events)**.

1. Unesite Streamable HTTP URL prikazan za MCP poslužitelj u API Managementu.
    Na primjer:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Unesite ID poslužitelja po želji. Ova vrijednost nije kritična, ali pomoći će vam zapamtiti koja je to instanca poslužitelja.

1. Odaberite želite li spremiti konfiguraciju u postavke radnog prostora ili korisničke postavke.

    - **Postavke radnog prostora** - Konfiguracija poslužitelja sprema se u datoteku `.vscode/mcp.json`, koja je dostupna samo u trenutnom radnom prostoru.

      *mcp.json*

      ```json
      "servers": {
          "APIM petstore" : {
              "type": "http",
              "url": "url-to-mcp-server/mcp"
          }
      }
      ```

    - **Korisničke postavke** - Konfiguracija poslužitelja se dodaje u globalnu datoteku *settings.json* i dostupna je u svim radnim prostorima. Konfiguracija izgleda otprilike ovako:

      ![Korisnička postavka](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Također trebate dodati konfiguracijski zaglavlje kako biste osigurali ispravnu autentifikaciju prema Azure API Managementu. Koristi se zaglavlje pod nazivom **Ocp-Apim-Subscription-Key**.

    - Evo kako ga možete dodati u postavke:


    ![Dodavanje zaglavlja za autentikaciju](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), to će prikazati upit za unos vrijednosti API ključa koju možete pronaći u Azure Portalu za vašu Azure API Management instancu.

   - Za dodavanje u *mcp.json* umjesto toga, možete to učiniti ovako:

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

### Koristite Agent način rada

Sada smo sve postavili bilo u postavkama ili u *.vscode/mcp.json*. Pokušajmo.

Trebao bi postojati ikona Alati kao ovdje, gdje su navedeni izloženi alati s vašeg poslužitelja:

![Alati s poslužitelja](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Kliknite na ikonu alata i trebali biste vidjeti popis alata ovako:

    ![Alati](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Unesite upit u chat da pokrenete alat. Na primjer, ako ste odabrali alat za dobivanje informacija o narudžbi, možete upitati agenta o narudžbi. Evo primjera upita:

    ```text
    get information from order 2
    ```

    Sada će vam se prikazati ikona alata koja traži da nastavite s pozivanjem alata. Odaberite da nastavite s izvršavanjem alata, sada biste trebali vidjeti rezultat poput ovoga:

    ![Rezultat upita](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **ono što vidite gore ovisi o tome koje ste alate postavili, ali ideja je da dobijete tekstualni odgovor poput gore navedenog**


## Reference

Evo kako možete saznati više:

- [Tutorijal o Azure API Managementu i MCP-u](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python primjer: Sigurni udaljeni MCP poslužitelji koristeći Azure API Management (eksperimentalno)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratorij za autorizaciju MCP klijenata](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Koristite Azure API Management ekstenziju za VS Code za uvoz i upravljanje API-jima](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrirajte i otkrijte udaljene MCP poslužitelje u Azure API Centeru](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Izvrsni repozitorij koji prikazuje mnoge AI mogućnosti s Azure API Managementom
- [AI Gateway radionice](https://azure-samples.github.io/AI-Gateway/) Sadrži radionice korištenjem Azure Portala, što je izvrstan način za početno procjenjivanje AI mogućnosti.

## Što slijedi

- Povratak na: [Pregled studija slučaja](./README.md)
- Sljedeće: [Azure AI Travel Agents](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->