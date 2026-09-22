# Najlepsze praktyki bezpieczeństwa MCP - aktualizacja wrzesień 2026

Ten kompleksowy przewodnik przedstawia istotne najlepsze praktyki bezpieczeństwa dla
wdrażania systemów Model Context Protocol (MCP) opartych na
**Specyfikacji MCP 2026-07-28** oraz obowiązujących standardach branżowych. Te
praktyki dotyczą zarówno tradycyjnych zagadnień bezpieczeństwa, jak i specyficznych zagrożeń AI
unikalnych dla wdrożeń MCP.

## Krytyczne wymagania bezpieczeństwa

### Obowiązkowe kontrole bezpieczeństwa (wymagania MUSZĄCE)

1. **Weryfikacja tokenów**: Serwery MCP **NIE MOGĄ** akceptować żadnych tokenów, które nie zostały wyraźnie wydane dla samego serwera MCP
2. **Weryfikacja autoryzacji**: Serwery MCP implementujące autoryzację **MUSZĄ** weryfikować WSZYSTKIE przychodzące żądania i **NIE MOGĄ** używać sesji do uwierzytelniania  
3. **Zgoda użytkownika**: Serwery proxy MCP używające statycznych identyfikatorów klientów stron trzecich **MUSZĄ** uzyskać wyraźną zgodę dla każdego klienta MCP przed przekazaniem procesu autoryzacji
4. **Bezpieczeństwo uchwytu stanu**: Serwery MCP **NIE MOGĄ** traktować posiadania
	uchwytu stanu aplikacji jako uwierzytelnienia oraz **MUSZĄ** autoryzować każde
	żądanie, które go używa

## Podstawowe praktyki bezpieczeństwa

### 1. Walidacja i oczyszczanie wejść
- **Kompleksowa walidacja wejść**: Waliduj i oczyszczaj wszystkie dane wejściowe, aby zapobiegać atakom wstrzykiwania, problemom confused deputy oraz podatnościom na wstrzykiwanie promptów
- **Wymuszanie schematów parametrów**: Zaimplementuj rygorystyczną walidację schematów JSON dla wszystkich parametrów narzędzi i wejść API
- **Filtrowanie treści**: Korzystaj z Microsoft Prompt Shields oraz Azure Content Safety do filtrowania złośliwych treści w promptach i odpowiedziach
- **Oczyszczanie wyjść**: Waliduj i oczyszczaj wszystkie wyjścia modelu przed prezentacją użytkownikom lub systemom docelowym

### 2. Doskonałość uwierzytelniania i autoryzacji  
- **Zewnętrzni dostawcy tożsamości**: Deleguj uwierzytelnianie do ugruntowanych dostawców tożsamości (Microsoft Entra ID, dostawcy OAuth 2.1) zamiast implementować własne
- **Rejestracja klienta**: Preferuj Metadane Client ID lub wstępną rejestrację; używaj przestarzałej Dynamicznej Rejestracji Klienta tylko dla kompatybilności
- **Szczegółowe uprawnienia**: Implementuj granulowane, specyficzne dla narzędzi uprawnienia zgodnie z zasadą najmniejszych uprawnień
- **Zarządzanie cyklem życia tokenów**: Używaj krótkotrwałych tokenów dostępowych z bezpieczną rotacją i odpowiednią walidacją odbiorcy
- **Uwierzytelnianie wieloskładnikowe**: Wymagaj MFA dla wszystkich dostępów administracyjnych i operacji wrażliwych

### 3. Bezpieczne protokoły komunikacji
- **Transport Layer Security**: Używaj HTTPS z odpowiednią walidacją certyfikatów
	dla zdalnej komunikacji HTTP MCP; używaj izolacji procesów i
	poświadczeń środowiskowych dla lokalnych serwerów stdio
- **Szyfrowanie end-to-end**: Implementuj dodatkowe warstwy szyfrowania dla danych wysoce wrażliwych w tranzycie i w spoczynku
- **Zarządzanie certyfikatami**: Utrzymuj właściwy cykl życia certyfikatów z automatycznymi procesami odnawiania
- **Wymuszanie wersji protokołu**: Używaj MCP `2026-07-28`, dołącz wymagane
	metadane wersji w każdym żądaniu i odrzucaj nieobsługiwane wersje

### 4. Zaawansowane ograniczenia tempa i ochrona zasobów
- **Wielowarstwowe ograniczenia tempa**: Wdrażaj ograniczenia tempa według użytkownika, poświadczeń,
  operacji, narzędzia i zasobu, aby zapobiegać nadużyciom
