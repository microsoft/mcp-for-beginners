# HTTPS Стриминг са Протоколом Контекста Модела (MCP)

Ово поглавље пружа свеобухватан водич за имплементацију безбедног, скалабилног и стриминга у реалном времену са Протоколом Контекста Модела (MCP) користећи HTTPS. Обухвата мотивацију за стриминг, доступне механизме транспорта, како имплементирати HTTP стриминг у MCP-у, најбоље праксе за безбедност, миграцију са SSE-а и практичне смернице за изградњу сопствених MCP апликација за стриминг.

## Механизми транспорта и стриминг у MCP-у

Овај део истражује различите механизме транспорта доступне у MCP-у и њихову улогу у омогућавању стриминг могућности за комуникацију у реалном времену између клијената и сервера.

### Шта је механизам транспорта?

Механизам транспорта дефинише како се подаци размењују између клијента и сервера. MCP подржава више типова транспорта како би одговарао различитим окружењима и захтевима:

- **stdio**: Стандардни улаз/излаз, погодан за локалне и CLI алате. Једноставан, али није погодан за веб или облак.
- **SSE (Server-Sent Events)**: Омогућава серверима да шаљу ажурирања у реалном времену клијентима преко HTTP-а. Добар за веб интерфејсе, али ограничен у скалабилности и флексибилности.
- **Streamable HTTP**: Модеран HTTP стриминг транспорт, који подржава обавештења и бољу скалабилност. Препоручује се за већину продукцијских и облачних сценарија.

### Табела поређења

Погледајте табелу поређења испод како бисте разумели разлике између ових механизама транспорта:

| Транспорт         | Ажурирања у реалном времену | Стриминг | Скалабилност | Примена                  |
|-------------------|----------------------------|----------|-------------|-------------------------|
| stdio             | Не                         | Не       | Ниска       | Локални CLI алати       |
| SSE               | Да                         | Да       | Средња      | Веб, ажурирања у реалном времену |
| Streamable HTTP   | Да                         | Да       | Висока      | Облак, више клијената   |

> **Савет:** Избор правог транспорта утиче на перформансе, скалабилност и корисничко искуство. **Streamable HTTP** се препоручује за модерне, скалабилне и апликације спремне за облак.

Запамтите транспорте stdio и SSE који су вам представљени у претходним поглављима и како је Streamable HTTP транспорт који се обрађује у овом поглављу.

## Стриминг: Концепти и мотивација

Разумевање основних концепата и мотивације иза стриминга је од суштинског значаја за имплементацију ефикасних система комуникације у реалном времену.

**Стриминг** је техника у мрежном програмирању која омогућава слање и примање података у малим, управљивим деловима или као низ догађаја, уместо чекања да цео одговор буде спреман. Ово је посебно корисно за:

- Велике датотеке или скупове података.
- Ажурирања у реалном времену (нпр. чет, траке напретка).
- Дуготрајне рачунске операције где желите да корисника држите информисаним.

Ево шта треба да знате о стримингу на високом нивоу:

- Подаци се испоручују постепено, а не одједном.
- Клијент може обрађивати податке како стижу.
- Смањује перципирану латенцију и побољшава корисничко искуство.

### Зашто користити стриминг?

Разлози за коришћење стриминга су следећи:

- Корисници добијају повратне информације одмах, а не само на крају.
- Омогућава апликације у реалном времену и одзивне интерфејсе.
- Ефикасније коришћење мрежних и рачунских ресурса.

### Једноставан пример: HTTP стриминг сервер и клијент

Ево једноставног примера како се стриминг може имплементирати:

#### Python

**Сервер (Python, користећи FastAPI и StreamingResponse):**

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

async def event_stream():
    for i in range(1, 6):
        yield f"data: Message {i}\n\n"
        time.sleep(1)

@app.get("/stream")
def stream():
    return StreamingResponse(event_stream(), media_type="text/event-stream")
