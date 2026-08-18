# Protokół Kontekstu Modelu dla Wyszukiwania w Internecie w Czasie Rzeczywistym

## Przegląd

Wyszukiwanie w Internecie w czasie rzeczywistym stało się niezbędne we współczesnym środowisku opartym na informacji, gdzie aplikacje potrzebują natychmiastowego dostępu do aktualnych informacji dostępnych w Internecie, aby zapewnić odpowiednie i terminowe odpowiedzi. Protokół Kontekstu Modelu (MCP) stanowi znaczący postęp w optymalizacji tych procesów wyszukiwania w czasie rzeczywistym, zwiększając efektywność wyszukiwania, zachowując integralność kontekstu oraz poprawiając ogólną wydajność systemu.

Ten moduł bada, jak MCP przekształca wyszukiwanie internetowe w czasie rzeczywistym, dostarczając ustandaryzowane podejście do zarządzania kontekstem pomiędzy modelami AI, silnikami wyszukiwania oraz aplikacjami.

### Czego się Nauczysz

W tym kompleksowym przewodniku odkryjesz:

- Jak MCP tworzy płynne połączenie pomiędzy modelami AI a możliwościami wyszukiwania w czasie rzeczywistym
- Wzorce architektoniczne do realizacji efektywnych i skalowalnych rozwiązań wyszukiwania z MCP
- Techniki zachowania kontekstu wyszukiwania w wielu zapytaniach i interakcjach
- Praktyczne implementacje kodu w Pythonie i JavaScript dla różnych scenariuszy wyszukiwania
- Metody równoważenia trafności, aktualności i wydajności w systemach wyszukiwania opartych na MCP

## Wprowadzenie do Wyszukiwania w Internecie w Czasie Rzeczywistym

Wyszukiwanie w Internecie w czasie rzeczywistym to podejście technologiczne umożliwiające ciągłe zadawanie zapytań, przetwarzanie i analizę informacji internetowych w miarę ich publikacji lub aktualizacji, pozwalając systemom dostarczać świeże i istotne informacje przy minimalnych opóźnieniach. W odróżnieniu od tradycyjnych systemów wyszukiwania działających na zindeksowanych danych, które mogą być godzinami lub dniami przestarzałe, wyszukiwanie w czasie rzeczywistym korzysta z danych na żywo, dostarczając wgląd i informacje odzwierciedlające aktualny stan treści online.

### Podstawowe Koncepcje Wyszukiwania w Internecie w Czasie Rzeczywistym:

- **Ciągłe Przetwarzanie Zapytania**: Zapytania wyszukiwania są przetwarzane względem stale aktualizowanych źródeł danych
- **Priorytet Aktualności**: Systemy są zaprojektowane tak, aby priorytetowo traktować świeże informacje
- **Równoważenie Trafności**: Zachowanie równowagi między trafnością a aktualnością
- **Skalowalna Architektura**: Systemy muszą radzić sobie z zmiennym obciążeniem zapytań i wolumenem danych
- **Zrozumienie Kontekstu**: Utrzymanie kontekstu użytkownika w trakcie iteracji wyszukiwania jest kluczowe dla sensownych wyników
- **Dynamiczna Reformulacja Zapytania**: Adaptacyjne modyfikowanie zapytań na podstawie kontekstu i wcześniejszych wyników
- **Integracja Wielu Źródeł**: Łączenie wyników z wielu dostawców wyszukiwania i źródeł internetowych
- **Zrozumienie Semantyczne**: Przetwarzanie zapytań i treści na podstawie znaczenia, a nie tylko słów kluczowych
- **Ranking w Czasie Rzeczywistym**: Ciągłe dostosowywanie rankingów wyników, gdy pojawiają się nowe informacje

### Model Context Protocol a Wyszukiwanie w Internecie w Czasie Rzeczywistym

Model Context Protocol (MCP) adresuje kilka kluczowych wyzwań w środowiskach wyszukiwania internetowego w czasie rzeczywistym:

1. **Zachowanie Kontekstu Wyszukiwania**: MCP standaryzuje sposób utrzymania kontekstu pomiędzy rozproszonymi komponentami wyszukiwania, zapewniając, że modele AI i węzły przetwarzające mają dostęp do odpowiedniej historii zapytań i preferencji użytkownika.

2. **Efektywne Zarządzanie Zapytaniami**: Poprzez zapewnienie ustrukturyzowanych mechanizmów transmisji kontekstu, MCP zmniejsza narzut powtarzania kontekstu w każdej iteracji wyszukiwania.

3. **Interoperacyjność**: MCP tworzy wspólny język do dzielenia się kontekstem pomiędzy różnorodnymi technologiami wyszukiwania i modelami AI, umożliwiając bardziej elastyczne i rozszerzalne architektury.

4. **Kontekst Optymalizowany pod Wyszukiwanie**: Implementacje MCP mogą priorytetowo traktować elementy kontekstu, które są najbardziej istotne dla efektywnego wyszukiwania, optymalizując zarówno wydajność, jak i dokładność.

