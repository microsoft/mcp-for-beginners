# Alap Számológép MCP Szolgáltatás

Ez a szolgáltatás alapvető számológép műveleteket biztosít a Model Context Protocol (MCP) segítségével. Egyszerű példaként készült kezdők számára, akik az MCP megvalósításokat tanulják.

További információkért lásd a [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) oldalt.

## Jellemzők

Ez a számológép szolgáltatás a következő funkciókat kínálja:

1. **Alapvető Aritmetikai Műveletek**:
   - Két szám összeadása
   - Egy szám kivonása egy másikból
   - Két szám szorzása
   - Egy szám osztása egy másikkal (nullával való osztás ellenőrzéssel)

## `stdio` típus használata

## Konfiguráció

1. **MCP szerverek beállítása**:
   - Nyisd meg a munkaterületedet a VS Code-ban.
   - Hozz létre egy `.vscode/mcp.json` fájlt a munkaterület mappájában az MCP szerverek konfigurálásához. Példa konfiguráció:

     ```jsonc
     {
       "inputs": [
         {
           "type": "promptString",
           "id": "repository-root",
           "description": "The absolute path to the repository root"
         }
       ],
       "servers": {
         "calculator-mcp-dotnet": {
           "type": "stdio",
           "command": "dotnet",
           "args": [
             "run",
             "--project",
             "${input:repository-root}/03-GettingStarted/samples/csharp/src/calculator.csproj"
           ]
         }
       }
     }
     ```

   - Megkérnek majd, hogy add meg a GitHub tároló gyökérkönyvtárát, amit a `git rev-parse --show-toplevel` parancsból tudsz lekérdezni.

## A szolgáltatás használata

A szolgáltatás az MCP protokollon keresztül a következő API végpontokat teszi elérhetővé:

- `add(a, b)`: Két szám összeadása
- `subtract(a, b)`: A második szám kivonása az elsőből
- `multiply(a, b)`: Két szám szorzása
- `divide(a, b)`: Az első szám osztása a másodikkal (nulla ellenőrzéssel)
- isPrime(n): Ellenőrzi, hogy egy szám prím-e

## Tesztelés Github Copilot Chattel a VS Code-ban

1. Próbálj meg kérni a szolgáltatást az MCP protokoll használatával. Például kérdezhetsz:
   - "Add össze 5 és 3"
   - "Vonj ki 10-et 4-ből"
   - "Szorozd meg 6-ot 7-tel"
   - "Oszd el 8-at 2-vel"
   - "Prím-e a 37854?"
   - "Melyek a 3 prím számok 4242 előtt és után?"
2. Hogy biztosan a megfelelő eszközt használd, add hozzá a #MyCalculator címkét a kéréshez. Például:
   - "Add össze 5 és 3 #MyCalculator"
   - "Vonj ki 10-et 4-ből #MyCalculator"

## Konténerizált verzió

Az előző megoldás nagyszerű, ha a .NET SDK telepítve van, és minden függőség rendelkezésre áll. Ha azonban meg szeretnéd osztani a megoldást vagy más környezetben futtatni, használhatod a konténerizált verziót.

1. Indítsd el a Dockert, és győződj meg róla, hogy fut.
1. Egy terminálból navigálj a `03-GettingStarted\samples\csharp\src` mappába.
1. A számológép szolgáltatás Docker képének elkészítéséhez futtasd a következő parancsot (cseréld le a `<YOUR-DOCKER-USERNAME>` részt a Docker Hub felhasználónevedre):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ```
1. Miután a kép elkészült, töltsd fel a Docker Hubra a következő paranccsal:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## A Dockerizált verzió használata

1. A `.vscode/mcp.json` fájlban cseréld le a szerver konfigurációt a következőre:
   ```json
    "mcp-calc": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calc"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   A konfigurációból látható, hogy a parancs `docker`, az argumentumok pedig `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. A `--rm` kapcsoló gondoskodik arról, hogy a konténer leállás után törlődjön, az `-i` pedig lehetővé teszi, hogy a konténer standard bemenetével interakcióba lépj. Az utolsó argumentum a kép neve, amit épp építettünk és feltöltöttünk a Docker Hubra.

## A Dockerizált verzió tesztelése

Indítsd el az MCP szervert a kis Start gombra kattintva a `"mcp-calc": {` fölött, és ugyanúgy kérheted a számológép szolgáltatást, hogy végezzen el néhány számítást.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.