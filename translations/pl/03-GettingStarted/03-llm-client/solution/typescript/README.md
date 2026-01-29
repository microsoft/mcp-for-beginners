# Uruchamianie tego przykładu

Ten przykład zakłada posiadanie LLM po stronie klienta. LLM wymaga, abyś uruchomił to w Codespaces lub skonfigurował osobisty token dostępu w GitHub, aby działało.

## -1- Zainstaluj zależności

```bash
npm install
```

## -3- Uruchom serwer

```bash
npm run build
```

## -4- Uruchom klienta

```sh
npm run client
```

Powinieneś zobaczyć wynik podobny do:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.