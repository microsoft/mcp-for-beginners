# Kontrole bezpieczeństwa MCP - aktualizacja grudzień 2025

> **Aktualny standard**: Dokument odzwierciedla wymagania bezpieczeństwa [specyfikacji MCP 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) oraz oficjalne [najlepsze praktyki bezpieczeństwa MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices).

Protokół Model Context (MCP) znacznie dojrzał, wprowadzając zaawansowane kontrole bezpieczeństwa obejmujące zarówno tradycyjne zagrożenia w oprogramowaniu, jak i specyficzne dla AI. Dokument ten przedstawia kompleksowe kontrole bezpieczeństwa dla bezpiecznych implementacji MCP na grudzień 2025.

## **OBOWIĄZKOWE wymagania bezpieczeństwa**

### **Krytyczne zakazy ze specyfikacji MCP:**

> **ZABRONIONE**: Serwery MCP **NIE MOGĄ** akceptować żadnych tokenów, które nie zostały wyraźnie wydane dla serwera MCP  
>
> **ZAKAZANE**: Serwery MCP **NIE MOGĄ** używać sesji do uwierzytelniania  
>
> **WYMAGANE**: Serwery MCP implementujące autoryzację **MUSZĄ** weryfikować WSZYSTKIE przychodzące żądania  
>
> **OBOWIĄZKOWE**: Serwery proxy MCP używające statycznych identyfikatorów klienta **MUSZĄ** uzyskać zgodę użytkownika dla każdego dynamicznie rejestrowanego klienta

---

## 1. **Kontrole uwierzytelniania i autoryzacji**

### **Integracja z zewnętrznym dostawcą tożsamości**

**Aktualny standard MCP (2025-06-18)** pozwala serwerom MCP delegować uwierzytelnianie do zewnętrznych dostawców tożsamości, co stanowi istotną poprawę bezpieczeństwa:

### **Integracja z zewnętrznym dostawcą tożsamości**

**Aktualny standard MCP (2025-11-25)** pozwala serwerom MCP delegować uwierzytelnianie do zewnętrznych dostawców tożsamości, co stanowi istotną poprawę bezpieczeństwa:

**Korzyści bezpieczeństwa:**
1. **Eliminacja ryzyka niestandardowego uwierzytelniania**: Zmniejsza powierzchnię podatności przez unikanie niestandardowych implementacji uwierzytelniania  
2. **Bezpieczeństwo klasy korporacyjnej**: Wykorzystuje uznanych dostawców tożsamości, takich jak Microsoft Entra ID, z zaawansowanymi funkcjami bezpieczeństwa  
3. **Centralne zarządzanie tożsamością**: Upraszcza zarządzanie cyklem życia użytkownika, kontrolę dostępu i audyt zgodności  
4. **Uwierzytelnianie wieloskładnikowe**: Dziedziczy możliwości MFA od korporacyjnych dostawców tożsamości  
5. **Polityki dostępu warunkowego**: Korzysta z kontroli dostępu opartej na ryzyku i adaptacyjnego uwierzytelniania  

**Wymagania implementacyjne:**
- **Weryfikacja odbiorcy tokena**: Sprawdzenie, czy wszystkie tokeny zostały wyraźnie wydane dla serwera MCP  
- **Weryfikacja wystawcy**: Potwierdzenie, że wystawca tokena odpowiada oczekiwanemu dostawcy tożsamości  
- **Weryfikacja podpisu**: Kryptograficzne potwierdzenie integralności tokena  
- **Egzekwowanie ważności**: Ścisłe przestrzeganie limitów czasu życia tokena  
- **Weryfikacja zakresu**: Zapewnienie, że tokeny zawierają odpowiednie uprawnienia do żądanych operacji  

### **Bezpieczeństwo logiki autoryzacji**

