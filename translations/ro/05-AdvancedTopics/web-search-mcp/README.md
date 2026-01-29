# Lecția: Construirea unui server MCP pentru căutare web

Acest capitol arată cum să construiești un agent AI real care se integrează cu API-uri externe, gestionează tipuri diverse de date, tratează erorile și coordonează mai multe unelte — toate într-un format pregătit pentru producție. Vei vedea:

- **Integrarea cu API-uri externe care necesită autentificare**
- **Gestionarea tipurilor diverse de date provenite din mai multe endpoint-uri**
- **Strategii robuste de tratare a erorilor și logare**
- **Orchestrarea mai multor unelte într-un singur server**

La final, vei avea experiență practică cu modele și bune practici esențiale pentru aplicații avansate AI și bazate pe LLM.

## Introducere

În această lecție vei învăța cum să construiești un server și un client MCP avansat care extind capabilitățile LLM cu date web în timp real folosind SerpAPI. Aceasta este o abilitate esențială pentru dezvoltarea agenților AI dinamici care pot accesa informații actualizate de pe web.

## Obiective de învățare

La finalul acestei lecții vei putea:

- Integra API-uri externe (precum SerpAPI) în siguranță într-un server MCP
- Implementa mai multe unelte pentru căutare web, știri, produse și întrebări-răspunsuri
- Parcurge și formata date structurate pentru consumul LLM
- Gestiona erorile și limita de rată a API-ului eficient
- Construi și testa atât clienți MCP automatizați, cât și interactivi

## Server MCP pentru căutare web

Această secțiune introduce arhitectura și funcționalitățile Serverului MCP pentru căutare web. Vei vedea cum FastMCP și SerpAPI sunt folosite împreună pentru a extinde capabilitățile LLM cu date web în timp real.

### Prezentare generală

Implementarea include patru unelte care demonstrează capacitatea MCP de a gestiona sarcini diverse, bazate pe API-uri externe, în mod sigur și eficient:

- **general_search**: Pentru rezultate web generale
- **news_search**: Pentru titluri recente de știri
- **product_search**: Pentru date de comerț electronic
- **qna**: Pentru fragmente de întrebări și răspunsuri

### Funcționalități
- **Exemple de cod**: Include blocuri de cod specifice limbajului Python (și ușor extensibile la alte limbaje) folosind pivoturi de cod pentru claritate

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

Înainte de a rula clientul, este util să înțelegi ce face serverul. Fișierul [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) implementează serverul MCP, expunând unelte pentru căutare web, știri, produse și Q&A prin integrarea cu SerpAPI. Acesta gestionează cererile primite, apelează API-ul, parsează răspunsurile și returnează rezultate structurate clientului.

