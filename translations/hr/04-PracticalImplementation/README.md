# Praktična Implementacija

[![Kako izgraditi, testirati i implementirati MCP aplikacije koristeći stvarne alate i radne procese](../../../translated_images/hr/05.64bea204e25ca891e3dd8b8f960d2170b9a000d8364305f57db3ec4a2c049a9a.png)](https://youtu.be/vCN9-mKBDfQ)

_(Kliknite na sliku iznad za video lekciju)_

Praktična implementacija je mjesto gdje snaga Model Context Protocola (MCP) postaje opipljiva. Dok je razumijevanje teorije i arhitekture MCP-a važno, prava vrijednost dolazi kada primijenite te koncepte za izgradnju, testiranje i implementaciju rješenja koja rješavaju stvarne probleme. Ovo poglavlje povezuje konceptualno znanje s praktičnim razvojem, vodeći vas kroz proces stvaranja aplikacija temeljenih na MCP-u.

Bilo da razvijate inteligentne asistente, integrirate AI u poslovne procese ili gradite prilagođene alate za obradu podataka, MCP pruža fleksibilnu osnovu. Njegov dizajn neovisan o jeziku i službeni SDK-ovi za popularne programske jezike čine ga dostupnim širokom spektru programera. Korištenjem ovih SDK-ova možete brzo prototipirati, iterirati i skalirati svoja rješenja na različitim platformama i okruženjima.

U sljedećim odjeljcima pronaći ćete praktične primjere, uzorke koda i strategije implementacije koje demonstriraju kako primijeniti MCP u C#, Java s Springom, TypeScriptu, JavaScriptu i Pythonu. Također ćete naučiti kako otkloniti pogreške i testirati MCP servere, upravljati API-ima i implementirati rješenja u oblaku koristeći Azure. Ovi praktični resursi osmišljeni su kako bi ubrzali vaše učenje i pomogli vam da s povjerenjem izgradite robusne MCP aplikacije spremne za produkciju.

## Pregled

Ova lekcija fokusira se na praktične aspekte implementacije MCP-a u više programskih jezika. Istražit ćemo kako koristiti MCP SDK-ove u C#, Java s Springom, TypeScriptu, JavaScriptu i Pythonu za izgradnju robusnih aplikacija, otklanjanje pogrešaka i testiranje MCP servera te stvaranje resursa, upita i alata koji se mogu ponovno koristiti.

## Ciljevi učenja

Na kraju ove lekcije, moći ćete:

- Implementirati MCP rješenja koristeći službene SDK-ove u raznim programskim jezicima
- Sustavno otklanjati pogreške i testirati MCP servere
- Stvarati i koristiti značajke servera (Resursi, Upiti i Alati)
- Dizajnirati učinkovite MCP radne procese za složene zadatke
- Optimizirati MCP implementacije za performanse i pouzdanost

## Službeni SDK resursi

Model Context Protocol nudi službene SDK-ove za više jezika:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java s Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **Napomena:** zahtijeva ovisnost o [Project Reactor](https://projectreactor.io). (Pogledajte [diskusiju pitanje 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## Rad s MCP SDK-ovima

Ovaj odjeljak pruža praktične primjere implementacije MCP-a u više programskih jezika. Uzorke koda možete pronaći u direktoriju `samples` organiziranom po jeziku.

### Dostupni uzorci

Repozitorij uključuje [uzorke implementacija](../../../04-PracticalImplementation/samples) u sljedećim jezicima:

- [C#](./samples/csharp/README.md)
- [Java s Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Svaki uzorak demonstrira ključne MCP koncepte i obrasce implementacije za taj specifični jezik i ekosustav.

## Osnovne značajke servera

MCP serveri mogu implementirati bilo koju kombinaciju ovih značajki:

### Resursi

Resursi pružaju kontekst i podatke koje korisnik ili AI model mogu koristiti:

- Repozitoriji dokumenata
- Baze znanja
- Strukturirani izvori podataka
- Datotečni sustavi

### Upiti

Upiti su predlošci poruka i radni procesi za korisnike:

- Preddefinirani predlošci razgovora
- Vođeni obrasci interakcije
- Specijalizirane strukture dijaloga

### Alati

Alati su funkcije koje AI model može izvršavati:

- Alati za obradu podataka
- Integracije vanjskih API-ja
- Računalne sposobnosti
- Funkcionalnost pretraživanja

## Uzorci implementacije: Implementacija u C#

Službeni C# SDK repozitorij sadrži nekoliko uzoraka implementacije koji demonstriraju različite aspekte MCP-a:

- **Osnovni MCP klijent**: Jednostavan primjer koji pokazuje kako stvoriti MCP klijent i pozvati alate
- **Osnovni MCP server**: Minimalna implementacija servera s osnovnom registracijom alata
- **Napredni MCP server**: Server s punim značajkama, uključujući registraciju alata, autentifikaciju i rukovanje pogreškama
- **Integracija s ASP.NET-om**: Primjeri koji demonstriraju integraciju s ASP.NET Core
- **Obrasci implementacije alata**: Razni obrasci za implementaciju alata različite složenosti

C# MCP SDK je u fazi pregleda i API-ji se mogu mijenjati. Kontinuirano ćemo ažurirati ovaj blog kako se SDK razvija.

### Ključne značajke

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Izgradnja vašeg [prvog MCP servera](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Za kompletne uzorke implementacije u C#, posjetite [službeni C# SDK repozitorij uzoraka](https://github.com/modelcontextprotocol/csharp-sdk).

## Uzorak implementacije: Implementacija u Java s Springom

Java s Spring SDK nudi robusne opcije implementacije MCP-a s značajkama na razini poduzeća.

### Ključne značajke

- Integracija s Spring Frameworkom
- Jaka sigurnost tipova
- Podrška za reaktivno programiranje
- Sveobuhvatno rukovanje pogreškama

Za kompletan uzorak implementacije u Java s Springom, pogledajte [Java s Spring uzorak](samples/java/containerapp/README.md) u direktoriju uzoraka.

## Uzorak implementacije: Implementacija u JavaScriptu

JavaScript SDK pruža lagan i fleksibilan pristup implementaciji MCP-a.

### Ključne značajke

- Podrška za Node.js i preglednike
- API temeljen na obećanjima
- Jednostavna integracija s Expressom i drugim okvirima
- Podrška za WebSocket za streaming

Za kompletan uzorak implementacije u JavaScriptu, pogledajte [JavaScript uzorak](samples/javascript/README.md) u direktoriju uzoraka.

## Uzorak implementacije: Implementacija u Pythonu

Python SDK nudi Pythonic pristup implementaciji MCP-a s izvrsnim integracijama s ML okvirima.

### Ključne značajke

- Podrška za async/await s asyncio
- Integracija s FastAPI-jem
- Jednostavna registracija alata
- Izvorna integracija s popularnim ML bibliotekama

Za kompletan uzorak implementacije u Pythonu, pogledajte [Python uzorak](samples/python/README.md) u direktoriju uzoraka.

## Upravljanje API-jem

Azure API Management je izvrsno rješenje za osiguranje MCP servera. Ideja je postaviti instancu Azure API Managementa ispred vašeg MCP servera i omogućiti joj upravljanje značajkama koje ćete vjerojatno trebati, poput:

- ograničavanja brzine
- upravljanja tokenima
- praćenja
- balansiranja opterećenja
- sigurnosti

### Azure uzorak

Evo Azure uzorka koji upravo to radi, tj. [stvara MCP server i osigurava ga pomoću Azure API Managementa](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Pogledajte kako se odvija tok autorizacije na slici ispod:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Na prethodnoj slici događa se sljedeće:

- Autentifikacija/autorizacija odvija se pomoću Microsoft Entra.
- Azure API Management djeluje kao gateway i koristi politike za usmjeravanje i upravljanje prometom.
- Azure Monitor bilježi sve zahtjeve za daljnju analizu.

#### Tok autorizacije

Pogledajmo tok autorizacije detaljnije:

![Dijagram sekvence](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### Specifikacija autorizacije MCP-a

Saznajte više o [specifikaciji autorizacije MCP-a](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow).

## Implementacija udaljenog MCP servera na Azure

Pogledajmo možemo li implementirati uzorak koji smo ranije spomenuli:

1. Klonirajte repozitorij

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Registrirajte `Microsoft.App` resursnog pružatelja.

   - Ako koristite Azure CLI, pokrenite `az provider register --namespace Microsoft.App --wait`.
   - Ako koristite Azure PowerShell, pokrenite `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Zatim nakon nekog vremena pokrenite `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` kako biste provjerili je li registracija dovršena.

1. Pokrenite ovu [azd](https://aka.ms/azd) naredbu za provisioniranje usluge upravljanja API-jem, funkcijske aplikacije (s kodom) i svih ostalih potrebnih Azure resursa

    ```shell
    azd up
    ```

    Ova naredba bi trebala implementirati sve resurse u oblaku na Azureu.

### Testiranje vašeg servera s MCP Inspectorom

1. U **novom terminalskom prozoru**, instalirajte i pokrenite MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Trebali biste vidjeti sučelje slično:

    ![Povezivanje s Node inspectorom](../../../translated_images/hr/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.png)

1. CTRL kliknite za učitavanje MCP Inspector web aplikacije s URL-a prikazanog od strane aplikacije (npr. [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources)).
1. Postavite vrstu transporta na `SSE`.
1. Postavite URL na vaš API Management SSE endpoint prikazan nakon `azd up` i **Povežite se**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Popis alata**. Kliknite na alat i **Pokrenite alat**.

Ako su svi koraci uspjeli, sada biste trebali biti povezani s MCP serverom i mogli ste pozvati alat.

## MCP serveri za Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Ovaj set repozitorija je predložak za brzo pokretanje za izgradnju i implementaciju prilagođenih udaljenih MCP (Model Context Protocol) servera koristeći Azure Functions s Pythonom, C# .NET ili Node/TypeScriptom.

Uzorci pružaju kompletno rješenje koje omogućuje programerima:

- Izgradnju i pokretanje lokalno: Razvoj i otklanjanje pogrešaka MCP servera na lokalnom računalu
- Implementaciju na Azure: Jednostavna implementacija u oblak pomoću jednostavne naredbe azd up
- Povezivanje s klijentima: Povezivanje s MCP serverom iz raznih klijenata, uključujući VS Code Copilot agent mode i MCP Inspector alat

### Ključne značajke

- Sigurnost po dizajnu: MCP server je osiguran pomoću ključeva i HTTPS-a
- Opcije autentifikacije: Podržava OAuth koristeći ugrađenu autentifikaciju i/ili upravljanje API-jem
- Izolacija mreže: Omogućuje izolaciju mreže koristeći Azure Virtual Networks (VNET)
- Serverless arhitektura: Koristi Azure Functions za skalabilno, događajno vođenje
- Lokalni razvoj: Sveobuhvatna podrška za lokalni razvoj i otklanjanje pogrešaka
- Jednostavna implementacija: Pojednostavljeni proces implementacije na Azure

Repozitorij uključuje sve potrebne konfiguracijske datoteke, izvorni kod i definicije infrastrukture za brzo pokretanje produkcijski spremne implementacije MCP servera.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Uzorak implementacije MCP-a koristeći Azure Functions s Pythonom.

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Uzorak implementacije MCP-a koristeći Azure Functions s C# .NET.

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Uzorak implementacije MCP-a koristeći Azure Functions s Node/TypeScriptom.

## Ključne točke

- MCP SDK-ovi pružaju alate specifične za jezik za implementaciju robusnih MCP rješenja
- Proces otklanjanja pogrešaka i testiranja ključan je za pouzdane MCP aplikacije
- Predlošci upita koji se mogu ponovno koristiti omogućuju dosljedne AI interakcije
- Dobro dizajnirani radni procesi mogu orkestrirati složene zadatke koristeći više alata
- Implementacija MCP rješenja zahtijeva razmatranje sigurnosti, performansi i rukovanja pogreškama

## Vježba

Dizajnirajte praktičan MCP radni proces koji rješava stvarni problem u vašem području:

1. Identificirajte 3-4 alata koji bi bili korisni za rješavanje ovog problema.
2. Stvorite dijagram radnog procesa koji pokazuje kako ti alati međusobno djeluju.
3. Implementirajte osnovnu verziju jednog od alata koristeći vaš preferirani jezik.
4. Stvorite predložak upita koji bi pomogao modelu učinkovito koristiti vaš alat.

## Dodatni resursi

---

Sljedeće: [Napredne teme](../05-AdvancedTopics/README.md)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.