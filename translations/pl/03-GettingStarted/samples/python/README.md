# Serwer MCP Kalkulator (Python)

Prosta implementacja serwera Model Context Protocol (MCP) w Pythonie, oferująca podstawową funkcjonalność kalkulatora.

## Instalacja

Zainstaluj wymagane zależności:

```bash
pip install -r requirements.txt
```

Lub zainstaluj bezpośrednio MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

## Użycie

### Uruchamianie serwera

Serwer jest przeznaczony do użytku przez klientów MCP (np. Claude Desktop). Aby uruchomić serwer:

```bash
python mcp_calculator_server.py
```

**Uwaga**: Podczas uruchamiania bezpośrednio w terminalu zobaczysz błędy walidacji JSON-RPC. To normalne zachowanie - serwer oczekuje na poprawnie sformatowane wiadomości od klienta MCP.

### Testowanie funkcji

Aby przetestować, czy funkcje kalkulatora działają poprawnie:

```bash
python test_calculator.py
```

## Rozwiązywanie problemów

### Błędy importu

Jeśli pojawi się `ModuleNotFoundError: No module named 'mcp'`, zainstaluj MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

### Błędy JSON-RPC podczas uruchamiania bezpośredniego

Błędy takie jak "Invalid JSON: EOF while parsing a value" podczas bezpośredniego uruchamiania serwera są oczekiwane. Serwer wymaga wiadomości od klienta MCP, a nie bezpośredniego wejścia z terminala.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.