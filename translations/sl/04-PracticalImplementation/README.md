# Praktična izvedba

[![Kako zgraditi, preizkusiti in namestiti MCP aplikacije z resničnimi orodji in delovnimi tokovi](../../../translated_images/sl/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Kliknite zgornjo sliko za ogled posnetka tega poglavja)_

Praktična izvedba je tam, kjer moč Model Context Protocol (MCP) postane otipljiva. Medtem ko je razumevanje teorije in arhitekture za MCP pomembno, se prava vrednost pokaže, ko te koncepte uporabite za izdelavo, testiranje in namestitev rešitev, ki rešujejo probleme iz resničnega sveta. To poglavje premošča vrzel med konceptualnim znanjem in praktičnim razvojem ter vas vodi skozi postopek uresničitve aplikacij temelječih na MCP.

Ne glede na to, ali razvijate inteligentne asistente, integrirate AI v poslovne delovne tokove ali gradite prilagojena orodja za obdelavo podatkov, MCP ponuja prilagodljivo podlago. Njegova jezikovno neodvisna zasnova in uradne SDK knjižnice za priljubljene programske jezike omogočajo dostop širokemu krogu razvijalcev. Z uporabo teh SDK knjižnic lahko hitro izdelate prototipe, iterirate in skalirate svoje rešitve na različnih platformah in okoljih.

V spodnjih razdelkih boste našli praktične primere, vzorčno kodo in strategije namestitve, ki prikazujejo, kako implementirati MCP v C#, Javi s Springom, TypeScriptu, JavaScriptu in Pythonu. Naučili se boste tudi, kako odkrivati in testirati svoje MCP strežnike, upravljati API-je ter nameščati rešitve v oblak preko Azure. Ti praktični viri so zasnovani, da pospešijo vaše učenje in vam pomagajo samozavestno graditi robustne, produkcijsko pripravljene MCP aplikacije.

## Pregled

To poglavje se osredotoča na praktične vidike implementacije MCP v več programskih jezikih. Raziskali bomo, kako uporabljati MCP SDK-je v C#, Javi s Springom, TypeScriptu, JavaScriptu in Pythonu za izdelavo robustnih aplikacij, odkrivanje in testiranje MCP strežnikov ter ustvarjanje ponovno uporabnih virov, pozivov (promptov) in orodij.

## Cilji učenja

Do konca tega poglavja boste znali:

- Implementirati MCP rešitve z uradnimi SDK-ji v različnih programskih jezikih
- Sistematično odkrivati in testirati MCP strežnike
- Ustvarjati in uporabljati funkcije strežnika (viri, pozivi in orodja)
- Načrtovati učinkovite MCP delovne tokove za kompleksne naloge
- Optimizirati MCP implementacije za zmogljivost in zanesljivost

## Uradni SDK viri

Model Context Protocol ponuja uradne SDK-je za več jezikov (skladen z [MCP specifikacijo 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java s Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **Opomba:** zahteva odvisnost od [Project Reactor](https://projectreactor.io). (Glej [diskusijo z istatkom 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## Delo z MCP SDK-ji

Ta razdelek ponuja praktične primere implementacije MCP v več programskih jezikih. V mapi `samples` lahko najdete vzorčno kodo razvrščeno po jezikih.

### Razpoložljivi primeri

Repozitorij vključuje [vzorce implementacij](../../../04-PracticalImplementation/samples) v naslednjih jezikih:

- [C#](./samples/csharp/README.md)
- [Java s Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Vsak vzorec prikazuje ključne koncepte MCP in vzorce implementacije za določen jezik in ekosistem.

### Praktični vodiči

Dodatni vodiči za praktično implementacijo MCP:

- [Straničenje in obsežni nabori rezultatov](./pagination/README.md) - Ravnanje s straničenjem, osnovanim na kazalcih za orodja, vire in velike podatkovne nize

## Osnovne funkcionalnosti strežnika

MCP strežniki lahko implementirajo katerokoli kombinacijo teh funkcij:

### Viri

Viri zagotavljajo kontekst in podatke za uporabnika ali AI model:

- Repozitoriji dokumentov
- Baze znanja
- Strukturirani podatkovni viri
- Datotečni sistemi

### Pozivi

Pozivi so predloge sporočil in delovnih tokov za uporabnike:

- Vnaprej definirani predlogi pogovorov
- Vodeni vzorci interakcij
- Specializirane strukture dialoga

### Orodja

Orodja so funkcije, ki jih AI model izvaja:

- Orodja za obdelavo podatkov
- Integracije z zunanjimi API-ji
- Računske sposobnosti
- Funkcionalnost iskanja

## Vzorčne implementacije: Implementacija v C#

Uradni repozitorij C# SDK vsebuje več vzorčnih implementacij, ki prikazujejo različne vidike MCP:

- **Osnovni MCP odjemalec**: preprost primer, ki prikazuje, kako ustvariti MCP odjemalca in klicati orodja
- **Osnovni MCP strežnik**: minimalna implementacija strežnika z osnovno registracijo orodij
- **Napredni MCP strežnik**: polno opremljen strežnik z registracijo orodij, avtorizacijo in obravnavo napak
- **Integracija ASP.NET**: primeri prikaza integracije z ASP.NET Core
- **Vzorce implementacije orodij**: različne vzorce za implementacijo orodij z različno stopnjo kompleksnosti

MCP C# SDK je v predogledni fazi in API-ji se lahko spremenijo. Ta blog bomo sproti posodabljali glede na razvoj SDK-ja.

### Ključne funkcije

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Gradnja vašega [prvega MCP strežnika](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Za popolne vzorce implementacije v C# obiščite [uradne C# SDK vzorce](https://github.com/modelcontextprotocol/csharp-sdk)

## Vzorčna implementacija: Implementacija Java s Springom

Java s Spring SDK ponuja robustne možnosti implementacije MCP z lastnostmi na ravni podjetja.

### Ključne funkcije

- Integracija Spring Frameworka
- Močna tipna varnost
- Podpora za reaktivno programiranje
- Celovita obravnava napak

Za popoln vzorec implementacije Java s Springom si oglejte [Java s Spring vzorec](samples/java/containerapp/README.md) v mapi vzorcev.

## Vzorčna implementacija: Implementacija JavaScript

JavaScript SDK nudi lahek in prilagodljiv pristop k implementaciji MCP.

### Ključne funkcije

- Podpora za Node.js in brskalnik
- API temelječ na Promise-jih
- Enostavna integracija z Express in drugimi okviri
- Podpora WebSocketom za pretočne podatke

Za popoln JavaScript vzorec implementacije si oglejte [JavaScript vzorec](samples/javascript/README.md) v mapi vzorcev.

## Vzorčna implementacija: Implementacija Python

Python SDK ponuja pythonovski pristop k implementaciji MCP z odlično integracijo ML okvirjev.

### Ključne funkcije

- Podpora async/await z asyncio
- Integracija FastAPI
- Enostavna registracija orodij
- Naravna integracija s priljubljenimi ML knjižnicami

Za popoln Python vzorec implementacije si oglejte [Python vzorec](samples/python/README.md) v mapi vzorcev.

## Upravljanje API-jev

Azure API Management je odličen odgovor na vprašanje, kako zaščititi MCP strežnike. Ideja je, da postavite Azure API Management instanco pred svoj MCP strežnik in ji dovolite, da upravlja funkcije, ki jih boste verjetno želeli, kot so:

- omejevanje hitrosti
- upravljanje žetonov
- nadzor
- uravnoteženje obremenitev
- varnost

### Azure vzorec

Tukaj je Azure vzorec, ki počne natanko to, torej [ustvarja MCP strežnik in ga ščiti z Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Oglejte si, kako poteka avtentikacija na spodnji sliki:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Na zgornji sliki se dogaja:

- Avtentikacija/avtorizacija poteka preko Microsoft Entra.
- Azure API Management deluje kot prehod in uporablja politike za usmerjanje ter upravljanje prometa.
- Azure Monitor beleži vse zahtevke za nadaljnjo analizo.

#### Potek avtorizacije

Poglejmo si podrobneje avtorizacijski potek:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP specifikacija avtorizacije

Več o [MCP specifikaciji avtorizacije](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Namestitev oddaljenega MCP strežnika v Azure

Poglejmo, ali lahko namestimo vzorec, ki smo ga omenili prej:

1. Klonirajte repozitorij

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Registrirajte `Microsoft.App` ponudnika virov.

   - Če uporabljate Azure CLI, zaženite `az provider register --namespace Microsoft.App --wait`.
   - Če uporabljate Azure PowerShell, zaženite `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Nato po določenem času preverite stanje z ukazom `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState`.

1. Zaženite ta [azd](https://aka.ms/azd) ukaz, da zagotovite storitve za upravljanje API-jev, funkcijsko aplikacijo (s kodo) in vse druge potrebne Azure vire

    ```shell
    azd up
    ```

    Ta ukaz bi moral namestiti vse oblačne vire v Azure

### Preizkušanje vašega strežnika z MCP Inspector

1. V **novem terminalskem oknu** namestite in zaženite MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Videli bi vmesnik, podoben temu:

    ![Povezava na Node inspector](../../../translated_images/sl/connect.141db0b2bd05f096.webp)

1. CTRL kliknite, da naložite MCP Inspector spletno aplikacijo iz URL-ja, prikazanega v aplikaciji (npr. [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Nastavite tip prenosa na `SSE`
1. Nastavite URL na vaš aktivni API Management SSE endpoint, prikazan po ukazu `azd up` in kliknite **Poveži**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Prikaži orodja**.  Kliknite na orodje in **Zaženi orodje**.  

Če so vsi koraki uspeli, bi morali biti zdaj povezani z MCP strežnikom in lahko ste poklicali orodje.

## MCP strežniki za Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): ta nabor repozitorijev služi kot začetni predloga za izdelavo in namestitev prilagojenih oddaljenih MCP (Model Context Protocol) strežnikov z uporabo Azure Functions v Pythonu, C# .NET ali Node/TypeScript.

Vzorce ponuja popolno rešitev, ki razvijalcem omogoča:

- Gradnjo in lokalno zagon: Razvijajte in odkrivajte MCP strežnik na lokalnem računalniku
- Namestitev v Azure: enostavna namestitev v oblak z ukazom azd up
- Povezovanje s klienti: Povežite se z MCP strežnikom iz različnih klientov, vključno z načinom agent Copilot v VS Code in orodjem MCP Inspector

### Ključne funkcije

- Varnost zasnovana v osnovi: MCP strežnik je zaščiten z ključi in HTTPS
- Možnosti avtorizacije: podpira OAuth z vgrajeno avtorizacijo in/ali API Managementom
- Omrežna izolacija: omogoča izolacijo omrežja z uporabo Azure Virtual Networks (VNET)
- Brezstrežniška arhitektura: uporablja Azure Functions za skalabilno, dogodkovno usmerjeno izvajanje
- Lokalni razvoj: celovita podpora za lokalni razvoj in odpravljanje napak
- Enostavna namestitev: poenostavljen postopek namestitve v Azure

Repozitorij vključuje vse potrebne konfiguracijske datoteke, izvorno kodo in definicije infrastrukture za hitro začetek s produkcijsko pripravljeno MCP implementacijo strežnika.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Vzorčna implementacija MCP z uporabo Azure Functions v Pythonu

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Vzorčna implementacija MCP z uporabo Azure Functions v C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Vzorčna implementacija MCP z uporabo Azure Functions v Node/TypeScript.

## Ključne ugotovitve

- MCP SDK-ji nudijo jeziku specifična orodja za implementacijo robustnih MCP rešitev
- Proces odkrivanja in testiranja je ključnega pomena za zanesljive MCP aplikacije
- Ponovno uporabne predloge pozivov omogočajo konsistentne AI interakcije
- Dobro zasnovani delovni tokovi lahko orkestrirajo kompleksne naloge z uporabo več orodij
- Implementacija MCP rešitev zahteva upoštevanje varnosti, zmogljivosti in obravnave napak

## Naloga

Oblikujte praktičen MCP delovni tok, ki rešuje problem iz vašega področja:

1. Identificirajte 3-4 orodja, ki bi bila uporabna za rešitev tega problema
2. Ustvarite diagram delovnega toka, ki prikazuje, kako ta orodja medsebojno sodelujejo
3. Implementirajte osnovno verzijo enega od orodij v vašem priljubljenem jeziku
4. Ustvarite predlogo poziva, ki bi pomagala modelu učinkovito uporabiti vaše orodje

## Dodatni viri

---

## Kaj sledi

Naprej: [Napredne teme](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvorni jezik naj velja za avtoritativni vir. Za kritične informacije priporočamo strokovni človeški prevod. Nismo odgovorni za nobena nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->