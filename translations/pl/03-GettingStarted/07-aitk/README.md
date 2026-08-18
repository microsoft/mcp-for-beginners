# Korzystanie z serwera z rozszerzenia AI Toolkit dla Visual Studio Code

Gdy tworzysz agenta AI, nie chodzi tylko o generowanie inteligentnych odpowiedzi; ważne jest także, aby agent miał możliwość podejmowania działań. Tutaj wchodzi w grę Model Context Protocol (MCP). MCP ułatwia agentom dostęp do zewnętrznych narzędzi i usług w spójny sposób. Można to porównać do podłączenia agenta do skrzynki narzędziowej, z której *faktycznie* może korzystać.

Załóżmy, że podłączysz agenta do serwera kalkulatora MCP. Nagle agent będzie mógł wykonywać operacje matematyczne, po prostu otrzymując polecenie „Ile to jest 47 razy 89?” — bez potrzeby kodowania logiki czy tworzenia niestandardowych API.

## Przegląd

Ta lekcja opisuje, jak podłączyć serwer kalkulator MCP do agenta za pomocą rozszerzenia [AI Toolkit](https://aka.ms/AIToolkit) w Visual Studio Code, umożliwiając agentowi wykonywanie operacji matematycznych takich jak dodawanie, odejmowanie, mnożenie i dzielenie za pomocą języka naturalnego.

AI Toolkit to potężne rozszerzenie dla Visual Studio Code, które upraszcza tworzenie agentów. Inżynierowie AI mogą łatwo budować aplikacje AI poprzez opracowywanie i testowanie modeli generatywnej AI — lokalnie lub w chmurze. Rozszerzenie obsługuje większość głównych dostępnych modeli generatywnych.

*Uwaga*: AI Toolkit obecnie obsługuje Pythona i TypeScript.

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił:

- Korzystać z serwera MCP za pomocą AI Toolkit.
- Skonfigurować konfigurację agenta tak, aby mógł odkrywać i wykorzystywać narzędzia dostarczane przez serwer MCP.
- Wykorzystywać narzędzia MCP za pomocą języka naturalnego.

## Podejście

Oto jak powinniśmy podejść do tego na wysokim poziomie:

- Utwórz agenta i zdefiniuj jego systemowy prompt.
- Utwórz serwer MCP z narzędziami kalkulatora.
- Połącz Agent Builder z serwerem MCP.
- Przetestuj wywołanie narzędzi agenta za pomocą języka naturalnego.

Świetnie, teraz gdy rozumiemy przepływ, skonfigurujmy agenta AI do korzystania z zewnętrznych narzędzi przez MCP, aby zwiększyć jego możliwości!

## Wymagania wstępne

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit for Visual Studio Code](https://aka.ms/AIToolkit)

## Ćwiczenie: Korzystanie z serwera

> [!WARNING]
> Uwaga dla użytkowników macOS. Obecnie badamy problem dotyczący instalacji zależności na macOS. W rezultacie użytkownicy macOS nie będą mogli ukończyć tego samouczka w tym momencie. Zaktualizujemy instrukcje, gdy tylko dostępna będzie poprawka. Dziękujemy za cierpliwość i zrozumienie!

W tym ćwiczeniu zbudujesz, uruchomisz i ulepszysz agenta AI korzystając z narzędzi z serwera MCP w Visual Studio Code za pomocą AI Toolkit.

### -0- Krok wstępny, dodaj model OpenAI GPT-4o do Moich modeli

Ćwiczenie wykorzystuje model **GPT-4o**. Model powinien być dodany do **Moich modeli** przed utworzeniem agenta.

![Zrzut ekranu interfejsu wyboru modelu w rozszerzeniu AI Toolkit dla Visual Studio Code. Nagłówek brzmi "Znajdź odpowiedni model dla swojego rozwiązania AI" z podtytułem zachęcającym użytkowników do odkrywania, testowania i wdrażania modeli AI. Poniżej, w sekcji „Popularne modele”, wyświetlonych jest sześć kart modeli: DeepSeek-R1 (hostowany przez GitHub), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - mały, szybki) i DeepSeek-R1 (hostowany przez Ollama). Każda karta zawiera opcje „Dodaj” model lub „Wypróbuj na placu zabaw](../../../../translated_images/pl/aitk-model-catalog.2acd38953bb9c119.webp)

1. Otwórz rozszerzenie **AI Toolkit** z **Activity Bar**.
1. W sekcji **Catalog** wybierz **Models**, aby otworzyć **Model Catalog**. Wybranie **Models** otworzy **Model Catalog** na nowej karcie edytora.
1. W pasku wyszukiwania **Model Catalog** wpisz **OpenAI GPT-4o**.
1. Kliknij **+ Add**, aby dodać model do swojej listy **Moje modele**. Upewnij się, że wybrałeś model, który jest **hostowany przez GitHub**.
1. Na **Activity Bar** upewnij się, że model **OpenAI GPT-4o** pojawia się na liście.

### -1- Utwórz agenta

