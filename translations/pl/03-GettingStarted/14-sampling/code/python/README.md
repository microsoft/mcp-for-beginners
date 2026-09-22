# Uruchom przykład

> [!WARNING]
> Ten przykład używa przestarzałego próbkowania i przestarzałego punktu końcowego HTTP+SSE. 
> Jest on zachowany dla kompatybilności MCP `2025-11-25`. Nowe implementacje powinny wywoływać
> dostawcę LLM bezpośrednio i używać Streamable HTTP do zdalnego ruchu MCP.

## Utwórz środowisko wirtualne

```sh
python -m venv venv
source ./venv/bin/activate
```

## Zainstaluj zależności

```sh
pip install "mcp[cli]"
```

## Uruchom serwer

```sh
uvicorn server:app --port 8000
```

## Przetestuj serwer z GitHub Copilot i VS Code

Dodaj wpis do pliku mcp.json w ten sposób:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Upewnij się, że kliknąłeś „start” na serwerze.

W GitHub Copilot wklej następującą komendę:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

Za pierwszym razem zostaniesz zapytany, czy zaakceptować akcję Próbkowania, następnie zostaniesz poproszony o zaakceptowanie narzędzia do uruchomienia "create_blog". Powinieneś zobaczyć odpowiedź podobną do:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->