**Krytyczne kontrole:**
- **Kompleksowe audyty autoryzacji**: Regularne przeglądy bezpieczeństwa wszystkich punktów decyzyjnych autoryzacji  
- **Domyślne zachowanie bezpieczne**: Odrzucanie dostępu, gdy logika autoryzacji nie może podjąć jednoznacznej decyzji  
- **Granice uprawnień**: Wyraźne rozdzielenie poziomów uprawnień i dostępu do zasobów  
- **Rejestrowanie audytu**: Pełne logowanie wszystkich decyzji autoryzacyjnych do monitoringu bezpieczeństwa  
- **Regularne przeglądy dostępu**: Okresowa weryfikacja uprawnień użytkowników i przypisań przywilejów  

## 2. **Bezpieczeństwo tokenów i kontrole zapobiegające przekazywaniu tokenów**

### **Zapobieganie przekazywaniu tokenów**

**Przekazywanie tokenów jest wyraźnie zabronione** w specyfikacji autoryzacji MCP ze względu na krytyczne ryzyka bezpieczeństwa:

**Adresowane ryzyka bezpieczeństwa:**
- **Ominięcie kontroli**: Omija kluczowe kontrole bezpieczeństwa, takie jak ograniczanie liczby żądań, walidacja żądań i monitorowanie ruchu  
- **Brak odpowiedzialności**: Uniemożliwia identyfikację klienta, psując ścieżki audytu i dochodzenia incydentów  
- **Eksfiltracja przez proxy**: Umożliwia złośliwym aktorom używanie serwerów jako proxy do nieautoryzowanego dostępu do danych  
- **Naruszenia granic zaufania**: Łamie założenia zaufania usług downstream dotyczące pochodzenia tokenów  
- **Ruch boczny**: Kompromitowane tokeny w wielu usługach umożliwiają szerszą ekspansję ataku  

**Kontrole implementacyjne:**
```yaml
Token Validation Requirements:
  audience_validation: MANDATORY
  issuer_verification: MANDATORY  
  signature_check: MANDATORY
  expiration_enforcement: MANDATORY
  scope_validation: MANDATORY
  
Token Lifecycle Management:
  rotation_frequency: "Short-lived tokens preferred"
  secure_storage: "Azure Key Vault or equivalent"
  transmission_security: "TLS 1.3 minimum"
  replay_protection: "Implemented via nonce/timestamp"
```

### **Wzorce bezpiecznego zarządzania tokenami**

**Najlepsze praktyki:**
- **Tokeny krótkotrwałe**: Minimalizowanie okna ekspozycji przez częstą rotację tokenów  
- **Wydawanie na żądanie**: Wydawanie tokenów tylko wtedy, gdy są potrzebne do konkretnych operacji  
- **Bezpieczne przechowywanie**: Używanie modułów bezpieczeństwa sprzętowego (HSM) lub bezpiecznych skarbców kluczy  
- **Powiązanie tokenów**: Powiązanie tokenów z konkretnymi klientami, sesjami lub operacjami, jeśli to możliwe  
- **Monitorowanie i alertowanie**: Wykrywanie w czasie rzeczywistym nadużyć tokenów lub nieautoryzowanych wzorców dostępu  

## 3. **Kontrole bezpieczeństwa sesji**

### **Zapobieganie przejęciu sesji**

**Adresowane wektory ataku:**
- **Wstrzyknięcie promptu przejęcia sesji**: Złośliwe zdarzenia wstrzykiwane do współdzielonego stanu sesji  
- **Podszywanie się pod sesję**: Nieautoryzowane użycie skradzionych identyfikatorów sesji do ominięcia uwierzytelniania  
- **Ataki na wznawialne strumienie**: Wykorzystanie wznowienia zdarzeń wysyłanych przez serwer do wstrzykiwania złośliwej zawartości  

**Obowiązkowe kontrole sesji:**
```yaml
Session ID Generation:
  randomness_source: "Cryptographically secure RNG"
  entropy_bits: 128 # Minimum recommended
  format: "Base64url encoded"
  predictability: "MUST be non-deterministic"

Session Binding:
  user_binding: "REQUIRED - <user_id>:<session_id>"
  additional_identifiers: "Device fingerprint, IP validation"
  context_binding: "Request origin, user agent validation"
  
Session Lifecycle:
  expiration: "Configurable timeout policies"
  rotation: "After privilege escalation events"
  invalidation: "Immediate on security events"
  cleanup: "Automated expired session removal"
```