**Agent (Prompt) Builder** umożliwia tworzenie i dostosowywanie własnych agentów zasilanych AI. W tej sekcji utworzysz nowego agenta i przydzielisz model do prowadzenia rozmowy.

![Zrzut ekranu interfejsu "Calculator Agent" w rozszerzeniu AI Toolkit dla Visual Studio Code. W lewym panelu wybrany model to "OpenAI GPT-4o (via GitHub)." Systemowy prompt brzmi "Jesteś profesorem na uniwersytecie uczącym matematyki," a prompt użytkownika to "Wyjaśnij mi równanie Fouriera prostymi słowami." Dodatkowe opcje obejmują przyciski do dodawania narzędzi, włączania serwera MCP i wyboru strukturalnego wyjścia. Na dole znajduje się niebieski przycisk „Uruchom”. Po prawej stronie, w sekcji „Get Started with Examples”, wymienione są trzy przykładowe agenty: Web Developer (z MCP Server, Second-Grade Simplifier i Dream Interpreter, każdy z krótkim opisem funkcji).](../../../../translated_images/pl/aitk-agent-builder.901e3a2960c3e477.webp)

1. Otwórz rozszerzenie **AI Toolkit** z **Activity Bar**.
1. W sekcji **Tools** wybierz **Agent (Prompt) Builder**. Wybranie **Agent (Prompt) Builder** otworzy **Agent (Prompt) Builder** na nowej karcie edytora.
1. Kliknij przycisk **+ New Agent**. Rozszerzenie uruchomi kreator konfiguracji przez **Command Palette**.
1. Wprowadź nazwę **Calculator Agent** i naciśnij **Enter**.
1. W **Agent (Prompt) Builder**, w polu **Model** wybierz model **OpenAI GPT-4o (via GitHub)**.

### -2- Utwórz systemowy prompt dla agenta

Po utworzeniu szkicu agenta czas zdefiniować jego osobowość i cel. W tej sekcji skorzystasz z funkcji **Generate system prompt**, aby opisać zamierzone zachowanie agenta — w tym przypadku agenta kalkulatora — i pozwolić modelowi napisać dla Ciebie systemowy prompt.

