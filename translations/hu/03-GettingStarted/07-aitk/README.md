# Az AI Toolkit kiterjesztés használata Visual Studio Code-ban egy szerver fogyasztásához

Amikor AI ügynököt építesz, nem csak az okos válaszok generálásáról van szó; az is fontos, hogy az ügynök képes legyen cselekedni. Itt jön képbe a Model Context Protocol (MCP). Az MCP lehetővé teszi az ügynökök számára, hogy külső eszközökhöz és szolgáltatásokhoz férjenek hozzá egységes módon. Gondolj rá úgy, mint egy szerszámosládára, amit az ügynök *valóban* használni tud.

Tegyük fel, hogy egy ügynököt csatlakoztatsz a számológép MCP szerveredhez. Hirtelen az ügynök képes matematikai műveleteket végezni, csak egy olyan utasítás alapján, mint például: „Mennyi 47 szorozva 89-cel?”—nincs szükség a logika kódolására vagy egyedi API-k létrehozására.

## Áttekintés

Ez a lecke bemutatja, hogyan lehet egy számológép MCP szervert csatlakoztatni egy ügynökhöz a [AI Toolkit](https://aka.ms/AIToolkit) kiterjesztés segítségével a Visual Studio Code-ban, lehetővé téve az ügynök számára, hogy természetes nyelven keresztül végezzen matematikai műveleteket, például összeadást, kivonást, szorzást és osztást.

Az AI Toolkit egy erőteljes kiterjesztés a Visual Studio Code-hoz, amely leegyszerűsíti az ügynökfejlesztést. Az AI mérnökök könnyedén építhetnek AI alkalmazásokat generatív AI modellek fejlesztésével és tesztelésével—helyben vagy a felhőben. A kiterjesztés támogatja a legtöbb ma elérhető generatív modellt.

*Megjegyzés*: Az AI Toolkit jelenleg Python és TypeScript nyelveket támogat.

## Tanulási célok

A lecke végére képes leszel:

- MCP szervert használni az AI Toolkit segítségével.
- Konfigurálni egy ügynököt, hogy felfedezze és használja az MCP szerver által biztosított eszközöket.
- MCP eszközöket használni természetes nyelven keresztül.

## Megközelítés

Íme, hogyan kell magas szinten megközelíteni a feladatot:

- Hozz létre egy ügynököt, és definiáld a rendszerutasítását.
- Hozz létre egy MCP szervert számológép eszközökkel.
- Csatlakoztasd az Agent Builder-t az MCP szerverhez.
- Teszteld az ügynök eszközhasználatát természetes nyelven keresztül.

Remek, most, hogy megértettük a folyamatot, konfiguráljunk egy AI ügynököt, hogy külső eszközöket használjon az MCP segítségével, és ezzel bővítse képességeit!

## Előfeltételek

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit for Visual Studio Code](https://aka.ms/AIToolkit)

## Gyakorlat: Egy szerver használata

> [!WARNING]
> Megjegyzés macOS felhasználóknak. Jelenleg vizsgálunk egy problémát, amely a függőségek telepítését érinti macOS rendszeren. Ennek eredményeként a macOS felhasználók jelenleg nem tudják befejezni ezt az oktatóanyagot. Amint elérhető lesz a javítás, frissítjük az utasításokat. Köszönjük a türelmet és a megértést!

Ebben a gyakorlatban egy AI ügynököt fogsz építeni, futtatni és bővíteni MCP szerver eszközökkel a Visual Studio Code-ban az AI Toolkit segítségével.

### -0- Előkészítő lépés: Add hozzá az OpenAI GPT-4o modellt a Saját modellekhez

A gyakorlat a **GPT-4o** modellt használja. A modellt hozzá kell adni a **Saját modellek** listához, mielőtt létrehoznád az ügynököt.

1. Nyisd meg az **AI Toolkit** kiterjesztést az **Aktivitás sávból**.
1. A **Katalógus** szekcióban válaszd a **Modellek** lehetőséget a **Modellek katalógusának** megnyitásához. A **Modellek** kiválasztása egy új szerkesztőfülön nyitja meg a katalógust.
1. A **Modellek katalógusa** keresősávjába írd be: **OpenAI GPT-4o**.
1. Kattints a **+ Hozzáadás** gombra, hogy a modellt hozzáadd a **Saját modellek** listádhoz. Győződj meg róla, hogy a **GitHub által hosztolt** modellt választottad.
1. Az **Aktivitás sávban** ellenőrizd, hogy az **OpenAI GPT-4o** modell megjelenik a listában.

### -1- Ügynök létrehozása

Az **Agent (Prompt) Builder** lehetővé teszi, hogy saját AI-alapú ügynököket hozz létre és testre szabj. Ebben a szekcióban létrehozol egy új ügynököt, és hozzárendelsz egy modellt, amely a beszélgetést vezérli.

1. Nyisd meg az **AI Toolkit** kiterjesztést az **Aktivitás sávból**.
1. A **Tools** szekcióban válaszd az **Agent (Prompt) Builder** lehetőséget. Az **Agent (Prompt) Builder** kiválasztása egy új szerkesztőfülön nyitja meg az eszközt.
1. Kattints az **+ Új ügynök** gombra. A kiterjesztés egy beállítási varázslót indít el a **Command Palette** segítségével.
1. Add meg az ügynök nevét: **Calculator Agent**, majd nyomj **Enter**-t.
1. Az **Agent (Prompt) Builder**-ben a **Model** mezőhöz válaszd az **OpenAI GPT-4o (via GitHub)** modellt.

### -2- Rendszerutasítás létrehozása az ügynök számára

Miután az ügynök alapját létrehoztad, ideje meghatározni a személyiségét és célját. Ebben a szekcióban az **Generate system prompt** funkciót használod, hogy leírd az ügynök szándékolt viselkedését—jelen esetben egy számológép ügynököt—és a modell megírja helyetted a rendszerutasítást.

1. A **Prompts** szekcióban kattints a **Generate system prompt** gombra. Ez megnyitja a prompt generátort, amely AI-t használ az ügynök rendszerutasításának létrehozásához.
1. A **Generate a prompt** ablakban írd be a következőt: `Te egy segítőkész és hatékony matematikai asszisztens vagy. Ha alapvető aritmetikai problémát kapsz, a helyes eredménnyel válaszolsz.`
1. Kattints a **Generate** gombra. Egy értesítés jelenik meg a jobb alsó sarokban, amely megerősíti, hogy a rendszerutasítás generálása folyamatban van. Amint a generálás befejeződik, az utasítás megjelenik az **Agent (Prompt) Builder** **System prompt** mezőjében.
1. Nézd át a **System prompt** mezőt, és szükség esetén módosítsd.

### -3- MCP szerver létrehozása

Most, hogy meghatároztad az ügynök rendszerutasítását—amely irányítja a viselkedését és válaszait—ideje gyakorlati képességekkel felruházni. Ebben a szekcióban létrehozol egy számológép MCP szervert, amely eszközöket biztosít összeadáshoz, kivonáshoz, szorzáshoz és osztáshoz. Ez a szerver lehetővé teszi az ügynök számára, hogy valós idejű matematikai műveleteket végezzen természetes nyelvű utasítások alapján.

Az AI Toolkit sablonokat biztosít az MCP szerverek egyszerű létrehozásához. A számológép MCP szerver létrehozásához a Python sablont fogjuk használni.

*Megjegyzés*: Az AI Toolkit jelenleg Python és TypeScript nyelveket támogat.

1. Az **Agent (Prompt) Builder** **Tools** szekciójában kattints a **+ MCP Server** gombra. A kiterjesztés egy beállítási varázslót indít el a **Command Palette** segítségével.
1. Válaszd a **+ Add Server** lehetőséget.
1. Válaszd a **Create a New MCP Server** lehetőséget.
1. Válaszd a **python-weather** sablont.
1. Válaszd az **Alapértelmezett mappa** lehetőséget az MCP szerver sablon mentéséhez.
1. Add meg a szerver nevét: **Calculator**.
1. Egy új Visual Studio Code ablak nyílik meg. Válaszd a **Yes, I trust the authors** lehetőséget.
1. A terminálban (**Terminal** > **New Terminal**) hozz létre egy virtuális környezetet: `python -m venv .venv`
1. A terminálban aktiváld a virtuális környezetet:
    - Windows: `.venv\Scripts\activate`
    - macOS/Linux: `source .venv/bin/activate`
1. A terminálban telepítsd a függőségeket: `pip install -e .[dev]`
1. Az **Activity Bar** **Explorer** nézetében bontsd ki a **src** könyvtárat, és válaszd ki a **server.py** fájlt, hogy megnyisd a szerkesztőben.
1. Cseréld ki a **server.py** fájl tartalmát a következőre, majd mentsd el:

    ```python
    """
    Sample MCP Calculator Server implementation in Python.

    
    This module demonstrates how to create a simple MCP server with calculator tools
    that can perform basic arithmetic operations (add, subtract, multiply, divide).
    """
    
    from mcp.server.fastmcp import FastMCP
    
    server = FastMCP("calculator")
    
    @server.tool()
    def add(a: float, b: float) -> float:
        """Add two numbers together and return the result."""
        return a + b
    
    @server.tool()
    def subtract(a: float, b: float) -> float:
        """Subtract b from a and return the result."""
        return a - b
    
    @server.tool()
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers together and return the result."""
        return a * b
    
    @server.tool()
    def divide(a: float, b: float) -> float:
        """
        Divide a by b and return the result.
        
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    ```

### -4- Az ügynök futtatása a számológép MCP szerverrel

Most, hogy az ügynököd rendelkezik eszközökkel, ideje használni őket! Ebben a szekcióban utasításokat küldesz az ügynöknek, hogy teszteld és ellenőrizd, vajon az ügynök megfelelően használja-e a számológép MCP szerver eszközeit.

1. Nyomd meg az `F5` gombot az MCP szerver hibakeresésének elindításához. Az **Agent (Prompt) Builder** új szerkesztőfülön nyílik meg. A szerver állapota látható a terminálban.
1. Az **Agent (Prompt) Builder** **User prompt** mezőjébe írd be a következő utasítást: `Vettem 3 darab terméket, darabonként 25 dollárért, majd felhasználtam egy 20 dolláros kedvezményt. Mennyit fizettem?`
1. Kattints a **Run** gombra az ügynök válaszának generálásához.
1. Nézd át az ügynök válaszát. A modellnek arra kell jutnia, hogy **55 dollárt** fizettél.
1. Íme, mi történik:
    - Az ügynök kiválasztja a **multiply** és **subtract** eszközöket a számítás elvégzéséhez.
    - A megfelelő `a` és `b` értékek kerülnek hozzárendelésre a **multiply** eszközhöz.
    - A megfelelő `a` és `b` értékek kerülnek hozzárendelésre a **subtract** eszközhöz.
    - Az egyes eszközök válaszai megjelennek a **Tool Response** mezőben.
    - A modell végső válasza a **Model Response** mezőben jelenik meg.
1. Küldj további utasításokat az ügynök további teszteléséhez. Az **User prompt** mezőben módosíthatod a meglévő utasítást, ha rákattintasz a mezőre, és kicseréled a meglévő szöveget.
1. Miután befejezted az ügynök tesztelését, a szervert leállíthatod a **terminálban** a **CTRL/CMD+C** beírásával.

## Feladat

Próbálj meg egy új eszközt hozzáadni a **server.py** fájlodhoz (például: egy szám négyzetgyökének visszaadása). Küldj olyan további utasításokat, amelyek az ügynököt az új eszköz (vagy meglévő eszközök) használatára késztetik. Ne felejtsd el újraindítani a szervert az új eszközök betöltéséhez.

## Megoldás

[Megoldás](./solution/README.md)

## Főbb tanulságok

A fejezet főbb tanulságai a következők:

- Az AI Toolkit kiterjesztés kiváló kliens, amely lehetővé teszi MCP szerverek és azok eszközeinek használatát.
- Új eszközöket adhatsz hozzá MCP szerverekhez, bővítve az ügynök képességeit az új igények kielégítésére.
- Az AI Toolkit sablonokat tartalmaz (például Python MCP szerver sablonokat), amelyek egyszerűsítik az egyedi eszközök létrehozását.

## További források

- [AI Toolkit dokumentáció](https://aka.ms/AIToolkit/doc)

## Mi következik?
- Következő: [Tesztelés és hibakeresés](../08-testing/README.md)

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális, emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.