**Bezpieczeństwo transportu:**
- **Wymuszanie HTTPS**: Cała komunikacja sesji przez TLS 1.3  
- **Atrybuty bezpiecznych ciasteczek**: HttpOnly, Secure, SameSite=Strict  
- **Pinowanie certyfikatów**: Dla krytycznych połączeń, aby zapobiec atakom MITM  

### **Rozważania dotyczące stanowych i bezstanowych implementacji**

**Dla implementacji stanowych:**
- Współdzielony stan sesji wymaga dodatkowej ochrony przed atakami wstrzyknięcia  
- Zarządzanie sesją oparte na kolejkach wymaga weryfikacji integralności  
- Wiele instancji serwera wymaga bezpiecznej synchronizacji stanu sesji  

**Dla implementacji bezstanowych:**
- Zarządzanie sesją oparte na JWT lub podobnych tokenach  
- Kryptograficzna weryfikacja integralności stanu sesji  
- Zmniejszona powierzchnia ataku, ale wymaga solidnej walidacji tokenów  

## 4. **Specyficzne kontrole bezpieczeństwa AI**

### **Obrona przed wstrzyknięciem promptów**

**Integracja Microsoft Prompt Shields:**
```yaml
Detection Mechanisms:
  - "Advanced ML-based instruction detection"
  - "Contextual analysis of external content"
  - "Real-time threat pattern recognition"
  
Protection Techniques:
  - "Spotlighting trusted vs untrusted content"
  - "Delimiter systems for content boundaries"  
  - "Data marking for content source identification"
  
Integration Points:
  - "Azure Content Safety service"
  - "Real-time content filtering"
  - "Threat intelligence updates"
```

**Kontrole implementacyjne:**
- **Sanityzacja wejścia**: Kompleksowa walidacja i filtrowanie wszystkich danych wejściowych od użytkownika  
- **Definicja granic zawartości**: Wyraźne oddzielenie instrukcji systemowych od treści użytkownika  
- **Hierarchia instrukcji**: Właściwe reguły pierwszeństwa dla sprzecznych instrukcji  
- **Monitorowanie wyjścia**: Wykrywanie potencjalnie szkodliwych lub zmanipulowanych wyników  

### **Zapobieganie zatruciu narzędzi**

**Ramowy system bezpieczeństwa narzędzi:**
```yaml
Tool Definition Protection:
  validation:
    - "Schema validation against expected formats"
    - "Content analysis for malicious instructions" 
    - "Parameter injection detection"
    - "Hidden instruction identification"
  
  integrity_verification:
    - "Cryptographic hashing of tool definitions"
    - "Digital signatures for tool packages"
    - "Version control with change auditing"
    - "Tamper detection mechanisms"
  
  monitoring:
    - "Real-time change detection"
    - "Behavioral analysis of tool usage"
    - "Anomaly detection for execution patterns"
    - "Automated alerting for suspicious modifications"
```

**Dynamiczne zarządzanie narzędziami:**
- **Procesy zatwierdzania**: Wyraźna zgoda użytkownika na modyfikacje narzędzi  
- **Możliwości wycofania**: Możliwość powrotu do poprzednich wersji narzędzi  
- **Audyt zmian**: Pełna historia modyfikacji definicji narzędzi  
- **Ocena ryzyka**: Automatyczna ocena postawy bezpieczeństwa narzędzi  

## 5. **Zapobieganie atakom typu Confused Deputy**

### **Bezpieczeństwo proxy OAuth**

**Kontrole zapobiegające atakom:**
```yaml
Client Registration:
  static_client_protection:
    - "Explicit user consent for dynamic registration"
    - "Consent bypass prevention mechanisms"  
    - "Cookie-based consent validation"
    - "Redirect URI strict validation"
    
  authorization_flow:
    - "PKCE implementation (OAuth 2.1)"
    - "State parameter validation"
    - "Authorization code binding"
    - "Nonce verification for ID tokens"
```

