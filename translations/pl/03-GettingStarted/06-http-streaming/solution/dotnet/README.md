# Uruchamianie tego przykładu

## -1- Zainstaluj zależności

```bash
dotnet restore
```

## -2- Uruchom przykład

```bash
dotnet run
```

## -3- Przetestuj przykład

Uruchom osobny terminal przed wykonaniem poniższych kroków (upewnij się, że serwer nadal działa).

Gdy serwer działa w jednym terminalu, otwórz drugi terminal i uruchom następujące polecenie:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

Powinno to uruchomić serwer WWW z interfejsem wizualnym, który umożliwia testowanie przykładu.

> Upewnij się, że jako typ transportu wybrano **Streamable HTTP**, a URL to `http://localhost:3001/mcp`.

Gdy serwer zostanie połączony:

- spróbuj wyświetlić listę narzędzi i uruchom `add` z argumentami 2 i 4, powinieneś zobaczyć wynik 6.
- przejdź do zasobów i szablonu zasobów, wywołaj "greeting", wpisz imię, a powinieneś zobaczyć powitanie z podanym imieniem.

### Testowanie w trybie CLI

Możesz uruchomić go bezpośrednio w trybie CLI, wykonując następujące polecenie:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

To wyświetli listę wszystkich narzędzi dostępnych na serwerze. Powinieneś zobaczyć następujący wynik:

```text
{
  "tools": [
    {
      "name": "AddNumbers",
      "description": "Add two numbers together.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "description": "The first number",
            "type": "integer"
          },
          "b": {
            "description": "The second number",
            "type": "integer"
          }
        },
        "title": "AddNumbers",
        "description": "Add two numbers together.",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

Aby wywołać narzędzie, wpisz:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

Powinieneś zobaczyć następujący wynik:

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> Zazwyczaj uruchamianie inspektora w trybie CLI jest znacznie szybsze niż w przeglądarce.
> Przeczytaj więcej o inspektorze [tutaj](https://github.com/modelcontextprotocol/inspector).

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.