![Zrzut ekranu interfejsu "Calculator Agent" w AI Toolkit dla Visual Studio Code z otwartym modalnym oknem zatytułowanym "Generate a prompt." Modal wyjaśnia, że szablon prompt można wygenerować, podając podstawowe szczegóły i zawiera pole tekstowe z przykładowym systemowym promptem: "Jesteś pomocnym i efektywnym asystentem matematycznym. Gdy otrzymasz zadanie obejmujące podstawową arytmetykę, odpowiadasz poprawnym wynikiem." Poniżej pola znajdują się przyciski „Zamknij” i „Generuj”. W tle widoczna jest część konfiguracji agenta, w tym wybrany model "OpenAI GPT-4o (via GitHub)" oraz pola systemowego i użytkownika promptu.](../../../../translated_images/pl/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. W sekcji **Prompts** kliknij przycisk **Generate system prompt**. Przycisk ten otworzy kreator promptów, który wykorzystuje AI do wygenerowania promptu systemowego dla agenta.
1. W oknie **Generate a prompt** wpisz następujące zdanie: `Jesteś pomocnym i efektywnym asystentem matematycznym. Gdy otrzymasz zadanie obejmujące podstawową arytmetykę, odpowiadasz poprawnym wynikiem.`
1. Kliknij przycisk **Generate**. W prawym dolnym rogu pojawi się powiadomienie potwierdzające generowanie promptu systemowego. Po zakończeniu generowania prompt pojawi się w polu **System prompt** w **Agent (Prompt) Builder**.
1. Przejrzyj **System prompt** i w razie potrzeby go zmodyfikuj.

### -3- Utwórz serwer MCP

Teraz, gdy zdefiniowałeś systemowy prompt agenta — który kieruje jego zachowaniem i odpowiedziami — czas wyposażyć agenta w praktyczne możliwości. W tej sekcji utworzysz serwer MCP kalkulatora z narzędziami do wykonywania dodawania, odejmowania, mnożenia i dzielenia. Ten serwer umożliwi agentowi wykonywanie operacji matematycznych w czasie rzeczywistym w odpowiedzi na naturalne zapytania.

![Zrzut ekranu dolnej części interfejsu Calculator Agent w rozszerzeniu AI Toolkit dla Visual Studio Code. Pokazuje rozwijane menu „Tools” i „Structure output” oraz menu rozwijane oznaczone „Choose output format” ustawione na „text”. Po prawej stronie jest przycisk „+ MCP Server” do dodania serwera Model Context Protocol. Nad sekcją Tools widoczny jest symbol zastępczy ikony obrazu.](../../../../translated_images/pl/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit jest wyposażony w szablony ułatwiające tworzenie własnego serwera MCP. Skorzystamy z szablonu Pythona do utworzenia serwera kalkulatora MCP.

*Uwaga*: AI Toolkit obecnie obsługuje Pythona i TypeScript.

1. W sekcji **Tools** w **Agent (Prompt) Builder** kliknij przycisk **+ MCP Server**. Rozszerzenie uruchomi kreatora konfiguracji przez **Command Palette**.
1. Wybierz **+ Add Server**.
1. Wybierz **Create a New MCP Server**.
1. Wybierz szablon **python-weather**.
1. Wybierz **Default folder** do zapisania szablonu serwera MCP.
1. Wpisz następującą nazwę serwera: **Calculator**
1. Otworzy się nowe okno Visual Studio Code. Wybierz **Yes, I trust the authors**.
1. Korzystając z terminala (**Terminal** > **New Terminal**), utwórz środowisko wirtualne: `python -m venv .venv`
1. Aktywuj środowisko wirtualne w terminalu:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. W terminalu zainstaluj zależności: `pip install -e .[dev]`
1. W widoku **Explorer** w **Activity Bar**, rozwiń katalog **src** i otwórz plik **server.py** w edytorze.
1. Zamień kod w pliku **server.py** na poniższy i zapisz:

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

### -4- Uruchom agenta z serwerem kalkulatora MCP

Teraz, gdy Twój agent ma narzędzia, czas z nich skorzystać! W tej sekcji wyślesz zapytania do agenta, aby przetestować i zweryfikować, czy agent wykorzystuje odpowiednie narzędzia z serwera kalkulatora MCP.

![Zrzut ekranu interfejsu Calculator Agent w rozszerzeniu AI Toolkit dla Visual Studio Code. W lewym panelu, w sekcji „Tools”, dodany jest serwer MCP o nazwie local-server-calculator_server, pokazujący cztery dostępne narzędzia: add, subtract, multiply i divide. Oznaczenie pokazuje, że cztery narzędzia są aktywne. Poniżej znajduje się zwinięta sekcja „Structure output” oraz niebieski przycisk „Run”. W prawym panelu, w sekcji „Model Response”, agent wywołuje narzędzia multiply i subtract z wejściami {"a": 3, "b": 25} i {"a": 75, "b": 20} odpowiednio. Końcowa „Odpowiedź narzędzia” pokazana jest jako 75.0. U dołu pojawia się przycisk „View Code”.](../../../../translated_images/pl/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

Będziesz uruchamiać serwer kalkulatora MCP na swoim lokalnym komputerze deweloperskim za pomocą **Agent Builder** jako klienta MCP.

1. Naciśnij `F5`, aby rozpocząć debugowanie serwera MCP. **Agent (Prompt) Builder** otworzy się na nowej karcie edytora. Status serwera będzie widoczny w terminalu.
1. W polu **User prompt** w **Agent (Prompt) Builder** wpisz następujące zapytanie: `Kupiłem 3 produkty po 25 dolarów każdy, a następnie skorzystałem z rabatu 20 dolarów. Ile zapłaciłem?`
1. Kliknij przycisk **Run**, aby wygenerować odpowiedź agenta.
1. Przejrzyj wyjście agenta. Model powinien dojść do wniosku, że zapłaciłeś **55 dolarów**.
1. Oto, co powinno się wydarzyć:
    - Agent wybierze narzędzia **multiply** i **subtract**, aby pomóc w obliczeniach.
    - Odpowiednie wartości `a` i `b` zostaną przypisane dla narzędzia **multiply**.
    - Odpowiednie wartości `a` i `b` zostaną przypisane dla narzędzia **subtract**.
    - Odpowiedź z każdego narzędzia zostanie podana w odpowiedniej sekcji **Tool Response**.
    - Końcowy wynik modelu zostanie podany w końcowej sekcji **Model Response**.
1. Wyślij dodatkowe zapytania, aby dalej testować agenta. Możesz edytować istniejące zapytanie w polu **User prompt** klikając w pole i zamieniając obecne zapytanie.
1. Po zakończeniu testowania agenta możesz zatrzymać serwer przez terminal, wpisując **CTRL/CMD+C** aby zakończyć.

## Zadanie

Spróbuj dodać dodatkową funkcję do pliku **server.py** (np. zwraca pierwiastek kwadratowy z liczby). Przetestuj dodatkowe zapytania, które wymagałyby od agenta użycia nowego narzędzia (lub istniejących). Pamiętaj, aby zrestartować serwer, aby załadować nowo dodane narzędzia.

## Rozwiązanie

[Rozwiązanie](./solution/README.md)

## Najważniejsze wnioski

Najważniejsze wnioski z tego rozdziału to:

- Rozszerzenie AI Toolkit to świetny klient umożliwiający korzystanie z serwerów MCP i ich narzędzi.
- Możesz dodawać nowe narzędzia do serwerów MCP, rozszerzając możliwości agenta, aby sprostać zmieniającym się wymaganiom.
- AI Toolkit zawiera szablony (np. szablony serwerów MCP w Pythonie) upraszczające tworzenie niestandardowych narzędzi.

## Dodatkowe zasoby

- [Dokumentacja AI Toolkit](https://aka.ms/AIToolkit/doc)

## Co dalej
- Dalej: [Testowanie i debugowanie](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->