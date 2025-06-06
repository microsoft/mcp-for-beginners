<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bc249f8b228953fafca05f94bb572aac",
  "translation_date": "2025-06-02T19:33:17+00:00",
  "source_file": "05-AdvancedTopics/web-search-mcp/README.md",
  "language_code": "ro"
}
-->
# Lesson: Construirea unui Server MCP pentru Căutare Web

Acest capitol demonstrează cum să construiești un agent AI real care se integrează cu API-uri externe, gestionează diverse tipuri de date, tratează erorile și coordonează mai multe unelte — toate într-un format pregătit pentru producție. Vei vedea:

- **Integrarea cu API-uri externe ce necesită autentificare**
- **Gestionarea diverselor tipuri de date provenite de la multiple endpoint-uri**
- **Strategii robuste de tratare a erorilor și logare**
- **Orchestrarea mai multor unelte într-un singur server**

La final, vei avea experiență practică cu modele și bune practici esențiale pentru aplicații avansate AI și bazate pe LLM.

## Introducere

În această lecție vei învăța cum să construiești un server și un client MCP avansat care extinde capabilitățile LLM cu date web în timp real folosind SerpAPI. Aceasta este o abilitate critică pentru dezvoltarea agenților AI dinamici care pot accesa informații actualizate de pe web.

## Obiective de Învățare

La finalul acestei lecții vei putea:

- Integra API-uri externe (precum SerpAPI) în mod securizat într-un server MCP
- Implementa multiple unelte pentru căutare web, știri, produse și întrebări-răspunsuri
- Parcurge și formata date structurate pentru consumul LLM
- Gestiona erorile și limita de cereri API eficient
- Construi și testa atât clienți MCP automatizați, cât și interactivi

## Server MCP pentru Căutare Web

Această secțiune prezintă arhitectura și funcționalitățile Serverului MCP pentru Căutare Web. Vei vedea cum FastMCP și SerpAPI sunt folosite împreună pentru a extinde capabilitățile LLM cu date web în timp real.

### Prezentare generală

Implementarea include patru unelte care evidențiază abilitatea MCP de a gestiona în mod securizat și eficient sarcini diverse bazate pe API-uri externe:

- **general_search**: Pentru rezultate generale de pe web
- **news_search**: Pentru titluri recente de știri
- **product_search**: Pentru date de comerț electronic
- **qna**: Pentru fragmente de întrebări și răspunsuri

### Funcționalități
- **Exemple de cod**: Include blocuri de cod specifice limbajului Python (și ușor extensibile pentru alte limbaje) folosind secțiuni extensibile pentru claritate

<details>  
<summary>Python</summary>  

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
</details>

Înainte de a rula clientul, este util să înțelegi ce face serverul. [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) file implements the MCP server, exposing tools for web, news, product search, and Q&A by integrating with SerpAPI. It handles incoming requests, manages API calls, parses responses, and returns structured results to the client.

