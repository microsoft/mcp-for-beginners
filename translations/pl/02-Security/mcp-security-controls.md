# Kontrole Bezpieczeństwa MCP - Aktualizacja Wrzesień 2026

> **Obecny standard:** Ten dokument odzwierciedla
> [Specyfikację MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/)
> oraz oficjalne
> [Najlepsze Praktyki Bezpieczeństwa MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices).

Protokół Model Context (MCP) znacznie dojrzał, oferując rozszerzone kontrole bezpieczeństwa obejmujące zarówno tradycyjne zagrożenia dla oprogramowania, jak i specyficzne zagrożenia związane z AI. Ten dokument dostarcza kompleksowych kontroli bezpieczeństwa dla bezpiecznych implementacji MCP zgodnych z ramami OWASP MCP Top 10.

## 🏔️ Praktyczne Szkolenie z Bezpieczeństwa

Dla praktycznego, warsztatowego doświadczenia we wdrażaniu bezpieczeństwa, zalecamy **[Warsztaty MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** – kompleksową prowadzoną ekspedycję zabezpieczania serwerów MCP w Azure, korzystając z metody „podatność → atak → naprawa → walidacja”.

Wszystkie kontrole bezpieczeństwa w tym dokumencie są zgodne z **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)**, który dostarcza architektury referencyjne i wskazówki dotyczące implementacji specyficznych dla Azure dla zagrożeń OWASP MCP Top 10.

## **WYMAGANE Wymagania Bezpieczeństwa**

### **Krytyczne Zakazy ze Specyfikacji MCP:**

> **ZABRONIONE**: Serwery MCP **NIE MOGĄ** akceptować tokenów, które nie zostały wyraźnie wydane dla serwera MCP
>
> **ZAKAZANE**: Serwery MCP **NIE MOGĄ** używać sesji do uwierzytelniania  
>
> **WYMAGANE**: Serwery MCP implementujące autoryzację **MUSZĄ** weryfikować WSZYSTKIE przychodzące żądania
>
> **OBOWIĄZKOWE**: Serwery proxy MCP korzystające ze statycznego identyfikatora klienta strony trzeciej
> **MUSZĄ** uzyskać zgodę dla każdego klienta MCP przed przekazaniem autoryzacji

---

## 1. **Kontrole Uwierzytelniania i Autoryzacji**

### **Integracja z Zewnętrznym Dostawcą Tożsamości**

**Specyfikacja MCP `2026-07-28`** pozwala serwerom MCP delegować
uwierzytelnianie do zewnętrznych dostawców tożsamości. Autoryzacja dla transportów HTTP
jest oceniana na każde żądanie; lokalne serwery stdio pobierają poświadczenia
zamiast tego ze swojego środowiska.

**Zagrożenie MCP wg OWASP:** [MCP07 - Niewystarczające uwierzytelnianie i autoryzacja](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp07-authz/)

**Korzyści Bezpieczeństwa:**
1. **Eliminacja ryzyka niestandardowego uwierzytelniania**: Zmniejsza powierzchnię podatności przez unikanie niestandardowych implementacji uwierzytelniania
2. **Bezpieczeństwo klasy korporacyjnej**: Wykorzystuje sprawdzonych dostawców tożsamości, takich jak Microsoft Entra ID, z zaawansowanymi funkcjami bezpieczeństwa
3. **Centralne zarządzanie tożsamością**: Upraszcza zarządzanie cyklem życia użytkownika, kontrolę dostępu i audyty zgodności
4. **Uwierzytelnianie wieloskładnikowe**: Dziedziczy możliwości MFA od korporacyjnych dostawców tożsamości
5. **Polityki dostępu warunkowego**: Korzysta z kontroli dostępu opartej na ryzyku i adaptacyjnego uwierzytelniania

**Wymagania implementacyjne:**
- **Rejestracja klienta**: Preferowane dokumenty metadanych klienta lub
  wstępna rejestracja; używaj przestarzałej Dynamicznej Rejestracji Klienta tylko dla
  kompatybilności