- **Adaptacyjne ograniczenia tempa**: Korzystaj z ograniczeń tempa opartych na uczeniu maszynowym, które dopasowują się do wzorców użycia i wskaźników zagrożeń
- **Zarządzanie limitami zasobów**: Ustaw odpowiednie limity zasobów obliczeniowych, zużycia pamięci i czasu wykonywania
- **Ochrona przed DDoS**: Wdrażaj kompleksowe systemy ochrony DDoS i analizy ruchu

### 5. Kompleksowe logowanie i monitoring
- **Strukturyzowane logi audytowe**: Implementuj szczegółowe, przeszukiwalne logi dla wszystkich operacji MCP, wykonywania narzędzi i zdarzeń bezpieczeństwa
- **Monitoring bezpieczeństwa w czasie rzeczywistym**: Wdrażaj systemy SIEM z detekcją anomalii zasilaną AI dla obciążeń MCP
- **Logowanie zgodne z prywatnością**: Loguj zdarzenia bezpieczeństwa z poszanowaniem wymogów i regulacji ochrony danych
- **Integracja odpowiedzi na incydenty**: Połącz systemy logowania z automatycznymi procesami reagowania na incydenty

### 6. Ulepszone praktyki bezpiecznego przechowywania
- **Moduły bezpieczeństwa sprzętowego (HSM)**: Używaj przechowywania kluczy wspieranego przez HSM (Azure Key Vault, AWS CloudHSM) dla krytycznych operacji kryptograficznych
- **Zarządzanie kluczami szyfrowania**: Wdrażaj odpowiednią rotację kluczy, segregację oraz kontrolę dostępu do kluczy szyfrowania
- **Zarządzanie sekretami**: Przechowuj wszystkie klucze API, tokeny i poświadczenia w dedykowanych systemach zarządzania sekretami
- **Klasyfikacja danych**: Klasyfikuj dane według poziomu wrażliwości i stosuj odpowiednie środki ochrony

### 7. Zaawansowane zarządzanie tokenami
- **Zapobieganie przekazywaniu tokenów**: Wyraźnie zabroń wzorców przekazywania tokenów omijających kontrole bezpieczeństwa
- **Weryfikacja odbiorcy**: Zawsze weryfikuj, czy roszczenia tokena dotyczą odpowiedniej tożsamości serwera MCP
- **Autoryzacja bazująca na roszczeniach**: Implementuj granulowaną autoryzację opartą na roszczeniach tokena i atrybutach użytkownika
- **Powiązanie tokenów**: Waliduj, że tokeny są przeznaczone dla konkretnego zasobu MCP oraz
	powiąż uchwyty stanu aplikacji po stronie serwera z uwierzytelnionym podmiotem

### 8. Bezpieczny stan aplikacji

- **Kryptograficzne uchwyty stanu**: Generuj nieprzezroczyste, niedeterministyczne uchwyty
	dla stanu obejmującego wiele żądań
- **Powiązanie specyficzne dla użytkownika**: Powiąż każdy uchwyt po stronie serwera z uwierzytelnionym
	podmiotem; nie ufaj identyfikatorowi użytkownika dostarczonemu przez klienta
- **Kontrole cyklu życia**: Wygasaj i odwołuj uchwyty oraz definiuj sposoby
	odzyskiwania ze stanu przestarzałego
- **Autoryzacja przy każdym żądaniu**: Ponownie sprawdzaj autoryzację za każdym razem, gdy uchwyt jest
	przekazywany; uchwyt jest nazwą, nie poświadczeniem

### 9. Specyficzne kontrole bezpieczeństwa AI
- **Obrona przed wstrzykiwaniem promptów**: Wdrażaj Microsoft Prompt Shields z podświetlaniem, delimiterami i technikami datamarkowania
- **Zapobieganie zatruciu narzędzi**: Waliduj metadane narzędzi, monitoruj dynamiczne zmiany oraz weryfikuj integralność narzędzi
- **Walidacja wyjść modelu**: Przeskanuj wyjścia modelu pod kątem potencjalnych wycieków danych, szkodliwych treści lub naruszeń polityk bezpieczeństwa
- **Ochrona okna kontekstu**: Wdrażaj kontrole zapobiegające zatruciu i manipulacji oknem kontekstu

### 10. Bezpieczeństwo wykonywania narzędzi
- **Sandboxing wykonywania**: Uruchamiaj wykonywanie narzędzi w konteneryzowanych, izolowanych środowiskach z ograniczeniami zasobów
- **Separacja przywilejów**: Wykonuj narzędzia z minimalnymi wymaganymi uprawnieniami i oddzielnymi kontami usługowymi
- **Izolacja sieciowa**: Wdrażaj segmentację sieci dla środowisk wykonawczych narzędzi
- **Monitoring wykonywania**: Monitoruj działanie narzędzi pod kątem nietypowego zachowania, zużycia zasobów i naruszeń bezpieczeństwa