5. **Adaptacyjne Przetwarzanie Wyszukiwania**: Dzięki właściwemu zarządzaniu kontekstem przez MCP, systemy wyszukiwania mogą dynamicznie dostosowywać przetwarzanie na podstawie ewoluujących potrzeb użytkowników i krajobrazów informacyjnych.

W nowoczesnych aplikacjach, począwszy od agregacji wiadomości po asystentów badawczych, integracja MCP z technologiami wyszukiwania internetowego umożliwia inteligentniejsze, świadome kontekstu wyszukiwanie, które może dostarczać coraz bardziej trafne wyniki wraz z postępem interakcji użytkownika.

## Cele nauki

Po ukończeniu tej lekcji będziesz w stanie:

- Zrozumieć podstawy wyszukiwania internetowego w czasie rzeczywistym i jego wyzwania w nowoczesnych aplikacjach
- Wyjaśnić, jak Protokół Kontekstu Modelu (MCP) wzmacnia możliwości wyszukiwania w czasie rzeczywistym
- Implementować rozwiązania wyszukiwania oparte na MCP, wykorzystując popularne frameworki i API
- Projektować i wdrażać skalowalne, wysokowydajne architektury wyszukiwania z MCP
- Stosować koncepcje MCP w różnych przypadkach użycia, w tym wyszukiwanie semantyczne, asystę badawczą oraz przeglądanie wspomagane AI
- Ocenić nadchodzące trendy i przyszłe innowacje w technologiach wyszukiwania opartych na MCP
- Opracowywać systemy wyszukiwania świadome kontekstu, które uczą się na podstawie interakcji użytkownika
- Integrując możliwości wyszukiwania w sieci z asystentami AI za pomocą ustandaryzowanych protokołów MCP
- Tworzyć wieloetapowe potoki wyszukiwania, które stopniowo precyzują wyniki na podstawie kontekstu
- Optymalizować wydajność wyszukiwania przy zachowaniu pełnej świadomości kontekstu

### Definicja i Znaczenie

Wyszukiwanie internetowe w czasie rzeczywistym polega na ciągłym zadawaniu zapytań, pobieraniu i dostarczaniu informacji internetowych z minimalnymi opóźnieniami. W odróżnieniu od tradycyjnych wyszukiwarek, które okresowo indeksują internet, wyszukiwanie w czasie rzeczywistym stara się udostępniać informacje w miarę ich dostępności, umożliwiając natychmiastowy dostęp do najświeższych treści.

Kluczowe cechy wyszukiwania internetowego w czasie rzeczywistym obejmują:

- **Świeżość**: Priorytetowo traktowanie najnowszych treści i aktualizacji
- **Ciągłe Przetwarzanie**: Stałe monitorowanie nowych informacji
- **Adaptacja Zapytania**: Udoskonalanie zapytań wyszukiwania na podstawie kontekstu i informacji zwrotnych
- **Natychmiastowa Dostawa**: Zapewnianie wyników wyszukiwania z minimalnym opóźnieniem
- **Utrzymanie Kontekstu**: Budowanie na podstawie wcześniejszych zapytań dla poprawienia trafności

### Wyzwania w Tradycyjnym Wyszukiwaniu Internetowym

Tradycyjne podejścia do wyszukiwania w Internecie napotykają wiele ograniczeń, gdy stosowane są w scenariuszach czasu rzeczywistego:

1. **Fragmentacja Kontekstu**: Trudność w utrzymaniu kontekstu wyszukiwania w wielu zapytaniach
2. **Świeżość Informacji**: Problemy z dostępem i priorytetyzacją najnowszych informacji
3. **Złożoność Integracji**: Problemy z interoperacyjnością między systemami wyszukiwania a aplikacjami
4. **Problemy z Opóźnieniami**: Równoważenie kompleksowego wyszukiwania z wymaganiami czasów odpowiedzi
5. **Dostosowanie Trafności**: Zapewnienie dokładności i trafności przy priorytecie aktualności

## Zrozumienie Protokółu Kontekstu Modelu (MCP) dla Wyszukiwania

### Czym jest MCP w Kontekstach Wyszukiwania?

Model Context Protocol (MCP) to ustandaryzowany protokół komunikacyjny zaprojektowany do ułatwienia efektywnej interakcji między modelami AI a aplikacjami. W kontekście wyszukiwania w Internecie w czasie rzeczywistym, MCP zapewnia ramy do:

- Zachowania kontekstu wyszukiwania w całych sekwencjach zapytań
- Standaryzacji formatów zapytań i wyników wyszukiwania
- Optymalizacji transmisji parametrów wyszukiwania i wyników
- Ulepszenia komunikacji pomiędzy modelami a silnikami wyszukiwania

### Podstawowe Komponenty i Architektura

Architektura MCP dla wyszukiwania w Internecie w czasie rzeczywistym składa się z kilku kluczowych komponentów:

1. **Obsługi Kontekstu Zapytania**: Zarządzają i utrzymują kontekst wyszukiwania w wielu zapytaniach
2. **Procesory Wyszukiwania**: Przetwarzają nadchodzące zapytania wyszukiwania przy użyciu technik świadomych kontekstu
3. **Adaptery Protokółu**: Konwertują pomiędzy różnymi API wyszukiwania przy zachowaniu kontekstu
4. **Magazyn Kontekstu**: Efektywnie przechowują i pobierają historię wyszukiwań oraz preferencje
5. **Łączniki Wyszukiwania**: Łączą się z różnymi silnikami wyszukiwania i API internetowymi