**Wymagania implementacyjne:**
- **Weryfikacja zgody użytkownika**: Nigdy nie pomijać ekranów zgody dla dynamicznej rejestracji klienta  
- **Weryfikacja URI przekierowania**: Ścisła walidacja docelowych adresów przekierowań na podstawie białej listy  
- **Ochrona kodu autoryzacyjnego**: Kody krótkotrwałe z wymuszeniem jednokrotnego użycia  
- **Weryfikacja tożsamości klienta**: Solidna walidacja poświadczeń i metadanych klienta  

## 6. **Bezpieczeństwo wykonywania narzędzi**

### **Sandboxing i izolacja**

**Izolacja oparta na kontenerach:**
```yaml
Execution Environment:
  containerization: "Docker/Podman with security profiles"
  resource_limits:
    cpu: "Configurable CPU quotas"
    memory: "Memory usage restrictions"
    disk: "Storage access limitations"
    network: "Network policy enforcement"
  
  privilege_restrictions:
    user_context: "Non-root execution mandatory"
    capability_dropping: "Remove unnecessary Linux capabilities"
    syscall_filtering: "Seccomp profiles for syscall restriction"
    filesystem: "Read-only root with minimal writable areas"
```

**Izolacja procesów:**
- **Oddzielne konteksty procesów**: Każde wykonanie narzędzia w izolowanej przestrzeni procesowej  
- **Komunikacja międzyprocesowa**: Bezpieczne mechanizmy IPC z walidacją  
- **Monitorowanie procesów**: Analiza zachowania w czasie rzeczywistym i wykrywanie anomalii  
- **Egzekwowanie zasobów**: Twarde limity CPU, pamięci i operacji I/O  

### **Implementacja zasady najmniejszych uprawnień**

**Zarządzanie uprawnieniami:**
```yaml
Access Control:
  file_system:
    - "Minimal required directory access"
    - "Read-only access where possible"
    - "Temporary file cleanup automation"
    
  network_access:
    - "Explicit allowlist for external connections"
    - "DNS resolution restrictions" 
    - "Port access limitations"
    - "SSL/TLS certificate validation"
  
  system_resources:
    - "No administrative privilege elevation"
    - "Limited system call access"
    - "No hardware device access"
    - "Restricted environment variable access"
```

## 7. **Kontrole bezpieczeństwa łańcucha dostaw**

### **Weryfikacja zależności**

**Kompleksowe bezpieczeństwo komponentów:**
```yaml
Software Dependencies:
  scanning: 
    - "Automated vulnerability scanning (GitHub Advanced Security)"
    - "License compliance verification"
    - "Known vulnerability database checks"
    - "Malware detection and analysis"
  
  verification:
    - "Package signature verification"
    - "Checksum validation"
    - "Provenance attestation"
    - "Software Bill of Materials (SBOM)"

AI Components:
  model_verification:
    - "Model provenance validation"
    - "Training data source verification" 
    - "Model behavior testing"
    - "Adversarial robustness assessment"
  
  service_validation:
    - "Third-party API security assessment"
    - "Service level agreement review"
    - "Data handling compliance verification"
    - "Incident response capability evaluation"
```

### **Ciągłe monitorowanie**

**Wykrywanie zagrożeń w łańcuchu dostaw:**
- **Monitorowanie stanu zależności**: Ciągła ocena wszystkich zależności pod kątem problemów bezpieczeństwa  
- **Integracja wywiadu zagrożeń**: Aktualizacje w czasie rzeczywistym o pojawiających się zagrożeniach w łańcuchu dostaw  
- **Analiza zachowań**: Wykrywanie nietypowych zachowań w komponentach zewnętrznych  
- **Automatyczna reakcja**: Natychmiastowe ograniczanie skutków kompromitacji komponentów  

## 8. **Kontrole monitorowania i wykrywania**

### **System zarządzania informacjami i zdarzeniami bezpieczeństwa (SIEM)**

**Kompleksowa strategia logowania:**
```yaml
Authentication Events:
  - "All authentication attempts (success/failure)"
  - "Token issuance and validation events"
  - "Session creation, modification, termination"
  - "Authorization decisions and policy evaluations"

Tool Execution:
  - "Tool invocation details and parameters"
  - "Execution duration and resource usage"
  - "Output generation and content analysis"
  - "Error conditions and exception handling"

Security Events:
  - "Potential prompt injection attempts"
  - "Tool poisoning detection events"
  - "Session hijacking indicators"
  - "Unusual access patterns and anomalies"
```