- **Weryfikacja odbiorcy tokena**: Sprawdź, czy wszystkie tokeny są wyraźnie wydane dla serwera MCP
- **Weryfikacja wystawcy**: Potwierdź, że wystawca tokena odpowiada oczekiwanemu dostawcy tożsamości
- **Weryfikacja podpisu**: Kryptograficzna walidacja integralności tokena
- **Egzekwowanie wygaśnięcia**: Ścisłe egzekwowanie limitów czasu życia tokena
- **Weryfikacja zakresu**: Upewnij się, że tokeny zawierają odpowiednie uprawnienia do żądanych operacji

### **Bezpieczeństwo logiki autoryzacji**


**Kluczowe Kontrole:**
- **Kompleksowe Audyty Autoryzacji**: Regularne przeglądy bezpieczeństwa wszystkich punktów podejmowania decyzji autoryzacyjnych
- **Bezpieczne Domyślne Ustawienia**: Odrzucanie dostępu, gdy logika autoryzacji nie może podjąć jednoznacznej decyzji
- **Granice Uprawnień**: Wyraźne rozgraniczenie między różnymi poziomami uprawnień i dostępem do zasobów
- **Rejestrowanie Audytu**: Pełne rejestrowanie wszystkich decyzji autoryzacyjnych dla monitorowania bezpieczeństwa
- **Regularne Przeglądy Dostępu**: Okresowa weryfikacja uprawnień użytkowników i przypisań uprawnień

## 2. **Bezpieczeństwo Tokenów i Kontrole Anti-Passthrough**

**OWASP MCP Rozwiązany Ryzyko**: [MCP01 - Nieprawidłowe Zarządzanie Tokenami i Ujawnienie Sekretów](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp01-token-mismanagement/)

### **Zapobieganie Przekazywaniu Tokenów**

**Przekazywanie tokenów jest wyraźnie zabronione** w Specyfikacji Autoryzacji MCP ze względu na krytyczne ryzyka bezpieczeństwa:

**Rozwiązane Ryzyka Bezpieczeństwa:**
- **Omijanie Kontroli**: Pomija istotne zabezpieczenia, takie jak ograniczenia tempa, walidacja żądań i monitorowanie ruchu
- **Brak Odpowiedzialności**: Uniemożliwia identyfikację klienta, co niszczy ścieżki audytu i dochodzenia incydentów
- **Eksfiltracja przez Proxy**: Umożliwia złośliwym podmiotom używanie serwerów jako proxy do nieautoryzowanego dostępu do danych
- **Naruszenia Granicy Zaufania**: Podważa założenia o pochodzeniu tokenów w usługach downstream
- **Przemieszczanie się Poziome**: Skompromitowane tokeny w wielu usługach umożliwiają szerszą ekspansję ataku

**Kontrole Implementacji:**
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

### **Wzorce Bezpiecznego Zarządzania Tokenami**

**Najlepsze Praktyki:**
- **Tokeny o Krótkim Okresie Żywotności**: Minimalizacja czasu ekspozycji przez częste rotacje tokenów
- **Wydawanie Na Żądanie**: Wydawanie tokenów tylko wtedy, gdy są potrzebne do konkretnych operacji
- **Bezpieczne Przechowywanie**: Korzystanie ze sprzętowych modułów bezpieczeństwa (HSM) lub bezpiecznych sejfów kluczy
- **Powiązanie Tokenów**: Walidacja odbiorcy tokena i wystawcy dla przeznaczonego zasobu MCP,
  klienta i operacji
- **Monitorowanie i Alarmowanie**: Wykrywanie w czasie rzeczywistym nadużyć tokenów lub nieautoryzowanych wzorców dostępu

## 3. **Kontrole Bezpieczeństwa Stanu Aplikacji**

### **Zapobieganie Przejęciu Uchwyconego Stanu**

**Adresowane Wektory Ataku:**
- **Odgadywanie Uchwyconego Stanu**: Przewidywalne identyfikatory ujawniają stan innego wywołującego
- **Wielokrotne Użycie przez Różnych Użytkowników**: Skradziony uchwyt jest używany z inną tożsamością
- **Implicitna Autoryzacja**: Posiadanie uchwytu jest błędnie traktowane jako
  dowód dostępu

**Kontrole Uchwyconego Stanu:**

```yaml
State Handle Generation:
  randomness_source: "Cryptographically secure RNG"
  entropy_bits: 128 # Minimum recommended
  format: "Base64url encoded"
  predictability: "MUST be non-deterministic"

State Binding:
  user_binding: "Bind server-side to the authenticated principal"
  authorization: "Recheck on every request"
  client_input: "Never trust a client-supplied user ID"
  
State Lifecycle:
  expiration: "Configurable timeout policies"
  rotation: "After privilege escalation events"
  invalidation: "Immediate on security events"
  cleanup: "Automated expired state removal"
```