```mermaid
graph TD
    subgraph "Źródła danych"
        Web[Zawartość sieci Web]
        APIs[Zewnętrzne API]
        DB[Bazy wiedzy]
        News[Kanały informacyjne]
    end

    subgraph "Warstwa wyszukiwania MCP"
        SC[Łączniki wyszukiwania]
        PA[Adaptery protokołów]
        CH[Obsługa kontekstu]
        SP[Procesory wyszukiwania]
        CS[Magazyn kontekstu]
    end

    subgraph "Przetwarzanie i analiza"
        RE[Silnik trafności]
        ML[Modele uczenia maszynowego]
        NLP[Przetwarzanie NLP]
        Rank[System rankingowy]
    end

    subgraph "Aplikacje i usługi"
        RA[Asystent badawczy]
        Alerts[Systemy alarmowe]
        KB[Baza wiedzy]
        API[Usługi API]
    end

    Web -->|Zawartość| SC
    APIs -->|Dane| SC
    DB -->|Wiedza| SC
    News -->|Aktualizacje| SC
    
    SC -->|Surowe wyniki| PA
    PA -->|Wyniki znormalizowane| CH
    CH <-->|Operacje na kontekście| CS
    CH -->|Wyniki wzbogacone kontekstem| SP
    SP -->|Wyniki przetworzone| RE
    SP -->|Cechy| ML
    SP -->|Tekst| NLP
    
    RE -->|Wyniki uszeregowane| Rank
    ML -->|Prognozy| Rank
    NLP -->|Encje i relacje| Rank
    
    Rank -->|Wyniki końcowe| RA
    ML -->|Wnioski| Alerts
    NLP -->|Dane ustrukturyzowane| KB
    
    RA -->|Badania| Users((Users))
    Alerts -->|Powiadomienia| Users
    KB <-->|Dostęp do wiedzy| API

    classDef sources fill:#f9f,stroke:#333,stroke-width:2px,color:#4a004a
    classDef mcp fill:#bbf,stroke:#333,stroke-width:2px,color:#00004a
    classDef processing fill:#bfb,stroke:#333,stroke-width:2px,color:#003300
    classDef apps fill:#fbb,stroke:#333,stroke-width:2px,color:#4a0000
    
    class Web,APIs,DB,News sources
    class SC,PA,CH,SP,CS mcp
    class RE,ML,NLP,Rank processing
    class RA,Alerts,KB,API apps
```

### Jak MCP Poprawia Wyszukiwanie w Internecie w Czasie Rzeczywistym

MCP odpowiada na wyzwania tradycyjnego wyszukiwania internetowego poprzez:

- **Ciągłość Kontekstową**: Utrzymywanie relacji między zapytaniami w całej sesji wyszukiwania
- **Optymalizację Transmisji**: Redukcję nadmiarowości parametrów wyszukiwania poprzez inteligentne zarządzanie kontekstem
- **Ustandaryzowane Interfejsy**: Zapewnianie spójnych API dla komponentów wyszukiwania
- **Zmniejszone Opóźnienia**: Minimalizację obciążenia przetwarzania dzięki efektywnemu zarządzaniu kontekstem
- **Zwiększoną Trafność**: Poprawę trafności wyników przez zachowanie intencji użytkownika między zapytaniami

## Integracja i Implementacja

Systemy wyszukiwania internetowego w czasie rzeczywistym wymagają starannego zaprojektowania architektury i implementacji, aby utrzymać zarówno wydajność, jak i integralność kontekstu. Protokół Kontekstu Modelu oferuje ustandaryzowane podejście do integracji modeli AI i technologii wyszukiwania, umożliwiając bardziej zaawansowane, świadome kontekstu potoki wyszukiwania.

### Przegląd Integracji MCP w Architekturach Wyszukiwania

Wdrażanie MCP w środowiskach wyszukiwania internetowego w czasie rzeczywistym wymaga uwzględnienia kilku kluczowych kwestii:

1. **Serializacja Kontekstu Wyszukiwania**: MCP zapewnia efektywne mechanizmy kodowania informacji kontekstowych w żądaniach wyszukiwania, gwarantując, że istotny kontekst podąża za zapytaniem przez cały proces przetwarzania. Obejmuje to ustandaryzowane formaty serializacji zoptymalizowane dla metadanych związanych z wyszukiwaniem.

2. **Stanowe Przetwarzanie Wyszukiwania**: MCP umożliwia inteligentniejsze, stanowe przetwarzanie dzięki utrzymaniu spójnej reprezentacji kontekstu w kolejnych iteracjach wyszukiwania. Jest to szczególnie cenne w wieloetapowych potokach wyszukiwania, gdzie udoskonalanie kontekstu polepsza wyniki.

3. **Rozszerzanie i Udoskonalanie Zapytania**: Implementacje MCP w systemach wyszukiwania mogą wspierać wyrafinowane rozszerzanie i doprecyzowywanie zapytań na podstawie zgromadzonego kontekstu, pozwalając na coraz bardziej trafne wyniki w miarę postępu sesji wyszukiwania.