```

**Клијент (Python, користећи requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Овај пример демонстрира сервер који шаље серију порука клијенту како постају доступне, уместо да чека да све поруке буду спремне.

**Како функционише:**

- Сервер шаље сваку поруку како је спремна.
- Клијент прима и штампа сваки део како стиже.

**Захтеви:**

- Сервер мора користити стриминг одговор (нпр. `StreamingResponse` у FastAPI-ју).
- Клијент мора обрађивати одговор као стрим (`stream=True` у requests).
- Content-Type је обично `text/event-stream` или `application/octet-stream`.

#### Java

**Сервер (Java, користећи Spring Boot и Server-Sent Events):**

```java
@RestController
public class CalculatorController {

    @GetMapping(value = "/calculate", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<ServerSentEvent<String>> calculate(@RequestParam double a,
                                                   @RequestParam double b,
                                                   @RequestParam String op) {
        
        double result;
        switch (op) {
            case "add": result = a + b; break;
            case "sub": result = a - b; break;
            case "mul": result = a * b; break;
            case "div": result = b != 0 ? a / b : Double.NaN; break;
            default: result = Double.NaN;
        }

        return Flux.<ServerSentEvent<String>>just(
                    ServerSentEvent.<String>builder()
                        .event("info")
                        .data("Calculating: " + a + " " + op + " " + b)
                        .build(),
                    ServerSentEvent.<String>builder()
                        .event("result")
                        .data(String.valueOf(result))
                        .build()
                )
                .delayElements(Duration.ofSeconds(1));
    }
}
```

**Клијент (Java, користећи Spring WebFlux WebClient):**

```java
@SpringBootApplication
public class CalculatorClientApplication implements CommandLineRunner {

    private final WebClient client = WebClient.builder()
            .baseUrl("http://localhost:8080")
            .build();

