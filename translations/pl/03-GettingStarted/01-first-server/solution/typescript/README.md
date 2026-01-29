# Uruchamianie tego przykładu

Zaleca się zainstalowanie `uv`, ale nie jest to konieczne, zobacz [instrukcje](https://docs.astral.sh/uv/#highlights)

## -1- Zainstaluj zależności

```bash
npm install
```

## -3- Uruchom przykład

```bash
npm run build
```

## -4- Przetestuj przykład

Gdy serwer działa w jednym terminalu, otwórz drugi terminal i uruchom następujące polecenie:

```bash
npm run inspector
```

Powinno to uruchomić serwer WWW z interfejsem wizualnym, który umożliwia testowanie przykładu.

Gdy serwer zostanie połączony:

- spróbuj wyświetlić listę narzędzi i uruchom `add` z argumentami 2 i 4, powinieneś zobaczyć wynik 6.
- przejdź do zasobów i szablonu zasobów, wywołaj "greeting", wpisz imię, a powinieneś zobaczyć powitanie z podanym przez Ciebie imieniem.

### Testowanie w trybie CLI

Inspektor, który uruchomiłeś, to w rzeczywistości aplikacja Node.js, a `mcp dev` jest jej nakładką.

Możesz uruchomić go bezpośrednio w trybie CLI, wykonując następujące polecenie:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

To wyświetli listę wszystkich narzędzi dostępnych na serwerze. Powinieneś zobaczyć następujący wynik:

```text
{
  "tools": [
    {
      "name": "add",
      "description": "Add two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "addArguments"
      }
    }
  ]
}
```

Aby wywołać narzędzie, wpisz:

```bash
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
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
> Zazwyczaj inspektor działa znacznie szybciej w trybie CLI niż w przeglądarce.
> Przeczytaj więcej o inspektorze [tutaj](https://github.com/modelcontextprotocol/inspector).

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby zapewnić poprawność tłumaczenia, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.