# Najlepsze praktyki bezpieczeństwa MCP 2025

Ten kompleksowy przewodnik przedstawia niezbędne najlepsze praktyki bezpieczeństwa dotyczące wdrażania systemów Model Context Protocol (MCP) opartych na najnowszej **Specyfikacji MCP 2025-11-25** oraz aktualnych standardach branżowych. Praktyki te dotyczą zarówno tradycyjnych zagadnień bezpieczeństwa, jak i specyficznych zagrożeń związanych ze sztuczną inteligencją unikalnych dla wdrożeń MCP.

## Krytyczne wymagania bezpieczeństwa

### Obowiązkowe kontrole bezpieczeństwa (wymagania MUST)

1. **Weryfikacja tokenów**: Serwery MCP **NIE MOGĄ** akceptować żadnych tokenów, które nie zostały wyraźnie wydane dla samego serwera MCP
2. **Weryfikacja autoryzacji**: Serwery MCP implementujące autoryzację **MUSZĄ** weryfikować WSZYSTKIE przychodzące żądania i **NIE MOGĄ** używać sesji do uwierzytelniania  
3. **Zgoda użytkownika**: Serwery proxy MCP używające statycznych identyfikatorów klienta **MUSZĄ** uzyskać wyraźną zgodę użytkownika dla każdego dynamicznie rejestrowanego klienta
4. **Bezpieczne identyfikatory sesji**: Serwery MCP **MUSZĄ** używać kryptograficznie bezpiecznych, niedeterministycznych identyfikatorów sesji generowanych za pomocą bezpiecznych generatorów liczb losowych

## Podstawowe praktyki bezpieczeństwa

### 1. Walidacja i oczyszczanie danych wejściowych
- **Kompleksowa walidacja danych wejściowych**: Waliduj i oczyszczaj wszystkie dane wejściowe, aby zapobiec atakom wstrzyknięcia, problemom z „confused deputy” oraz podatnościom na wstrzyknięcia w promptach
- **Egzekwowanie schematów parametrów**: Wdrażaj ścisłą walidację schematów JSON dla wszystkich parametrów narzędzi i wejść API
- **Filtrowanie treści**: Używaj Microsoft Prompt Shields i Azure Content Safety do filtrowania złośliwych treści w promptach i odpowiedziach
- **Oczyszczanie danych wyjściowych**: Waliduj i oczyszczaj wszystkie wyjścia modelu przed ich prezentacją użytkownikom lub systemom dalszego przetwarzania

### 2. Doskonałość uwierzytelniania i autoryzacji  
- **Zewnętrzni dostawcy tożsamości**: Deleguj uwierzytelnianie do uznanych dostawców tożsamości (Microsoft Entra ID, dostawcy OAuth 2.1) zamiast implementować własne mechanizmy uwierzytelniania
- **Szczegółowe uprawnienia**: Wdrażaj granularne, specyficzne dla narzędzi uprawnienia zgodnie z zasadą najmniejszych uprawnień
- **Zarządzanie cyklem życia tokenów**: Używaj krótkotrwałych tokenów dostępu z bezpieczną rotacją i właściwą weryfikacją odbiorcy
- **Uwierzytelnianie wieloskładnikowe**: Wymagaj MFA dla całego dostępu administracyjnego i operacji wrażliwych

### 3. Bezpieczne protokoły komunikacyjne
- **Transport Layer Security**: Używaj HTTPS/TLS 1.3 dla wszystkich komunikacji MCP z właściwą weryfikacją certyfikatów
- **Szyfrowanie end-to-end**: Wdrażaj dodatkowe warstwy szyfrowania dla danych wysoce wrażliwych w tranzycie i w spoczynku
- **Zarządzanie certyfikatami**: Utrzymuj właściwe zarządzanie cyklem życia certyfikatów z automatycznymi procesami odnawiania
- **Egzekwowanie wersji protokołu**: Używaj aktualnej wersji protokołu MCP (2025-11-25) z właściwą negocjacją wersji.

