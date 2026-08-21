# Egy szerver használata az AI Toolkit kiterjesztésből a Visual Studio Code-ban  

Amikor AI ügynököt építesz, nem csak az okos válaszok generálásáról van szó; az is fontos, hogy az ügynök képes legyen cselekedni. Erre szolgál a Model Context Protocol (MCP). Az MCP megkönnyíti, hogy az ügynökök következetes módon férjenek hozzá külső eszközökhöz és szolgáltatásokhoz. Olyan, mintha az ügynöködet egy valóban használható szerszámosláda csatlakoztatnád.  

Tegyük fel, hogy egy ügynököt csatlakoztatsz a kalkulátor MCP szerveredhez. Hirtelen az ügynököd képes matematikai műveleteket végrehajtani egyszerűen azáltal, hogy kap egy promptot, például „Mennyi 47 szor 89?” — nem kell logikát beépíteni vagy egyedi API-kat készíteni.  

## Áttekintés  

Ez a lecke bemutatja, hogyan lehet egy kalkulátor MCP szervert csatlakoztatni egy ügynökhöz az [AI Toolkit](https://aka.ms/AIToolkit) kiterjesztéssel a Visual Studio Code-ban, lehetővé téve az ügynök számára matematikai műveletek, például összeadás, kivonás, szorzás és osztás elvégzését természetes nyelven keresztül.  

Az AI Toolkit egy hatékony Visual Studio Code kiterjesztés, amely egyszerűsíti az ügynökfejlesztést. AI mérnökök könnyedén építhetnek AI alkalmazásokat generatív AI modellek fejlesztésével és tesztelésével — helyileg vagy felhőben. A kiterjesztés a legtöbb ma elérhető jelentős generatív modellt támogatja.  

*Megjegyzés*: Az AI Toolkit jelenleg a Python-t és a TypeScript-et támogatja.  

## Tanulási célok  

E lecke végére képes leszel:  

- MCP szerver fogyasztása az AI Toolkit-en keresztül.  
- Ügynök konfiguráció létrehozása az MCP szerver által biztosított eszközök felfedezéséhez és használatához.  
- MCP eszközök használata természetes nyelven keresztül.  

## Megközelítés  

Itt van, hogyan kell ezt nagy vonalakban megközelíteni:  

- Ügynök létrehozása és a rendszer promptjának definiálása.  
- MCP szerver létrehozása kalkulátor eszközökkel.  
- Az Agent Builder csatlakoztatása az MCP szerverhez.  
- Az ügynök eszközfelhívásának tesztelése természetes nyelv használatával.  

Nagyszerű, most hogy értjük a folyamatot, konfiguráljuk az AI ügynököt, hogy MCP-n keresztül külső eszközöket használhasson, ezáltal kibővítve képességeit!  

## Előfeltételek  

- [Visual Studio Code](https://code.visualstudio.com/)  
- [AI Toolkit a Visual Studio Code-hoz](https://aka.ms/AIToolkit)  

## Gyakorlat: Egy szerver használata  

> [!WARNING]  
> Megjegyzés macOS felhasználóknak. Jelenleg egy olyan probléma vizsgálata folyik, amely érinti a függőség telepítést macOS-en. Emiatt macOS felhasználók jelenleg nem tudják befejezni ezt az oktatóanyagot. Amint elérhető javítás, frissítjük az útmutatót. Köszönjük türelmüket és megértésüket!  

Ebben a gyakorlatban egy AI ügynököt építesz, futtatsz és fejlesztesz MCP szerver eszközeivel a Visual Studio Code-ban az AI Toolkit segítségével.  

### -0- Előkészület, add hozzá az OpenAI GPT-4o modellt a Saját Modellekhez  

A gyakorlat a **GPT-4o** modellt használja. A modellt hozzá kell adni a **Saját Modellek** listához az ügynök létrehozása előtt.  

![Képernyőkép egy modellválasztó felületről a Visual Studio Code AI Toolkit kiterjesztésében. A címsorban „Find the right model for your AI Solution” szerepel, alatta egy alcím, amely arra ösztönzi a felhasználókat, hogy fedezzenek fel, teszteljenek és telepítsenek AI modelleket. Alatta, a “Popular Models” (népszerű modellek) alatt hat modell kártya látható: DeepSeek-R1 (GitHub-hostolt), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Kicsi, Gyors), és DeepSeek-R1 (Ollama-hostolt). Minden kártyán van lehetőség „Add” (Hozzáadás) vagy „Try in Playground” (Próbáld ki a játéktéren) kiválasztására](../../../../translated_images/hu/aitk-model-catalog.2acd38953bb9c119.webp)  

1. Nyisd meg az **AI Toolkit** kiterjesztést az **Activity Bar**-ról.  
1. A **Katalógus** szekcióban válaszd ki a **Modelleket**, hogy megnyisd a **Modell katalógust**. A modellek kiválasztása új szerkesztőfülön nyitja meg a katalógust.  
1. Írd be a **OpenAI GPT-4o**-t a keresősávba a **Modell katalógusban**.  
1. Kattints a **+ Hozzáadás** gombra, hogy a modellt a **Saját Modellek** listához add. Győződj meg arról, hogy a GitHub által hostolt modellt választottad.  
1. Az **Activity Bar**-on ellenőrizd, hogy az **OpenAI GPT-4o** modell megjelenik a listában.  

### -1- Ügynök létrehozása  

Az **Agent (Prompt) Builder** lehetővé teszi, hogy saját AI alapú ügynököket hozz létre és testre szabj. Ebben a részben létrehozol egy új ügynököt és hozzárendelsz egy modellt a beszélgetéshez.  

![Képernyőkép a „Calculator Agent” felépítő felületéről az AI Toolkit kiterjesztésben Visual Studio Code-hoz. Bal oldali panelen az „OpenAI GPT-4o (via GitHub)” modell van kiválasztva. A rendszer prompt így szól: „Ön egy egyetemi matematikaprofesszor,” a felhasználói prompt: „Magyarázza el nekem a Fourier-egyenletet egyszerű szavakkal.” További opciók: gombok eszközök hozzáadásához, MCP szerver engedélyezése, strukturált kimenet választása. Alul kék „Futtatás” gomb látható. Jobb oldali panelen az „Indulás mintákkal” alatt három példa agent látható: Webfejlesztő (MCP szerverrel, másodikos egyszerűsítővel, álomfejtővel, rövid leírásokkal a funkcióikról).](../../../../translated_images/hu/aitk-agent-builder.901e3a2960c3e477.webp)  

1. Nyisd meg az **AI Toolkit** kiterjesztést az **Activity Bar**-ról.  
1. A **Tools** (eszközök) részben válaszd az **Agent (Prompt) Builder** opciót. Ez új szerkesztőfülön nyitja meg az ügynök felépítőt.  
1. Kattints a **+ Új Ügynök** gombra. A kiterjesztés elindít egy telepítő varázslót a **Command Palette**-en keresztül.  
1. Írd be a nevet: **Calculator Agent** és nyomj Entert.  
1. Az **Agent (Prompt) Builder**-ben a **Modell** mezőnél válaszd az **OpenAI GPT-4o (via GitHub)** modellt.  

### -2- Rendszer prompt létrehozása az ügynöknek  

Az ügynök vázlat elkészítése után itt az ideje meghatározni a személyiségét és célját. Ebben a részben a **Generate system prompt** funkciót használod annak leírására, hogy az ügynök mit várjunk el — jelen esetben egy kalkulátor ügynököt — és a modell automatikusan megírja a rendszer promptot.  

![Képernyőkép a „Calculator Agent” felületről a Visual Studio Code AI Toolkitjében egy modális ablak nyitva „Prompt generálása” címmel. Az ablak arról tájékoztat, hogy egy prompt sablon generálható alapadatok megadásával, valamint egy szövegdoboz látható a mintaszöveggel: „Ön egy segítőkész és hatékony matematikai asszisztens. Amikor egyszerű aritmetikai problémát kap, helyes eredménnyel válaszol.” Az ablak alatt „Bezárás” és „Generálás” gombok láthatók. Háttérben részben látható az ügynök konfigurációja, beleértve a kiválasztott modellt: „OpenAI GPT-4o (via GitHub)” és mezők a rendszer- és felhasználói promptokhoz.](../../../../translated_images/hu/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)  

1. A **Prompts** részben kattints a **Generate system prompt** gombra. Ez a gomb megnyit egy prompt építőt, amely AI segítséggel generálja az ügynök rendszer promptját.  
1. A **Generate a prompt** ablakban írd be a következőt: `Ön egy segítőkész és hatékony matematikai asszisztens. Amikor egyszerű aritmetikai problémát kap, helyes eredménnyel válaszol.`  
1. Kattints a **Generate** gombra. A képernyő jobb alsó sarkában értesítés jelenik meg, amely jelzi, hogy a rendszer prompt generálása folyamatban van. Amint befejeződik, a prompt megjelenik az **Agent (Prompt) Builder** **Rendszer prompt** mezőjében.  
1. Ellenőrizd a **Rendszer promptot**, és szükség esetén módosítsd.  

### -3- MCP szerver létrehozása  

Miután meghatároztad az ügynök rendszer promptját — amely irányítja a viselkedését és válaszait — ideje gyakorlati képességekkel felszerelni. Ebben a részben létrehozol egy kalkulátor MCP szervert eszközökkel az összeadás, kivonás, szorzás és osztás műveletek végrehajtásához. Ez a szerver lehetővé teszi az ügynök számára, hogy valós időben hajtson végre matematikai műveleteket természetes nyelvű promptokra válaszul.  

![Képernyőkép a Calculator Agent felület alsó részéről a Visual Studio Code AI Toolkit kiterjesztésében. Kihajtható menük láthatók "Tools" és "Structure output" címmel, egy legördülő menüvel „Choose output format” felirattal, ami „text”-re van állítva. Jobb oldalon egy gomb „+ MCP Server” a Model Context Protocol szerver hozzáadásához. Az eszközök része felett egy kép ikon helyőrzője látható.](../../../../translated_images/hu/aitk-add-mcp-server.9742cfddfe808353.webp)  

Az AI Toolkit sablonokat kínál, hogy megkönnyítse a saját MCP szerver létrehozását. A kalkulátor MCP szerver készítéséhez a Python sablont fogjuk használni.  

*Megjegyzés*: Az AI Toolkit jelenleg Python-t és TypeScript-et támogat.  

1. Az **Agent (Prompt) Builder** **Tools** részében kattints a **+ MCP Server** gombra. A kiterjesztés elindít egy telepítő varázslót a **Command Palette**-n keresztül.  
1. Válaszd a **+ Szerver hozzáadása** opciót.  
1. Válaszd a **Új MCP szerver létrehozása** lehetőséget.  
1. Válaszd a **python-weather** sablont.  
1. Válaszd az **Alapértelmezett mappa** opciót az MCP szerver sablon mentéséhez.  
1. Írd be a szerver nevét: **Calculator**  
1. Egy új Visual Studio Code ablak nyílik meg. Válaszd az **Igen, megbízok a szerzőkben** lehetőséget.  
1. A terminálban (Terminal > New Terminal) hozz létre egy virtuális környezetet: `python -m venv .venv`  
1. A terminálban aktiváld a virtuális környezetet:  
    1. Windows - `.venv\Scripts\activate`  
    1. macOS/Linux - `source .venv/bin/activate`  
1. A terminálban telepítsd a függőségeket: `pip install -e .[dev]`  
1. Az **Explorer** nézetben az **Activity Bar**-on bontsd ki a **src** mappát, és nyisd meg a **server.py** fájlt szerkesztésre.  
1. Cseréld le a **server.py** fájl tartalmát a következőre, majd mentsd el:  

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
  
### -4- Az ügynök futtatása a kalkulátor MCP szerverrel  

Most, hogy az ügynöknek eszközei vannak, ideje használni őket! Ebben a részben promptokat küldesz az ügynöknek, hogy teszteld és érvényesítsd, vajon az ügynök megfelelően használja-e a kalkulátor MCP szerver által biztosított eszközöket.  

![Képernyőkép a Calculator Agent felületről az AI Toolkit Visual Studio Code kiterjesztésében. Bal oldalt, az „Eszközök” alatt egy MCP szerver: local-server-calculator_server van hozzáadva, négy elérhető eszközzel: add, subtract, multiply és divide. Egy jelvény mutatja, hogy négy eszköz aktív. Lent egy összehajtható „Structure output” rész és egy kék „Futtatás” gomb látható. Jobb oldalt, a „Model Response” alatt az ügynök használja a multiply és subtract eszközöket bemenetekkel {"a": 3, "b": 25} és {"a": 75, "b": 20}. A végső „Eszköz válasz” 75.0. Alul egy „View Code” gomb található.](../../../../translated_images/hu/aitk-agent-response-with-tools.e7c781869dc8041a.webp)  

A kalkulátor MCP szervert a helyi fejlesztői gépeden futtatod a **Agent Builder**-en keresztül, mint MCP kliens.  

1. Nyomd meg az `F5` billentyűt az MCP szerver hibakereső indításához. Az **Agent (Prompt) Builder** új szerkesztőfülön nyílik meg. A szerver státusza látható a terminálban.  
1. Az **Agent (Prompt) Builder** **User prompt** mezőjébe írd be a következő promptot: `Vettem 3 terméket egyenként 25 dollárért, majd használtam egy 20 dolláros kedvezményt. Mennyi pénzt fizettem?`  
1. Kattints a **Futtatás** gombra az ügynök válaszának generálásához.  
1. Ellenőrizd az ügynök kimenetét. A modellnek arra kell következtetnie, hogy **55 dollárt** fizettél.  
1. Íme, hogy mi kell történjen:  
    - Az ügynök kiválasztja a **multiply** és **subtract** eszközöket, hogy segítsenek a számításban.  
    - A megfelelő `a` és `b` értékek kiadódnak a **multiply** eszköznek.  
    - A megfelelő `a` és `b` értékek kiadódnak a **subtract** eszköznek.  
    - Az eszközök válaszai megjelennek a megfelelő **Eszköz válasz** mezőkben.  
    - A modell végső kimenete megjelenik a **Végső válasz** mezőben.  
1. Küldj be további promptokat az ügynök teszteléséhez. A meglévő promptot módosíthatod a **User prompt** mezőben azzal, hogy belekattintasz és átírod a szöveget.  
1. Miután befejezted az ügynök tesztelését, a szervert leállíthatod a **terminálban** a **CTRL/CMD+C** megnyomásával.  

## Feladat  

Próbálj meg egy további eszközt hozzáadni a **server.py** fájlodhoz (például számítsd ki egy szám négyzetgyökét). Küldj be új promptokat, amelyekhez az ügynök a te új eszközödet (vagy a meglévő eszközöket) használná. Ne felejtsd el újraindítani a szervert, hogy betöltse az új eszközöket.  

## Megoldás  

[Megoldás](./solution/README.md)  

## Legfontosabb tanulságok  

A fejezet tanulságai a következők:  

- Az AI Toolkit kiterjesztés nagyszerű kliens, amely lehetővé teszi MCP szerverek és eszközeik használatát.  
- Új eszközöket adhatsz hozzá az MCP szerverekhez, így bővítve az ügynök képességeit az igények változásával.  
- Az AI Toolkit sablonokat is tartalmaz (pl. Python MCP szerver sablonokat), hogy megkönnyítse az egyedi eszközök létrehozását.  

## További erőforrások  

- [AI Toolkit dokumentáció](https://aka.ms/AIToolkit/doc)  

## Mi következik  
- Következő: [Tesztelés & Hibakeresés](../08-testing/README.md)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->