4. **Buforowanie Wyników i Priorytetyzacja**: Poprzez standaryzację obsługi kontekstu, MCP pomaga zarządzać buforowaniem wyników i ich priorytetyzacją, umożliwiając komponentom adaptację do zmieniającego się kontekstu wyszukiwania.

5. **Federacja i Agregacja Wyszukiwania**: MCP ułatwia bardziej zaawansowaną federację wyszukiwania pomiędzy wieloma backendami, dostarczając ustrukturyzowane reprezentacje kontekstu wyszukiwania, co pozwala na bardziej znaczącą agregację wyników z różnorodnych źródeł.

Implementacja MCP w różnych technologiach wyszukiwania tworzy ujednolicone podejście do zarządzania kontekstem, zmniejszając potrzebę pisania niestandardowego kodu integracyjnego, jednocześnie zwiększając zdolność systemu do utrzymania znaczącego kontekstu w miarę ewolucji zapytań wyszukiwania.

### MCP w Różnych Implementacjach Wyszukiwania Internetowego

Te przykłady odpowiadają obecnej specyfikacji MCP, która koncentruje się na protokole opartym na JSON-RPC z różnymi mechanizmami transportu. Kod demonstruje, jak można implementować niestandardowe integracje wyszukiwania przy zachowaniu pełnej kompatybilności z protokołem MCP.


<details>
<summary>Implementacja w Pythonie z Uniwersalnym API Wyszukiwania</summary>

```python
import asyncio
import json
import aiohttp
from typing import Dict, Any, Optional, List
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

# Importuj standardowe biblioteki MCP
from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from mcp.types import TextContent, CreateMessageRequestParams, CreateMessageResult
from mcp.server.fastmcp import FastMCP

# Utwórz serwer FastMCP do wyszukiwania w sieci
search_server = FastMCP("WebSearch")

# Klasa do obsługi operacji wyszukiwania w sieci
class WebSearchHandler:
    def __init__(self, api_endpoint: str, api_key: str):
        self.api_endpoint = api_endpoint
        self.api_key = api_key
        self.session = None
        
    async def initialize(self):
        """Initialize the HTTP session"""
        self.session = aiohttp.ClientSession(
            headers={"Authorization": f"Bearer {self.api_key}"}
        )
    
    async def close(self):
        """Close the HTTP session"""
        if self.session:
            await self.session.close()
            
    async def perform_search(self, query: str, max_results: int = 5, 
                           include_domains: List[str] = None, 
                           exclude_domains: List[str] = None,
                           time_period: str = "any") -> Dict[str, Any]:
        """Perform web search using the search API"""
        # Utwórz parametry wyszukiwania
        search_params = {
            "q": query,
            "limit": max_results,
            "time": time_period
        }
        
        if include_domains:
            search_params["site"] = ",".join(include_domains)
            
        if exclude_domains:
            search_params["exclude_site"] = ",".join(exclude_domains)
        
        # Wykonaj zapytanie wyszukiwania
        try:
            async with self.session.get(
                self.api_endpoint,
                params=search_params
            ) as response:
                if response.status != 200:
                    error_text = await response.text()
                    raise Exception(f"Search API error: {response.status} - {error_text}")
                
                search_data = await response.json()
                
                # Przekształć specyficzną dla API odpowiedź na standardowy format
                results = []
                for item in search_data.get("results", []):
                    results.append({
                        "title": item.get("title", ""),
                        "url": item.get("url", ""),
                        "snippet": item.get("snippet", ""),
                        "date": item.get("published_date", ""),
                        "source": item.get("source", "")
                    })
                
                return {
                    "query": query,
                    "totalResults": len(results),
                    "results": results
                }
        except Exception as e:
            print(f"Search API request error: {e}")
            raise

# Zainicjuj obsługę wyszukiwania
search_handler = WebSearchHandler(
    api_endpoint="https://api.search-service.example/search",
    api_key="your-api-key-here"
)

# Skonfiguruj czas życia do zarządzania obsługą wyszukiwania
@asyncio.asynccontextmanager
async def app_lifespan(server: FastMCP):
    """Manage application lifecycle"""
    await search_handler.initialize()
    try:
        yield {"search_handler": search_handler}
    finally:
        await search_handler.close()

# Ustaw czas życia dla serwera
search_server = FastMCP("WebSearch", lifespan=app_lifespan)

# Zarejestruj narzędzie wyszukiwania w sieci
@search_server.tool()
async def web_search(query: str, max_results: int = 5, 
                   include_domains: List[str] = None,
                   exclude_domains: List[str] = None,
                   time_period: str = "any") -> Dict[str, Any]:
    """
    Search the web for information
    
    Args:
        query: The search query
        max_results: Maximum number of results to return (default: 5)
        include_domains: List of domains to include in search results
        exclude_domains: List of domains to exclude from search results
        time_period: Time period for results ("day", "week", "month", "any")
        
    Returns:
        Dictionary containing search results
    """
    ctx = search_server.get_context()
    search_handler = ctx.request_context.lifespan_context["search_handler"]
    
    results = await search_handler.perform_search(
        query=query,
        max_results=max_results,
        include_domains=include_domains,
        exclude_domains=exclude_domains,
        time_period=time_period
    )
    
    return results

# Przykład użycia klienta
async def client_example():
    # Połącz się z serwerem wyszukiwania używając Streamable HTTP transport
    async with streamablehttp_client("http://localhost:8000/mcp") as (read, write, _):
        async with ClientSession(read, write) as session:
            # Zainicjuj połączenie
            await session.initialize()
            
            # Wywołaj narzędzie web_search
            search_results = await session.call_tool(
                "web_search", 
                {
                    "query": "latest developments in AI and Model Context Protocol",
                    "max_results": 5,
                    "time_period": "day",
                    "include_domains": ["github.com", "microsoft.com"]
                }
            )
            
            print(f"Search results: {search_results}")

# Przykład uruchomienia serwera
if __name__ == "__main__":
    # Uruchom serwer z użyciem Streamable HTTP transportu
    search_server.run(transport="streamable-http")
```
</details> 