You can review the full implementation in [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Iată un exemplu scurt despre cum serverul definește și înregistrează o unealtă:

<details>  
<summary>Python Server</summary> 

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
</details>

- **Integrarea API-urilor externe**: Demonstrează gestionarea securizată a cheilor API și a cererilor externe
- **Parsarea datelor structurate**: Arată cum se transformă răspunsurile API în formate prietenoase pentru LLM
- **Tratarea erorilor**: Gestionare robustă a erorilor cu logare corespunzătoare
- **Client interactiv**: Include teste automate și un mod interactiv pentru testare
- **Gestionarea contextului**: Folosește MCP Context pentru logare și urmărirea cererilor

## Cerințe preliminare

Înainte să începi, asigură-te că mediul tău este configurat corect urmând acești pași. Astfel vei garanta că toate dependențele sunt instalate și cheile tale API sunt configurate corespunzător pentru o dezvoltare și testare fără probleme.

- Python 3.8 sau versiune superioară
- Cheie API SerpAPI (Înregistrează-te la [SerpAPI](https://serpapi.com/) - disponibil plan gratuit)

## Instalare

Pentru a începe, urmează acești pași pentru configurarea mediului:

1. Instalează dependențele folosind uv (recomandat) sau pip:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. Creează un fișier `.env` în rădăcina proiectului cu cheia ta SerpAPI:

```
SERPAPI_KEY=your_serpapi_key_here
```

## Utilizare

Serverul MCP pentru Căutare Web este componenta centrală care expune unelte pentru căutare web, știri, produse și Q&A prin integrarea cu SerpAPI. El preia cererile, gestionează apelurile API, parsează răspunsurile și returnează rezultate structurate clientului.

Poți consulta implementarea completă în [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Pornirea serverului

Pentru a porni serverul MCP, folosește comanda următoare:

```bash
python server.py
```

Serverul va rula ca un MCP bazat pe stdio la care clientul se poate conecta direct.

### Moduri client

Clientul (`client.py`) supports two modes for interacting with the MCP server:

- **Normal mode**: Runs automated tests that exercise all the tools and verify their responses. This is useful for quickly checking that the server and tools are working as expected.
- **Interactive mode**: Starts a menu-driven interface where you can manually select and call tools, enter custom queries, and see results in real time. This is ideal for exploring the server's capabilities and experimenting with different inputs.

You can review the full implementation in [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Pornirea clientului

Pentru a rula testele automate (asta va porni automat serverul):

```bash
python client.py
```

Sau rulează în mod interactiv:

```bash
python client.py --interactive
```

### Testarea cu metode diferite

Există mai multe moduri de a testa și interacționa cu uneltele oferite de server, în funcție de nevoile și fluxul tău de lucru.

#### Scrierea scripturilor de test personalizate cu MCP Python SDK
Poți să-ți construiești propriile scripturi de test folosind MCP Python SDK:

<details>
<summary>Python</summary>

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
</details>

În acest context, un „script de test” înseamnă un program Python personalizat pe care îl scrii pentru a acționa ca un client pentru serverul MCP. În loc să fie un test formal unitar, acest script îți permite să te conectezi programatic la server, să apelezi oricare dintre uneltele sale cu parametrii pe care îi alegi și să inspectezi rezultatele. Această abordare este utilă pentru:
- Prototiparea și experimentarea cu apeluri către unelte
- Validarea modului în care serverul răspunde la diferite intrări
- Automatizarea invocărilor repetate ale uneltelor
- Construirea propriilor fluxuri de lucru sau integrări peste serverul MCP

Poți folosi scripturile de test pentru a încerca rapid interogări noi, a depana comportamentul uneltelor sau chiar ca punct de plecare pentru automatizări mai avansate. Mai jos este un exemplu de utilizare a MCP Python SDK pentru a crea un astfel de script:

## Descrierea uneltelor

Poți folosi următoarele unelte oferite de server pentru a efectua diferite tipuri de căutări și interogări. Fiecare unealtă este descrisă mai jos împreună cu parametrii și un exemplu de utilizare.

Această secțiune oferă detalii despre fiecare unealtă disponibilă și parametrii lor.

### general_search

Execută o căutare generală pe web și returnează rezultate formatate.

**Cum să apelezi această unealtă:**

Poți apela `general_search` din propriul script folosind MCP Python SDK sau interactiv, folosind Inspectorul sau modul client interactiv. Iată un exemplu de cod folosind SDK-ul:

<details>
<summary>Exemplu Python</summary>

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
</details>

Alternativ, în modul interactiv, selectează `general_search` from the menu and enter your query when prompted.

**Parameters:**
- `query` (string): Interogarea de căutare

**Exemplu de cerere:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

Caută articole recente de știri legate de o interogare.

**Cum să apelezi această unealtă:**

Poți apela `news_search` din propriul script folosind MCP Python SDK sau interactiv, folosind Inspectorul sau modul client interactiv. Iată un exemplu de cod folosind SDK-ul:

<details>
<summary>Exemplu Python</summary>

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
</details>

Alternativ, în modul interactiv, selectează `news_search` from the menu and enter your query when prompted.

**Parameters:**
- `query` (string): Interogarea de căutare

**Exemplu de cerere:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

Caută produse care corespund unei interogări.

**Cum să apelezi această unealtă:**

Poți apela `product_search` din propriul script folosind MCP Python SDK sau interactiv, folosind Inspectorul sau modul client interactiv. Iată un exemplu de cod folosind SDK-ul:

<details>
<summary>Exemplu Python</summary>

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
</details>

Alternativ, în modul interactiv, selectează `product_search` from the menu and enter your query when prompted.

**Parameters:**
- `query` (string): Interogarea pentru căutarea produselor

**Exemplu de cerere:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

Oferă răspunsuri directe la întrebări din motoarele de căutare.

**Cum să apelezi această unealtă:**

Poți apela `qna` din propriul script folosind MCP Python SDK sau interactiv, folosind Inspectorul sau modul client interactiv. Iată un exemplu de cod folosind SDK-ul:

<details>
<summary>Exemplu Python</summary>

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
</details>

Alternativ, în modul interactiv, selectează `qna` from the menu and enter your question when prompted.

**Parameters:**
- `question` (string): Întrebarea pentru care vrei un răspuns

**Exemplu de cerere:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Detalii despre cod

Această secțiune oferă fragmente de cod și referințe pentru implementările serverului și clientului.

<details>
<summary>Python</summary>

Vezi [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) and [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) pentru detalii complete ale implementării.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```
</details>

## Concepte Avansate în Această Lecție

Înainte să începi să construiești, iată câteva concepte avansate importante care vor apărea pe tot parcursul acestui capitol. Înțelegerea lor te va ajuta să urmezi mai ușor, chiar dacă sunt noi pentru tine:

- **Orchestrarea mai multor unelte**: Aceasta înseamnă rularea simultană a mai multor unelte diferite (cum ar fi căutare web, știri, produse și Q&A) într-un singur server MCP. Permite serverului tău să gestioneze o varietate de sarcini, nu doar una singură.
- **Gestionarea limitelor API**: Multe API-uri externe (precum SerpAPI) limitează câte cereri poți face într-un interval de timp. Codul bine scris verifică aceste limite și le gestionează elegant, astfel încât aplicația ta să nu se blocheze dacă atingi o limită.
- **Parsarea datelor structurate**: Răspunsurile API sunt adesea complexe și imbricate. Acest concept înseamnă transformarea acestor răspunsuri în formate curate, ușor de folosit, prietenoase pentru LLM-uri sau alte programe.
- **Recuperarea după erori**: Uneori apar probleme — poate rețeaua cade sau API-ul nu returnează ce te aștepți. Recuperarea după erori înseamnă că codul tău poate gestiona aceste probleme și tot oferă feedback util, în loc să se blocheze.
- **Validarea parametrilor**: Aceasta înseamnă verificarea faptului că toate intrările către uneltele tale sunt corecte și sigure pentru utilizare. Include setarea valorilor implicite și asigurarea tipurilor corecte, ceea ce ajută la prevenirea erorilor și confuziilor.

Această secțiune te va ajuta să diagnostichezi și să rezolvi probleme comune pe care le-ai putea întâmpina lucrând cu Serverul MCP pentru Căutare Web. Dacă întâmpini erori sau comportamente neașteptate, această secțiune de depanare oferă soluții pentru cele mai frecvente probleme. Consultă aceste sfaturi înainte de a căuta ajutor suplimentar — ele rezolvă adesea rapid problemele.

## Depanare

Lucrând cu Serverul MCP pentru Căutare Web, este normal să întâlnești ocazional probleme — acest lucru este firesc când dezvolți cu API-uri externe și unelte noi. Această secțiune oferă soluții practice pentru cele mai comune probleme, astfel încât să te poți întoarce rapid pe drumul cel bun. Dacă întâmpini o eroare, începe de aici: sfaturile de mai jos abordează problemele pe care cei mai mulți utilizatori le întâlnesc și pot rezolva adesea problema fără ajutor suplimentar.

### Probleme frecvente

Mai jos sunt câteva dintre cele mai des întâlnite probleme, împreună cu explicații clare și pași pentru rezolvare:

1. **Lipsește SERPAPI_KEY în fișierul .env**
   - Dacă vezi eroarea `SERPAPI_KEY environment variable not found`, it means your application can't find the API key needed to access SerpAPI. To fix this, create a file named `.env` in your project root (if it doesn't already exist) and add a line like `SERPAPI_KEY=your_serpapi_key_here`. Make sure to replace `your_serpapi_key_here` with your actual key from the SerpAPI website.

2. **Module not found errors**
   - Errors such as `ModuleNotFoundError: No module named 'httpx'` indicate that a required Python package is missing. This usually happens if you haven't installed all the dependencies. To resolve this, run `pip install -r requirements.txt` in your terminal to install everything your project needs.

3. **Connection issues**
   - If you get an error like `Error during client execution`, it often means the client can't connect to the server, or the server isn't running as expected. Double-check that both the client and server are compatible versions, and that `server.py` is present and running in the correct directory. Restarting both the server and client can also help.

4. **SerpAPI errors**
   - Seeing `Search API returned error status: 401` means your SerpAPI key is missing, incorrect, or expired. Go to your SerpAPI dashboard, verify your key, and update your `, creează fișierul `.env` dacă este nevoie. Dacă cheia ta este corectă, dar încă vezi această eroare, verifică dacă planul gratuit nu ți-a expirat cota.

### Modul Debug

Implicit, aplicația loghează doar informațiile importante. Dacă vrei să vezi mai multe detalii despre ce se întâmplă (de exemplu, pentru a diagnostica probleme dificile), poți activa modul DEBUG. Acesta îți va arăta mult mai multe despre fiecare pas pe care îl face aplicația.

**Exemplu: Ieșire normală**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**Exemplu: Ieșire DEBUG**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

Observă cum modul DEBUG include linii suplimentare despre cererile HTTP, răspunsuri și alte detalii interne. Acest lucru poate fi foarte util pentru depanare.

Pentru a activa modul DEBUG, setează nivelul de logare la DEBUG în partea de sus a fișierului `client.py` or `server.py`:

<details>
<summary>Python</summary>

```python
# At the top of your client.py or server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```
</details>

---

## Ce urmează

- [6. Community Contributions](../../06-CommunityContributions/README.md)

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot rezulta din utilizarea acestei traduceri.