### 4. Zaawansowane ograniczanie szybkości i ochrona zasobów
- **Wielowarstwowe ograniczanie szybkości**: Wdrażaj ograniczanie szybkości na poziomie użytkownika, sesji, narzędzia i zasobów, aby zapobiec nadużyciom
- **Adaptacyjne ograniczanie szybkości**: Używaj ograniczania szybkości opartego na uczeniu maszynowym, które dostosowuje się do wzorców użycia i wskaźników zagrożeń
- **Zarządzanie limitami zasobów**: Ustal odpowiednie limity dla zasobów obliczeniowych, użycia pamięci i czasu wykonania
- **Ochrona przed DDoS**: Wdrażaj kompleksowe systemy ochrony przed DDoS i analizy ruchu

### 5. Kompleksowe logowanie i monitorowanie
- **Strukturalne logowanie audytowe**: Wdrażaj szczegółowe, przeszukiwalne logi dla wszystkich operacji MCP, wykonania narzędzi i zdarzeń bezpieczeństwa
- **Monitorowanie bezpieczeństwa w czasie rzeczywistym**: Wdrażaj systemy SIEM z wykrywaniem anomalii wspieranym przez AI dla obciążeń MCP
- **Logowanie zgodne z prywatnością**: Loguj zdarzenia bezpieczeństwa z poszanowaniem wymagań i regulacji dotyczących prywatności danych
- **Integracja z reakcją na incydenty**: Połącz systemy logowania z automatycznymi procesami reagowania na incydenty

### 6. Ulepszone praktyki bezpiecznego przechowywania
- **Moduły bezpieczeństwa sprzętowego**: Używaj magazynów kluczy opartych na HSM (Azure Key Vault, AWS CloudHSM) dla krytycznych operacji kryptograficznych
- **Zarządzanie kluczami szyfrowania**: Wdrażaj właściwą rotację kluczy, segregację i kontrolę dostępu do kluczy szyfrowania
- **Zarządzanie sekretami**: Przechowuj wszystkie klucze API, tokeny i poświadczenia w dedykowanych systemach zarządzania sekretami
- **Klasyfikacja danych**: Klasyfikuj dane według poziomów wrażliwości i stosuj odpowiednie środki ochrony

### 7. Zaawansowane zarządzanie tokenami
- **Zapobieganie przekazywaniu tokenów**: Wyraźnie zabraniaj wzorców przekazywania tokenów omijających kontrole bezpieczeństwa
- **Weryfikacja odbiorcy**: Zawsze weryfikuj, czy roszczenia odbiorcy tokena odpowiadają tożsamości docelowego serwera MCP
- **Autoryzacja oparta na roszczeniach**: Wdrażaj szczegółową autoryzację opartą na roszczeniach tokena i atrybutach użytkownika
- **Powiązanie tokenów**: Powiązuj tokeny z konkretnymi sesjami, użytkownikami lub urządzeniami tam, gdzie jest to stosowne

### 8. Bezpieczne zarządzanie sesjami
- **Kryptograficzne identyfikatory sesji**: Generuj identyfikatory sesji za pomocą kryptograficznie bezpiecznych generatorów liczb losowych (nieprzewidywalnych sekwencji)
- **Powiązanie z użytkownikiem**: Powiąż identyfikatory sesji z informacjami specyficznymi dla użytkownika, używając bezpiecznych formatów, np. `<user_id>:<session_id>`
- **Kontrola cyklu życia sesji**: Wdrażaj właściwe mechanizmy wygasania, rotacji i unieważniania sesji
- **Nagłówki bezpieczeństwa sesji**: Używaj odpowiednich nagłówków HTTP dla ochrony sesji

### 9. Specyficzne kontrole bezpieczeństwa dla AI
- **Obrona przed wstrzyknięciami w promptach**: Wdrażaj Microsoft Prompt Shields z technikami podświetlania, ograniczników i znakowania danych
- **Zapobieganie zatruciu narzędzi**: Weryfikuj metadane narzędzi, monitoruj dynamiczne zmiany i sprawdzaj integralność narzędzi
- **Walidacja wyjść modelu**: Skanuj wyjścia modelu pod kątem potencjalnego wycieku danych, szkodliwych treści lub naruszeń polityki bezpieczeństwa
- **Ochrona okna kontekstu**: Wdrażaj kontrole zapobiegające zatruciu i manipulacji okna kontekstu

