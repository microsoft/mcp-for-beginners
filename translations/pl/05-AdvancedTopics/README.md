# Zaawansowane tematy w MCP

[![Zaawansowane MCP: Bezpieczne, Skalowalne i Wielomodalne Agentury AI](../../../translated_images/pl/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(Kliknij powyższy obraz, aby obejrzeć wideo z tej lekcji)_

Ten rozdział obejmuje szereg zaawansowanych tematów dotyczących implementacji Model Context Protocol (MCP), w tym integrację wielomodalną, skalowalność, najlepsze praktyki bezpieczeństwa oraz integrację korporacyjną. Tematy te są kluczowe dla budowania solidnych i gotowych do produkcji aplikacji MCP, które mogą sprostać wymaganiom nowoczesnych systemów AI.

## Przegląd

Ta lekcja bada zaawansowane koncepcje implementacji Model Context Protocol, koncentrując się na integracji wielomodalnej, skalowalności, najlepszych praktykach bezpieczeństwa oraz integracji korporacyjnej. Tematy te są niezbędne do budowania aplikacji MCP klasy produkcyjnej, które mogą obsługiwać złożone wymagania w środowiskach przedsiębiorstw.

## Cele lekcji

Do końca tej lekcji będziesz mógł:

- Implementować zdolności wielomodalne w ramach MCP
- Projektować skalowalne architektury MCP do scenariuszy o wysokim zapotrzebowaniu
- Stosować najlepsze praktyki bezpieczeństwa zgodne z zasadami bezpieczeństwa MCP
- Integrować MCP z korporacyjnymi systemami i frameworkami AI
- Optymalizować wydajność i niezawodność w środowiskach produkcyjnych

## Lekcje i przykładowe projekty

| Link | Tytuł | Opis |
|------|-------|-------------|
| [5.1 Integration with Azure](./mcp-integration/README.md) | Integracja z Azure | Naucz się, jak zintegrować swój serwer MCP na platformie Azure |
| [5.2 Multi modal sample](./mcp-multi-modality/README.md) | Przykłady wielomodalności MCP | Przykłady odpowiedzi audio, obrazu i wielomodalnych |
| [5.3 MCP OAuth2 sample](../../../05-AdvancedTopics/mcp-oauth2-demo) | Demonstracja MCP OAuth2 | Minimalna aplikacja Spring Boot pokazująca OAuth2 z MCP jako serwer autoryzacji i zasobów. Demonstruje bezpieczne wydawanie tokenów, chronione punkty końcowe, wdrożenie Azure Container Apps oraz integrację z API Management. |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | Konteksty główne | Dowiedz się więcej o kontekstach głównych i jak je implementować |
| [5.5 Routing](./mcp-routing/README.md) | Trasowanie | Poznaj różne typy trasowania |
| [5.6 Sampling](./mcp-sampling/README.md) | Próbkowanie | Naucz się pracy z próbkowaniem |
| [5.7 Scaling](./mcp-scaling/README.md) | Skalowanie | Poznaj zagadnienia skalowania |
| [5.8 Security](./mcp-security/README.md) | Bezpieczeństwo | Zabezpiecz swój serwer MCP |
| [5.9 Web Search sample](./web-search-mcp/README.md) | Przeszukiwanie sieci MCP | Pythonowy serwer i klient MCP integrujący się z SerpAPI w celu wyszukiwania treści online, wiadomości, produktów i Q&A w czasie rzeczywistym. Demonstruje orkiestrację wielu narzędzi, integrację zewnętrznych API oraz solidne obsługiwanie błędów. |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | Streaming | Transmisje danych w czasie rzeczywistym stały się niezbędne w dzisiejszym świecie opartym na danych, gdzie firmy i aplikacje potrzebują natychmiastowego dostępu do informacji, by podejmować szybkie decyzje. |
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | Wyszukiwanie internetowe | Jak MCP transformuje wyszukiwanie internetowe w czasie rzeczywistym, zapewniając ustandaryzowane podejście do zarządzania kontekstem w modelach AI, silnikach wyszukiwania i aplikacjach. | 
| [5.12  Entra ID Authentication for Model Context Protocol Servers](./mcp-security-entra/README.md) | Uwierzytelnianie Entra ID | Microsoft Entra ID zapewnia solidne rozwiązanie do zarządzania tożsamością i dostępem w chmurze, pomagając zapewnić, że tylko upoważnieni użytkownicy i aplikacje mogą współdziałać z Twoim serwerem MCP. |
| [5.13 Azure AI Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Integracja Azure AI Foundry | Naucz się, jak integrować serwery Model Context Protocol z agentami Azure AI Foundry, co umożliwia potężną orkiestrację narzędzi i korporacyjne możliwości AI z ustandaryzowanymi połączeniami z zewnętrznymi źródłami danych. |
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | Inżynieria kontekstu | Przyszłe możliwości technik inżynierii kontekstu dla serwerów MCP, w tym optymalizacja kontekstu, dynamiczne zarządzanie kontekstem oraz strategie efektywnego inżynieringu promptów w ramach MCP. |
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | Własny transport | Naucz się implementować niestandardowe mechanizmy transportu dla specjalistycznych scenariuszy komunikacji MCP. |
| [5.16 Protocol Features Deep Dive](./mcp-protocol-features/README.md) | Funkcje protokołu | Opanuj zaawansowane funkcje protokołu, w tym powiadomienia o postępie, anulowanie żądań, szablony zasobów i wzorce obsługi błędów. |
| [5.17 Adversarial Multi-Agent Reasoning](./mcp-adversarial-agents/README.md) | Agenci o charakterze kontradyktoryjnym | Wykorzystaj dwóch agentów o przeciwnych stanowiskach, dzielących jeden zestaw narzędzi MCP, aby uchwycić halucynacje, uwypuklić przypadki brzegowe oraz wytwarzać lepiej skalibrowane wyniki przez ustrukturyzowaną debatę. |

> **Nowość w specyfikacji MCP 2025-11-25**: Specyfikacja zawiera teraz eksperymentalne wsparcie dla **Zadań** (operacje długotrwałe z monitorowaniem postępu), **Adnotacji Narzędzi** (metadane o zachowaniu narzędzi dla bezpieczeństwa), **URL Mode Elicitation** (żądanie konkretnych treści URL od klientów) oraz ulepszonych **Korzeni** (do zarządzania kontekstem przestrzeni roboczej). Pełne szczegóły znajdują się w [lista zmian specyfikacji MCP](https://spec.modelcontextprotocol.io/).

## Dodatkowe odniesienia

Dla najnowszych informacji na temat zaawansowanych tematów MCP, odwołaj się do:
- [Dokumentacja MCP](https://modelcontextprotocol.io/)
- [Specyfikacja MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Repozytorium GitHub](https://github.com/modelcontextprotocol)
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – zagrożenia i środki zaradcze w zakresie bezpieczeństwa
- [Warsztat MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) – praktyczne szkolenie z bezpieczeństwa

## Najważniejsze wnioski

- Wielomodalne implementacje MCP rozszerzają możliwości AI poza przetwarzanie tekstu
- Skalowalność jest kluczowa dla wdrożeń korporacyjnych i można ją osiągnąć poprzez skalowanie poziome oraz pionowe
- Kompleksowe środki bezpieczeństwa chronią dane i zapewniają odpowiednią kontrolę dostępu
- Integracja korporacyjna z platformami takimi jak Azure OpenAI i Microsoft AI Foundry zwiększa możliwości MCP
- Zaawansowane implementacje MCP korzystają z optymalizowanych architektur i starannego zarządzania zasobami

## Ćwiczenie

Zaprojektuj implementację MCP klasy korporacyjnej dla konkretnego przypadku użycia:

1. Określ wymagania wielomodalne dla swojego przypadku użycia
2. Nakreśl kontrole bezpieczeństwa niezbędne do ochrony danych wrażliwych
3. Zaprojektuj skalowalną architekturę zdolną obsłużyć zmienne obciążenie
4. Zaplanuj punkty integracji z korporacyjnymi systemami AI
5. Udokumentuj potencjalne wąskie gardła wydajności i strategie ich łagodzenia

## Dodatkowe zasoby

- [Dokumentacja Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Dokumentacja Microsoft AI Foundry](https://learn.microsoft.com/en-us/ai-services/)

---

## Co dalej

Przeanalizuj lekcje w tym module, zaczynając od: [5.1 Integracja MCP](./mcp-integration/README.md)

Po ukończeniu tego modułu kontynuuj do: [Moduł 6: Wkłady społeczności](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było precyzyjne, należy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->