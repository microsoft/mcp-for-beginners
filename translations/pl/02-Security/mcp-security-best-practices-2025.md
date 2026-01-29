# Najlepsze praktyki bezpieczeństwa MCP – aktualizacja grudzień 2025

> **Ważne**: Ten dokument odzwierciedla najnowsze wymagania bezpieczeństwa [specyfikacji MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) oraz oficjalne [Najlepsze praktyki bezpieczeństwa MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices). Zawsze odwołuj się do aktualnej specyfikacji, aby uzyskać najnowsze wytyczne.

## Podstawowe praktyki bezpieczeństwa dla implementacji MCP

Model Context Protocol wprowadza unikalne wyzwania bezpieczeństwa wykraczające poza tradycyjne zabezpieczenia oprogramowania. Praktyki te dotyczą zarówno podstawowych wymagań bezpieczeństwa, jak i specyficznych zagrożeń MCP, w tym wstrzykiwania promptów, zatruwania narzędzi, przechwytywania sesji, problemów z „confused deputy” oraz podatności na przekazywanie tokenów.

### **OBOWIĄZKOWE wymagania bezpieczeństwa**

**Krytyczne wymagania ze specyfikacji MCP:**

### **OBOWIĄZKOWE wymagania bezpieczeństwa**

**Krytyczne wymagania ze specyfikacji MCP:**

> **NIE WOLNO**: Serwery MCP **NIE WOLNO** akceptować żadnych tokenów, które nie zostały wyraźnie wydane dla serwera MCP  
>  
> **WOLNO**: Serwery MCP implementujące autoryzację **MUSZĄ** weryfikować WSZYSTKIE przychodzące żądania  
>  
> **NIE WOLNO**: Serwery MCP **NIE WOLNO** używać sesji do uwierzytelniania  
>  
> **WOLNO**: Serwery proxy MCP używające statycznych identyfikatorów klienta **MUSZĄ** uzyskać zgodę użytkownika dla każdego dynamicznie zarejestrowanego klienta

---

## 1. **Bezpieczeństwo tokenów i uwierzytelnianie**

**Kontrole uwierzytelniania i autoryzacji:**  
   - **Rygorystyczna weryfikacja autoryzacji**: Przeprowadzaj kompleksowe audyty logiki autoryzacji serwera MCP, aby zapewnić dostęp tylko dla zamierzonych użytkowników i klientów  
   - **Integracja z zewnętrznymi dostawcami tożsamości**: Korzystaj z uznanych dostawców tożsamości, takich jak Microsoft Entra ID, zamiast implementować własne uwierzytelnianie  
   - **Weryfikacja odbiorcy tokena**: Zawsze sprawdzaj, czy tokeny zostały wyraźnie wydane dla Twojego serwera MCP – nigdy nie akceptuj tokenów pochodzących z wyższych warstw  
   - **Prawidłowy cykl życia tokenów**: Wdrażaj bezpieczną rotację tokenów, polityki wygasania oraz zapobiegaj atakom powtórzeniowym tokenów

**Chronione przechowywanie tokenów:**  
   - Używaj Azure Key Vault lub podobnych bezpiecznych magazynów poświadczeń dla wszystkich sekretów  
   - Wdrażaj szyfrowanie tokenów zarówno w spoczynku, jak i podczas transmisji  
   - Regularna rotacja poświadczeń i monitorowanie nieautoryzowanego dostępu

## 2. **Zarządzanie sesjami i bezpieczeństwo transportu**

**Bezpieczne praktyki sesji:**  
   - **Kryptograficznie bezpieczne identyfikatory sesji**: Używaj bezpiecznych, niedeterministycznych identyfikatorów sesji generowanych za pomocą bezpiecznych generatorów liczb losowych  
   - **Powiązanie z użytkownikiem**: Powiąż identyfikatory sesji z tożsamościami użytkowników, stosując formaty takie jak `<user_id>:<session_id>`, aby zapobiec nadużyciom sesji między użytkownikami  
   - **Zarządzanie cyklem życia sesji**: Wdrażaj odpowiednie wygasanie, rotację i unieważnianie, aby ograniczyć okna podatności  
   - **Wymuszanie HTTPS/TLS**: Obowiązkowe HTTPS dla całej komunikacji, aby zapobiec przechwytywaniu identyfikatorów sesji

**Bezpieczeństwo warstwy transportowej:**  
   - Konfiguruj TLS 1.3 tam, gdzie to możliwe, z odpowiednim zarządzaniem certyfikatami  
   - Wdrażaj pinning certyfikatów dla krytycznych połączeń  
   - Regularna rotacja certyfikatów i weryfikacja ich ważności

## 3. **Ochrona przed zagrożeniami specyficznymi dla AI** 🤖

**Obrona przed wstrzykiwaniem promptów:**  
   - **Microsoft Prompt Shields**: Wdrażaj AI Prompt Shields do zaawansowanego wykrywania i filtrowania złośliwych instrukcji  
   - **Sanityzacja wejścia**: Waliduj i oczyszczaj wszystkie dane wejściowe, aby zapobiec atakom wstrzykiwania i problemom „confused deputy”  
   - **Granice treści**: Używaj systemów delimiterów i oznaczania danych, aby rozróżnić zaufane instrukcje od treści zewnętrznych

