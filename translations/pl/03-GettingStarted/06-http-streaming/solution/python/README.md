# Uruchamianie tego przykładu

Oto jak uruchomić klasyczny serwer i klient HTTP streaming, a także serwer i klient MCP streaming za pomocą Pythona.

### Przegląd

- Skonfigurujesz serwer MCP, który przesyła powiadomienia o postępie do klienta podczas przetwarzania elementów.
- Klient będzie wyświetlał każde powiadomienie w czasie rzeczywistym.
- Ten przewodnik obejmuje wymagania wstępne, konfigurację, uruchamianie i rozwiązywanie problemów.

### Wymagania wstępne

- Python 3.9 lub nowszy
- Pakiet Python `mcp` (zainstaluj za pomocą `pip install mcp`)

### Instalacja i konfiguracja

1. Sklonuj repozytorium lub pobierz pliki rozwiązania.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Utwórz i aktywuj wirtualne środowisko (zalecane):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Zainstaluj wymagane zależności:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Pliki

- **Serwer:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Klient:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Uruchamianie klasycznego serwera HTTP streaming

1. Przejdź do katalogu z rozwiązaniem:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Uruchom klasyczny serwer HTTP streaming:

   ```pwsh
   python server.py
   ```

3. Serwer uruchomi się i wyświetli:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Uruchamianie klasycznego klienta HTTP streaming

1. Otwórz nowe okno terminala (aktywuj to samo wirtualne środowisko i katalog):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Powinieneś zobaczyć strumieniowo wyświetlane wiadomości w kolejności:

   ```text
   Running classic HTTP streaming client...
   Connecting to http://localhost:8000/stream with message: hello
   --- Streaming Progress ---
   Processing file 1/3...
   Processing file 2/3...
   Processing file 3/3...
   Here's the file content: hello
   --- Stream Ended ---
   ```

### Uruchamianie serwera MCP streaming

1. Przejdź do katalogu z rozwiązaniem:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Uruchom serwer MCP z transportem streamable-http:
   ```pwsh
   python server.py mcp
   ```
3. Serwer uruchomi się i wyświetli:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Uruchamianie klienta MCP streaming

1. Otwórz nowe okno terminala (aktywuj to samo wirtualne środowisko i katalog):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Powinieneś zobaczyć powiadomienia wyświetlane w czasie rzeczywistym, gdy serwer przetwarza każdy element:
   ```
   Running MCP client...
   Starting client...
   Session ID before init: None
   Session ID after init: a30ab7fca9c84f5fa8f5c54fe56c9612
   Session initialized, ready to call tools.
   Received message: root=LoggingMessageNotification(...)
   NOTIFICATION: root=LoggingMessageNotification(...)
   ...
   Tool result: meta=None content=[TextContent(type='text', text='Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello from client')]
   ```

### Kluczowe kroki implementacji

1. **Utwórz serwer MCP za pomocą FastMCP.**
2. **Zdefiniuj narzędzie, które przetwarza listę i wysyła powiadomienia za pomocą `ctx.info()` lub `ctx.log()`.**
3. **Uruchom serwer z `transport="streamable-http"`.**
4. **Zaimplementuj klienta z obsługą wiadomości, aby wyświetlać powiadomienia w miarę ich przychodzenia.**

### Przegląd kodu
- Serwer używa funkcji asynchronicznych i kontekstu MCP do wysyłania aktualizacji postępu.
- Klient implementuje asynchroniczną obsługę wiadomości, aby drukować powiadomienia i wynik końcowy.

### Wskazówki i rozwiązywanie problemów

- Używaj `async/await` do operacji nieblokujących.
- Zawsze obsługuj wyjątki zarówno po stronie serwera, jak i klienta, aby zapewnić niezawodność.
- Testuj z wieloma klientami, aby zaobserwować aktualizacje w czasie rzeczywistym.
- Jeśli napotkasz błędy, sprawdź wersję Pythona i upewnij się, że wszystkie zależności są zainstalowane.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.