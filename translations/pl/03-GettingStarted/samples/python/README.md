# Serwer Kalkulatora MCP (Python)



Prosta implementacja serwera Model Context Protocol (MCP) w Pythonie, który zapewnia podstawową funkcjonalność kalkulatora.


## Instalacja

Zainstaluj wymagane zależności:

```bash
pip install -r requirements.txt
```

Lub zainstaluj bezpośrednio MCP Python SDK:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Użytkowanie

### Uruchamianie serwera

Serwer jest zaprojektowany do użytku przez klientów MCP (np. Claude Desktop). Aby uruchomić serwer:

```bash
python mcp_calculator_server.py
```

**Uwaga**: Uruchamiając bezpośrednio w terminalu, zobaczysz błędy walidacji JSON-RPC. To normalne zachowanie - serwer oczekuje na poprawnie sformatowane wiadomości klientów MCP.

### Testowanie funkcji

Aby przetestować poprawność działania funkcji kalkulatora:

```bash
python test_calculator.py
```

## Rozwiązywanie problemów

### Błędy importu

Jeśli pojawi się `ModuleNotFoundError: No module named 'mcp'`, zainstaluj MCP Python SDK:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### Błędy JSON-RPC przy bezpośrednim uruchomieniu

Błędy takie jak "Invalid JSON: EOF while parsing a value" podczas bezpośredniego uruchamiania serwera są spodziewane. Serwer potrzebuje wiadomości od klientów MCP, a nie bezpośredniego wejścia z terminala.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->