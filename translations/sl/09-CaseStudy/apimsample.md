# Študija primera: Izpostavitev REST API v upravljanju API kot MCP strežnik

Azure API Management je storitev, ki zagotavlja Prehod nad vašimi API končnimi točkami. Deluje tako, da Azure API Management deluje kot proxy pred vašimi API-ji in lahko odloči, kaj storiti z dohodnimi zahtevami.

Z njegovo uporabo dodate vrsto funkcij, kot so:

- **Varnost**, lahko uporabite vse od API ključev, JWT do upravljane identitete.
- **Omejevanje hitrosti**, odlična funkcija je možnost odločanja, koliko klicev preide v določenem časovnem obdobju. To pomaga zagotoviti, da vsi uporabniki imajo odlično izkušnjo in tudi, da vaša storitev ni preplavljena z zahtevami.
- **Prilagajanje in uravnoteženje obremenitve**. Lahko nastavite več končnih točk za uravnoteženje obremenitve in se lahko odločite tudi, kako "uravnotežiti obremenitev".
- **AI funkcije, kot so semantični predpomnilnik**, omejitev tokenov in nadzor tokenov ter še več. To so odlične funkcije, ki izboljšujejo odzivnost in vam pomagajo imeti nadzor nad porabo tokenov. [Preberite več tukaj](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Zakaj MCP + Azure API Management?

Model Context Protocol hitro postaja standard za agentne AI aplikacije in način izpostavitve orodij in podatkov na dosleden način. Azure API Management je naravna izbira, ko želite "upravljati" API-je. MCP strežniki se pogosto integrirajo z drugimi API-ji, da razrešijo zahteve do orodja na primer. Zato kombinacija Azure API Management in MCP logično deluje.

## Pregled

V tem specifičnem primeru uporabe se bomo naučili izpostaviti API končne točke kot MCP strežnik. S tem lahko te točke enostavno vključimo v agentno aplikacijo, hkrati pa izkoristimo funkcije iz Azure API Management.

## Ključne funkcije

- Izberete metode končne točke, ki jih želite izpostaviti kot orodja.
- Dodatne funkcije, ki jih dobite, so odvisne od tega, kaj nastavite v delu pravil za vaš API. Tukaj pa vam bomo pokazali, kako dodati omejevanje hitrosti.

## Predkorak: uvoz API-ja

Če že imate API v Azure API Management, super, lahko ta korak preskočite. Če ne, si oglejte to povezavo, [uvoz API-ja v Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Izpostavi API kot MCP strežnik

Za izpostavitev API končnih točk sledite naslednjim korakom:

1. Pojdite na Azure Portal na naslov <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
Odprite svoj primer upravljanja API.

1. V levem meniju izberite APIs > MCP Servers > + Ustvari nov MCP strežnik.

1. V API-ju izberite REST API, ki ga želite izpostaviti kot MCP strežnik.

1. Izberite eno ali več API Operacij, ki jih želite izpostaviti kot orodja. Lahko izberete vse operacije ali samo določene.

    ![Izberi metode za izpostavitev](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Izberite **Ustvari**.

1. Pojdite na menijsko možnost **APIs** in **MCP Servers**, morali bi videti naslednje:

    ![Poglej MCP strežnik v glavnem pogledu](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP strežnik je ustvarjen in API operacije so izpostavljene kot orodja. MCP strežnik je prikazan v seznamu MCP strežnikov. Stolpec URL prikazuje končno točko MCP strežnika, ki jo lahko pokličete za testiranje ali v odjemalski aplikaciji.

## Izbirno: konfigurirajte pravilnike

Azure API Management ima osnovni koncept pravilnikov, kjer nastavite različna pravila za vaše končne točke, na primer omejevanje hitrosti ali semantični predpomnilnik. Ti pravilniki so napisani v XML.

Tukaj je, kako lahko nastavite pravilnik za omejitev hitrosti vašega MCP strežnika:

1. V portalu, pod APIs, izberite **MCP Servers**.

1. Izberite MCP strežnik, ki ste ga ustvarili.

1. V levem meniju, pod MCP, izberite **Policies**.

1. V urejevalniku pravilnikov dodajte ali uredite pravilnike, ki jih želite uporabiti za orodja MCP strežnika. Pravilniki so definirani v XML formatu. Na primer, lahko dodate pravilnik za omejevanje klicev do orodij MCP strežnika (v tem primeru 5 klicev na 30 sekund na IP naslov odjemalca). Tukaj je XML, ki bo povzročil omejitev hitrosti:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Tukaj je slika urejevalnika pravilnikov:

    ![Urejevalnik pravilnikov](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Preizkusite

Prepričajmo se, da naš MCP strežnik deluje kot je mišljeno.

> [!NOTE]
> Azure API Management trenutno izpostavlja ta strežnik prek Streamable
> HTTP `/mcp` končne točke. Stari HTTP+SSE `/sse` prenos je zastarel in
> naj se uporablja le z zastarelimi odjemalci.

Za to bomo uporabili Visual Studio Code in GitHub Copilot v Agent načinu. Dodali bomo MCP strežnik v *mcp.json* datoteko. Na ta način bo Visual Studio Code deloval kot odjemalec z agentnimi zmožnostmi in končni uporabniki bodo lahko vtipkali poziv in komunicirali s tem strežnikom.

Poglejmo, kako dodati MCP strežnik v Visual Studio Code:

1. Uporabite ukaz MCP: **Dodaj strežnik iz ukazne palete**.

1. Ko vas system vpraša, izberite tip strežnika: **HTTP (HTTP ali Server Sent Events)**.

1. Vnesite Streamable HTTP URL, prikazan za MCP strežnik v upravljanju API.
    Na primer:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Vnesite ID strežnika po svoji izbiri. To ni pomembna vrednost, a vam bo pomagala zapomniti, kaj je ta primer strežnika.

1. Izberite, ali želite shraniti konfiguracijo v nastavitve delovnega prostora ali uporabniške nastavitve.

  - **Nastavitve delovnega prostora** - konfiguracija strežnika se shrani v datoteko .vscode/mcp.json, ki je na voljo samo v trenutnem delovnem prostoru.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Uporabniške nastavitve** - konfiguracija strežnika je dodana v vašo globalno *settings.json* datoteko in je na voljo v vseh delovnih prostorih. Konfiguracija izgleda približno tako:

    ![Uporabniška nastavitev](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Prav tako morate dodati konfiguracijo, glavo, da se zagotovi pravilna avtorizacija proti Azure API Management. Uporablja glavo z imenom **Ocp-Apim-Subscription-Key**.

    - Tako jo lahko dodate v nastavitve:

    ![Dodajanje glave za avtorizacijo](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), to bo povzročilo, da se prikaže poziv, ki vas bo vprašal za vrednost API ključa, ki ga najdete v Azure portalu za vaš primer Azure API Management.

   - Če jo želite dodati raje v *mcp.json*, jo lahko dodate tako:

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

### Uporaba Agent načina

Zdaj smo pripravljeni bodisi v nastavitvah ali v *.vscode/mcp.json*. Preizkusimo.

Morala bi biti ikona Orodij, kjer so navedena izpostavljena orodja vašega strežnika:

![Orodja iz strežnika](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Kliknite ikono orodij in videli boste seznam orodij, kot sledi:

    ![Orodja](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. V klepet vnesite poziv za klic orodja. Na primer, če ste izbrali orodje za pridobivanje informacij o naročilu, lahko vprašate agenta o naročilu. Tukaj je primer poziva:

    ```text
    get information from order 2
    ```

    Sedaj boste videli ikono orodij, ki vas vpraša, ali želite nadaljevati s klicem orodja. Izberite nadaljevanje izvajanja orodja, zdaj bi morali videti izhod, kot sledi:

    ![Rezultat poziva](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **kar vidite zgoraj je odvisno od tega, katera orodja ste nastavili, ampak ideja je, da dobite besedilni odgovor, kot je zgoraj**


## Reference

Tako se lahko naučite več:

- [Vodič o Azure API Management in MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python primer: Varnost oddaljenih MCP strežnikov z Azure API Management (eksperimentalno)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratorij za avtorizacijo MCP odjemalcev](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Uporaba razširitve Azure API Management za VS Code za uvoz in upravljanje API-jev](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registracija in iskanje oddaljenih MCP strežnikov v Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Odličen repozitorij, ki prikazuje številne AI zmožnosti z Azure API Management
- [Delavnice AI Gateway](https://azure-samples.github.io/AI-Gateway/) Vsebuje delavnice z uporabo Azure Portala, kar je odličen način za začetek ocenjevanja AI zmožnosti.

## Kaj sledi

- Nazaj na: [Pregled študij primerov](./README.md)
- Naprej: [Azure AI potovalni agenti](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->