**Zapobieganie zatruwaniu narzędzi:**  
   - **Weryfikacja metadanych narzędzi**: Wdrażaj kontrole integralności definicji narzędzi i monitoruj nieoczekiwane zmiany  
   - **Monitorowanie narzędzi w czasie rzeczywistym**: Obserwuj zachowanie podczas działania i ustawiaj alerty na nieoczekiwane wzorce wykonania  
   - **Procesy zatwierdzania**: Wymagaj wyraźnej zgody użytkownika na modyfikacje narzędzi i zmiany ich możliwości

## 4. **Kontrola dostępu i uprawnienia**

**Zasada najmniejszych uprawnień:**  
   - Przyznawaj serwerom MCP tylko minimalne uprawnienia niezbędne do zamierzonej funkcjonalności  
   - Wdrażaj kontrolę dostępu opartą na rolach (RBAC) z precyzyjnymi uprawnieniami  
   - Regularne przeglądy uprawnień i ciągłe monitorowanie eskalacji uprawnień

**Kontrole uprawnień w czasie działania:**  
   - Stosuj limity zasobów, aby zapobiec atakom wyczerpania zasobów  
   - Używaj izolacji kontenerów dla środowisk wykonawczych narzędzi  
   - Wdrażaj dostęp just-in-time dla funkcji administracyjnych

## 5. **Bezpieczeństwo treści i monitorowanie**

**Implementacja bezpieczeństwa treści:**  
   - **Integracja Azure Content Safety**: Używaj Azure Content Safety do wykrywania szkodliwych treści, prób jailbreak i naruszeń polityk  
   - **Analiza zachowań**: Wdrażaj monitorowanie zachowań w czasie działania, aby wykrywać anomalie w działaniu serwera MCP i narzędzi  
   - **Kompleksowe logowanie**: Rejestruj wszystkie próby uwierzytelniania, wywołania narzędzi i zdarzenia bezpieczeństwa z bezpiecznym, odpornym na manipulacje magazynem

**Ciągłe monitorowanie:**  
   - Alerty w czasie rzeczywistym na podejrzane wzorce i nieautoryzowane próby dostępu  
   - Integracja z systemami SIEM dla scentralizowanego zarządzania zdarzeniami bezpieczeństwa  
   - Regularne audyty bezpieczeństwa i testy penetracyjne implementacji MCP

## 6. **Bezpieczeństwo łańcucha dostaw**

**Weryfikacja komponentów:**  
   - **Skanowanie zależności**: Używaj automatycznego skanowania podatności dla wszystkich zależności oprogramowania i komponentów AI  
   - **Weryfikacja pochodzenia**: Sprawdzaj pochodzenie, licencjonowanie i integralność modeli, źródeł danych oraz usług zewnętrznych  
   - **Podpisane pakiety**: Używaj kryptograficznie podpisanych pakietów i weryfikuj podpisy przed wdrożeniem

**Bezpieczny pipeline rozwoju:**  
   - **GitHub Advanced Security**: Wdrażaj skanowanie sekretów, analizę zależności i statyczną analizę CodeQL  
   - **Bezpieczeństwo CI/CD**: Integruj walidację bezpieczeństwa w całym zautomatyzowanym pipeline wdrożeniowym  
   - **Integralność artefaktów**: Wdrażaj kryptograficzną weryfikację wdrażanych artefaktów i konfiguracji

## 7. **Bezpieczeństwo OAuth i zapobieganie atakom confused deputy**

**Implementacja OAuth 2.1:**  
   - **Wdrożenie PKCE**: Używaj Proof Key for Code Exchange (PKCE) dla wszystkich żądań autoryzacji  
   - **Wyraźna zgoda**: Uzyskuj zgodę użytkownika dla każdego dynamicznie zarejestrowanego klienta, aby zapobiec atakom confused deputy  
   - **Weryfikacja URI przekierowania**: Wdrażaj ścisłą weryfikację URI przekierowania i identyfikatorów klientów

**Bezpieczeństwo proxy:**  
   - Zapobiegaj obejściu autoryzacji przez wykorzystanie statycznych identyfikatorów klienta  
   - Wdrażaj odpowiednie procesy zgody dla dostępu do API stron trzecich  
   - Monitoruj kradzież kodów autoryzacyjnych i nieautoryzowany dostęp do API

## 8. **Reakcja na incydenty i odzyskiwanie**

**Szybkie możliwości reakcji:**  
   - **Automatyczna reakcja**: Wdrażaj systemy automatycznej rotacji poświadczeń i ograniczania zagrożeń  
   - **Procedury rollback**: Możliwość szybkiego przywrócenia znanych, poprawnych konfiguracji i komponentów  
   - **Możliwości śledcze**: Szczegółowe ścieżki audytu i logowanie do badania incydentów

