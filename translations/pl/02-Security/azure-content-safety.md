# Zaawansowane zabezpieczenia MCP z Azure Content Safety

Azure Content Safety oferuje kilka potężnych narzędzi, które mogą zwiększyć bezpieczeństwo Twoich implementacji MCP:

## Prompt Shields

Microsoft AI Prompt Shields zapewniają solidną ochronę przed bezpośrednimi i pośrednimi atakami typu prompt injection poprzez:

1. **Zaawansowane wykrywanie**: Wykorzystuje uczenie maszynowe do identyfikacji złośliwych instrukcji ukrytych w treści.
2. **Wyróżnianie**: Przekształca tekst wejściowy, aby pomóc systemom AI rozróżnić prawidłowe instrukcje od danych zewnętrznych.
3. **Separatory i oznaczanie danych**: Oznacza granice między zaufanymi a niezaufanymi danymi.
4. **Integracja z Content Safety**: Współpracuje z Azure AI Content Safety w celu wykrywania prób jailbreak i szkodliwych treści.
5. **Ciągłe aktualizacje**: Microsoft regularnie aktualizuje mechanizmy ochronne przeciw nowym zagrożeniom.

## Implementacja Azure Content Safety z MCP

To podejście zapewnia wielowarstwową ochronę:
- Skanowanie danych wejściowych przed przetwarzaniem
- Walidacja wyników przed zwróceniem
- Wykorzystanie list blokujących znane szkodliwe wzorce
- Korzystanie z ciągle aktualizowanych modeli bezpieczeństwa treści Azure

## Zasoby Azure Content Safety

Aby dowiedzieć się więcej o implementacji Azure Content Safety z serwerami MCP, zapoznaj się z tymi oficjalnymi materiałami:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Oficjalna dokumentacja Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Dowiedz się, jak zapobiegać atakom typu prompt injection.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Szczegółowy opis API do implementacji Content Safety.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Szybki przewodnik implementacji w C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Biblioteki klienckie dla różnych języków programowania.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Specjalne wskazówki dotyczące wykrywania i zapobiegania próbom jailbreak.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Najlepsze praktyki skutecznej implementacji bezpieczeństwa treści.

Aby uzyskać bardziej szczegółowe informacje na temat implementacji, zobacz nasz [przewodnik po implementacji Azure Content Safety](./azure-content-safety-implementation.md).

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.