    @Override
    public void run(String... args) {
        client.get()
                .uri(uriBuilder -> uriBuilder
                        .path("/calculate")
                        .queryParam("a", 7)
                        .queryParam("b", 5)
                        .queryParam("op", "mul")
                        .build())
                .accept(MediaType.TEXT_EVENT_STREAM)
                .retrieve()
                .bodyToFlux(String.class)
                .doOnNext(System.out::println)
                .blockLast();
    }
}
```

**Напомене о имплементацији у Java:**

- Користи реактивни стек Spring Boot-а са `Flux` за стриминг.
- `ServerSentEvent` пружа структуриран стриминг догађаја са типовима догађаја.
- `WebClient` са `bodyToFlux()` омогућава реактивну потрошњу стриминга.
- `delayElements()` симулира време обраде између догађаја.
- Догађаји могу имати типове (`info`, `result`) за боље руковање на страни клијента.

### Поређење: Класични стриминг vs MCP стриминг

Разлике између начина на који стриминг функционише на "класичан" начин у односу на MCP стриминг могу се приказати овако:

| Карактеристика          | Класични HTTP стриминг         | MCP стриминг (Обавештења)          |
|-------------------------|-------------------------------|------------------------------------|
| Главни одговор          | У деловима                   | Један, на крају                   |
| Ажурирања напретка      | Шаљу се као делови података   | Шаљу се као обавештења            |
| Захтеви клијента        | Мора обрађивати стрим         | Мора имплементирати обрађивач порука |
| Примена                 | Велике датотеке, AI токени    | Напредак, логови, повратне информације у реалном времену |

### Препоруке

Постоје неке препоруке када је реч о избору између имплементације класичног стриминга (као што је крајња тачка коју смо вам показали горе користећи `/stream`) у односу на избор стриминга преко MCP-а.

- **За једноставне потребе стриминга:** Класични HTTP стриминг је једноставнији за имплементацију и довољан за основне потребе стриминга.

- **За сложене, интерактивне апликације:** MCP стриминг пружа структуриран приступ са богатијим метаподацима и одвајањем између обавештења и коначних резултата.

- **За AI апликације:** MCP-ов систем обавештења је посебно користан за дуготрајне AI задатке где желите да кориснике држите информисаним о напретку.

## Стриминг у MCP-у

У реду, видели сте неке препоруке и поређења до сада о разлици између класичног стриминга и стриминга у MCP-у. Хајде да детаљно објаснимо како можете искористити стриминг у MCP-у.

Разумевање како стриминг функционише у оквиру MCP оквира је од суштинског значаја за изградњу одзивних апликација које пружају повратне информације у реалном времену корисницима током дуготрајних операција.

У MCP-у, стриминг није о слању главног одговора у деловима, већ о слању **обавештења** клијенту док алат обрађује захтев. Ова обавештења могу укључивати ажурирања напретка, логове или друге догађаје.

### Како функционише

Главни резултат се и даље шаље као један одговор. Међутим, обавештења се могу слати као посебне поруке током обраде и на тај начин ажурирати клијента у реалном времену. Клијент мора бити у стању да обрађује и приказује ова обавештења.

## Шта је обавештење?

Рекли смо "обавештење", шта то значи у контексту MCP-а?

Обавештење је порука коју сервер шаље клијенту како би га обавестио о напретку, статусу или другим догађајима током дуготрајне операције. Обавештења побољшавају транспарентност и корисничко искуство.

На пример, клијент треба да пошаље обавештење након што је иницијални handshake са сервером направљен.

Обавештење изгледа овако као JSON порука:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Обавештења припадају теми у MCP-у која се назива ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

Да би логовање функционисало, сервер мора да га омогући као функцију/способност овако:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> У зависности од коришћеног SDK-а, логовање може бити подразумевано омогућено или ћете га можда морати експлицитно омогућити у конфигурацији сервера.

Постоје различити типови обавештења:

| Ниво       | Опис                          | Пример употребе                 |
|------------|-------------------------------|---------------------------------|
| debug      | Детаљне информације за дебаг   | Улаз/излаз функције             |
| info       | Опште информационе поруке     | Ажурирања напретка операције    |
| notice     | Нормални али значајни догађаји | Промене конфигурације           |
| warning    | Упозоравајући услови           | Коришћење застареле функције    |
| error      | Услов грешке                   | Неуспех операције               |
| critical   | Критични услови                | Неуспех компоненти система      |
| alert      | Потребна је хитна акција      | Откривена корупција података    |
| emergency  | Систем је неупотребљив         | Потпуни неуспех система         |

## Имплементација обавештења у MCP-у

Да бисте имплементирали обавештења у MCP-у, потребно је да подесите и серверску и клијентску страну за обраду ажурирања у реалном времену. Ово омогућава вашој апликацији да пружи тренутне повратне информације корисницима током дуготрајних операција.

### Серверска страна: Слање обавештења

Почнимо са серверском страном. У MCP-у, дефинишете алате који могу слати обавештења током обраде захтева. Сервер користи објекат контекста (обично `ctx`) за слање порука клијенту.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

У претходном примеру, алат `process_files` шаље три обавештења клијенту док обрађује сваку датотеку. Метод `ctx.info()` се користи за слање информационих порука.

Додатно, да бисте омогућили обавештења, уверите се да ваш сервер користи стриминг транспорт (као што је `streamable-http`) и да ваш клијент имплементира обрађивач порука за обраду обавештења. Ево како можете подесити сервер да користи `streamable-http` транспорт:

```python
mcp.run(transport="streamable-http")
```

#### .NET

```csharp
[Tool("A tool that sends progress notifications")]
public async Task<TextContent> ProcessFiles(string message, ToolContext ctx)
{
    await ctx.Info("Processing file 1/3...");
    await ctx.Info("Processing file 2/3...");
    await ctx.Info("Processing file 3/3...");
    return new TextContent
    {
        Type = "text",
        Text = $"Done: {message}"
    };
}
```

У овом .NET примеру, алат `ProcessFiles` је декорисан са атрибутом `Tool` и шаље три обавештења клијенту док обрађује сваку датотеку. Метод `ctx.Info()` се користи за слање информационих порука.

Да бисте омогућили обавештења у вашем .NET MCP серверу, уверите се да користите стриминг транспорт:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Клијентска страна: Примање обавештења

Клијент мора имплементирати обрађивач порука за обраду и приказивање обавештења како стижу.

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)

async with ClientSession(
   read_stream, 
   write_stream,
   logging_callback=logging_collector,
   message_handler=message_handler,
) as session:
```

У претходном коду, функција `message_handler` проверава да ли је долазна порука обавештење. Ако јесте, штампа обавештење; у супротном, обрађује је као редовну поруку сервера. Такође, обратите пажњу како је `ClientSession` иницијализован са `message_handler` за обраду долазних обавештења.

#### .NET

```csharp
// Define a message handler
void MessageHandler(IJsonRpcMessage message)
{
    if (message is ServerNotification notification)
    {
        Console.WriteLine($"NOTIFICATION: {notification}");
    }
    else
    {
        Console.WriteLine($"SERVER MESSAGE: {message}");
    }
}

// Create and use a client session with the message handler
var clientOptions = new ClientSessionOptions
{
    MessageHandler = MessageHandler,
    LoggingCallback = (level, message) => Console.WriteLine($"[{level}] {message}")
};

using var client = new ClientSession(readStream, writeStream, clientOptions);
await client.InitializeAsync();

// Now the client will process notifications through the MessageHandler
```

У овом .NET примеру, функција `MessageHandler` проверава да ли је долазна порука обавештење. Ако јесте, штампа обавештење; у супротном, обрађује је као редовну поруку сервера. `ClientSession` је иницијализован са обрађивачем порука преко `ClientSessionOptions`.

Да бисте омогућили обавештења, уверите се да ваш сервер користи стриминг транспорт (као што је `streamable-http`) и да ваш клијент имплементира обрађивач порука за обраду обавештења.

## Ажурирања напретка и сценарији

Овај део објашњава концепт ажурирања напретка у MCP-у, зашто су важна и како их имплементирати користећи Streamable HTTP. Такође ћете пронаћи практичан задатак за јачање вашег разумевања.

Ажурирања напретка су поруке у реалном времену које сервер шаље клијенту током дуготрајних операција. Уместо да чека да цео процес заврши, сервер ажурира клијента о тренутном статусу. Ово побољшава транспарентност, корисничко искуство и олакшава дебаговање.

**Пример:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Зашто користити ажурирања напретка?

Ажурирања напретка су важна из неколико разлога:

- **Боље корисничко искуство:** Корисници виде ажурирања како рад напредује, а не само на крају.
- **Повратне информације у реалном времену:** Клијенти могу приказивати траке напретка или логове, чинећи апликацију одзивном.
- **Лакше дебаговање и праћење:** Програмери и корисници могу видети где процес може бити спор или заглављен.

### Како имплементирати ажурирања напретка

Ево како можете имплементирати ажурирања напретка у MCP-у:

- **На серверу:** Користите `ctx.info()` или `ctx.log()` за слање обавештења како се свака ставка обрађује. Ово шаље поруку клијенту пре него што је главни резултат спреман.
- **На клијенту:** Имплементирајте обрађивач порука који слуша и приказује обавештења како стижу. Овај обрађивач разликује обавештења од коначног резултата.

**Пример сервера:**

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Пример клијента:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Безбедносни аспекти

Када имплементирате MCP сервере са HTTP-б
Postoje dva ključna razloga za prelazak sa SSE na Streamable HTTP:

- Streamable HTTP nudi bolju skalabilnost, kompatibilnost i bogatiju podršku za obaveštenja u poređenju sa SSE.
- Preporučeni je transport za nove MCP aplikacije.

### Koraci za migraciju

Evo kako možete migrirati sa SSE na Streamable HTTP u vašim MCP aplikacijama:

- **Ažurirajte serverski kod** tako da koristi `transport="streamable-http"` u `mcp.run()`.
- **Ažurirajte klijentski kod** tako da koristi `streamablehttp_client` umesto SSE klijenta.
- **Implementirajte rukovalac porukama** u klijentu za obradu obaveštenja.
- **Testirajte kompatibilnost** sa postojećim alatima i radnim tokovima.

### Održavanje kompatibilnosti

Preporučuje se da održavate kompatibilnost sa postojećim SSE klijentima tokom procesa migracije. Evo nekoliko strategija:

- Možete podržavati i SSE i Streamable HTTP tako što ćete pokrenuti oba transporta na različitim krajnjim tačkama.
- Postepeno migrirajte klijente na novi transport.

### Izazovi

Obratite pažnju na sledeće izazove tokom migracije:

- Ažuriranje svih klijenata
- Upravljanje razlikama u isporuci obaveštenja

## Bezbednosni aspekti

Bezbednost treba da bude glavni prioritet prilikom implementacije bilo kog servera, posebno kada koristite HTTP-bazirane transporte poput Streamable HTTP u MCP.

Prilikom implementacije MCP servera sa HTTP-baziranim transportima, bezbednost postaje ključna tema koja zahteva pažljivo razmatranje različitih vektora napada i mehanizama zaštite.

### Pregled

Bezbednost je od suštinskog značaja kada izlažete MCP servere putem HTTP-a. Streamable HTTP uvodi nove površine za napade i zahteva pažljivu konfiguraciju.

Evo nekoliko ključnih bezbednosnih aspekata:

- **Validacija Origin zaglavlja**: Uvek validirajte `Origin` zaglavlje kako biste sprečili DNS rebinding napade.
- **Povezivanje na localhost**: Za lokalni razvoj, povežite servere na `localhost` kako biste izbegli izlaganje javnom internetu.
- **Autentifikacija**: Implementirajte autentifikaciju (npr. API ključevi, OAuth) za produkcijska okruženja.
- **CORS**: Konfigurišite Cross-Origin Resource Sharing (CORS) politike kako biste ograničili pristup.
- **HTTPS**: Koristite HTTPS u produkciji za šifrovanje saobraćaja.

### Najbolje prakse

Pored toga, evo nekoliko najboljih praksi koje treba slediti prilikom implementacije bezbednosti u vašem MCP streaming serveru:

- Nikada ne verujte dolaznim zahtevima bez validacije.
- Beležite i pratite sav pristup i greške.
- Redovno ažurirajte zavisnosti kako biste zakrpili bezbednosne ranjivosti.

### Izazovi

Suočićete se sa nekim izazovima prilikom implementacije bezbednosti u MCP streaming serverima:

- Balansiranje između bezbednosti i jednostavnosti razvoja
- Obezbeđivanje kompatibilnosti sa različitim klijentskim okruženjima

### Zadatak: Napravite sopstvenu MCP streaming aplikaciju

**Scenario:**
Napravite MCP server i klijent gde server obrađuje listu stavki (npr. fajlova ili dokumenata) i šalje obaveštenje za svaku obrađenu stavku. Klijent treba da prikazuje svako obaveštenje čim stigne.

**Koraci:**

1. Implementirajte serverski alat koji obrađuje listu i šalje obaveštenja za svaku stavku.
2. Implementirajte klijent sa rukovaocem poruka za prikaz obaveštenja u realnom vremenu.
3. Testirajte implementaciju pokretanjem i servera i klijenta, i posmatrajte obaveštenja.

[Rešenje](./solution/README.md)

## Dalje čitanje i šta dalje?

Da biste nastavili svoje istraživanje MCP streaminga i proširili svoje znanje, ovaj odeljak pruža dodatne resurse i predložene sledeće korake za izgradnju naprednijih aplikacija.

### Dalje čitanje

- [Microsoft: Uvod u HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS u ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Šta dalje?

- Pokušajte da napravite naprednije MCP alate koji koriste streaming za analitiku u realnom vremenu, čet ili kolaborativno uređivanje.
- Istražite integraciju MCP streaminga sa frontend okvirima (React, Vue, itd.) za ažuriranja korisničkog interfejsa uživo.
- Sledeće: [Korišćenje AI alata za VSCode](../07-aitk/README.md)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, молимо вас да имате у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква неспоразумевања или погрешна тумачења која могу произаћи из коришћења овог превода.