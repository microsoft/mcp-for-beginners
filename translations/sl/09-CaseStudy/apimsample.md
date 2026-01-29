# Študija primera: Izpostavitev REST API-ja v API Management kot MCP strežnik

Azure API Management je storitev, ki zagotavlja prehod (Gateway) nad vašimi API končnimi točkami. Deluje tako, da Azure API Management deluje kot posrednik pred vašimi API-ji in lahko odloča, kaj storiti z dohodnimi zahtevami.

Z uporabo te storitve pridobite številne funkcionalnosti, kot so:

- **Varnost**, lahko uporabite vse od API ključev, JWT do upravljane identitete.
- **Omejevanje hitrosti**, odlična funkcionalnost, ki omogoča določanje, koliko klicev je dovoljenih v določenem časovnem obdobju. To pomaga zagotoviti dobro uporabniško izkušnjo in preprečuje preobremenitev vaše storitve.
- **Skaliranje in uravnoteženje obremenitve**. Nastavite lahko več končnih točk za uravnoteženje obremenitve in določite, kako naj se obremenitev porazdeli.
- **AI funkcionalnosti, kot so semantično predpomnjenje**, omejitev žetonov, spremljanje žetonov in drugo. Te funkcionalnosti izboljšajo odzivnost in vam pomagajo spremljati porabo žetonov. [Več o tem preberite tukaj](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Zakaj MCP + Azure API Management?

Model Context Protocol hitro postaja standard za agentne AI aplikacije in način izpostavljanja orodij ter podatkov na dosleden način. Azure API Management je naravna izbira, ko potrebujete "upravljanje" API-jev. MCP strežniki se pogosto integrirajo z drugimi API-ji za reševanje zahtevkov za orodja, na primer. Zato je kombinacija Azure API Management in MCP smiselna.

## Pregled

V tem specifičnem primeru bomo spoznali, kako izpostaviti API končne točke kot MCP strežnik. S tem lahko te končne točke enostavno vključimo v agentno aplikacijo, hkrati pa izkoristimo funkcionalnosti Azure API Management.

## Ključne funkcionalnosti

- Izberete metode končnih točk, ki jih želite izpostaviti kot orodja.
- Dodatne funkcionalnosti so odvisne od tega, kaj konfigurirate v razdelku s politikami za vaš API. Tukaj pa bomo pokazali, kako lahko dodate omejevanje hitrosti.

## Predkorak: uvoz API-ja

Če že imate API v Azure API Management, lahko ta korak preskočite. Če ne, si oglejte ta povezava: [uvoz API-ja v Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Izpostavitev API-ja kot MCP strežnik

Za izpostavitev API končnih točk sledite tem korakom:

1. Pojdite na Azure Portal in na naslednji naslov <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>. 
   Pojdite do vaše instance API Management.

1. V levem meniju izberite **APIs > MCP Servers > + Create new MCP Server**.

1. Pri **API** izberite REST API, ki ga želite izpostaviti kot MCP strežnik.

1. Izberite eno ali več API operacij, ki jih želite izpostaviti kot orodja. Lahko izberete vse operacije ali samo specifične.

    ![Izberite metode za izpostavitev](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Izberite **Create**.

1. Pojdite na možnost menija **APIs** in **MCP Servers**, kjer bi morali videti naslednje:

    ![Poglejte MCP strežnik v glavnem oknu](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP strežnik je ustvarjen, API operacije pa so izpostavljene kot orodja. MCP strežnik je naveden v razdelku MCP Servers. Stolpec URL prikazuje končno točko MCP strežnika, ki jo lahko uporabite za testiranje ali v odjemalski aplikaciji.

## Neobvezno: Konfiguracija politik

Azure API Management ima osnovni koncept politik, kjer nastavite različna pravila za vaše končne točke, na primer omejevanje hitrosti ali semantično predpomnjenje. Te politike so napisane v XML.

Tukaj je, kako lahko nastavite politiko za omejevanje hitrosti vašega MCP strežnika:

1. V portalu, pod **APIs**, izberite **MCP Servers**.

1. Izberite MCP strežnik, ki ste ga ustvarili.

1. V levem meniju, pod **MCP**, izberite **Policies**.

1. V urejevalniku politik dodajte ali uredite politike, ki jih želite uporabiti za orodja MCP strežnika. Politike so definirane v XML formatu. Na primer, lahko dodate politiko za omejitev klicev na orodja MCP strežnika (v tem primeru 5 klicev na 30 sekund na IP naslov odjemalca). Tukaj je XML, ki bo povzročil omejevanje hitrosti:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Tukaj je slika urejevalnika politik:

    ![Urejevalnik politik](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Preizkusite

Prepričajmo se, da naš MCP strežnik deluje, kot je predvideno.

Za to bomo uporabili Visual Studio Code in GitHub Copilot v načinu Agent. MCP strežnik bomo dodali v datoteko *mcp.json*. S tem bo Visual Studio Code deloval kot odjemalec z agentnimi zmožnostmi, končni uporabniki pa bodo lahko vnesli poziv in komunicirali s strežnikom.

Poglejmo, kako dodati MCP strežnik v Visual Studio Code:

1. Uporabite ukaz **MCP: Add Server** iz ukazne palete.

1. Ko ste pozvani, izberite vrsto strežnika: **HTTP (HTTP ali Server Sent Events)**.

1. Vnesite URL MCP strežnika v API Management. Primer: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (za SSE končno točko) ali **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (za MCP končno točko), pri čemer je razlika med transporti `/sse` ali `/mcp`.

1. Vnesite ID strežnika po vaši izbiri. Ta vrednost ni pomembna, vendar vam bo pomagala prepoznati to instanco strežnika.

1. Izberite, ali želite konfiguracijo shraniti v nastavitve delovnega prostora ali uporabniške nastavitve.

  - **Nastavitve delovnega prostora** - Konfiguracija strežnika je shranjena v datoteko .vscode/mcp.json, ki je na voljo samo v trenutnem delovnem prostoru.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    ali če izberete pretakanje HTTP kot transport, bo nekoliko drugače:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Uporabniške nastavitve** - Konfiguracija strežnika je dodana v vašo globalno datoteko *settings.json* in je na voljo v vseh delovnih prostorih. Konfiguracija je videti podobna naslednjemu:

    ![Uporabniške nastavitve](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Prav tako morate dodati konfiguracijo, glavo, da zagotovite pravilno avtentikacijo proti Azure API Management. Uporablja glavo z imenom **Ocp-Apim-Subscription-Key**.

    - Tukaj je, kako jo lahko dodate v nastavitve:

    ![Dodajanje glave za avtentikacijo](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), to bo povzročilo, da se prikaže poziv za vnos vrednosti API ključa, ki ga najdete v Azure Portalu za vašo instanco Azure API Management.

   - Če jo želite dodati v *mcp.json*, jo lahko dodate tako:

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

### Uporaba načina Agent

Zdaj smo vse nastavili bodisi v nastavitvah bodisi v *.vscode/mcp.json*. Preizkusimo.

Moral bi biti gumb za orodja, kjer so navedena izpostavljena orodja vašega strežnika:

![Orodja s strežnika](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Kliknite gumb za orodja in morali bi videti seznam orodij, kot je prikazano:

    ![Orodja](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Vnesite poziv v klepet za izvedbo orodja. Na primer, če ste izbrali orodje za pridobivanje informacij o naročilu, lahko vprašate agenta o naročilu. Tukaj je primer poziva:

    ```text
    get information from order 2
    ```

    Zdaj se vam bo prikazal gumb za orodja, ki vas bo pozval, da nadaljujete z izvajanjem orodja. Izberite nadaljevanje izvajanja orodja, zdaj bi morali videti rezultat, kot je prikazano:

    ![Rezultat poziva](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **kar vidite zgoraj, je odvisno od tega, katera orodja ste nastavili, vendar je ideja, da dobite besedilni odgovor, kot je zgoraj**

## Reference

Tukaj lahko izveste več:

- [Vadnica o Azure API Management in MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python primer: Zavarovanje oddaljenih MCP strežnikov z uporabo Azure API Management (eksperimentalno)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratorij za avtentikacijo MCP odjemalcev](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Uporaba razširitve Azure API Management za VS Code za uvoz in upravljanje API-jev](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registracija in odkrivanje oddaljenih MCP strežnikov v Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Odličen repozitorij, ki prikazuje številne AI zmožnosti z Azure API Management
- [Delavnice AI Gateway](https://azure-samples.github.io/AI-Gateway/) Vsebuje delavnice z uporabo Azure Portala, kar je odličen način za začetek ocenjevanja AI zmožnosti.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.