Poți consulta implementarea completă în [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

Iată un exemplu scurt despre cum serverul definește și înregistrează o unealtă:

### Server Python

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

- **Integrare API extern**: Demonstrează gestionarea sigură a cheilor API și a cererilor externe
- **Parsare date structurate**: Arată cum se transformă răspunsurile API în formate prietenoase pentru LLM
- **Gestionarea erorilor**: Tratare robustă a erorilor cu logare adecvată
- **Client interactiv**: Include atât teste automate, cât și un mod interactiv pentru testare
- **Managementul contextului**: Folosește MCP Context pentru logare și urmărirea cererilor

## Cerințe preliminare

Înainte să începi, asigură-te că mediul tău este configurat corect urmând acești pași. Astfel vei avea toate dependențele instalate și cheile API configurate corect pentru o dezvoltare și testare fără probleme.

- Python 3.8 sau versiune superioară
- Cheie API SerpAPI (Înscrie-te la [SerpAPI](https://serpapi.com/) - există un plan gratuit)

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

Serverul MCP pentru căutare web este componenta principală care expune unelte pentru căutare web, știri, produse și Q&A prin integrarea cu SerpAPI. Acesta gestionează cererile primite, apelează API-ul, parsează răspunsurile și returnează rezultate structurate clientului.

Poți consulta implementarea completă în [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py).

### Pornirea serverului

Pentru a porni serverul MCP, folosește comanda următoare:

```bash
python server.py
```

Serverul va rula ca un server MCP bazat pe stdio, la care clientul se poate conecta direct.

### Moduri client

Clientul (`client.py`) suportă două moduri de interacțiune cu serverul MCP:

- **Mod normal**: Rulează teste automate care verifică toate uneltele și răspunsurile lor. Este util pentru a verifica rapid dacă serverul și uneltele funcționează corect.
- **Mod interactiv**: Pornește o interfață cu meniu unde poți selecta manual uneltele, introduce întrebări personalizate și vedea rezultatele în timp real. Ideal pentru explorarea capabilităților serverului și experimentarea cu diferite inputuri.

Poți consulta implementarea completă în [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py).

### Pornirea clientului

Pentru a rula testele automate (aceasta va porni automat și serverul):

```bash
python client.py
```

Sau pentru a rula în mod interactiv:

```bash
python client.py --interactive
```

### Testarea cu metode diferite

Există mai multe moduri de a testa și interacționa cu uneltele oferite de server, în funcție de nevoile și fluxul tău de lucru.

#### Scrierea scripturilor de test personalizate cu MCP Python SDK
Poți construi și propriile scripturi de test folosind MCP Python SDK:

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

În acest context, un „script de test” înseamnă un program Python personalizat pe care îl scrii pentru a acționa ca un client pentru serverul MCP. În loc să fie un test unitar formal, acest script îți permite să te conectezi programatic la server, să apelezi oricare dintre uneltele sale cu parametrii aleși de tine și să inspectezi rezultatele. Această abordare este utilă pentru:
- Prototiparea și experimentarea cu apeluri către unelte
- Validarea modului în care serverul răspunde la inputuri diferite
- Automatizarea apelurilor repetate către unelte
- Construirea propriilor fluxuri de lucru sau integrări peste serverul MCP

Poți folosi scripturile de test pentru a încerca rapid întrebări noi, a depana comportamentul uneltelor sau chiar ca punct de plecare pentru automatizări mai avansate. Mai jos este un exemplu de utilizare a MCP Python SDK pentru a crea un astfel de script:

## Descrierea uneltelor

Poți folosi următoarele unelte oferite de server pentru a efectua diferite tipuri de căutări și interogări. Fiecare unealtă este descrisă mai jos împreună cu parametrii și un exemplu de utilizare.

Această secțiune oferă detalii despre fiecare unealtă disponibilă și parametrii lor.

### general_search

Efectuează o căutare web generală și returnează rezultate formatate.

**Cum să apelezi această unealtă:**

Poți apela `general_search` din propriul script folosind MCP Python SDK, sau interactiv folosind Inspectorul sau modul interactiv al clientului. Iată un exemplu de cod folosind SDK-ul:

# [Exemplu Python](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativ, în modul interactiv, selectează `general_search` din meniu și introdu întrebarea când ți se cere.

**Parametri:**
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

Poți apela `news_search` din propriul script folosind MCP Python SDK, sau interactiv folosind Inspectorul sau modul interactiv al clientului. Iată un exemplu de cod folosind SDK-ul:

# [Exemplu Python](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativ, în modul interactiv, selectează `news_search` din meniu și introdu întrebarea când ți se cere.

**Parametri:**
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

Poți apela `product_search` din propriul script folosind MCP Python SDK, sau interactiv folosind Inspectorul sau modul interactiv al clientului. Iată un exemplu de cod folosind SDK-ul:

# [Exemplu Python](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativ, în modul interactiv, selectează `product_search` din meniu și introdu întrebarea când ți se cere.

**Parametri:**
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

Poți apela `qna` din propriul script folosind MCP Python SDK, sau interactiv folosind Inspectorul sau modul interactiv al clientului. Iată un exemplu de cod folosind SDK-ul:

# [Exemplu Python](../../../../05-AdvancedTopics/web-search-mcp)

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

Alternativ, în modul interactiv, selectează `qna` din meniu și introdu întrebarea când ți se cere.

**Parametri:**
- `question` (string): Întrebarea pentru care vrei un răspuns

**Exemplu de cerere:**

```json
{
  "question": "what is artificial intelligence"
}
```

## Detalii despre cod

Această secțiune oferă fragmente de cod și referințe pentru implementările serverului și clientului.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

Vezi [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) și [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) pentru detalii complete de implementare.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## Concepte avansate în această lecție

Înainte să începi să construiești, iată câteva concepte avansate importante care vor apărea pe parcursul acestui capitol. Înțelegerea lor te va ajuta să urmărești mai ușor, chiar dacă sunt noi pentru tine:

- **Orchestrarea mai multor unelte**: Înseamnă rularea mai multor unelte diferite (precum căutare web, știri, produse și Q&A) într-un singur server MCP. Permite serverului să gestioneze o varietate de sarcini, nu doar una singură.
- **Gestionarea limitelor de rată API**: Multe API-uri externe (precum SerpAPI) limitează câte cereri poți face într-un anumit interval. Un cod bine scris verifică aceste limite și le gestionează elegant, astfel încât aplicația ta să nu se blocheze dacă atingi limita.
- **Parsarea datelor structurate**: Răspunsurile API sunt adesea complexe și ierarhizate. Acest concept se referă la transformarea acestor răspunsuri în formate curate, ușor de folosit, prietenoase pentru LLM-uri sau alte programe.
- **Recuperarea după erori**: Uneori apar probleme — poate rețeaua cade sau API-ul nu returnează ce te aștepți. Recuperarea după erori înseamnă că codul tău poate gestiona aceste probleme și tot oferă feedback util, în loc să se oprească brusc.
- **Validarea parametrilor**: Este vorba despre verificarea faptului că toate inputurile către uneltele tale sunt corecte și sigure de folosit. Include setarea valorilor implicite și asigurarea tipurilor corecte, ceea ce ajută la prevenirea erorilor și confuziilor.

Această secțiune te va ajuta să diagnostichezi și să rezolvi probleme comune pe care le-ai putea întâlni lucrând cu Serverul MCP pentru căutare web. Dacă întâmpini erori sau comportamente neașteptate, această secțiune de depanare oferă soluții pentru cele mai frecvente probleme. Consultă aceste sfaturi înainte de a cere ajutor suplimentar — adesea rezolvă rapid problemele.

## Depanare

Lucrând cu Serverul MCP pentru căutare web, este normal să întâlnești uneori probleme — acest lucru este frecvent când dezvolți cu API-uri externe și unelte noi. Această secțiune oferă soluții practice pentru cele mai comune probleme, ca să te poți întoarce rapid la lucru. Dacă întâmpini o eroare, începe de aici: sfaturile de mai jos abordează problemele cu care se confruntă majoritatea utilizatorilor și pot rezolva adesea problema fără ajutor suplimentar.

### Probleme comune

Mai jos sunt câteva dintre cele mai frecvente probleme întâlnite de utilizatori, împreună cu explicații clare și pași pentru rezolvare:

1. **Lipsa variabilei SERPAPI_KEY în fișierul .env**
   - Dacă vezi eroarea `SERPAPI_KEY environment variable not found`, înseamnă că aplicația ta nu găsește cheia API necesară pentru accesul la SerpAPI. Pentru a remedia, creează un fișier numit `.env` în rădăcina proiectului (dacă nu există deja) și adaugă o linie de forma `SERPAPI_KEY=cheia_ta_serpapi`. Asigură-te că înlocuiești `cheia_ta_serpapi` cu cheia ta reală de pe site-ul SerpAPI.

2. **Erori de tipul „Module not found”**
   - Erori precum `ModuleNotFoundError: No module named 'httpx'` indică faptul că un pachet Python necesar lipsește. Acest lucru se întâmplă de obicei dacă nu ai instalat toate dependențele. Pentru a rezolva, rulează `pip install -r requirements.txt` în terminal pentru a instala tot ce are nevoie proiectul.

3. **Probleme de conexiune**
   - Dacă primești o eroare de genul `Error during client execution`, de obicei înseamnă că clientul nu poate să se conecteze la server sau serverul nu rulează cum trebuie. Verifică dacă clientul și serverul sunt versiuni compatibile și dacă fișierul `server.py` este prezent și rulează în directorul corect. Restartarea ambelor poate ajuta.

4. **Erori SerpAPI**
   - Mesajul `Search API returned error status: 401` indică faptul că cheia ta SerpAPI lipsește, este incorectă sau a expirat. Accesează dashboard-ul SerpAPI, verifică cheia și actualizează fișierul `.env` dacă este nevoie. Dacă cheia este corectă, dar eroarea persistă, verifică dacă planul tău gratuit nu a depășit cota.

### Mod debug

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
Pentru a activa modul DEBUG, setează nivelul de logare la DEBUG în partea de sus a fișierului `client.py` sau `server.py`:

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

## Ce urmează

- [5.10 Streaming în timp real](../mcp-realtimestreaming/README.md)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.