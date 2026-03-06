# Praktična implementacija

[![Kako izgraditi, testirati i implementirati MCP aplikacije s pravim alatima i radnim procesima](../../../translated_images/hr/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Kliknite na gornju sliku za pregled video lekcije)_

Praktična implementacija je mjesto gdje snaga Model Context Protocola (MCP) postaje opipljiva. Dok je razumijevanje teorije i arhitekture iza MCP-a važno, prava vrijednost se pojavljuje kada ove koncepte primijenite za izgradnju, testiranje i implementaciju rješenja koja rješavaju stvarne probleme. Ovo poglavlje premošćuje jaz između konceptualnog znanja i praktičnog razvoja, vodeći vas kroz proces oživljavanja aplikacija temeljenih na MCP-u.

Bilo da razvijate inteligentne asistente, integrirate AI u poslovne radne procese ili gradite prilagođene alate za obradu podataka, MCP pruža fleksibilnu osnovu. Njegov dizajn neovisnih o jeziku i službeni SDK-ovi za popularne programske jezike čine ga dostupnim širokom krugu programera. Koristeći ove SDK-ove, možete brzo napraviti prototip, iterirati i skalirati svoja rješenja na različitim platformama i okruženjima.

U sljedećim odjeljcima pronaći ćete praktične primjere, uzorak koda i strategije implementacije koje pokazuju kako implementirati MCP u C#, Java s Springom, TypeScript, JavaScript i Python. Također ćete naučiti kako otklanjati pogreške i testirati svoje MCP servere, upravljati API-jima i implementirati rješenja u oblak koristeći Azure. Ovi praktični resursi dizajnirani su da ubrzaju vaše učenje i pomognu vam da samouvjereno izgradite robusne, proizvodno spremne MCP aplikacije.

## Pregled

Ova lekcija se fokusira na praktične aspekte implementacije MCP-a u više programskih jezika. Istražit ćemo kako koristiti MCP SDK-ove u C#, Java sa Springom, TypeScriptu, JavaScriptu i Pythonu za izgradnju robusnih aplikacija, otklanjanje pogrešaka i testiranje MCP servera te kreiranje ponovljivih resursa, promptova i alata.

## Ciljevi učenja

Do kraja ove lekcije, moći ćete:

- Implementirati MCP rješenja koristeći službene SDK-ove u različitim programskim jezicima
- Sistematski otklanjati pogreške i testirati MCP servere
- Kreirati i koristiti značajke servera (Resurse, Prompte i Alate)
- Dizajnirati učinkovite MCP radne procese za složene zadatke
- Optimizirati MCP implementacije za performanse i pouzdanost

## Službeni SDK resursi

Model Context Protocol nudi službene SDK-ove za više jezika (usklađene s [MCP specifikacijom 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java sa Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **Napomena:** zahtijeva ovisnost o [Project Reactor](https://projectreactor.io). (Vidi [raspravu issue 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## Rad s MCP SDK-ovima

Ovaj odjeljak daje praktične primjere implementacije MCP-a u više programskih jezika. Uzorak koda možete pronaći u direktoriju `samples` organiziranom prema jezicima.

### Dostupni uzorci

Repozitorij uključuje [uzorke implementacija](../../../04-PracticalImplementation/samples) u sljedećim jezicima:

- [C#](./samples/csharp/README.md)
- [Java sa Springom](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Svaki uzorak pokazuje ključne MCP koncepte i obrasce implementacije za taj specifični jezik i ekosustav.

### Praktični vodiči

Dodatni vodiči za praktičnu MCP implementaciju:

- [Paginacija i veliki skupovi rezultata](./pagination/README.md) - Upravljanje paginacijom temeljenu na pokazivačima za alate, resurse i velike skupove podataka

## Ključne značajke servera

MCP serveri mogu implementirati bilo koju kombinaciju ovih značajki:

### Resursi

Resursi pružaju kontekst i podatke za korisnika ili AI model:

- Spremišta dokumenata
- Baze znanja
- Strukturirani izvori podataka
- Datotečni sustavi

### Prompti

Prompti su predlošci poruka i radnih procesa za korisnike:

- Preddefinirani predlošci razgovora
- Vođeni obrasci interakcije
- Specijalizirane strukture dijaloga

### Alati

Alati su funkcije koje AI model izvršava:

- Pomoćni alati za obradu podataka
- Integracije s vanjskim API-jima
- Računalne sposobnosti
- Funkcionalnost pretraživanja

## Primjeri implementacija: C# implementacija

Službeni repozitorij C# SDK-a sadrži nekoliko primjera implementacija koji pokazuju različite aspekte MCP-a:

- **Osnovni MCP klijent**: Jednostavan primjer kako napraviti MCP klijenta i pozvati alate
- **Osnovni MCP server**: Minimalna implementacija servera s osnovnom registracijom alata
- **Napredni MCP server**: Server s punim značajkama, uključujući registraciju alata, autentikaciju i rukovanje greškama
- **Integracija s ASP.NET-om**: Primjeri integracije s ASP.NET Coreom
- **Obrasci implementacije alata**: Razni obrasci za implementaciju alata različitih razina složenosti

MCP C# SDK je u pretpregledu i API-ji se mogu mijenjati. Nastavit ćemo ažurirati ovaj blog kako se SDK razvija.

### Ključne značajke

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Izgradnja vašeg [prvog MCP servera](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Za kompletne uzorke C# implementacije posjetite [službeni repozitorij C# SDK primjera](https://github.com/modelcontextprotocol/csharp-sdk)

## Primjer implementacije: Java sa Springom

Java sa Spring SDK nudi robusne opcije MCP implementacije s enterprise značajkama.

### Ključne značajke

- Integracija sa Spring Frameworkom
- Snažna tipna sigurnost
- Podrška za reaktivno programiranje
- Sveobuhvatno rukovanje pogreškama

Za kompletan primjer implementacije Java sa Springom pogledajte [Java with Spring sample](samples/java/containerapp/README.md) u direktoriju uzoraka.

## Primjer implementacije: JavaScript implementacija

JavaScript SDK pruža lagani i fleksibilan pristup MCP implementaciji.

### Ključne značajke

- Podrška za Node.js i preglednik
- Promise baziran API
- Jednostavna integracija s Expressom i drugim frameworkima
- Podrška za WebSocket za streaming

Za kompletan primjer JavaScript implementacije pogledajte [JavaScript sample](samples/javascript/README.md) u direktoriju uzoraka.

## Primjer implementacije: Python implementacija

Python SDK nudi pitonski pristup MCP implementaciji s izvrsnim integracijama ML okvira.

### Ključne značajke

- Podrška za async/await s asyncio
- Integracija s FastAPI-jem
- Jednostavna registracija alata
- Izvorna integracija s popularnim ML bibliotekama

Za kompletan primjer Python implementacije pogledajte [Python sample](samples/python/README.md) u direktoriju uzoraka.

## Upravljanje API-jima

Azure API Management je sjajno rješenje za sigurno upravljanje MCP serverima. Ideja je staviti instancu Azure API Managementa ispred vašeg MCP servera i dopustiti mu da upravlja značajkama koje ćete vjerojatno željeti poput:

- ograničenja brzine
- upravljanja tokenima
- nadzor
- balansiranje opterećenja
- sigurnost

### Azure uzorak

Evo jednog Azure uzorka koji točno to radi, tj. [stvara MCP server i osigurava ga pomoću Azure API Managementa](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Pogledajte kako se odvija autorizacijski tijek na donjoj slici:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Na prethodnoj slici događa se sljedeće:

- Autentikacija/Autorizacija se odvija korištenjem Microsoft Entra.
- Azure API Management djeluje kao ulazna točka i koristi politike za usmjeravanje i upravljanje prometom.
- Azure Monitor bilježi sve zahtjeve za daljnju analizu.

#### Tijek autorizacije

Pogledajmo tijek autorizacije detaljnije:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP specifikacija autorizacije

Saznajte više o [MCP specifikaciji autorizacije](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Implementacija udaljenog MCP servera u Azure

Pogledajmo možemo li implementirati ranije spomenuti uzorak:

1. Klonirajte repozitorij

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Registrirajte `Microsoft.App` resource providera.

   - Ako koristite Azure CLI, pokrenite `az provider register --namespace Microsoft.App --wait`.
   - Ako koristite Azure PowerShell, pokrenite `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Zatim pokrenite `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` nakon nekog vremena da provjerite je li registracija završena.

1. Pokrenite ovu [azd](https://aka.ms/azd) naredbu za provisioning servisa za upravljanje API-jima, funkcijske aplikacije (s kodom) i svih ostalih potrebnih Azure resursa

    ```shell
    azd up
    ```

     Ova naredba bi trebala implementirati sve cloud resurse na Azureu

### Testiranje vašeg servera s MCP Inspectorom

1. U **novom terminal prozoru**, instalirajte i pokrenite MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

     Trebali biste vidjeti sučelje slično:

    ![Connect to Node inspector](../../../translated_images/hr/connect.141db0b2bd05f096.webp)

1. Kliknite CTRL i otvorite MCP Inspector web aplikaciju s URL-a kojeg aplikacija prikazuje (npr. [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Postavite tip transporta na `SSE`
1. Postavite URL na vaš pokrenuti API Management SSE endpoint prikazan nakon `azd up` i **Povežite se**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Lista alata**. Kliknite na alat i **Pokreni alat**.

Ako su svi koraci uspjeli, sada ste povezani s MCP serverom i uspjeli ste pozvati alat.

## MCP serveri za Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Ovaj skup repozitorija su predlošci za brzo pokretanje izgradnje i implementacije prilagođenih udaljenih MCP (Model Context Protocol) servera koristeći Azure Functions s Python, C# .NET ili Node/TypeScript.

Uzorci pružaju kompletno rješenje koje developerima omogućuje:

- Izgradnju i lokalno pokretanje: razvoj i otklanjanje pogrešaka MCP servera na lokalnom računalu
- Implementaciju u Azure: jednostavnu implementaciju u oblak jednim naredbom azd up
- Povezivanje s klijentima: povezivanje s MCP serverom s raznim klijentima uključujući VS Code-ov Copilot agent mod i MCP Inspector alat

### Ključne značajke

- Sigurnost dizajnirana od početka: MCP server je zaštićen ključevima i HTTPS-om
- Opcije autentikacije: podržava OAuth koristeći ugrađenu autentikaciju i/ili API Management
- Izolacija mreže: omogućava mrežnu izolaciju koristeći Azure Virtual Networks (VNET)
- Serverless arhitektura: koristi Azure Functions za skalabilno, event-driven izvršavanje
- Lokalni razvoj: sveobuhvatna podrška za lokalni razvoj i otklanjanje pogrešaka
- Jednostavna implementacija: pojednostavljen proces implementacije u Azure

Repozitorij uključuje sve potrebne konfiguracijske datoteke, izvorni kod i definicije infrastrukture za brzo započinjanje proizvodno spremne MCP implementacije servera.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Primjer implementacije MCP koristeći Azure Functions sa Pythonom

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Primjer implementacije MCP koristeći Azure Functions s C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Primjer implementacije MCP koristeći Azure Functions s Node/TypeScript.

## Ključne lekcije

- MCP SDK-ovi pružaju jezično specifične alate za implementaciju robusnih MCP rješenja
- Proces otklanjanja pogrešaka i testiranja kritičan je za pouzdane MCP aplikacije
- Ponovno upotrebljivi prompt predlošci omogućuju konzistentne AI interakcije
- Dobro dizajnirani radni procesi mogu orkestrirati složene zadatke koristeći više alata
- Implementacija MCP rješenja zahtijeva razmatranje sigurnosti, performansi i rukovanja greškama

## Vježba

Dizajnirajte praktičan MCP radni proces koji rješava stvarni problem u vašem području:

1. Identificirajte 3-4 alata koji bi bili korisni za rješavanje tog problema
2. Kreirajte dijagram radnog procesa koji prikazuje kako ti alati međusobno djeluju
3. Implementirajte osnovnu verziju jednog od alata u vašem preferiranom jeziku
4. Kreirajte prompt predložak koji bi pomogao modelu da učinkovito koristi vaš alat

## Dodatni resursi

---

## Što slijedi

Sljedeće: [Napredne teme](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Izjava o odricanju od odgovornosti**:
Ovaj dokument je preveden pomoću AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, molimo imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->