<details>
<summary>Implementacja w JavaScript z Wyszukiwaniem w Przeglądarce</summary>


```javascript
// Implementacja serwera MCP do wyszukiwania w sieci
import { McpServer, ResourceTemplate } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StreamableHTTPServerTransport } from '@modelcontextprotocol/sdk/server/streamableHttp.js';
import { z } from 'zod';

// Utwórz serwer MCP do wyszukiwania w sieci
const searchServer = new McpServer({
    name: "BrowserSearch",
    description: "A server that provides web search capabilities"
});

// Klasa usługi wyszukiwania
class SearchService {
    constructor(searchApiUrl, apiKey) {
        this.searchApiUrl = searchApiUrl;
        this.apiKey = apiKey;
    }

    async performSearch(parameters) {
        const {
            query = '',
            maxResults = 5,
            includeDomains = [],
            excludeDomains = [],
            timePeriod = 'any'
        } = parameters;
        
        // Zbuduj URL wyszukiwania z parametrami
        const url = new URL(this.searchApiUrl);
        url.searchParams.append('q', query);
        url.searchParams.append('limit', maxResults);
        url.searchParams.append('time', timePeriod);
        
        if (includeDomains.length > 0) {
            url.searchParams.append('site', includeDomains.join(','));
        }
        
        if (excludeDomains.length > 0) {
            url.searchParams.append('exclude_site', excludeDomains.join(','));
        }
        
        try {
            const response = await fetch(url.toString(), {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${this.apiKey}`,
                    'Content-Type': 'application/json'
                }
            });
            
            if (!response.ok) {
                const errorText = await response.text();
                throw new Error(`Search API error: ${response.status} - ${errorText}`);
            }
            
            const searchData = await response.json();
            
            // Przekształć odpowiedź specyficzną dla API do standardowego formatu
            const results = searchData.results?.map(item => ({
                title: item.title || '',
                url: item.url || '',
                snippet: item.snippet || '',
                date: item.published_date || '',
                source: item.source || ''
            })) || [];
            
            return {
                query,
                totalResults: results.length,
                results
            };
        } catch (error) {
            console.error('Search API request error:', error);
            throw error;
        }
    }
}

// Zainicjuj usługę wyszukiwania
const searchService = new SearchService(
    'https://api.search-service.example/search',
    'your-api-key-here'
);

// Skonfiguruj dostawcę kontekstu dla serwera
searchServer.setContextProvider(() => {
    return {
        searchService
    };
});

// Zarejestruj narzędzie do wyszukiwania w sieci
searchServer.tool({
    name: 'web_search',
    description: 'Search the web for information',
    parameters: {
        type: 'object',
        properties: {
            query: {
                type: 'string',
                description: 'The search query'
            },
            maxResults: {
                type: 'integer',
                description: 'Maximum number of results to return',
                default: 5
            },
            includeDomains: {
                type: 'array',
                items: { type: 'string' },
                description: 'List of domains to include in search results'
            },
            excludeDomains: {
                type: 'array',
                items: { type: 'string' },
                description: 'List of domains to exclude from search results'
            },
            timePeriod: {
                type: 'string',
                description: 'Time period for results',
                enum: ['day', 'week', 'month', 'any'],
                default: 'any'
            }
        },
        required: ['query']
    },
    handler: async (params, context) => {
        const { searchService } = context;
        return await searchService.performSearch(params);
    }
});

// Przykładowy kod klienta do połączenia z serwerem wyszukiwania
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';

async function connectToSearchServer() {
    // Połącz się z serwerem wyszukiwania
    const transport = new StreamableHTTPClientTransport(
        new URL('http://localhost:8000/mcp')
    );
    
    const client = new Client({
        name: 'search-client',
        version: '1.0.0'
    });
    
    await client.connect(transport);
    
    // Wykonaj narzędzie wyszukiwania
    const searchResults = await client.callTool({
        name: 'web_search',
        arguments: {
            query: 'Model Context Protocol implementation examples',
            maxResults: 10,
            timePeriod: 'week',
            includeDomains: ['github.com', 'docs.microsoft.com']
        }
    });
    
    console.log('Search results:', searchResults);
    
    // Sprzątanie
    await client.disconnect();
}