**Komunikacja i koordynacja:**  
   - Jasne procedury eskalacji incydentów bezpieczeństwa  
   - Integracja z zespołami reagowania na incydenty organizacji  
   - Regularne symulacje incydentów bezpieczeństwa i ćwiczenia tabletop

## 9. **Zgodność i zarządzanie**

**Zgodność regulacyjna:**  
   - Zapewnij, że implementacje MCP spełniają wymagania branżowe (GDPR, HIPAA, SOC 2)  
   - Wdrażaj klasyfikację danych i kontrole prywatności dla przetwarzania danych AI  
   - Utrzymuj kompleksową dokumentację do audytów zgodności

**Zarządzanie zmianami:**  
   - Formalne procesy przeglądu bezpieczeństwa dla wszystkich modyfikacji systemu MCP  
   - Kontrola wersji i procesy zatwierdzania zmian konfiguracji  
   - Regularne oceny zgodności i analiza luk

## 10. **Zaawansowane kontrole bezpieczeństwa**

**Architektura Zero Trust:**  
   - **Nigdy nie ufaj, zawsze weryfikuj**: Ciągła weryfikacja użytkowników, urządzeń i połączeń  
   - **Mikrosegmentacja**: Szczegółowe kontrole sieci izolujące poszczególne komponenty MCP  
   - **Dostęp warunkowy**: Kontrole dostępu oparte na ryzyku, dostosowujące się do aktualnego kontekstu i zachowania

**Ochrona aplikacji w czasie działania:**  
   - **Runtime Application Self-Protection (RASP)**: Wdrażaj techniki RASP do wykrywania zagrożeń w czasie rzeczywistym  
   - **Monitorowanie wydajności aplikacji**: Obserwuj anomalie wydajności mogące wskazywać na ataki  
   - **Dynamiczne polityki bezpieczeństwa**: Wdrażaj polityki bezpieczeństwa dostosowujące się do aktualnego krajobrazu zagrożeń

## 11. **Integracja z ekosystemem bezpieczeństwa Microsoft**

**Kompleksowe bezpieczeństwo Microsoft:**  
   - **Microsoft Defender for Cloud**: Zarządzanie postawą bezpieczeństwa chmury dla obciążeń MCP  
   - **Azure Sentinel**: Natywne w chmurze SIEM i SOAR do zaawansowanego wykrywania zagrożeń  
   - **Microsoft Purview**: Zarządzanie danymi i zgodność dla przepływów pracy AI i źródeł danych

**Zarządzanie tożsamością i dostępem:**  
   - **Microsoft Entra ID**: Zarządzanie tożsamością przedsiębiorstwa z politykami dostępu warunkowego  
   - **Privileged Identity Management (PIM)**: Dostęp just-in-time i procesy zatwierdzania dla funkcji administracyjnych  
   - **Ochrona tożsamości**: Dostęp warunkowy oparty na ryzyku i automatyczna reakcja na zagrożenia

## 12. **Ciągła ewolucja bezpieczeństwa**

**Bycie na bieżąco:**  
   - **Monitorowanie specyfikacji**: Regularne przeglądy aktualizacji specyfikacji MCP i zmian wytycznych bezpieczeństwa  
   - **Wywiad zagrożeń**: Integracja kanałów zagrożeń specyficznych dla AI i wskaźników kompromitacji  
   - **Zaangażowanie społeczności bezpieczeństwa**: Aktywny udział w społeczności bezpieczeństwa MCP i programach ujawniania podatności

**Adaptacyjne bezpieczeństwo:**  
   - **Bezpieczeństwo oparte na uczeniu maszynowym**: Wykorzystuj wykrywanie anomalii oparte na ML do identyfikacji nowych wzorców ataków  
   - **Predykcyjna analiza bezpieczeństwa**: Wdrażaj modele predykcyjne do proaktywnej identyfikacji zagrożeń  
   - **Automatyzacja bezpieczeństwa**: Automatyczne aktualizacje polityk bezpieczeństwa na podstawie wywiadu zagrożeń i zmian specyfikacji

---

## **Krytyczne zasoby bezpieczeństwa**

### **Oficjalna dokumentacja MCP**  
- [Specyfikacja MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [Najlepsze praktyki bezpieczeństwa MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [Specyfikacja autoryzacji MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)  

### **Rozwiązania bezpieczeństwa Microsoft**  
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)  
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)  
- [Bezpieczeństwo Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)  
- [GitHub Advanced Security](https://github.com/security/advanced-security)  

### **Standardy bezpieczeństwa**  
- [Najlepsze praktyki bezpieczeństwa OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP Top 10 dla dużych modeli językowych](https://genai.owasp.org/)  
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)  

### **Przewodniki implementacji**  
- [Azure API Management MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)  
- [Microsoft Entra ID z serwerami MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)  

---

> **Informacja o bezpieczeństwie**: Praktyki bezpieczeństwa MCP rozwijają się szybko. Zawsze weryfikuj je względem aktualnej [specyfikacji MCP](https://spec.modelcontextprotocol.io/) oraz [oficjalnej dokumentacji bezpieczeństwa](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) przed wdrożeniem.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->