### 11. Ciągła walidacja bezpieczeństwa
- **Automatyczne testy bezpieczeństwa**: Integruj testy bezpieczeństwa w pipeline'ach CI/CD z narzędziami takimi jak GitHub Advanced Security
- **Zarządzanie podatnościami**: Regularnie skanuj wszystkie zależności, w tym modele AI i usługi zewnętrzne
- **Testy penetracyjne**: Przeprowadzaj regularne oceny bezpieczeństwa skierowane bezpośrednio na implementacje MCP
- **Przeglądy kodu pod kątem bezpieczeństwa**: Wprowadzaj obowiązkowe przeglądy bezpieczeństwa dla wszystkich zmian kodu dotyczących MCP

### 12. Bezpieczeństwo łańcucha dostaw AI
- **Weryfikacja komponentów**: Weryfikuj pochodzenie, integralność i bezpieczeństwo wszystkich komponentów AI (modele, embeddingi, API)
- **Zarządzanie zależnościami**: Utrzymuj aktualne inwentaryzacje wszystkich zależności oprogramowania i AI wraz z monitorowaniem podatności
- **Zaufane repozytoria**: Używaj weryfikowanych, zaufanych źródeł dla wszystkich modeli, bibliotek i narzędzi AI
- **Monitoring łańcucha dostaw**: Ciągle monitoruj kompromitacje dostawców usług AI i repozytoriów modeli

## Zaawansowane wzorce bezpieczeństwa

### Architektura Zero Trust dla MCP
- **Nigdy nie ufaj, zawsze weryfikuj**: Wdrażaj ciągłą weryfikację wszystkich uczestników MCP
- **Mikrosegmentacja**: Izoluj komponenty MCP za pomocą granulowanych kontroli sieci i tożsamości
- **Dostęp warunkowy**: Wdrażaj kontrole dostępu oparte na ryzyku, które dostosowują się do kontekstu i zachowania
- **Ciągła ocena ryzyka**: Dynamicznie oceniaj postawę bezpieczeństwa na podstawie aktualnych wskaźników zagrożeń

### Implementacja AI z zachowaniem prywatności
- **Minimalizacja danych**: Udostępniaj tylko minimalnie niezbędne dane dla każdej operacji MCP
- **Prywatność różnicowa**: Wdrażaj techniki ochrony prywatności dla przetwarzania danych wrażliwych
- **Szyfrowanie homomorficzne**: Używaj zaawansowanych technik szyfrowania do bezpiecznych obliczeń na zaszyfrowanych danych
- **Uczenie federacyjne**: Wdrażaj rozproszone metody uczenia, które zachowują lokalność danych i prywatność

### Reagowanie na incydenty w systemach AI
- **Procedury incydentów specyficzne dla AI**: Opracuj procedury reagowania dostosowane do zagrożeń AI i MCP
- **Automatyczna reakcja**: Wdrażaj automatyczne akcje izolacji i naprawy dla powszechnych incydentów bezpieczeństwa AI  
- **Możliwości kryminalistyczne**: Utrzymuj gotowość na potrzeby kryminalistyczne związane z kompromitacjami systemów AI i wyciekami danych
- **Procedury odzyskiwania**: Ustal procedury odzyskiwania po zatruciu modeli AI, atakach wstrzykiwania promptów i kompromitacjach usług

## Zasoby wdrożeniowe i standardy

### 🏔️ Praktyczne szkolenia z bezpieczeństwa
- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Kompleksowe praktyczne warsztaty zabezpieczania serwerów MCP w Azure
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - Architektura referencyjna i wytyczne wdrażania OWASP MCP Top 10

