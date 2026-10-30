# Študija primera: Izpostavitev REST API-ja v upravljanju API-jev kot MCP strežnik

Azure API Management je storitev, ki zagotavlja prehod (Gateway) nad vašimi API končnimi točkami. Delovanje je takšno, da Azure API Management deluje kot proxy pred vašimi API-ji in lahko odloča, kaj storiti z dohodnimi zahtevki.

Z njegovo uporabo dodate številne funkcije, kot so:

- **Varnost**, lahko uporabljate vse od API ključev, JWT do upravljane identitete.
- **Omejevanje hitrosti**, odlična funkcija je možnost odločanja, koliko klicev lahko pride skozi v določeni časovni enoti. To pomaga zagotoviti odlično uporabniško izkušnjo za vse in prepreči preobremenitev storitve z zahtevki.
- **Prilagajanje in uravnoteženje obremenitve**. Lahko nastavite več končnih točk za uravnoteženje obremenitve in prav tako določite način "uravnoteženja obremenitve".
- **AI funkcije, kot so semantični predpomnilnik**, omejitev žetonov in nadzor žetonov ter več. Te odlične funkcije izboljšujejo odzivnost in pomagajo nadzorovati porabo žetonov. [Več preberite tukaj](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Zakaj MCP + Azure API Management?

Protokol Model Context hitro postaja standard za agentne AI aplikacije in za izpostavljanje orodij ter podatkov na konsistenten način. Azure API Management je naravna izbira, ko potrebujete "upravljanje" API-jev. MCP strežniki se pogosto integrirajo z drugimi API-ji, da denimo rešijo zahteve do orodja. Zato kombinacija Azure API Management in MCP logično povsem drži.

## Pregled

V tem specifičnem primeru bomo spoznali, kako izpostaviti API končne točke kot MCP strežnik. Tako lahko te končne točke enostavno uporabljamo kot del agentne aplikacije in hkrati izkoristimo funkcije Azure API Managementa.

## Ključne funkcije

- Izberete metode končnih točk, ki jih želite izpostaviti kot orodja.
- Dodatne funkcije, ki jih dobite, so odvisne od tega, kaj nastavite v pravilnikih za vaš API. Tukaj bomo prikazali, kako dodati omejevanje hitrosti.

## Predpriprava: uvoz API-ja

Če že imate API v Azure API Management, super, ta korak lahko preskočite. Če ne, si oglejte ta povezavo, [uvoz API-ja v Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Izpostavitev API-ja kot MCP strežnik

Za izpostavitev API končnih točk sledite tem korakom:

1. Pojdite na Azure Portal na naslov <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
Pojdite v svojo Azure API Management instanco.

1. V levem meniju izberite APIs > MCP Servers > + Create new MCP Server.

1. Pri API-ju izberite REST API za izpostavitev kot MCP strežnik.

1. Izberite eno ali več operacij API-ja za izpostavitev kot orodja. Izbirate lahko vse operacije ali samo določene.

    ![Izberi metode za izpostavitev](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Kliknite **Create**.

1. Pojdite v meni **APIs** in **MCP Servers**, kjer bi morali videti naslednje:

    ![Poglej MCP strežnik v glavnem oknu](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP strežnik je ustvarjen in API operacije so izpostavljene kot orodja. MCP strežnik je na voljo v pogledu MCP Servers. Stolpec URL prikazuje končno točko MCP strežnika, ki jo lahko pokličete za testiranje ali v odjemalski aplikaciji.

## Neobvezno: Konfiguracija pravilnikov

Azure API Management ima osnovni koncept pravilnikov, kjer nastavljate različna pravila za svoje končne točke, kot na primer omejevanje hitrosti ali semantični predpomnilnik. Ti pravilniki so napisani v XML-ju.

Tukaj je, kako lahko nastavite pravilnik za omejevanje hitrosti vašega MCP strežnika:

1. V portalu v razdelku APIs izberite **MCP Servers**.

1. Izberite MCP strežnik, ki ste ga ustvarili.

1. V levem meniju pod MCP izberite **Policies**.

1. V urejevalniku pravilnikov dodajte ali uredite pravilnike, ki jih želite uporabiti za orodja MCP strežnika. Pravilniki so definirani v formatu XML. Na primer, lahko dodate pravilnik za omejitev klicev do orodij MCP strežnika (v tem primeru 5 klicev na 30 sekund na IP naslov odjemalca). Tukaj je XML, ki bo omejil hitrost:

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

Prepričajmo se, da naš MCP strežnik deluje kot je predvideno.

> [!NOTE]
> Azure API Management trenutno izpostavlja ta strežnik preko vmesnika Streamable
> HTTP `/mcp`. Starejši HTTP+SSE `/sse` prenos je zastarel in
> naj se uporablja le z legacijski odjemalci.

Za to bomo uporabili Visual Studio Code in GitHub Copilot ter njegov Agent način. MCP strežnik bomo dodali v datoteko *mcp.json*. Tako bo Visual Studio Code deloval kot odjemalec z agentnimi zmogljivostmi in končni uporabniki bodo lahko vnesli poziv in komunicirali s tem strežnikom.

Poglejmo, kako dodati MCP strežnik v Visual Studio Code:

1. Uporabite ukaz MCP: **Add Server iz Command Palette**.

1. Ko vas vpraša, izberite vrsto strežnika: **HTTP (HTTP ali Server Sent Events)**.

1. Vnesite Streamable HTTP URL, ki je prikazan za MCP strežnik v API Managementu.
    Na primer:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Vnesite ID strežnika po svoje želji. To ni ključna vrednost, a pomaga pri prepoznavanju instance strežnika.

1. Izberite, ali shranite konfiguracijo v nastavitve delovnega prostora ali uporabniške nastavitve.

    - **Nastavitve delovnega prostora** - konfiguracija strežnika se shrani v datoteko `.vscode/mcp.json`, ki je na voljo samo v trenutnem delovnem prostoru.

      *mcp.json*

      ```json
      "servers": {
          "APIM petstore" : {
              "type": "http",
              "url": "url-to-mcp-server/mcp"
          }
      }
      ```

    - **Uporabniške nastavitve** - konfiguracija strežnika je dodana v globalno datoteko *settings.json* in je na voljo v vseh delovnih prostorih. Konfiguracija je videti takole:

      ![Uporabniška nastavitev](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Prav tako morate dodati glavo konfiguracije, da se ustrezno avtenticira proti Azure API Management. Uporablja glavo z imenom **Ocp-Apim-Subscription-Key**.

    - Tukaj je, kako jo lahko dodate v nastavitve:


    ![Dodajanje glave za avtentikacijo](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), kar bo povzročilo, da se prikaže poziv za vnos vrednosti API ključa, ki ga najdete v Azure portalu za vašo Azure API Management instanco.

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

Sedaj smo nastavljeni bodisi v nastavitvah ali v *.vscode/mcp.json*. Poskusimo.

Ikona Orodij (Tools) bi morala izgledati takole, kjer so našteta orodja, ki jih strežnik izpostavlja:

![Orodja s strežnika](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Kliknite ikono orodij in videli boste seznam orodij, kot je ta:

    ![Orodja](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Vnesite poziv v klepet, da pokličete orodje. Na primer, če ste izbrali orodje za pridobitev informacij o naročilu, lahko agenta vprašate o naročilu. Tukaj je primer poziva:

    ```text
    get information from order 2
    ```

    Zdaj vam bo prikazana ikona orodij, ki vas bo vprašala, ali želite nadaljevati s klicanjem orodja. Izberite za nadaljevanje, prikazan bo izhod, kot je ta:

    ![Rezultat poziva](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **To, kar vidite zgoraj, je odvisno od orodij, ki ste jih nastavili, vendar je ideja, da dobite tekstovni odgovor, kot zgoraj**


## Viri

Tukaj je, kako se lahko naučite več:

- [Vadnica o Azure API Management in MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Vzorec v Pythonu: Varnost oddaljenih MCP strežnikov z Azure API Management (eksperimentalno)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratorij za odobritev MCP odjemalca](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Uporaba razširitve Azure API Management za VS Code za uvoz in upravljanje API-jev](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registracija in odkrivanje oddaljenih MCP strežnikov v Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Odličen repozitorij, ki prikazuje številne AI zmogljivosti z Azure API Managementom
- [Delavnice AI Gateway](https://azure-samples.github.io/AI-Gateway/) Vsebuje delavnice, ki uporabljajo Azure Portal, kar je odličen način za začetek ocenjevanja AI zmogljivosti.

## Kaj sledi

- Nazaj na: [Pregled študij primerov](./README.md)
- Naprej: [Azure AI potovalni agenti](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->