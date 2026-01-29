# Uruchamianie tego przykładu

## -1- Zainstaluj zależności

```bash
dotnet restore
```

## -3- Uruchom przykład

```bash
dotnet run
```

## -4- Przetestuj przykład

Gdy serwer działa w jednym terminalu, otwórz drugi terminal i uruchom następujące polecenie:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Powinno to uruchomić serwer WWW z interfejsem wizualnym, który umożliwia testowanie przykładu.

Gdy serwer jest połączony:

- spróbuj wyświetlić listę narzędzi i uruchom `add` z argumentami 2 i 4, powinieneś zobaczyć wynik 6.
- przejdź do zasobów i szablonu zasobów, wywołaj "greeting", wpisz imię, a powinieneś zobaczyć powitanie z podanym imieniem.

### Testowanie w trybie CLI

Możesz uruchomić go bezpośrednio w trybie CLI, wykonując następujące polecenie:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

To wyświetli listę wszystkich dostępnych narzędzi na serwerze. Powinieneś zobaczyć następujący wynik:

```text
{
  "tools": [
    {
      "name": "Add",
      "description": "Adds two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "integer"
          },
          "b": {
            "type": "integer"
          }
        },
        "title": "Add",
        "description": "Adds two numbers",
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
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

Powinieneś zobaczyć następujący wynik:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Sum 3"
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
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.