**Bezpieczeństwo Transportu:**
- **Wymuszanie HTTPS**: Wymaganie HTTPS dla zdalnego transportu HTTP
- **Obsługa Poświadczeń**: Wysyłanie i walidacja autoryzacji przy każdym żądaniu HTTP
- **Izolacja stdio**: Ochrona lokalnych serwerów stdio poprzez izolację procesów i
  kontrolę poświadczeń środowiskowych

### **Zagadnienia związane ze stanem (Stateful vs Stateless)**

MCP `2026-07-28` jest bezstanowe na warstwie protokołu. Aplikacje mogą nadal
utrzymywać stan, zwracając jawny uchwyt z jednego wywołania narzędzia i akceptując
go jako zwykły argument w kolejnych wywołaniach.

- Przechowywać stan niezależnie od jakiegokolwiek połączenia transportowego.
- Powiązywać uchwyty stanu z uwierzytelnionym podmiotem po stronie serwera.
- Traktować uchwyt jako nazwę, a nie jako poświadczenie posiadacza.
- Definiować zachowanie wygasania i odzyskiwania dla przeterminowanych uchwytów.

## 4. **Kontrole Bezpieczeństwa Specyficzne dla AI**

**OWASP MCP Rozwiązane Ryzyka**:

- [MCP06 - Subwersja przepływu intencji](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp06-prompt-injection/)
- [MCP03 - Zatrucie narzędzi](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp03-tool-poisoning/)
- [MCP05 - Wstrzyknięcie i wykonanie poleceń](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp05-command-injection/)

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

**Kontrole wdrożeniowe:**
- **Sanityzacja wejścia**: Kompleksowa walidacja i filtrowanie wszystkich danych wejściowych użytkownika
- **Definicja granic treści**: Jasne rozdzielenie instrukcji systemowych i zawartości użytkownika
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
- **Możliwości cofania**: Możliwość powrotu do poprzednich wersji narzędzi
- **Audyt zmian**: Pełna historia modyfikacji definicji narzędzi
- **Ocena ryzyka**: Automatyczna ocena stanu bezpieczeństwa narzędzi

## 5. **Zapobieganie atakom Confused Deputy**

### **Bezpieczeństwo proxy OAuth**

**Kontrole zapobiegające atakom:**
```yaml
Client Registration:
  preferred_methods:
    - "Pre-registration when client and server have an existing relationship"
    - "Client ID Metadata Documents for clients without prior registration"
  compatibility_fallback:
    - "Dynamic Client Registration only when CIMD is unavailable"
    - "Consent bypass prevention mechanisms"  
    - "Cookie-based consent validation"
    - "Redirect URI strict validation"
    
  authorization_flow:
    - "PKCE implementation (OAuth 2.1)"
    - "State parameter validation"
    - "Authorization code binding"
    - "Nonce verification for ID tokens"
```

**Wymagania wdrożeniowe:**
- **Rejestracja klienta**: Preferowana wstępna rejestracja lub dokumenty metadanych Client ID
  ; traktować dynamiczną rejestrację klienta jako opcję zapasową zgodności
- **Weryfikacja zgody użytkownika**: Proxy MCP używające statycznego identyfikatora klienta zewnętrznego
  muszą uzyskać zgodę dla każdego klienta przed przekazaniem autoryzacji
- **Weryfikacja URI przekierowania**: Ścisła walidacja docelowych miejsc przekierowania oparta na białej liście
- **Ochrona kodu autoryzacyjnego**: Krótkoterminowe kody z wymuszeniem jednokrotnego użycia
- **Weryfikacja tożsamości klienta**: Solidna walidacja poświadczeń i metadanych klienta

## 6. **Bezpieczeństwo wykonywania narzędzi**

### **Sandałowanie i izolacja**

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
- **Oddzielne konteksty procesów**: Każde wykonywanie narzędzia w odizolowanej przestrzeni procesów
- **Komunikacja międzyprocesowa**: Bezpieczne mechanizmy IPC z walidacją
- **Monitorowanie procesów**: Analiza zachowania w czasie rzeczywistym i wykrywanie anomalii
- **Egzekwowanie zasobów**: Twarde limity na CPU, pamięć i operacje I/O

