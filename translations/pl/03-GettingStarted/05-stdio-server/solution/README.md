# Rozwiązania serwerowe MCP stdio

> **⚠️ Ważne**: Te rozwiązania zostały zaktualizowane, aby korzystać z **transportu stdio**, zgodnie z zaleceniami Specyfikacji MCP z dnia 2025-06-18. Oryginalny transport SSE (Server-Sent Events) został wycofany.

Oto kompletne rozwiązania do budowy serwerów MCP z wykorzystaniem transportu stdio w każdym środowisku wykonawczym:

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - Kompleksowa implementacja serwera stdio
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - Serwer stdio w Pythonie z asyncio
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - Serwer stdio w .NET z wstrzykiwaniem zależności

Każde rozwiązanie pokazuje:
- Konfigurację transportu stdio
- Definiowanie narzędzi serwera
- Poprawne obsługiwanie wiadomości JSON-RPC
- Integrację z klientami MCP, takimi jak Claude

Wszystkie rozwiązania są zgodne z aktualną specyfikacją MCP i wykorzystują zalecany transport stdio dla optymalnej wydajności i bezpieczeństwa.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.