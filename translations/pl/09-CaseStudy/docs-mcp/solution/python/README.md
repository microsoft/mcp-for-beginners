# Generator Planów Nauki z Chainlit i Microsoft Learn Docs MCP

## Wymagania wstępne

- Python 3.8 lub nowszy
- pip (menedżer pakietów Pythona)
- Dostęp do internetu, aby połączyć się z serwerem Microsoft Learn Docs MCP

## Instalacja

1. Sklonuj to repozytorium lub pobierz pliki projektu.
2. Zainstaluj wymagane zależności:

   ```bash
   pip install -r requirements.txt
   ```

## Użycie

### Scenariusz 1: Proste zapytanie do Docs MCP
Klient wiersza poleceń, który łączy się z serwerem Docs MCP, wysyła zapytanie i wyświetla wynik.

1. Uruchom skrypt:
   ```bash
   python scenario1.py
   ```
2. Wprowadź swoje pytanie dotyczące dokumentacji w wierszu poleceń.

### Scenariusz 2: Generator Planów Nauki (Aplikacja Webowa Chainlit)
Interfejs webowy (oparty na Chainlit), który pozwala użytkownikom generować spersonalizowany, tygodniowy plan nauki dla dowolnego tematu technicznego.

1. Uruchom aplikację Chainlit:
   ```bash
   chainlit run scenario2.py
   ```
2. Otwórz lokalny adres URL podany w terminalu (np. http://localhost:8000) w przeglądarce.
3. W oknie czatu wprowadź temat nauki oraz liczbę tygodni, przez które chcesz się uczyć (np. „Certyfikacja AI-900, 8 tygodni”).
4. Aplikacja odpowie tygodniowym planem nauki, zawierającym linki do odpowiedniej dokumentacji Microsoft Learn.

**Wymagane zmienne środowiskowe:**

Aby korzystać ze Scenariusza 2 (aplikacji webowej Chainlit z Azure OpenAI), musisz ustawić następujące zmienne środowiskowe w pliku `.env` w katalogu `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Uzupełnij te wartości szczegółami swojego zasobu Azure OpenAI przed uruchomieniem aplikacji.

> [!TIP]
> Możesz łatwo wdrożyć własne modele, korzystając z [Azure AI Foundry](https://ai.azure.com/).

### Scenariusz 3: Dokumentacja w Edytorze z MCP Server w VS Code

Zamiast przełączać się między kartami przeglądarki w poszukiwaniu dokumentacji, możesz przynieść Microsoft Learn Docs bezpośrednio do swojego edytora VS Code, korzystając z serwera MCP. Dzięki temu możesz:
- Wyszukiwać i przeglądać dokumentację w VS Code bez opuszczania środowiska programistycznego.
- Wstawiać linki do dokumentacji bezpośrednio do plików README lub materiałów kursowych.
- Korzystać z GitHub Copilot i MCP razem, aby uzyskać płynny, wspomagany przez AI przepływ pracy z dokumentacją.

**Przykładowe zastosowania:**
- Szybkie dodawanie linków referencyjnych do README podczas pisania dokumentacji kursu lub projektu.
- Generowanie kodu za pomocą Copilot i natychmiastowe znajdowanie oraz cytowanie odpowiednich dokumentów za pomocą MCP.
- Skupienie się na pracy w edytorze i zwiększenie produktywności.

> [!IMPORTANT]
> Upewnij się, że masz poprawną konfigurację [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) w swoim środowisku roboczym (lokalizacja: `.vscode/mcp.json`).

## Dlaczego Chainlit w Scenariuszu 2?

Chainlit to nowoczesny, otwartoźródłowy framework do budowy konwersacyjnych aplikacji webowych. Ułatwia tworzenie interfejsów czatowych, które łączą się z usługami backendowymi, takimi jak serwer Microsoft Learn Docs MCP. Ten projekt wykorzystuje Chainlit, aby zapewnić prosty, interaktywny sposób generowania spersonalizowanych planów nauki w czasie rzeczywistym. Dzięki Chainlit możesz szybko budować i wdrażać narzędzia czatowe, które zwiększają produktywność i wspierają naukę.

## Co robi ta aplikacja?

Aplikacja pozwala użytkownikom tworzyć spersonalizowany plan nauki, po prostu wprowadzając temat i czas trwania. Aplikacja analizuje dane wejściowe, wysyła zapytanie do serwera Microsoft Learn Docs MCP w poszukiwaniu odpowiednich treści i organizuje wyniki w uporządkowany, tygodniowy plan. Rekomendacje na każdy tydzień są wyświetlane w oknie czatu, co ułatwia ich śledzenie i realizację. Integracja zapewnia dostęp do najnowszych i najbardziej odpowiednich zasobów edukacyjnych.

## Przykładowe zapytania

Wypróbuj te zapytania w oknie czatu, aby zobaczyć, jak aplikacja odpowiada:

- `Certyfikacja AI-900, 8 tygodni`
- `Nauka Azure Functions, 4 tygodnie`
- `Azure DevOps, 6 tygodni`
- `Inżynieria danych na Azure, 10 tygodni`
- `Podstawy bezpieczeństwa Microsoft, 5 tygodni`
- `Power Platform, 7 tygodni`
- `Usługi Azure AI, 12 tygodni`
- `Architektura chmurowa, 9 tygodni`

Te przykłady pokazują elastyczność aplikacji w dostosowywaniu się do różnych celów edukacyjnych i ram czasowych.

## Źródła

- [Dokumentacja Chainlit](https://docs.chainlit.io/)
- [Dokumentacja MCP](https://github.com/MicrosoftDocs/mcp)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.