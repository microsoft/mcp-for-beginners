# Pamoka: Internetinės paieškos MCP serverio kūrimas

Šiame skyriuje parodoma, kaip sukurti realaus pasaulio AI agentą, kuris integruojasi su išoriniais API, tvarko įvairius duomenų tipus, valdo klaidas ir koordinuoja kelis įrankius – visa tai gamybai paruoštu formatu. Jūs sužinosite:

- **Integraciją su išoriniais API, reikalaujančiais autentifikacijos**
- **Įvairių duomenų tipų tvarkymą iš kelių galinių taškų**
- **Patikimas klaidų valdymo ir registravimo strategijas**
- **Kelių įrankių koordinavimą viename serveryje**

Pamokos pabaigoje turėsite praktinės patirties su modeliais ir geriausiomis praktikomis, kurios yra būtinos pažangioms AI ir LLM pagrįstoms programoms.

## Įvadas

Šioje pamokoje sužinosite, kaip sukurti pažangų MCP serverį ir klientą, kuris praplečia LLM galimybes realaus laiko interneto duomenimis naudojant SerpAPI. Tai yra kritinis įgūdis kuriant dinamiškus AI agentus, galinčius pasiekti naujausią informaciją iš interneto.

## Mokymosi tikslai

Pamokos pabaigoje galėsite:

- Saugiai integruoti išorinius API (pvz., SerpAPI) į MCP serverį
- Įgyvendinti kelis įrankius interneto, naujienų, produktų paieškai ir klausimų-atsakymų funkcijoms
- Analizuoti ir formatuoti struktūrizuotus duomenis LLM naudojimui
- Efektyviai valdyti klaidas ir API kvotų apribojimus
- Kurti ir testuoti tiek automatizuotus, tiek interaktyvius MCP klientus

## Internetinės paieškos MCP serveris

Šiame skyriuje pristatoma internetinės paieškos MCP serverio architektūra ir funkcijos. Sužinosite, kaip FastMCP ir SerpAPI naudojami kartu, kad praplėstų LLM galimybes realaus laiko interneto duomenimis.

### Apžvalga

Ši implementacija apima keturis įrankius, kurie demonstruoja MCP gebėjimą saugiai ir efektyviai tvarkyti įvairias užduotis, pagrįstas išoriniais API:

- **general_search**: Bendri interneto paieškos rezultatai
- **news_search**: Naujausios antraštės
- **product_search**: E. komercijos duomenys
- **qna**: Klausimų-atsakymų fragmentai

### Funkcijos
- **Kodo pavyzdžiai**: Apima kalbai specifinius kodo blokus Python (ir lengvai pritaikomus kitoms kalboms) naudojant kodo perjungimus aiškumui

### Python

```python
# Example usage of the general_search tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "open source LLMs"})
            print(result)
```

---

Prieš paleisdami klientą, naudinga suprasti, ką daro serveris. [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) faile įgyvendintas MCP serveris, kuris teikia įrankius interneto, naujienų, produktų paieškai ir klausimų-atsakymų funkcijoms, integruojantis su SerpAPI. Jis tvarko gaunamus užklausas, valdo API kvietimus, analizuoja atsakymus ir grąžina struktūrizuotus rezultatus klientui.