// Uruchom serwer
const transport = new StreamableHTTPServerTransport();
await searchServer.connect(transport);
console.log('Search server running at http://localhost:8000/mcp');

// W osobnym procesie lub po uruchomieniu serwera
// connectToSearchServer().catch(console.error);
```
</details> 




## Zastrzeżenie dotyczące przykładów kodu

> **Ważna Uwaga**: Poniższe przykłady kodu demonstrują integrację Protokółu Kontekstu Modelu (MCP) z funkcjonalnością wyszukiwania internetowego. Choć opierają się na wzorcach i strukturach oficjalnych SDK MCP, zostały uproszczone w celach edukacyjnych.
> 
> Przykłady te przedstawiają:
> 
> 1. **Implementacja w Pythonie**: Implementację serwera FastMCP, która udostępnia narzędzie do wyszukiwania internetowego i łączy się z zewnętrznym API wyszukiwarki. Przykład demonstruje właściwe zarządzanie cyklem życia, obsługę kontekstu i implementację narzędzia zgodnie ze wzorcami [oficjalnego MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk). Serwer korzysta z rekomendowanego transportu HTTP Streamable, który zastąpił starszy transport SSE dla wdrożeń produkcyjnych.
> 
> 2. **Implementacja w JavaScript**: Implementację TypeScript/JavaScript wykorzystującą wzorzec FastMCP z [oficjalnego MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) do stworzenia serwera wyszukiwania z właściwą definicją narzędzi i połączeniami klientów. Stosuje najnowsze zalecane wzorce zarządzania sesją i zachowaniem kontekstu.
> 
> Te przykłady wymagałyby dodania obsługi błędów, uwierzytelniania i specyficznego kodu integracji API dla zastosowań produkcyjnych. Pokazane punkty końcowe API wyszukiwania (`https://api.search-service.example/search`) to symbole zastępcze, które należy zastąpić rzeczywistymi punktami końcowymi usług wyszukiwania.
> 
> Dla pełnych szczegółów implementacji i najnowszych podejść, prosimy odnieść się do [oficjalnej specyfikacji MCP](https://spec.modelcontextprotocol.io/) oraz dokumentacji SDK.

## Podstawowe Koncepcje

### Ramy Protokółu Kontekstu Modelu (MCP)

Na swoim fundamencie Protokół Kontekstu Modelu zapewnia ustandaryzowany sposób wymiany kontekstu między modelami AI, aplikacjami i usługami. W wyszukiwaniu internetowym w czasie rzeczywistym ten framework jest niezbędny do tworzenia spójnych, wieloetapowych doświadczeń wyszukiwania. Kluczowe komponenty obejmują:

1. **Architektura Klient-Serwer**: MCP ustanawia wyraźny podział między klientami wyszukiwania (żądającymi) a serwerami wyszukiwania (dostawcami), umożliwiając elastyczne modele wdrożeń.

2. **Komunikacja JSON-RPC**: Protokół używa JSON-RPC do wymiany wiadomości, co czyni go kompatybilnym z technologiami webowymi i łatwym do implementacji na różnych platformach.

3. **Zarządzanie Kontekstem**: MCP definiuje ustrukturyzowane metody utrzymywania, aktualizacji i wykorzystywania kontekstu wyszukiwania na wielu interakcjach.

4. **Definicje Narzędzi**: Możliwości wyszukiwania są udostępniane jako ustandaryzowane narzędzia z jasno określonymi parametrami i wartościami zwrotnymi.

5. **Wsparcie dla Strumieniowania**: Protokół wspiera strumieniowanie wyników, co jest kluczowe dla wyszukiwania w czasie rzeczywistym, gdzie wyniki mogą pojawiać się etapami.

### Wzorce Integracji Wyszukiwania Internetowego

Podczas integracji MCP z wyszukiwaniem internetowym pojawia się kilka wzorców:

#### 1. Bezpośrednia Integracja z Dostawcą Wyszukiwania

```mermaid
graph LR
    Client[Klient MCP] --> |Żądanie MCP| Server[Serwer MCP]
    Server --> |Wywołanie API| SearchAPI[API wyszukiwania]
    SearchAPI --> |Wyniki| Server
    Server --> |Odpowiedź MCP| Client
```

W tym wzorcu serwer MCP bezpośrednio komunikuje się z jednym lub wieloma API wyszukiwania, tłumacząc żądania MCP na wywołania specyficzne dla API i formatując wyniki jako odpowiedzi MCP.

#### 2. Federacyjne Wyszukiwanie z Zachowaniem Kontekstu

```mermaid
graph LR
    Client[Klient MCP] --> |Żądanie MCP| Federation[Warstwa Federacji MCP]
    Federation --> |Żądanie MCP 1| Search1[Dostawca Wyszukiwania 1]
    Federation --> |Żądanie MCP 2| Search2[Dostawca Wyszukiwania 2]
    Federation --> |Żądanie MCP 3| Search3[Dostawca Wyszukiwania 3]
    Search1 --> |Odpowiedź MCP 1| Federation
    Search2 --> |Odpowiedź MCP 2| Federation
    Search3 --> |Odpowiedź MCP 3| Federation
    Federation --> |Zagregowana odpowiedź MCP| Client
```

Ten wzorzec rozdziela zapytania wyszukiwania pomiędzy wielu kompatybilnych z MCP dostawców, z których każdy potencjalnie specjalizuje się w różnych typach treści lub możliwościach wyszukiwania, przy utrzymaniu jednolitego kontekstu.

#### 3. Łańcuch Wyszukiwania z Wzbogaconym Kontekstem

```mermaid
graph LR
    Client[Klient MCP] --> |Zapytanie + Kontekst| Server[Serwer MCP]
    Server --> |1. Analiza zapytania| NLP[Usługa NLP]
    NLP --> |Ulepszone zapytanie| Server
    Server --> |2. Wykonanie wyszukiwania| Search[Silnik wyszukiwania]
    Search --> |Surowe wyniki| Server
    Server --> |3. Przetwarzanie wyników| Enhancement[Ulepszenie wyników]
    Enhancement --> |Ulepszone wyniki| Server
    Server --> |Wyniki końcowe + Zaktualizowany kontekst| Client
```

W tym wzorcu proces wyszukiwania dzieli się na wiele etapów, przy czym kontekst jest wzbogacany na każdym kroku, co skutkuje stopniowo bardziej trafnymi wynikami.

### Komponenty Kontekstu Wyszukiwania

W wyszukiwaniu internetowym opartym na MCP, kontekst zazwyczaj obejmuje:

- **Historię Zapytania**: Poprzednie zapytania w sesji
- **Preferencje Użytkownika**: Język, region, ustawienia bezpiecznego wyszukiwania
- **Historię Interakcji**: Które wyniki były klikane, czas spędzony na wynikach
- **Parametry Wyszukiwania**: Filtry, kolejności sortowania i inne modyfikatory wyszukiwania
- **Wiedzę Dziedzinową**: Kontekst specyficzny dla tematu istotny dla wyszukiwania
- **Kontekst Czasowy**: Czynniki związane z aktualnością
- **Preferencje Źródeł**: Zaufane lub preferowane źródła informacji

## Przypadki Użycia i Zastosowania

### Badania i Gromadzenie Informacji

MCP wzmacnia przepływy pracy badawczej poprzez:

- Zachowanie kontekstu badawczego pomiędzy sesjami wyszukiwania
- Umożliwienie bardziej wyrafinowanych i kontekstowo trafnych zapytań
- Wspieranie federacji wyszukiwania z wielu źródeł
- Ułatwianie ekstrakcji wiedzy z wyników wyszukiwania

### Monitorowanie Wiadomości i Trendów w Czasie Rzeczywistym

Wyszukiwanie wspierane przez MCP oferuje korzyści dla monitoringu wiadomości:

- Odkrywanie nowych historii prawie w czasie rzeczywistym
- Kontekstowe filtrowanie istotnych informacji
- Śledzenie tematów i podmiotów w różnych źródłach
- Spersonalizowane alerty wiadomości oparte na kontekście użytkownika

### Przeglądanie i Badania Wspomagane AI

MCP tworzy nowe możliwości dla przeglądania wspomaganego AI:

- Kontekstowe sugestie wyszukiwania na podstawie aktualnej aktywności w przeglądarce
- Płynna integracja wyszukiwania internetowego z asystentami opartymi na LLM
- Wieloetapowe doprecyzowywanie wyszukiwania z utrzymanym kontekstem
- Ulepszone weryfikowanie faktów i informacji

## Przyszłe Trendy i Innowacje

### Ewolucja MCP w Wyszukiwaniu Internetowym

Patrząc w przyszłość, oczekujemy, że MCP będzie ewoluować, aby sprostać:


- **Wyszukiwanie multimodalne**: Integracja wyszukiwania tekstu, obrazu, audio i wideo z zachowaniem kontekstu
- **Wyszukiwanie zdecentralizowane**: Wsparcie dla rozproszonych i federacyjnych ekosystemów wyszukiwania
- **Prywatność wyszukiwania**: Mechanizmy ochrony prywatności świadome kontekstu
- **Zrozumienie zapytania**: Głębokie semantyczne przetwarzanie naturalnych językowo zapytań wyszukiwawczych

### Potencjalne postępy technologiczne

Nowo powstające technologie, które ukształtują przyszłość wyszukiwania MCP:

1. **Architektury wyszukiwania neuronowego**: Systemy wyszukiwania oparte na osadzaniu zoptymalizowane dla MCP
2. **Spersonalizowany kontekst wyszukiwania**: Nauka indywidualnych wzorców wyszukiwania użytkownika w czasie
3. **Integracja grafów wiedzy**: Kontekstowe wyszukiwanie wzbogacone o domenowo specyficzne grafy wiedzy
4. **Kontext międzymodalny**: Utrzymywanie kontekstu pomiędzy różnymi modalnościami wyszukiwania

## Ćwiczenia praktyczne

### Ćwiczenie 1: Konfiguracja podstawowego potoku wyszukiwania MCP

W tym ćwiczeniu nauczysz się:
- Konfigurować podstawowe środowisko wyszukiwania MCP
- Implementować obsługę kontekstu dla wyszukiwania w sieci
- Testować i weryfikować zachowanie kontekstu w kolejnych iteracjach wyszukiwania

### Ćwiczenie 2: Budowanie asystenta badawczego z wykorzystaniem wyszukiwania MCP

Stwórz kompletną aplikację, która:
- Przetwarza pytania badawcze w języku naturalnym
- Wykonuje kontekstowo świadome wyszukiwania w sieci
- Syntezuje informacje z wielu źródeł
- Prezentuje uporządkowane wyniki badań

### Ćwiczenie 3: Implementacja federacji wyszukiwania wieloźródłowego z MCP

Zaawansowane ćwiczenie obejmujące:
- Kontekstowe kierowanie zapytań do wielu silników wyszukiwania
- Ranking i agregację wyników
- Kontekstową deduplikację wyników wyszukiwania
- Obsługę metadanych specyficznych dla źródeł

## Dodatkowe zasoby

- [Model Context Protocol Specification](https://spec.modelcontextprotocol.io/) - Oficjalna specyfikacja MCP i szczegółowa dokumentacja protokołu
- [Model Context Protocol Documentation](https://modelcontextprotocol.io/) - Szczegółowe samouczki i przewodniki wdrożeniowe
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Oficjalna implementacja protokołu MCP w Pythonie
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Oficjalna implementacja protokołu MCP w TypeScript
- [MCP Reference Servers](https://github.com/modelcontextprotocol/servers) - Referencyjne implementacje serwerów MCP
- [Bing Web Search API Documentation](https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/overview) - API wyszukiwarki sieci Microsoftu
- [Google Custom Search JSON API](https://developers.google.com/custom-search/v1/overview) - Programowalna wyszukiwarka Google
- [SerpAPI Documentation](https://serpapi.com/search-api) - API wyświetlania wyników wyszukiwania
- [Meilisearch Documentation](https://www.meilisearch.com/docs) - Open-source’owy silnik wyszukiwania
- [Elasticsearch Documentation](https://www.elastic.co/guide/index.html) - Rozproszony silnik wyszukiwania i analityki
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction) - Budowanie aplikacji z LLM

## Efekty uczenia się

Po ukończeniu tego modułu będziesz potrafił:

- Zrozumieć podstawy wyszukiwania w czasie rzeczywistym i jego wyzwania
- Wyjaśnić, jak Model Context Protocol (MCP) usprawnia możliwości wyszukiwania w czasie rzeczywistym
- Implementować rozwiązania wyszukiwania oparte na MCP używając popularnych frameworków i API
- Projektować i wdrażać skalowalne, wysokowydajne architektury wyszukiwawcze z MCP
- Zastosować koncepcje MCP w różnych przypadkach użycia, w tym wyszukiwaniu semantycznym, asystencji badawczej i wspomaganym przeglądaniu AI
- Ocenić nowe trendy i przyszłe innowacje w technologiach wyszukiwania opartych na MCP


### Zagadnienia dotyczące zaufania i bezpieczeństwa

Podczas implementowania rozwiązań wyszukiwania sieciowego opartych na MCP pamiętaj o następujących ważnych zasadach ze specyfikacji MCP:

1. **Zgoda i kontrola użytkownika**: Użytkownicy muszą wyraźnie wyrazić zgodę i rozumieć wszystkie operacje i dostęp do danych. Jest to szczególnie ważne w implementacjach wyszukiwania sieciowego, które mogą uzyskiwać dostęp do zewnętrznych źródeł danych.

2. **Prywatność danych**: Zapewnij odpowiednie traktowanie zapytań i wyników wyszukiwania, zwłaszcza gdy mogą zawierać wrażliwe informacje. Wdróż odpowiednie mechanizmy kontroli dostępu w celu ochrony danych użytkowników.

3. **Bezpieczeństwo narzędzi**: Wdroż właściwe mechanizmy autoryzacji i walidacji narzędzi wyszukiwawczych, ponieważ mogą one stanowić potencjalne ryzyko bezpieczeństwa poprzez wykonywanie dowolnego kodu. Opisy zachowania narzędzi należy uważać za niezweryfikowane, chyba że pochodzą z zaufanego serwera.

4. **Jasna dokumentacja**: Dostarcz jasną dokumentację możliwości, ograniczeń oraz kwestii bezpieczeństwa Twojej implementacji wyszukiwania opartej na MCP, zgodnie z wytycznymi specyfikacji MCP.

5. **Solidne przepływy zgody**: Buduj solidne mechanizmy uzyskiwania zgody i autoryzacji, które jasno wyjaśniają, co robi każde narzędzie przed zezwoleniem na jego użycie, szczególnie dla narzędzi korzystających z zewnętrznych zasobów sieciowych.

Pełne informacje na temat bezpieczeństwa i zagadnień zaufania w MCP znajdziesz w [oficjalnej dokumentacji](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

## Co dalej 

- [5.12 Uwierzytelnianie Entra ID dla serwerów Model Context Protocol](../mcp-security-entra/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->