### 10. Bezpieczeństwo wykonywania narzędzi
- **Izolacja wykonania**: Uruchamiaj wykonania narzędzi w konteneryzowanych, izolowanych środowiskach z limitami zasobów
- **Separacja uprawnień**: Wykonuj narzędzia z minimalnymi wymaganymi uprawnieniami i oddzielnymi kontami usługowymi
- **Izolacja sieciowa**: Wdrażaj segmentację sieci dla środowisk wykonawczych narzędzi
- **Monitorowanie wykonania**: Monitoruj wykonanie narzędzi pod kątem anomalii, zużycia zasobów i naruszeń bezpieczeństwa

### 11. Ciągła walidacja bezpieczeństwa
- **Automatyczne testy bezpieczeństwa**: Integruj testy bezpieczeństwa w pipeline CI/CD za pomocą narzędzi takich jak GitHub Advanced Security
- **Zarządzanie podatnościami**: Regularnie skanuj wszystkie zależności, w tym modele AI i usługi zewnętrzne
- **Testy penetracyjne**: Przeprowadzaj regularne oceny bezpieczeństwa ukierunkowane na implementacje MCP
- **Przeglądy kodu pod kątem bezpieczeństwa**: Wdrażaj obowiązkowe przeglądy bezpieczeństwa dla wszystkich zmian kodu związanych z MCP

### 12. Bezpieczeństwo łańcucha dostaw dla AI
- **Weryfikacja komponentów**: Weryfikuj pochodzenie, integralność i bezpieczeństwo wszystkich komponentów AI (modele, osadzenia, API)
- **Zarządzanie zależnościami**: Utrzymuj aktualne inwentarze wszystkich zależności oprogramowania i AI z monitorowaniem podatności
- **Zaufane repozytoria**: Korzystaj ze zweryfikowanych, zaufanych źródeł dla wszystkich modeli AI, bibliotek i narzędzi
- **Monitorowanie łańcucha dostaw**: Ciągle monitoruj kompromitacje dostawców usług AI i repozytoriów modeli

## Zaawansowane wzorce bezpieczeństwa

### Architektura Zero Trust dla MCP
- **Nigdy nie ufaj, zawsze weryfikuj**: Wdrażaj ciągłą weryfikację wszystkich uczestników MCP
- **Mikrosegmentacja**: Izoluj komponenty MCP za pomocą granularnych kontroli sieci i tożsamości
- **Dostęp warunkowy**: Wdrażaj kontrolę dostępu opartą na ryzyku, dostosowującą się do kontekstu i zachowania
- **Ciągła ocena ryzyka**: Dynamicznie oceniaj postawę bezpieczeństwa na podstawie aktualnych wskaźników zagrożeń

### Prywatność w implementacji AI
- **Minimalizacja danych**: Udostępniaj tylko minimalnie niezbędne dane dla każdej operacji MCP
- **Prywatność różnicowa**: Wdrażaj techniki ochrony prywatności dla przetwarzania danych wrażliwych
- **Szyfrowanie homomorficzne**: Używaj zaawansowanych technik szyfrowania do bezpiecznych obliczeń na zaszyfrowanych danych
- **Uczenie federacyjne**: Wdrażaj rozproszone podejścia do uczenia, które zachowują lokalność i prywatność danych

### Reakcja na incydenty dla systemów AI
- **Procedury specyficzne dla AI**: Opracuj procedury reagowania na incydenty dostosowane do zagrożeń specyficznych dla AI i MCP
- **Automatyczna reakcja**: Wdrażaj automatyczne ograniczanie i naprawę dla typowych incydentów bezpieczeństwa AI  
- **Możliwości śledcze**: Utrzymuj gotowość śledczą na wypadek kompromitacji systemów AI i wycieków danych
- **Procedury odzyskiwania**: Ustal procedury odzyskiwania po zatruciu modeli AI, atakach wstrzyknięcia promptów i kompromitacjach usług

## Zasoby i standardy wdrożeniowe