Visą implementaciją galite peržiūrėti [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Trumpas pavyzdys, kaip serveris apibrėžia ir registruoja įrankį:

### Python Serveris

```python
# server.py (excerpt)
from mcp.server import MCPServer, Tool

async def general_search(query: str):
    # ...implementation...

server = MCPServer()
server.add_tool(Tool("general_search", general_search))

if __name__ == "__main__":
    server.run()
```

---

- **Išorinių API integracija**: Demonstruoja saugų API raktų ir išorinių užklausų tvarkymą
- **Struktūrizuotų duomenų analizė**: Parodo, kaip API atsakymus paversti LLM draugiškais formatais
- **Klaidų valdymas**: Patikimas klaidų valdymas su tinkamu registravimu
- **Interaktyvus klientas**: Apima tiek automatizuotus testus, tiek interaktyvų režimą testavimui
- **Konteksto valdymas**: Naudoja MCP kontekstą registravimui ir užklausų sekimui

## Reikalavimai

Prieš pradėdami, įsitikinkite, kad jūsų aplinka tinkamai paruošta, atlikdami šiuos veiksmus. Tai užtikrins, kad visos priklausomybės būtų įdiegtos ir jūsų API raktai būtų tinkamai sukonfigūruoti sklandžiam kūrimui ir testavimui.

- Python 3.8 ar naujesnė versija
- SerpAPI API raktas (Užsiregistruokite [SerpAPI](https://serpapi.com/) - nemokamas planas prieinamas)

## Įdiegimas

Norėdami pradėti, atlikite šiuos veiksmus, kad nustatytumėte savo aplinką:

1. Įdiekite priklausomybes naudodami uv (rekomenduojama) arba pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Sukurkite `.env` failą projekto šaknyje su savo SerpAPI raktu:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Naudojimas

Internetinės paieškos MCP serveris yra pagrindinis komponentas, kuris teikia įrankius interneto, naujienų, produktų paieškai ir klausimų-atsakymų funkcijoms, integruojantis su SerpAPI. Jis tvarko gaunamas užklausas, valdo API kvietimus, analizuoja atsakymus ir grąžina struktūrizuotus rezultatus klientui.

Visą implementaciją galite peržiūrėti [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Serverio paleidimas

Norėdami paleisti MCP serverį, naudokite šią komandą:

```bash
python server.py
```

Serveris veiks kaip stdio pagrįstas MCP serveris, prie kurio klientas gali tiesiogiai prisijungti.

### Kliento režimai

Klientas (`client.py`) palaiko du režimus sąveikai su MCP serveriu:

- **Normalus režimas**: Paleidžia automatizuotus testus, kurie patikrina visus įrankius ir jų atsakymus. Tai naudinga greitai patikrinti, ar serveris ir įrankiai veikia kaip tikėtasi.
- **Interaktyvus režimas**: Paleidžia meniu pagrįstą sąsają, kurioje galite rankiniu būdu pasirinkti ir kviesti įrankius, įvesti pasirinktines užklausas ir realiu laiku matyti rezultatus. Tai idealu norint tyrinėti serverio galimybes ir eksperimentuoti su skirtingais įvesties duomenimis.

Visą implementaciją galite peržiūrėti [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Kliento paleidimas

Norėdami paleisti automatizuotus testus (tai automatiškai paleis serverį):

```bash
python client.py
```

Arba paleiskite interaktyviu režimu:

```bash
python client.py --interactive
```

### Testavimas skirtingais metodais

Yra keli būdai testuoti ir sąveikauti su serverio teikiamais įrankiais, priklausomai nuo jūsų poreikių ir darbo eigos.

#### Pasirinktinių testavimo scenarijų rašymas naudojant MCP Python SDK
Taip pat galite sukurti savo testavimo scenarijus naudodami MCP Python SDK:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_custom_query():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call tools with your custom parameters
            result = await session.call_tool("general_search", 
                                           arguments={"query": "your custom query"})
            # Process the result
```

---

Šiame kontekste „testavimo scenarijus“ reiškia pasirinktą Python programą, kurią rašote kaip klientą MCP serveriui. Vietoj formalaus vieneto testo, šis scenarijus leidžia programiškai prisijungti prie serverio, kviesti bet kurį jo įrankį su jūsų pasirinktais parametrais ir analizuoti rezultatus. Šis metodas naudingas:

- Įrankių kvietimų prototipavimui ir eksperimentavimui
- Serverio atsakymų validavimui skirtingiems įvesties duomenims
- Pakartotinių įrankių kvietimų automatizavimui
- Savo darbo eigų ar integracijų kūrimui MCP serverio pagrindu

Testavimo scenarijai leidžia greitai išbandyti naujas užklausas, derinti įrankių elgseną ar net kaip pradinį tašką sudėtingesnei automatizacijai. Žemiau pateiktas pavyzdys, kaip naudoti MCP Python SDK tokiam scenarijui sukurti:

## Įrankių aprašymai

Galite naudoti šiuos serverio teikiamus įrankius skirtingų tipų paieškoms ir užklausoms atlikti. Kiekvienas įrankis aprašytas žemiau su jo parametrais ir naudojimo pavyzdžiais.

Šiame skyriuje pateikiama informacija apie kiekvieną galimą įrankį ir jų parametrus.

### general_search

Atlieka bendrą interneto paiešką ir grąžina suformatuotus rezultatus.

**Kaip kviesti šį įrankį:**

Galite kviesti `general_search` iš savo scenarijaus naudodami MCP Python SDK arba interaktyviai naudodami Inspector arba interaktyvų kliento režimą. Štai kodo pavyzdys naudojant SDK:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_general_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "latest AI trends"})
            print(result)
```

---

Arba interaktyviu režimu pasirinkite `general_search` iš meniu ir įveskite savo užklausą, kai būsite paprašyti.

**Parametrai:**
- `query` (string): Paieškos užklausa

**Užklausos pavyzdys:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Ieško naujausių naujienų straipsnių, susijusių su užklausa.

**Kaip kviesti šį įrankį:**

Galite kviesti `news_search` iš savo scenarijaus naudodami MCP Python SDK arba interaktyviai naudodami Inspector arba interaktyvų kliento režimą. Štai kodo pavyzdys naudojant SDK:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_news_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("news_search", arguments={"query": "AI policy updates"})
            print(result)
```

---

Arba interaktyviu režimu pasirinkite `news_search` iš meniu ir įveskite savo užklausą, kai būsite paprašyti.

**Parametrai:**
- `query` (string): Paieškos užklausa

**Užklausos pavyzdys:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Ieško produktų, atitinkančių užklausą.

**Kaip kviesti šį įrankį:**

Galite kviesti `product_search` iš savo scenarijaus naudodami MCP Python SDK arba interaktyviai naudodami Inspector arba interaktyvų kliento režimą. Štai kodo pavyzdys naudojant SDK:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_product_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("product_search", arguments={"query": "best AI gadgets 2025"})
            print(result)
```

---

Arba interaktyviu režimu pasirinkite `product_search` iš meniu ir įveskite savo užklausą, kai būsite paprašyti.

**Parametrai:**
- `query` (string): Produktų paieškos užklausa

**Užklausos pavyzdys:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Gauti tiesioginius atsakymus į klausimus iš paieškos sistemų.

**Kaip kviesti šį įrankį:**

Galite kviesti `qna` iš savo scenarijaus naudodami MCP Python SDK arba interaktyviai naudodami Inspector arba interaktyvų kliento režimą. Štai kodo pavyzdys naudojant SDK:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_qna():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("qna", arguments={"question": "what is artificial intelligence"})
            print(result)
```

---

Arba interaktyviu režimu pasirinkite `qna` iš meniu ir įveskite savo klausimą, kai būsite paprašyti.

**Parametrai:**
- `question` (string): Klausimas, į kurį reikia rasti atsakymą

**Užklausos pavyzdys:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Kodo detalės

Šiame skyriuje pateikiami kodo fragmentai ir nuorodos į serverio ir kliento implementacijas.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Žr. [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) ir [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) visą implementacijos informaciją.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Pažangios sąvokos šioje pamokoje

Prieš pradėdami kurti, štai keletas svarbių pažangių sąvokų, kurios pasirodys visame šiame skyriuje. Jų supratimas padės jums sekti, net jei esate naujokas:

- **Kelių įrankių koordinavimas**: Tai reiškia kelių skirtingų įrankių (pvz., interneto paieška, naujienų paieška, produktų paieška ir klausimų-atsakymų funkcijos) paleidimą viename MCP serveryje. Tai leidžia jūsų serveriui tvarkyti įvairias užduotis, o ne tik vieną.
- **API kvotų apribojimų valdymas**: Daugelis išorinių API (pvz., SerpAPI) riboja, kiek užklausų galite atlikti per tam tikrą laiką. Geras kodas tikrina šiuos apribojimus ir tvarko juos tinkamai, kad jūsų programa nesugestų, jei pasieksite limitą.
- **Struktūrizuotų duomenų analizė**: API atsakymai dažnai yra sudėtingi ir susiję. Ši sąvoka yra apie tai, kaip paversti tuos atsakymus švariais, lengvai naudojamais formatais, kurie yra draugiški LLM ar kitoms programoms.
- **Klaidų atkūrimas**: Kartais kažkas nepavyksta – galbūt tinklas sugenda arba API negrąžina to, ko tikitės. Klaidų atkūrimas reiškia, kad jūsų kodas gali tvarkyti šias problemas ir vis tiek pateikti naudingą grįžtamąjį ryšį, o ne sugriūti.
- **Parametrų validacija**: Tai apie tai, kaip patikrinti, ar visi įrankių įvesties duomenys yra teisingi ir saugūs naudoti. Tai apima numatytųjų reikšmių nustatymą ir tipų tikrinimą, kuris padeda išvengti klaidų ir painiavos.

Šis skyrius padės jums diagnozuoti ir išspręsti dažnas problemas, su kuriomis galite susidurti dirbdami su internetinės paieškos MCP serveriu. Jei susiduriate su klaidomis ar netikėtu elgesiu dirbdami su internetinės paieškos MCP serveriu, šis trikčių šalinimo skyrius pateikia sprendimus dažniausioms problemoms. Peržiūrėkite šiuos patarimus prieš ieškodami papildomos pagalbos – jie dažnai greitai išsprendžia problemas.

## Trikčių šalinimas

Dirbant su internetinės paieškos MCP serveriu, kartais galite susidurti su problemomis – tai normalu, kai dirbate su išoriniais API ir naujais įrankiais. Šiame skyriuje pateikiami praktiniai sprendimai dažniausioms problemoms, kad galėtumėte greitai grįžti prie darbo. Jei susiduriate su klaida, pradėkite čia: žemiau pateikti patarimai sprendžia problemas, su kuriomis dažniausiai susiduria vartotojai, ir dažnai gali išspręsti jūsų problemą be papildomos pagalbos.

### Dažnos problemos

Žemiau pateikiamos dažniausios problemos, su kuriomis susiduria vartotojai, kartu su aiškiais paaiškinimais ir žingsniais, kaip jas išspręsti:

1. **Trūksta SERPAPI_KEY `.env` faile**
   - Jei matote klaidą `SERPAPI_KEY environment variable not found`, tai reiškia, kad jūsų programa negali rasti API rakto, reikalingo prieigai prie SerpAPI. Norėdami tai išspręsti, sukurkite failą pavadinimu `.env` savo projekto šaknyje (jei jis dar neegzistuoja) ir pridėkite eilutę, pvz., `SERPAPI_KEY=your_serpapi_key_here`. Įsitikinkite, kad pakeitėte `your_serpapi_key_here` savo faktiniu raktu iš SerpAPI svetainės.

2. **Modulio nerasta klaidos**
   - Klaidos, tokios kaip `ModuleNotFoundError: No module named 'httpx'`, rodo, kad trūksta reikalingo Python paketo. Tai dažniausiai nutinka, jei neįdiegėte visų priklausomybių. Norėdami tai išspręsti, paleiskite `pip install -r requirements.txt` savo terminale, kad įdiegtumėte viską, ko reikia jūsų projektui.

3. **Ryšio problemos**
   - Jei gaunate klaidą, pvz., `Error during client execution`, tai dažnai reiškia, kad klientas negali prisijungti prie serverio arba serveris neveikia kaip tikėtasi. Patikrinkite, ar klientas ir serveris yra suderin
Norėdami įjungti DEBUG režimą, nustatykite registravimo lygį į DEBUG pačioje jūsų `client.py` arba `server.py` failo pradžioje:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
# At the top of your client.py or server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

---

---

## Kas toliau

- [5.10 Realaus laiko transliavimas](../mcp-realtimestreaming/README.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.