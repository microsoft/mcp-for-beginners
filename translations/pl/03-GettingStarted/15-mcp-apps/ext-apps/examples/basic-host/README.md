# Przykład: Podstawowy Host

Referencyjna implementacja pokazująca, jak zbudować aplikację hosta MCP, która łączy się z serwerami MCP i renderuje interfejsy narzędzi w bezpiecznym sandboxie.

Ten podstawowy host może być również używany do testowania aplikacji MCP podczas lokalnego rozwoju.

## Kluczowe pliki

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - host UI React z wyborem narzędzi, wprowadzaniem parametrów i zarządzaniem iframe
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - zewnętrzny iframe proxy z walidacją bezpieczeństwa i dwukierunkowym przesyłaniem wiadomości
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - logika podstawowa: połączenie z serwerem, wywoływanie narzędzi i konfiguracja AppBridge

## Rozpoczęcie pracy

```bash
npm install
npm run start
# Otwórz http://localhost:8080
```

Domyślnie aplikacja hosta będzie próbowała połączyć się z serwerem MCP pod adresem `http://localhost:3001/mcp`. Możesz skonfigurować to zachowanie, ustawiając zmienną środowiskową `SERVERS` jako tablicę JSON z adresami URL serwerów:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Architektura

Ten przykład używa wzorca podwójnego iframe sandbox do bezpiecznej izolacji UI:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Dlaczego dwa iframe?**

- Zewnętrzny iframe działa na oddzielnym pochodzeniu (port 8081), zapobiegając bezpośredniemu dostępowi do hosta
- Wewnętrzny iframe otrzymuje HTML za pomocą `srcdoc` i jest ograniczony przez atrybuty sandbox
- Wiadomości przepływają przez zewnętrzny iframe, który je weryfikuje i przesyła dwukierunkowo

Ta architektura zapewnia, że nawet jeśli kod UI narzędzia jest złośliwy, nie ma dostępu do DOM aplikacji hosta, ciasteczek ani kontekstu JavaScript.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->