### **Wykrywanie zagrożeń w czasie rzeczywistym**

**Analiza behawioralna:**
- **Analiza zachowań użytkowników (UBA)**: Wykrywanie nietypowych wzorców dostępu użytkowników  
- **Analiza zachowań podmiotów (EBA)**: Monitorowanie zachowań serwera MCP i narzędzi  
- **Wykrywanie anomalii z użyciem uczenia maszynowego**: Identyfikacja zagrożeń bezpieczeństwa wspomagana AI  
- **Korelacja wywiadu zagrożeń**: Dopasowywanie obserwowanych działań do znanych wzorców ataków  

## 9. **Reakcja na incydenty i odzyskiwanie**

### **Automatyczne możliwości reakcji**

**Natychmiastowe działania reakcyjne:**
```yaml
Threat Containment:
  session_management:
    - "Immediate session termination"
    - "Account lockout procedures"
    - "Access privilege revocation"
  
  system_isolation:
    - "Network segmentation activation"
    - "Service isolation protocols"
    - "Communication channel restriction"

Recovery Procedures:
  credential_rotation:
    - "Automated token refresh"
    - "API key regeneration"
    - "Certificate renewal"
  
  system_restoration:
    - "Clean state restoration"
    - "Configuration rollback"
    - "Service restart procedures"
```

### **Możliwości śledcze**

**Wsparcie dochodzeń:**
- **Zachowanie ścieżki audytu**: Niezmienne logowanie z kryptograficzną integralnością  
- **Zbieranie dowodów**: Automatyczne gromadzenie istotnych artefaktów bezpieczeństwa  
- **Rekonstrukcja osi czasu**: Szczegółowa sekwencja zdarzeń prowadzących do incydentów bezpieczeństwa  
- **Ocena wpływu**: Analiza zakresu kompromitacji i ujawnienia danych  

## **Kluczowe zasady architektury bezpieczeństwa**

### **Obrona w głąb**
- **Wielowarstwowe zabezpieczenia**: Brak pojedynczego punktu awarii w architekturze bezpieczeństwa  
- **Redundantne kontrole**: Nakładające się środki bezpieczeństwa dla krytycznych funkcji  
- **Mechanizmy bezpiecznego domyślnego działania**: Bezpieczne ustawienia domyślne w przypadku błędów lub ataków  

### **Implementacja Zero Trust**
- **Nigdy nie ufaj, zawsze weryfikuj**: Ciągła walidacja wszystkich podmiotów i żądań  
- **Zasada najmniejszych uprawnień**: Minimalne prawa dostępu dla wszystkich komponentów  
- **Mikrosegmentacja**: Szczegółowe kontrole sieci i dostępu  

### **Ciągła ewolucja bezpieczeństwa**
- **Adaptacja do krajobrazu zagrożeń**: Regularne aktualizacje odpowiadające nowym zagrożeniom  
- **Skuteczność kontroli bezpieczeństwa**: Stała ocena i ulepszanie środków ochrony  
- **Zgodność ze specyfikacją**: Dopasowanie do ewoluujących standardów bezpieczeństwa MCP  

---

## **Zasoby implementacyjne**

### **Oficjalna dokumentacja MCP**
- [Specyfikacja MCP (2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Najlepsze praktyki bezpieczeństwa MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [Specyfikacja autoryzacji MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### **Rozwiązania bezpieczeństwa Microsoft**
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)

### **Standardy bezpieczeństwa**
- [Najlepsze praktyki bezpieczeństwa OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 dla dużych modeli językowych](https://genai.owasp.org/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

> **Ważne**: Te kontrole bezpieczeństwa odzwierciedlają aktualną specyfikację MCP (2025-06-18). Zawsze weryfikuj w oparciu o najnowszą [oficjalną dokumentację](https://spec.modelcontextprotocol.io/), ponieważ standardy szybko się rozwijają.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiarygodne i autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->