### Oficjalna dokumentacja MCP
- [Specyfikacja MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Obowiązująca specyfikacja protokołu MCP
- [Najlepsze praktyki bezpieczeństwa MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - Oficjalne wytyczne bezpieczeństwa
- [Specyfikacja autoryzacji MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - Wzorce autoryzacji HTTP
- [Transporty MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - Wymagania dotyczące transportu

### Rozwiązania bezpieczeństwa Microsoft
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Zaawansowana ochrona przed wstrzykiwaniem promptów
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Kompletne filtrowanie treści AI
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Zarządzanie tożsamością i dostępem w przedsiębiorstwie
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Bezpieczne zarządzanie sekretami i poświadczeniami
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Skanowanie bezpieczeństwa łańcucha dostaw i kodu

### Standardy i ramy bezpieczeństwa
- [OAuth 2.1 Najlepsze praktyki bezpieczeństwa](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Aktualne wytyczne bezpieczeństwa OAuth
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Największe zagrożenia bezpieczeństwa aplikacji internetowych
- [OWASP Top 10 dla LLM](https://genai.owasp.org/download/43299/?tmstv=1731900559) - Zagrożenia bezpieczeństwa specyficzne dla AI
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Kompleksowe zarządzanie ryzykiem AI
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Systemy zarządzania bezpieczeństwem informacji

### Przewodniki i samouczki wdrożeniowe
- [Azure API Management jako MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Wzorce uwierzytelniania przedsiębiorstw
- [Microsoft Entra ID z serwerami MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integracja dostawcy tożsamości
- [Implementacja bezpiecznego przechowywania tokenów](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Najlepsze praktyki zarządzania tokenami
- [Szyfrowanie end-to-end dla AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Zaawansowane wzorce szyfrowania

### Zaawansowane zasoby bezpieczeństwa
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Praktyki bezpiecznego rozwoju
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - Testowanie bezpieczeństwa specyficzne dla AI
- [Modele zagrożeń dla systemów AI](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Metodologia modelowania zagrożeń AI
- [Inżynieria prywatności dla AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Techniki ochrony prywatności AI

### Zgodność i zarządzanie
- [Zgodność GDPR dla AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Wymogi prywatności w systemach AI
- [Ramowy model zarządzania AI](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Odpowiedzialne wdrożenie AI
- [SOC 2 dla usług AI](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Kontrole bezpieczeństwa dla dostawców usług AI
- [Zgodność HIPAA dla AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Wymogi zgodności AI w ochronie zdrowia

### DevSecOps i automatyzacja
- [Pipeline DevSecOps dla AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Bezpieczne pipeline'y rozwoju AI
- [Automatyczne testy bezpieczeństwa](https://learn.microsoft.com/security/engineering/devsecops) - Ciągła walidacja bezpieczeństwa
- [Bezpieczeństwo infrastruktury jako kodu](https://learn.microsoft.com/security/engineering/infrastructure-security) - Bezpieczne wdrażanie infrastruktury
- [Bezpieczeństwo kontenerów dla AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Bezpieczeństwo konteneryzacji obciążeń AI

### Monitoring i reagowanie na incydenty  
- [Azure Monitor dla obciążeń AI](https://learn.microsoft.com/azure/azure-monitor/overview) - Kompleksowe rozwiązania monitorujące
- [Reagowanie na incydenty bezpieczeństwa AI](https://learn.microsoft.com/security/compass/incident-response-playbooks) - Procedury incydentów specyficzne dla AI
- [SIEM dla systemów AI](https://learn.microsoft.com/azure/sentinel/overview) - Zarządzanie informacjami i zdarzeniami bezpieczeństwa

- [Wywiad Zagrożeń dla AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - źródła wywiadu zagrożeń AI

## 🔄 Ciągłe Doskonalenie

### Bądź na bieżąco z ewoluującymi standardami
- **Aktualizacje Specyfikacji MCP**: Monitoruj oficjalne zmiany specyfikacji MCP i komunikaty dotyczące bezpieczeństwa
- **Wywiad Zagrożeń**: Subskrybuj kanały dotyczące zagrożeń bezpieczeństwa AI oraz bazy danych podatności  
- **Zaangażowanie Społeczności**: Uczestnicz w dyskusjach i grupach roboczych społeczności bezpieczeństwa MCP
- **Regularna Ocena**: Przeprowadzaj kwartalne oceny stanu bezpieczeństwa i odpowiednio aktualizuj praktyki

### Wkład w bezpieczeństwo MCP
- **Badania Bezpieczeństwa**: Wnoś wkład w badania bezpieczeństwa MCP i programy ujawniania podatności
- **Dzielenie się Najlepszymi Praktykami**: Dziel się wdrożeniami zabezpieczeń i doświadczeniami ze społecznością
- **Rozwój Standardów**: Uczestnicz w tworzeniu specyfikacji MCP i standardów bezpieczeństwa
- **Tworzenie Narzędzi**: Twórz i udostępniaj narzędzia i biblioteki bezpieczeństwa dla ekosystemu MCP

---

*Ten dokument odzwierciedla najlepsze praktyki bezpieczeństwa MCP na dzień 9 września 2026 r.,
na podstawie specyfikacji MCP `2026-07-28`. Praktyki bezpieczeństwa powinny być regularnie
przeglądane w miarę rozwoju protokołu i krajobrazu zagrożeń.*

## Co dalej

- Przeczytaj: [Najlepsze praktyki bezpieczeństwa MCP](./mcp-security-best-practices.md)
- Wróć do: [Przegląd modułu bezpieczeństwa](./README.md)
- Kontynuuj do: [Moduł 3: Pierwsze kroki](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->