# Uruchom przykład

Ten przykład uruchamia serwer MCP z middleware, który sprawdza, czy nagłówek Authorization jest prawidłowy.

## Zainstaluj zależności

```bash
pip install "mcp[cli]" 
```

## Uruchom serwer

```bash
python server.py
```

uruchom klienta w innym terminalu

```bash
python client.py
```

Powinieneś zobaczyć wynik podobny do:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

to oznacza, że przesyłane poświadczenie zostało zaakceptowane.

Spróbuj zmienić poświadczenie w `client.py` na "secret-token2", wtedy powinieneś zobaczyć ten tekst jako część odpowiedzi:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

to oznacza, że zostałeś uwierzytelniony (posiadałeś poświadczenie), ale było ono nieprawidłowe.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.