### **Wdrażanie zasady najmniejszych uprawnień**

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

**Adresowany ryzyko OWASP MCP**: [MCP04 - Ataki na łańcuch dostaw oprogramowania i manipulacje zależnościami](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp04-supply-chain/)

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
- **Analiza zachowań**: Wykrywanie nietypowego zachowania zewnętrznych komponentów
- **Automatyczna reakcja**: Natychmiastowe powstrzymanie zagrożonych komponentów

## 8. **Kontrole monitorowania i wykrywania**

**Adresowany ryzyko OWASP MCP**: [MCP08 - Brak audytu i telemetrii](https://microsoft.github.io/mcp-azure-security-guide/mcp/mcp08-telemetry/)

### **Zarządzanie informacjami o bezpieczeństwie i zdarzeniami (SIEM)**

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
- **Analiza zachowań encji (EBA)**: Monitorowanie zachowań serwera MCP i narzędzi
- **Wykrywanie anomalii z użyciem uczenia maszynowego**: Wykrywanie zagrożeń bezpieczeństwa wspierane przez sztuczną inteligencję
- **Korelacja wywiadu zagrożeń**: Dopasowywanie zaobserwowanych działań do znanych wzorców ataków

## 9. **Reakcja na incydenty i odzyskiwanie**

### **Automatyczne zdolności reakcji**

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

### **Zdolności śledcze**

**Wsparcie dochodzeniowe:**
- **Zachowanie ścieżki audytu**: Niezmienialne logowanie z integralnością kryptograficzną
- **Zbieranie dowodów**: Automatyczne gromadzenie istotnych artefaktów bezpieczeństwa
- **Odtwarzanie osi czasu**: Szczegółowa sekwencja zdarzeń prowadzących do incydentów bezpieczeństwa
- **Ocena wpływu**: Ocena zakresu kompromitacji i ekspozycji danych

## **Kluczowe zasady architektury bezpieczeństwa**

### **Ochrona w głębi**
- **Wiele warstw bezpieczeństwa**: Brak pojedynczego punktu awarii w architekturze bezpieczeństwa
- **Kontrole redundantne**: Nakładające się środki bezpieczeństwa dla krytycznych funkcji
- **Mechanizmy bezpiecznego działania**: Bezpieczne domyślne ustawienia w przypadku błędów lub ataków

### **Wdrażanie Zero Trust**
- **Nigdy nie ufać, zawsze weryfikować**: Ciągła walidacja wszystkich podmiotów i żądań
- **Zasada najmniejszych uprawnień**: Minimalne prawa dostępu dla wszystkich komponentów
- **Mikrosegmentacja**: Szczegółowa kontrola dostępu i sieci

### **Ciągła ewolucja bezpieczeństwa**
- **Adaptacja do krajobrazu zagrożeń**: Regularne aktualizacje adresujące pojawiające się zagrożenia
- **Skuteczność kontroli bezpieczeństwa**: Stała ocena i ulepszanie środków kontroli
- **Zgodność ze specyfikacją**: Dopasowanie do ewoluujących standardów bezpieczeństwa MCP

---

## **Zasoby wdrożeniowe**

### **Oficjalna dokumentacja MCP**
- [Specyfikacja MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Najlepsze praktyki bezpieczeństwa MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Specyfikacja autoryzacji MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)

### **Zasoby bezpieczeństwa OWASP MCP**
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) - Kompleksowy OWASP MCP Top 10 z implementacją na Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Oficjalne ryzyka bezpieczeństwa OWASP MCP
- [Warsztaty MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktyczne szkolenia z bezpieczeństwa MCP na Azure

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

> **Ważne:** Te kontrole bezpieczeństwa odzwierciedlają Specyfikację MCP
> `2026-07-28`. Zawsze sprawdzaj w oparciu o
> [aktualną oficjalną dokumentację](https://modelcontextprotocol.io/specification/2026-07-28/)
> ponieważ standardy ciągle się rozwijają.

## Co dalej

- Powrót do: [Przegląd Modułu Bezpieczeństwa](./README.md)
- Kontynuuj do: [Moduł 3: Pierwsze kroki](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->