### Oficjalna dokumentacja MCP
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - Aktualna specyfikacja protokołu MCP
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - Oficjalne wytyczne bezpieczeństwa
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - Wzorce uwierzytelniania i autoryzacji
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - Wymagania dotyczące bezpieczeństwa warstwy transportowej

### Rozwiązania bezpieczeństwa Microsoft
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Zaawansowana ochrona przed wstrzyknięciami w promptach
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Kompleksowe filtrowanie treści AI
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - Zarządzanie tożsamością i dostępem w przedsiębiorstwie
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - Bezpieczne zarządzanie sekretami i poświadczeniami
- [GitHub Advanced Security](https://github.com/security/advanced-security) - Skanowanie bezpieczeństwa łańcucha dostaw i kodu

### Standardy i ramy bezpieczeństwa
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - Aktualne wytyczne bezpieczeństwa OAuth
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Ryzyka bezpieczeństwa aplikacji webowych
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - Specyficzne ryzyka bezpieczeństwa AI
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Kompleksowe zarządzanie ryzykiem AI
- [ISO 27001:2022](https://www.iso.org/standard/27001) - Systemy zarządzania bezpieczeństwem informacji

### Przewodniki i samouczki wdrożeniowe
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - Wzorce uwierzytelniania w przedsiębiorstwie
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - Integracja dostawcy tożsamości
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - Najlepsze praktyki zarządzania tokenami
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - Zaawansowane wzorce szyfrowania

### Zaawansowane zasoby bezpieczeństwa
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - Praktyki bezpiecznego rozwoju
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - Testowanie bezpieczeństwa specyficzne dla AI
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - Metodologia modelowania zagrożeń AI
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - Techniki ochrony prywatności AI

### Zgodność i zarządzanie
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - Zgodność z prywatnością w systemach AI
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - Odpowiedzialne wdrażanie AI
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - Kontrole bezpieczeństwa dla dostawców usług AI
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - Wymagania zgodności AI w opiece zdrowotnej

### DevSecOps i automatyzacja
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - Bezpieczne pipeline’y rozwoju AI
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - Ciągła walidacja bezpieczeństwa
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - Bezpieczne wdrażanie infrastruktury
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - Bezpieczeństwo konteneryzacji obciążeń AI

### Monitorowanie i reakcja na incydenty  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - Kompleksowe rozwiązania monitorujące
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - Procedury reagowania na incydenty specyficzne dla AI
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - Zarządzanie informacjami i zdarzeniami bezpieczeństwa
- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - Źródła informacji o zagrożeniach AI

## 🔄 Ciągłe doskonalenie

### Bądź na bieżąco z ewoluującymi standardami
- **Aktualizacje specyfikacji MCP**: Monitoruj oficjalne zmiany specyfikacji MCP i komunikaty bezpieczeństwa
- **Wywiad o zagrożeniach**: Subskrybuj kanały informacji o zagrożeniach bezpieczeństwa AI i bazy podatności  
- **Zaangażowanie społeczności**: Uczestnicz w dyskusjach i grupach roboczych społeczności bezpieczeństwa MCP
- **Regularna ocena**: Przeprowadzaj kwartalne oceny postawy bezpieczeństwa i aktualizuj praktyki odpowiednio

### Wkład w bezpieczeństwo MCP
- **Badania bezpieczeństwa**: Wnoś wkład w badania bezpieczeństwa MCP i programy ujawniania podatności
- **Dzielenie się najlepszymi praktykami**: Dziel się implementacjami bezpieczeństwa i zdobytymi doświadczeniami ze społecznością
- **Standardowy rozwój**: Uczestniczyć w opracowywaniu specyfikacji MCP oraz tworzeniu standardów bezpieczeństwa  
- **Rozwój narzędzi**: Tworzyć i udostępniać narzędzia oraz biblioteki bezpieczeństwa dla ekosystemu MCP

---

*Ten dokument odzwierciedla najlepsze praktyki bezpieczeństwa MCP na dzień 18 grudnia 2025 roku, opierając się na Specyfikacji MCP 2025-11-25. Praktyki bezpieczeństwa powinny być regularnie przeglądane i aktualizowane wraz z rozwojem protokołu i krajobrazu zagrożeń.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->