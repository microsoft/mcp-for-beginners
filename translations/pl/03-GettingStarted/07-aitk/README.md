<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6fb74f952ab79ed4b4a33fda5fa04ecb",
  "translation_date": "2025-07-31T01:19:16+00:00",
  "source_file": "03-GettingStarted/07-aitk/README.md",
  "language_code": "pl"
}
-->
# Korzystanie z serwera z rozszerzenia AI Toolkit dla Visual Studio Code

Podczas tworzenia agenta AI nie chodzi tylko o generowanie inteligentnych odpowiedzi, ale także o umożliwienie agentowi podejmowania działań. Właśnie tutaj wkracza Model Context Protocol (MCP). MCP ułatwia agentom dostęp do zewnętrznych narzędzi i usług w spójny sposób. Można to porównać do podłączenia agenta do skrzynki narzędziowej, z której faktycznie może korzystać.

Załóżmy, że podłączasz agenta do serwera MCP kalkulatora. Nagle Twój agent może wykonywać operacje matematyczne, otrzymując jedynie polecenie, takie jak „Ile to 47 razy 89?”—bez potrzeby twardego kodowania logiki czy budowania niestandardowych API.

## Przegląd

Ta lekcja pokazuje, jak połączyć serwer MCP kalkulatora z agentem za pomocą rozszerzenia [AI Toolkit](https://aka.ms/AIToolkit) w Visual Studio Code, umożliwiając agentowi wykonywanie operacji matematycznych, takich jak dodawanie, odejmowanie, mnożenie i dzielenie za pomocą języka naturalnego.

AI Toolkit to potężne rozszerzenie dla Visual Studio Code, które upraszcza rozwój agentów. Inżynierowie AI mogą łatwo tworzyć aplikacje AI, rozwijając i testując modele generatywne—lokalnie lub w chmurze. Rozszerzenie obsługuje większość dostępnych obecnie głównych modeli generatywnych.

*Uwaga*: AI Toolkit obecnie obsługuje Python i TypeScript.

## Cele nauki

Po ukończeniu tej lekcji będziesz w stanie:

- Korzystać z serwera MCP za pomocą AI Toolkit.
- Skonfigurować konfigurację agenta, aby umożliwić mu odkrywanie i korzystanie z narzędzi dostarczanych przez serwer MCP.
- Korzystać z narzędzi MCP za pomocą języka naturalnego.

## Podejście

Oto ogólny plan działania:

- Utwórz agenta i zdefiniuj jego systemowy prompt.
- Utwórz serwer MCP z narzędziami kalkulatora.
- Połącz Agent Builder z serwerem MCP.
- Przetestuj wywoływanie narzędzi agenta za pomocą języka naturalnego.

Świetnie, teraz gdy rozumiemy przepływ, skonfigurujmy agenta AI, aby korzystał z zewnętrznych narzędzi za pomocą MCP, zwiększając jego możliwości!

## Wymagania wstępne

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit dla Visual Studio Code](https://aka.ms/AIToolkit)

## Ćwiczenie: Korzystanie z serwera

> [!WARNING]
> Uwaga dla użytkowników macOS. Obecnie badamy problem dotyczący instalacji zależności na macOS. W rezultacie użytkownicy macOS nie będą w stanie ukończyć tego samouczka w tym momencie. Zaktualizujemy instrukcje, gdy tylko dostępne będzie rozwiązanie. Dziękujemy za cierpliwość i zrozumienie!

W tym ćwiczeniu zbudujesz, uruchomisz i ulepszysz agenta AI za pomocą narzędzi z serwera MCP w Visual Studio Code, korzystając z AI Toolkit.

### -0- Wstępny krok: dodaj model OpenAI GPT-4o do Moich Modeli

Ćwiczenie wykorzystuje model **GPT-4o**. Model powinien zostać dodany do **Moich Modeli** przed utworzeniem agenta.

1. Otwórz rozszerzenie **AI Toolkit** z **Paska Aktywności**.
1. W sekcji **Katalog** wybierz **Modele**, aby otworzyć **Katalog Modeli**. Wybranie **Modele** otwiera **Katalog Modeli** w nowej zakładce edytora.
1. W polu wyszukiwania **Katalogu Modeli** wpisz **OpenAI GPT-4o**.
1. Kliknij **+ Dodaj**, aby dodać model do listy **Moich Modeli**. Upewnij się, że wybrałeś model **Hostowany przez GitHub**.
1. W **Pasku Aktywności** potwierdź, że model **OpenAI GPT-4o** pojawia się na liście.

### -1- Utwórz agenta

**Agent (Prompt) Builder** umożliwia tworzenie i dostosowywanie własnych agentów AI. W tej sekcji utworzysz nowego agenta i przypiszesz model do obsługi rozmowy.

1. Otwórz rozszerzenie **AI Toolkit** z **Paska Aktywności**.
1. W sekcji **Narzędzia** wybierz **Agent (Prompt) Builder**. Wybranie **Agent (Prompt) Builder** otwiera **Agent (Prompt) Builder** w nowej zakładce edytora.
1. Kliknij przycisk **+ Nowy Agent**. Rozszerzenie uruchomi kreator konfiguracji za pomocą **Command Palette**.
1. Wpisz nazwę **Calculator Agent** i naciśnij **Enter**.
1. W **Agent (Prompt) Builder**, w polu **Model**, wybierz model **OpenAI GPT-4o (via GitHub)**.

### -2- Utwórz systemowy prompt dla agenta

Po utworzeniu szkieletu agenta czas zdefiniować jego osobowość i cel. W tej sekcji użyjesz funkcji **Generate system prompt**, aby opisać zamierzone zachowanie agenta—w tym przypadku agenta kalkulatora—i pozwolisz modelowi napisać systemowy prompt za Ciebie.

1. W sekcji **Prompts** kliknij przycisk **Generate system prompt**. Ten przycisk otwiera kreator promptów, który wykorzystuje AI do wygenerowania systemowego promptu dla agenta.
1. W oknie **Generate a prompt** wpisz następujące: `Jesteś pomocnym i efektywnym asystentem matematycznym. Gdy otrzymujesz zadanie związane z podstawową arytmetyką, odpowiadasz poprawnym wynikiem.`
1. Kliknij przycisk **Generate**. Powiadomienie pojawi się w prawym dolnym rogu, potwierdzając, że systemowy prompt jest generowany. Po zakończeniu generowania promptu, prompt pojawi się w polu **System prompt** w **Agent (Prompt) Builder**.
1. Przejrzyj **System prompt** i w razie potrzeby zmodyfikuj.

### -3- Utwórz serwer MCP

Teraz, gdy zdefiniowałeś systemowy prompt swojego agenta—określając jego zachowanie i odpowiedzi—czas wyposażyć agenta w praktyczne możliwości. W tej sekcji utworzysz serwer MCP kalkulatora z narzędziami do wykonywania obliczeń dodawania, odejmowania, mnożenia i dzielenia. Ten serwer umożliwi Twojemu agentowi wykonywanie operacji matematycznych w czasie rzeczywistym w odpowiedzi na polecenia w języku naturalnym.

AI Toolkit jest wyposażony w szablony, które ułatwiają tworzenie własnych serwerów MCP. Użyjemy szablonu Python do stworzenia serwera MCP kalkulatora.

*Uwaga*: AI Toolkit obecnie obsługuje Python i TypeScript.

1. W sekcji **Narzędzia** w **Agent (Prompt) Builder** kliknij przycisk **+ MCP Server**. Rozszerzenie uruchomi kreator konfiguracji za pomocą **Command Palette**.
1. Wybierz **+ Dodaj Serwer**.
1. Wybierz **Utwórz Nowy Serwer MCP**.
1. Wybierz **python-weather** jako szablon.
1. Wybierz **Domyślny folder**, aby zapisać szablon serwera MCP.
1. Wpisz następującą nazwę dla serwera: **Calculator**
1. Nowe okno Visual Studio Code otworzy się. Wybierz **Tak, ufam autorom**.
1. Korzystając z terminala (**Terminal** > **Nowy Terminal**), utwórz wirtualne środowisko: `python -m venv .venv`
1. Korzystając z terminala, aktywuj wirtualne środowisko:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source venv/bin/activate`
1. Korzystając z terminala, zainstaluj zależności: `pip install -e .[dev]`
1. W widoku **Explorer** w **Pasku Aktywności** rozwiń katalog **src** i wybierz **server.py**, aby otworzyć plik w edytorze.
1. Zastąp kod w pliku **server.py** następującym i zapisz:

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

### -4- Uruchom agenta z serwerem MCP kalkulatora

Teraz, gdy Twój agent ma narzędzia, czas je wykorzystać! W tej sekcji prześlesz polecenia do agenta, aby przetestować i zweryfikować, czy agent korzysta z odpowiedniego narzędzia z serwera MCP kalkulatora.

1. Naciśnij `F5`, aby rozpocząć debugowanie serwera MCP. **Agent (Prompt) Builder** otworzy się w nowej zakładce edytora. Status serwera jest widoczny w terminalu.
1. W polu **User prompt** w **Agent (Prompt) Builder** wpisz następujące polecenie: `Kupiłem 3 przedmioty po 25 dolarów każdy, a następnie użyłem rabatu 20 dolarów. Ile zapłaciłem?`
1. Kliknij przycisk **Run**, aby wygenerować odpowiedź agenta.
1. Przejrzyj wynik agenta. Model powinien stwierdzić, że zapłaciłeś **55 dolarów**.
1. Oto, co powinno się wydarzyć:
    - Agent wybiera narzędzia **multiply** i **subtract**, aby pomóc w obliczeniach.
    - Odpowiednie wartości `a` i `b` są przypisane do narzędzia **multiply**.
    - Odpowiednie wartości `a` i `b` są przypisane do narzędzia **subtract**.
    - Odpowiedź z każdego narzędzia jest dostarczana w odpowiednim **Tool Response**.
    - Ostateczny wynik modelu jest dostarczany w **Model Response**.
1. Prześlij dodatkowe polecenia, aby dalej testować agenta. Możesz zmodyfikować istniejące polecenie w polu **User prompt**, klikając w pole i zastępując istniejące polecenie.
1. Po zakończeniu testowania agenta możesz zatrzymać serwer za pomocą **terminala**, wpisując **CTRL/CMD+C**, aby zakończyć.

## Zadanie

Spróbuj dodać dodatkowe narzędzie do swojego pliku **server.py** (np. zwracanie pierwiastka kwadratowego liczby). Prześlij dodatkowe polecenia, które wymagałyby od agenta skorzystania z nowego narzędzia (lub istniejących narzędzi). Pamiętaj, aby ponownie uruchomić serwer, aby załadować nowo dodane narzędzia.

## Rozwiązanie

[Rozwiązanie](./solution/README.md)

## Kluczowe wnioski

Najważniejsze wnioski z tego rozdziału to:

- Rozszerzenie AI Toolkit to świetny klient, który pozwala korzystać z serwerów MCP i ich narzędzi.
- Możesz dodawać nowe narzędzia do serwerów MCP, rozszerzając możliwości agenta, aby sprostać zmieniającym się wymaganiom.
- AI Toolkit zawiera szablony (np. szablony serwerów MCP w Pythonie), które upraszczają tworzenie niestandardowych narzędzi.

## Dodatkowe zasoby

- [Dokumentacja AI Toolkit](https://aka.ms/AIToolkit/doc)

## Co dalej
- Następny rozdział: [Testowanie i debugowanie](../08-testing/README.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby zapewnić poprawność tłumaczenia, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.