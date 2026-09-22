# Korzenie MCP (funkcja legacy)

> [!WARNING]
> Korzenie zostały przestarzałe od wersji MCP `2026-07-28`. Pozostają w tej wersji dla
> kompatybilności i mogą zostać usunięte w pierwszej rewizji specyfikacji
> wydanej po 28 lipca 2027. Nowe implementacje powinny przekazywać
> katalogi lub pliki przez parametry narzędzi, URI zasobów lub konfigurację
> serwera.

## Przegląd

Korzenie pozwalają klientowi MCP poinformować serwer, które lokalizacje w systemie plików są istotne
dla bieżącego żądania. Korzeń zawiera wymagany URI `file://` oraz opcjonalną
nazwę czytelną dla człowieka.

Korzenie są wskazówkami informacyjnymi. Nie są kontenerami historii konwersacji,
sesjami protokołu ani mechanizmem kontroli dostępu. Protokół nie
wymusza, aby serwer pozostawał w obrębie wymienionych korzeni.

## Cele nauki

Po zakończeniu tej lekcji będziesz w stanie:

- Wyjaśnić, co reprezentują korzenie MCP, a czego nie reprezentują.
- Rozpoznać bieżący przebieg wielorundowy `roots/list`.
- Samodzielnie stosować kontrole bezpieczeństwa niezależnie od korzeni.
- Migrować nowe implementacje na wspierane alternatywy.

## Dane korzenia

Klient zwraca każdy korzeń jako URI `file://` z opcjonalną nazwą wyświetlaną:

```json
{
  "roots": [
    {
      "uri": "file:///home/user/projects/weather-service",
      "name": "Weather Service"
    }
  ]
}
```

Klienci powinni udostępniać tylko lokalizacje zatwierdzone przez użytkownika. Serwery powinny traktować
wynik jako wskazówkę dotyczącą istotnych plików, a nie dowód autoryzacji.

## Przebieg MCP 2026-07-28

Klient, który obsługuje korzenie, deklaruje tę zdolność w każdym żądaniu:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Podczas przetwarzania żądania klienta serwer może zwrócić
`InputRequiredResult` zawierający żądanie wejściowe `roots/list`:

```json
{
  "resultType": "input_required",
  "inputRequests": {
    "workspaceRoots": {
      "method": "roots/list"
    }
  },
  "requestState": "opaque-state-from-server"
}
```

Klient zbiera zatwierdzone korzenie i ponawia oryginalne żądanie z
dopasowanymi `inputResponses` i niezmienionym `requestState`. Ten wzór wielorundowy
utrzymuje protokół bezstanowym; nie ma negocjacji `initialize` ani
sesji na poziomie protokołu.

## Zachowanie Legacy 2025-11-25

W MCP `2025-11-25` klienci deklarowali korzenie podczas inicjalizacji. Serwer
mógł wydać bezpośrednie żądanie `roots/list`, a klient mógł wysłać
`notifications/roots/list_changed` gdy jego korzenie ulegały zmianie.

Ten cykl życia jest zachowaniem legacy. Nie łącz przykładów inicjalizacji lub
powiadomień z implementacją z `2026-07-28`.

## Zalecane zamienniki

### Parametry narzędzia

Uczyń wymagany katalog lub plik explicite w schemacie narzędzia:

```json
{
  "name": "analyze_project",
  "inputSchema": {
    "type": "object",
    "properties": {
      "projectDirectory": {
        "type": "string",
        "description": "Approved project directory to analyze"
      }
    },
    "required": ["projectDirectory"]
  }
}
```

### URI zasobów

Używaj zasobów MCP, gdy serwer może udostępnić odpowiednie pliki przez stabilne
URI. To utrzymuje odkrywanie i pobieranie explicite.

### Konfiguracja serwera

W przypadku stałych wdrożeń skonfiguruj dozwolone katalogi przy starcie serwera.
Często jest to jaśniejsze niż odkrywanie ich w trakcie wywołania narzędzia.

## Wymagania bezpieczeństwa

Bez względu na wybraną zamianę:

- Uzyskaj zgodę użytkownika przed udostępnianiem lokalizacji systemu plików.
- Kanonizuj i waliduj ścieżki, aby zapobiec przejściom poza dozwolone obszary.
- Egzekwuj autoryzację i izolację sandbox niezależnie od wartości korzeni.
- Sprawdzaj uprawnienia w momencie dostępu do pliku, nie tylko podczas listowania.
- Unikaj zwracania wrażliwych ścieżek w logach lub komunikatach o błędach.

## Kluczowe wnioski

- Korzenie opisują istotne lokalizacje systemu plików; nie przechowują stanu
  konwersacji.
- Korzenie to wskazówki, nie granica kontroli dostępu.
- MCP `2026-07-28` przenosi zdolność per każde żądanie i używa
  `InputRequiredResult` dla `roots/list`.
- Nowe implementacje powinny używać parametrów narzędzi, URI zasobów lub
  konfiguracji serwera zamiast tego.

## Dodatkowe zasoby

- [Korzenie w MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Rejestr funkcji przestarzałych](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [Co się zmieniło w MCP: Specyfikacja z 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->