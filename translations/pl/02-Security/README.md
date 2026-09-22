# MCP Security: Kompleksowa ochrona systemów AI

[![MCP Security Best Practices](../../../translated_images/pl/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Kliknij powyższy obraz, aby obejrzeć film z tej lekcji)_

Bezpieczeństwo jest podstawą projektowania systemów AI, dlatego traktujemy je jako naszą drugą sekcję. Jest to zgodne z zasadą Microsoftu **Secure by Design** z inicjatywy [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Protokół Kontekstu Modelu (MCP) wprowadza potężne nowe możliwości do aplikacji napędzanych sztuczną inteligencją, jednocześnie stawiając unikalne wyzwania związane z bezpieczeństwem, które wykraczają poza tradycyjne zagrożenia dla oprogramowania. Systemy MCP muszą radzić sobie zarówno z ugruntowanymi zagrożeniami bezpieczeństwa (bezpieczne kodowanie, zasada najmniejszych uprawnień, bezpieczeństwo w łańcuchu dostaw), jak i nowymi specyficznymi dla AI zagrożeniami, w tym wstrzyknięciem promptów, zatruwaniem narzędzi, przechwyceniem sesji, atakami typu confused deputy, lukami w przekazywaniu tokenów oraz dynamiczną modyfikacją uprawnień.

Ta lekcja omawia najważniejsze zagrożenia bezpieczeństwa w implementacjach MCP — obejmujące uwierzytelnianie, autoryzację, nadmierne uprawnienia, pośrednie wstrzyknięcie promptów, bezpieczeństwo sesji, problemy typu confused deputy, zarządzanie tokenami oraz podatności w łańcuchu dostaw. Poznasz praktyczne rozwiązania i najlepsze praktyki, które pomogą ograniczyć te zagrożenia, korzystając przy tym z rozwiązań Microsoft takich jak Prompt Shields, Azure Content Safety oraz GitHub Advanced Security, aby wzmocnić wdrożenie MCP.

## Cele nauki

Po zakończeniu tej lekcji będziesz potrafił:

- **Zidentyfikować specyficzne zagrożenia MCP**: Rozpoznać unikalne ryzyka bezpieczeństwa w systemach MCP, w tym wstrzyknięcie promptów, zatruwanie narzędzi, nadmierne uprawnienia, przechwycenie sesji, problemy typu confused deputy, luki w przekazywaniu tokenów oraz zagrożenia w łańcuchu dostaw
- **Zastosować zabezpieczenia**: Wdrożyć skuteczne środki zaradcze, w tym solidne uwierzytelnianie, dostęp na zasadzie najmniejszych uprawnień, bezpieczne zarządzanie tokenami, kontrolę bezpieczeństwa sesji oraz weryfikację łańcucha dostaw
- **Wykorzystać rozwiązania Microsoft**: Zrozumieć i wdrożyć Microsoft Prompt Shields, Azure Content Safety oraz GitHub Advanced Security dla ochrony obciążeń MCP
- **Zweryfikować bezpieczeństwo narzędzi**: Docenić znaczenie walidacji metadanych narzędzi, monitorowania dynamicznych zmian oraz obrony przed pośrednimi atakami wstrzyknięcia promptów
- **Zintegrować najlepsze praktyki**: Połączyć ustalone podstawy bezpieczeństwa (bezpieczne kodowanie, wzmacnianie serwerów, zero trust) ze specyficznymi kontrolami MCP dla kompleksowej ochrony

# Architektura bezpieczeństwa MCP i kontrole

Nowoczesne implementacje MCP wymagają wielowarstwowych podejść do bezpieczeństwa, które adresują zarówno tradycyjne zabezpieczenia oprogramowania, jak i specyficzne dla AI zagrożenia. Dynamicznie rozwijająca się specyfikacja MCP stale doskonali mechanizmy bezpieczeństwa, umożliwiając lepszą integrację z architekturami bezpieczeństwa przedsiębiorstw i ustalonymi najlepszymi praktykami.

Badania z [Microsoft Digital Defense Report](https://aka.ms/mddr) pokazują, że **98% zgłoszonych naruszeń można byłoby zapobiec dzięki solidnej higienie bezpieczeństwa**. Najskuteczniejsza strategia ochrony łączy podstawowe praktyki bezpieczeństwa z kontrolami specyficznymi dla MCP — sprawdzone środki bezpieczeństwa bazowe pozostają najistotniejsze dla ograniczenia ogólnego ryzyka.

## Aktualny krajobraz bezpieczeństwa

> **Uwaga:** Ten rozdział łączy ustalone kontrole MCP z
> aktualnymi wytycznymi autoryzacji **MCP Specification 2026-07-28**. Zawsze odwołuj się
> do bieżącej [specyfikacji MCP](https://modelcontextprotocol.io/specification/2026-07-28/),
> [repozytorium MCP na GitHub](https://github.com/modelcontextprotocol) oraz
> [dokumentacji najlepszych praktyk bezpieczeństwa](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> podczas implementacji kodu wrażliwego na bezpieczeństwo.

> **Aktualizacja autoryzacji:** MCP `2026-07-28` wymaga od klientów walidacji
> parametru `iss` w odpowiedziach autoryzacyjnych (RFC 9207) oraz powiązania
> zarejestrowanych poświadczeń z serwerem autoryzacji, który je wydał. Dynamiczna rejestracja klientów
> jest przestarzała; nowe implementacje powinny korzystać z dokumentów metadanych identyfikatorów klienta.
> Zobacz [Co się zmieniło w MCP: Specyfikacja 2026-07-28](../01-CoreConcepts/mcp-2026-07-28.md)
> dla pełnej listy zmian autoryzacyjnych.

## 🏔️ Warsztaty MCP Security Summit (Sherpa)

Dla **praktycznego szkolenia z bezpieczeństwa** gorąco polecamy **Warsztaty MCP Security Summit** (Sherpa) — kompleksową prowadzoną wyprawę zabezpieczania serwerów MCP w Microsoft Azure.

### Przegląd warsztatów

[MCP Security Summit Workshop](https://azure-samples.github.io/sherpa/) oferuje praktyczne, wykonalne szkolenie bezpieczeństwa oparte na sprawdzonej metodologii "wrażliwość → eksploatacja → naprawa → weryfikacja". Podczas warsztatów:

- **Ucz się przez łamanie**: Doświadczaj podatności bezpośrednio, wykorzystując celowo niebezpieczne serwery
- **Wykorzystuj natywne zabezpieczenia Azure**: Korzystaj z Azure Entra ID, Key Vault, API Management oraz AI Content Safety
- **Stosuj obronę w głąb**: Przechodzisz przez kolejne obozy, budując kompleksowe warstwy bezpieczeństwa
- **Zgodność z OWASP**: Każda technika odpowiada [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- **Zdobądź kod produkcyjny**: Otrzymujesz działające, przetestowane implementacje

### Trasa wyprawy

| Obóz | Temat | Omówione ryzyka OWASP |
|------|-------|---------------------|
| **Obóz Główny** | Podstawy MCP & podatności uwierzytelniania | MCP01, MCP07 |
| **Obóz 1: Tożsamość** | OAuth 2.1, Managed Identity Azure, Key Vault | MCP01, MCP02, MCP07 |
| **Obóz 2: Brama** | API Management, prywatne punkty końcowe, zarządzanie | MCP02, MCP06, MCP07, MCP09 |
| **Obóz 3: Bezpieczeństwo We/Wy** | Wstrzyknięcie promptów, ochrona danych osobowych, bezpieczeństwo treści | MCP03, MCP05, MCP06, MCP10 |
| **Obóz 4: Monitorowanie** | Log Analytics, pulpity, wykrywanie zagrożeń | MCP04, MCP08 |
| **Szczyt** | Test integracyjny Red Team / Blue Team | Wszystkie |

**Zacznij tutaj**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## OWASP MCP Top 10 zagrożeń bezpieczeństwa

[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) szczegółowo opisuje dziesięć najważniejszych zagrożeń bezpieczeństwa dla implementacji MCP:

| Ryzyko | Opis | Mitigacja Azure |
|------|-------------|------------------|
| **MCP01** | Niepoprawne zarządzanie tokenami & ujawnienie sekretów | Azure Key Vault, Managed Identity |
| **MCP02** | Eskalacja uprawnień przez rozszerzanie zakresów | RBAC, warunkowy dostęp |
| **MCP03** | Zatruwanie narzędzi | Walidacja narzędzi, weryfikacja integralności |
| **MCP04** | Ataki na łańcuch dostaw & manipulacja zależnościami | GitHub Advanced Security, skanowanie zależności |
| **MCP05** | Wstrzykiwanie i wykonywanie poleceń | Walidacja wejścia, sandboxing |
| **MCP06** | Podważanie przepływu intencji | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Niewystarczające uwierzytelnianie & autoryzacja | Azure Entra ID, OAuth 2.1 z PKCE |
| **MCP08** | Brak audytu i telemetrii | Azure Monitor, Application Insights |
| **MCP09** | Cienie serwerów MCP | Governance API Center, izolacja sieciowa |
| **MCP10** | Wstrzyknięcie kontekstu & nadmierne udostępnianie | Klasyfikacja danych, minimalna ekspozycja |

### Ewolucja uwierzytelniania MCP

Specyfikacja MCP znacząco zmieniła podejście do uwierzytelniania i autoryzacji:

- **Początkowe podejście**: Wczesne specyfikacje wymagały implementacji własnych serwerów uwierzytelniania, przy czym serwery MCP działały jako serwery autoryzacyjne OAuth 2.0 zarządzające bezpośrednio uwierzytelnianiem użytkowników
- **Aktualny standard (`2026-07-28`)**: Serwery MCP mogą delegować uwierzytelnianie
  do zewnętrznych dostawców tożsamości, takich jak Microsoft Entra ID. Klienci muszą również
  stosować aktualne wymagania walidacji wystawcy i powiązania poświadczeń.
- **Warstwa transportowa**: Zwiększone wsparcie dla bezpiecznych mechanizmów transportu z odpowiednimi wzorcami uwierzytelniania zarówno dla połączeń lokalnych (STDIO), jak i zdalnych (Streamable HTTP)

## Bezpieczeństwo uwierzytelniania i autoryzacji

### Aktualne wyzwania w bezpieczeństwie

Współczesne implementacje MCP stają przed wieloma wyzwaniami w zakresie uwierzytelniania i autoryzacji:

### Zagrożenia i wektory ataku

- **Błędna logika autoryzacji**: Nieprawidłowa implementacja autoryzacji w serwerach MCP może ujawnić dane wrażliwe i niepoprawnie zastosować kontrole dostępu
- **Kompromitacja tokenów OAuth**: Kradzież tokenów lokalnego serwera MCP umożliwia atakującym podszywanie się pod serwery i dostęp do usług downstream
- **Luki w przekazywaniu tokenów**: Niewłaściwe zarządzanie tokenami tworzy obejścia kontroli zabezpieczeń i luki odpowiedzialności
- **Nadmierne uprawnienia**: Serwery MCP z nadmiernymi uprawnieniami naruszają zasadę najmniejszych uprawnień i rozszerzają powierzchnie ataku

#### Przekazywanie tokenów: krytyczny antywzorzec

**Przekazywanie tokenów jest wyraźnie zakazane** w aktualnej specyfikacji autoryzacji MCP ze względu na poważne implikacje bezpieczeństwa:

##### Obejście kontroli zabezpieczeń
- Serwery MCP i API downstream implementują kluczowe zabezpieczenia (ograniczenia tempa, walidacja żądań, monitorowanie ruchu), które opierają się na prawidłowej walidacji tokenów
- Bezpośrednie użycie tokenów klienta do API pomija te istotne zabezpieczenia, osłabiając architekturę bezpieczeństwa

##### Problemy z odpowiedzialnością i audytem  
- Serwery MCP nie mogą rozróżnić klientów używających tokenów wydanych upstream, co niweczy ślady audytu
- Logi serwerów zasobów downstream pokazują mylące źródła żądań zamiast faktycznych pośredników MCP
- Badanie incydentów i audyty zgodności stają się znacznie trudniejsze

##### Ryzyko wycieku danych
- Niewalidowane roszczenia tokenów umożliwiają złośliwym aktorom ze skradzionymi tokenami korzystanie z serwerów MCP jako proxy do wycieku danych
- Naruszenia granic zaufania pozwalają na nieautoryzowany dostęp, omijając zamierzone zabezpieczenia

##### Wektory ataków wielousługowych
- Kompromitowane tokeny akceptowane przez wiele usług umożliwiają poruszanie się boczne po powiązanych systemach
- Założenia zaufania między usługami mogą być naruszone, gdy pochodzenie tokenów nie może być zweryfikowane

### Kontrole bezpieczeństwa i środki zaradcze

**Krytyczne wymagania bezpieczeństwa:**

> **OBOWIĄZKOWE**: Serwery MCP **NIE MOGĄ** akceptować żadnych tokenów, które nie zostały wyraźnie wydane dla konkretnego serwera MCP

#### Kontrole uwierzytelniania i autoryzacji

- **Skrupulatna weryfikacja autoryzacji**: Przeprowadzaj kompleksowe audyty logiki autoryzacji serwerów MCP, aby upewnić się, że tylko zamierzeni użytkownicy i klienci mają dostęp do wrażliwych zasobów
  - **Przewodnik wdrożenia**: [Azure API Management jako brama uwierzytelniania dla serwerów MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integracja tożsamości**: [Używanie Microsoft Entra ID do uwierzytelniania serwerów MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Bezpieczne zarządzanie tokenami**: Wdróż [praktyki Microsoft dotyczące walidacji tokenów i cyklu życia](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Waliduj roszczenia audience tokena, aby pasowały do tożsamości serwera MCP
  - Wdróż odpowiednie polityki rotacji i wygaszania tokenów
  - Zapobiegaj atakom powtórnego użycia tokenów oraz nieautoryzowanemu użyciu

- **Chronione przechowywanie tokenów**: Zabezpiecz przechowywanie tokenów szyfrowaniem zarówno w stanie spoczynku, jak i podczas transmisji
  - **Najlepsze praktyki**: [Zasady bezpiecznego przechowywania i szyfrowania tokenów](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementacja kontroli dostępu

- **Zasada najmniejszych uprawnień**: Nadaj serwerom MCP wyłącznie minimalne uprawnienia niezbędne do zamierzonej funkcjonalności
  - Regularne przeglądy i aktualizacje uprawnień zapobiegające eskalacji uprawnień
  - **Dokumentacja Microsoft**: [Bezpieczny dostęp z minimalnymi uprawnieniami](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Kontrola dostępu oparta na rolach (RBAC)**: Wdrażaj precyzyjne przypisywanie ról
  - Ograniczaj zakres ról do konkretnych zasobów i działań
  - Unikaj szerokich lub niepotrzebnych uprawnień rozszerzających powierzchnię ataku

- **Ciągły monitoring uprawnień**: Wprowadź stały audyt i monitorowanie dostępu
  - Monitoruj wzorce użycia uprawnień pod kątem anomalii
  - Szybko usuń nadmierne lub nieużywane uprawnienia

## Specyficzne zagrożenia bezpieczeństwa dla AI

### Ataki polegające na wstrzyknięciu promptów i manipulacji narzędziami

Nowoczesne implementacje MCP stają twarzą w twarz ze złożonymi wektorami ataków specyficznych dla AI, których tradycyjne środki bezpieczeństwa nie potrafią w pełni adresować:

#### **Pośrednie wstrzyknięcie promptów (Cross-Domain Prompt Injection)**

**Pośrednie wstrzyknięcie promptów** jest jednym z najbardziej krytycznych podatności w systemach AI opartych na MCP. Atakujący wprowadzają złośliwe instrukcje w treściach zewnętrznych — dokumentach, stronach internetowych, wiadomościach e-mail lub źródłach danych — które systemy AI następnie traktują jako prawidłowe polecenia.

**Scenariusze ataku:**
- **Wstrzyknięcie oparte na dokumentach**: Złośliwe instrukcje ukryte w przetwarzanych dokumentach, wywołujące niezamierzone działania AI
- **Wykorzystanie treści internetowych**: Zhakowane strony internetowe zawierające osadzone prompt-y manipulujące zachowaniem AI podczas scrapowania
- **Ataki przez e-mail**: Złośliwe prompt-y w e-mailach, które powodują wyciek informacji lub nieautoryzowane działania asystentów AI
- **Zanieczyszczenie źródeł danych**: Skraje bazy danych lub API dostarczające skażone treści systemom AI

**Rzeczywisty wpływ**: Te ataki mogą prowadzić do wycieku danych, naruszenia prywatności, generowania szkodliwych treści oraz manipulacji interakcjami użytkowników. Szczegółową analizę znajdziesz w [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/pl/prompt-injection.ed9fbfde297ca877.webp)

#### **Ataki zatruwania narzędzi**

**Zatruwanie narzędzi** koncentruje się na metadanych definiujących narzędzia MCP, wykorzystując sposób, w jaki modele językowe (LLM) interpretują opisy narzędzi i parametry podejmując decyzje o wykonaniu.

**Mechanizmy ataku:**
- **Manipulacja metadanymi**: Atakujący wstrzykują złośliwe instrukcje do opisów narzędzi, definicji parametrów lub przykładów użycia
- **Niewidoczne instrukcje**: Ukryte prompt-y w metadanych narzędzi przetwarzane przez modele AI, ale niewidoczne dla użytkowników
- **Dynamiczna modyfikacja narzędzi („Rug Pulls”)**: Narzędzia zatwierdzone przez użytkowników są później zmieniane, aby wykonywać złośliwe działania bez wiedzy użytkownika
- **Wstrzyknięcie parametrów**: Złośliwe treści osadzone w schematach parametrów narzędziowych, które wpływają na zachowanie modelu


**Ryzyka serwerów hostowanych**: Zdalne serwery MCP niosą ze sobą podwyższone ryzyko, ponieważ definicje narzędzi mogą być aktualizowane po początkowej akceptacji użytkownika, tworząc scenariusze, w których wcześniej bezpieczne narzędzia stają się złośliwe. W celu uzyskania kompleksowej analizy, zobacz [Ataki zatruwania narzędzi (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Schemat ataku wstrzyknięcia narzędzia](../../../translated_images/pl/tool-injection.3b0b4a6b24de6bef.webp)

#### **Dodatkowe wektory ataków AI**

- **Wstrzyknięcie promptów międzydomenowych (XPIA)**: Zaawansowane ataki wykorzystujące treści z wielu domen do omijania zabezpieczeń
- **Dynamiczna modyfikacja możliwości**: Zmiany możliwości narzędzi w czasie rzeczywistym, które uchodzą ocenie zabezpieczeń
- **Zatrucie okna kontekstu**: Ataki manipulujące dużym oknem kontekstu w celu ukrycia złośliwych instrukcji
- **Ataki mieszania modeli**: Wykorzystywanie ograniczeń modelu do tworzenia nieprzewidywalnych lub niebezpiecznych zachowań


### Wpływ ryzyka bezpieczeństwa AI

**Konsekwencje o wysokim wpływie:**
- **Eksfiltracja danych**: Nieautoryzowany dostęp i kradzież poufnych danych przedsiębiorstwa lub danych osobowych
- **Naruszenia prywatności**: Ujawnienie danych umożliwiających identyfikację osoby (PII) oraz poufnych danych biznesowych  
- **Manipulacja systemem**: Nieintencjonalne modyfikacje krytycznych systemów i procesów
- **Kradzież poświadczeń**: Kompromitacja tokenów uwierzytelniających i danych uwierzytelniających usług
- **Ruch boczny**: Wykorzystanie skompromitowanych systemów AI jako punktów pośrednich dla szerszych ataków sieciowych

### Rozwiązania bezpieczeństwa AI firmy Microsoft

#### **AI Prompt Shields: Zaawansowana ochrona przed atakami wstrzyknięcia**

Microsoft **AI Prompt Shields** zapewniają kompleksową obronę przed bezpośrednimi i pośrednimi atakami wstrzyknięcia promptów poprzez wielowarstwowe zabezpieczenia:

##### **Podstawowe mechanizmy ochrony:**

1. **Zaawansowane wykrywanie i filtrowanie**
   - Algorytmy uczenia maszynowego i techniki NLP wykrywają złośliwe instrukcje w zewnętrznych treściach
   - Analiza w czasie rzeczywistym dokumentów, stron internetowych, e-maili i źródeł danych pod kątem ukrytych zagrożeń
   - Kontekstowe rozróżnianie wzorców promptów legalnych i złośliwych

2. **Techniki wyróżniania**  
   - Rozróżnia zaufane instrukcje systemowe od potencjalnie skompromitowanych danych zewnętrznych
   - Metody transformacji tekstu, które zwiększają trafność modelu przy izolacji złośliwych treści
   - Pomaga systemom AI utrzymać prawidłową hierarchię instrukcji i ignorować wstrzyknięte polecenia

3. **Systemy ograniczników i znakowania danych**
   - Wyraźne definiowanie granic między zaufanymi komunikatami systemowymi a zewnętrznym tekstem wejściowym
   - Specjalne znaczniki podkreślają granice między zaufanymi i niezaufanymi źródłami danych
   - Jasne oddzielenie zapobiega zamieszaniu instrukcji i nieautoryzowanemu wykonywaniu poleceń

4. **Ciągłe rozpoznawanie zagrożeń**
   - Microsoft nieustannie monitoruje nowe wzorce ataków i aktualizuje mechanizmy obronne
   - Proaktywne poszukiwanie zagrożeń nowych technik wstrzyknięć i wektorów ataku
   - Regularne aktualizacje modeli zabezpieczeń dla utrzymania skuteczności wobec ewoluujących zagrożeń

5. **Integracja Azure Content Safety**
   - Część kompleksowego pakietu Azure AI Content Safety
   - Dodatkowe wykrywanie prób jailbreak, szkodliwych treści i naruszeń polityk bezpieczeństwa
   - Zunifikowana kontrola bezpieczeństwa napędzająca komponenty aplikacji AI

**Zasoby implementacyjne**: [Dokumentacja Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Ochrona Microsoft Prompt Shields](../../../translated_images/pl/prompt-shield.ff5b95be76e9c78c.webp)


## Zaawansowane zagrożenia bezpieczeństwa MCP

### Luki w zabezpieczeniach przejęcia sesji

**Przejęcie sesji** jest krytycznym wektorem ataku w stanowych implementacjach MCP, gdzie nieuprawnione podmioty uzyskują i nadużywają legalnych identyfikatorów sesji, aby podszywać się pod klientów i wykonywać nieautoryzowane działania.

#### **Scenariusze ataków i ryzyka**

- **Wstrzyknięcie poleceń przez przejętą sesję**: Atakujący z kradzionymi identyfikatorami sesji wstrzykują złośliwe zdarzenia do serwerów współdzielących stan sesji, potencjalnie wywołując szkodliwe działania lub dostęp do poufnych danych
- **Bezpośrednie podszywanie się**: Skradzione identyfikatory sesji umożliwiają bezpośrednie wywołania serwera MCP omijające uwierzytelnianie, traktując atakujących jak legalnych użytkowników
- **Skompromitowane strumienie z możliwością wznowienia**: Atakujący mogą przedwcześnie zakończyć żądania, powodując, że legalni klienci wznawiają z potencjalnie złośliwą zawartością

#### **Kontrole bezpieczeństwa zarządzania sesjami**

**Wymagania krytyczne:**
- **Weryfikacja autoryzacji**: Serwery MCP implementujące autoryzację **MUSZĄ** weryfikować WSZYSTKIE przychodzące żądania i **NIE MOGĄ** polegać na sesjach do uwierzytelniania
- **Bezpieczne generowanie sesji**: Używać kryptograficznie bezpiecznych, niedeterministycznych identyfikatorów sesji generowanych za pomocą bezpiecznych generatorów liczb losowych
- **Powiązanie z użytkownikiem**: Powiązać identyfikatory sesji z informacjami specyficznymi dla użytkownika, np. w formacie `<user_id>:<session_id>`, aby zapobiec nadużyciom między użytkownikami
- **Zarządzanie cyklem życia sesji**: Wprowadzić odpowiednią ważność, rotację i unieważnianie w celu ograniczenia okien podatności
- **Bezpieczeństwo transportu**: Wymagane stosowanie HTTPS dla całej komunikacji, aby zapobiec przechwyceniu identyfikatorów sesji

### Problem „zagubionego pełnomocnika” (Confused Deputy)

**Problem zagubionego pełnomocnika** występuje, gdy serwery MCP pełnią rolę pośredników uwierzytelniających między klientami a usługami stron trzecich, tworząc możliwości obejścia autoryzacji poprzez wykorzystanie statycznych identyfikatorów klienta.

#### **Mechanika ataków i ryzyka**

- **Ominięcie zgody oparte na ciasteczkach**: Poprzednie uwierzytelnienie użytkownika tworzy ciasteczka zgody, które atakujący wykorzystują poprzez złośliwe żądania autoryzacyjne z przygotowanymi URI przekierowań
- **Kradzież kodów autoryzacyjnych**: Istniejące ciasteczka zgody mogą spowodować, że serwery autoryzacji pominą ekrany zgody, przekierowując kody do punktów kontrolowanych przez atakującego  
- **Nieautoryzowany dostęp do API**: Skradzione kody autoryzacji umożliwiają wymianę tokenów i podszywanie się pod użytkowników bez wyraźnej zgody

#### **Strategie łagodzenia**

**Wymagane kontrole:**
- **Wymaganie wyraźnej zgody**: Serwery proxy MCP używające statycznych identyfikatorów klienta **MUSZĄ** uzyskiwać zgodę użytkownika dla każdego dynamicznie rejestrowanego klienta
- **Implementacja bezpieczeństwa OAuth 2.1**: Stosować aktualne najlepsze praktyki bezpieczeństwa OAuth, w tym PKCE (Proof Key for Code Exchange) dla wszystkich żądań autoryzacyjnych
- **Ścisła walidacja klienta**: Wdrożyć rygorystyczną walidację URI przekierowań i identyfikatorów klienta, aby zapobiec nadużyciom

### Luki w podatności Token Passthrough  

**Token passthrough** to jawny antywzorzec, w którym serwery MCP przyjmują tokeny klientów bez odpowiedniej walidacji i przekazują je do niższych warstw API, naruszając specyfikacje autoryzacji MCP.

#### **Implikacje bezpieczeństwa**

- **Obejście kontroli**: Bezpośrednie użycie tokenów klienta do API omija krytyczne kontroli limitów, walidacji i monitoringu
- **Naruszenie ścieżki audytu**: Tokeny wydane upstream uniemożliwiają identyfikację klienta, co utrudnia dochodzenia incydentów
- **Eksfiltracja danych przez proxy**: Niezwalidowane tokeny pozwalają złośliwym aktorom wykorzystywać serwery jako proxy do nieautoryzowanego dostępu do danych
- **Naruszenie granic zaufania**: Usługi downstream mogą mieć naruszone założenia dotyczące zaufania, gdy źródła tokenów nie są weryfikowalne
- **Rozprzestrzenianie ataków między usługami**: Skompromitowane tokeny akceptowane w wielu usługach umożliwiają ruch boczny

#### **Wymagane kontrole bezpieczeństwa**

**Bezwarunkowe wymagania:**
- **Walidacja tokenów**: Serwery MCP **NIE MOGĄ** akceptować tokenów, które nie zostały wyraźnie wydane dla serwera MCP
- **Weryfikacja odbiorcy (audience)**: Zawsze weryfikować zgodność odbiorcy tokena z tożsamością serwera MCP
- **Prawidłowy cykl życia tokena**: Wprowadzić krótkotrwałe tokeny dostępu ze bezpieczną rotacją


## Bezpieczeństwo łańcucha dostaw dla systemów AI

Bezpieczeństwo łańcucha dostaw rozwinęło się poza tradycyjne zależności oprogramowania, aby objąć cały ekosystem AI. Nowoczesne implementacje MCP muszą rygorystycznie weryfikować i monitorować wszystkie komponenty związane z AI, ponieważ każdy z nich może wprowadzać potencjalne luki zagrażające integralności systemu.

### Rozszerzone komponenty łańcucha dostaw AI

**Tradycyjne zależności oprogramowania:**
- Biblioteki i frameworki open source
- Obrazy kontenerów i systemy bazowe  
- Narzędzia deweloperskie i pipeline'y buildów
- Komponenty infrastruktury i usługi

**Specyficzne elementy łańcucha dostaw AI:**
- **Modele bazowe**: Wstępnie wytrenowane modele od różnych dostawców wymagające weryfikacji pochodzenia
- **Usługi osadzania**: Zewnętrzne usługi wektoryzacji i wyszukiwania semantycznego
- **Dostawcy kontekstu**: Źródła danych, bazy wiedzy i repozytoria dokumentów  
- **API stron trzecich**: Zewnętrzne usługi AI, pipeline'y ML i punkty końcowe przetwarzania danych
- **Artefakty modeli**: Wagi, konfiguracje i warianty modeli dopasowanych
- **Źródła danych treningowych**: Zbiory danych używane do treningu i dopasowywania modeli

### Kompleksowa strategia bezpieczeństwa łańcucha dostaw

#### **Weryfikacja komponentów i zaufanie**
- **Weryfikacja pochodzenia**: Sprawdzenie źródła, licencji i integralności wszystkich komponentów AI przed integracją
- **Ocena bezpieczeństwa**: Przeprowadzanie skanów podatności i przeglądów bezpieczeństwa modeli, źródeł danych i usług AI
- **Analiza reputacji**: Ocena historii bezpieczeństwa i praktyk dostawców usług AI
- **Weryfikacja zgodności**: Zapewnienie spełnienia wymogów organizacyjnych dotyczących bezpieczeństwa i regulacji przez wszystkie komponenty

#### **Bezpieczne pipeline'y wdrożeniowe**  
- **Zautomatyzowane bezpieczeństwo CI/CD**: Integracja skanowania bezpieczeństwa w całych automatycznych pipeline'ach wdrożeniowych
- **Integralność artefaktów**: Wdrożenie kryptograficznej weryfikacji wszystkich artefaktów (kod, modele, konfiguracje)
- **Wdrożenie etapowe**: Stosowanie progresywnych strategii wdrożenia z weryfikacją bezpieczeństwa na każdym etapie
- **Zaufane repozytoria artefaktów**: Wdrażanie tylko z zweryfikowanych, bezpiecznych rejestrów i repozytoriów artefaktów

#### **Ciągły monitoring i reakcja**
- **Skanowanie zależności**: Ciągły monitoring podatności wszystkich zależności oprogramowania i komponentów AI
- **Monitoring modeli**: Stała ocena zachowania modeli, dryfu wydajności oraz anomalii bezpieczeństwa
- **Monitoring zdrowia usług**: Monitorowanie zewnętrznych usług AI pod kątem dostępności, incydentów bezpieczeństwa i zmian polityk
- **Integracja wywiadu zagrożeń**: Uwzględnianie źródeł informacji o zagrożeniach specyficznych dla bezpieczeństwa AI i ML

#### **Kontrola dostępu i zasada najmniejszego uprzywilejowania**
- **Uprawnienia na poziomie komponentów**: Ograniczenie dostępu do modeli, danych i usług na zasadzie konieczności biznesowej
- **Zarządzanie kontami usług**: Wdrażanie dedykowanych kont usług z minimalnymi niezbędnymi uprawnieniami
- **Segmentacja sieci**: Izolacja komponentów AI i ograniczanie dostępu sieciowego między usługami
- **Kontrole API Gateway**: Wykorzystywanie scentralizowanych bram API do kontroli i monitorowania dostępu do zewnętrznych usług AI

#### **Reagowanie na incydenty i odzyskiwanie**
- **Procedury szybkiej reakcji**: Ustanowione procesy łatania lub wymiany skompromitowanych komponentów AI
- **Rotacja poświadczeń**: Zautomatyzowane systemy rotacji sekretów, kluczy API i danych uwierzytelniających usług
- **Możliwości wycofania zmian**: Zdolność do szybkiego przywrócenia poprzednich, zweryfikowanych wersji komponentów AI
- **Odzyskiwanie po naruszeniach łańcucha dostaw**: Specyficzne procedury reagowania na kompromitacje usług AI upstream

### Narzędzia i integracja bezpieczeństwa Microsoft

**GitHub Advanced Security** zapewnia kompleksową ochronę łańcucha dostaw, w tym:
- **Skanowanie sekretów**: Automatyczne wykrywanie poświadczeń, kluczy API i tokenów w repozytoriach
- **Skanowanie zależności**: Ocena podatności bibliotek i zależności open source
- **Analiza CodeQL**: Statyczna analiza kodu w celu wykrywania luk bezpieczeństwa i problemów ze składnią
- **Wgląd w łańcuch dostaw**: Widoczność zdrowia i statusu bezpieczeństwa zależności

**Integracja Azure DevOps & Azure Repos:**
- Bezproblemowa integracja skanowania bezpieczeństwa w platformach rozwoju Microsoft
- Automatyczne kontrole bezpieczeństwa w Azure Pipelines dla obciążeń AI
- Wdrażanie polityk dotyczących bezpiecznego wdrażania komponentów AI

**Praktyki wewnętrzne Microsoft:**
Microsoft wdraża obszerne praktyki bezpieczeństwa łańcucha dostaw we wszystkich produktach. Poznaj sprawdzone podejścia w [Podróży do zabezpieczenia łańcucha dostaw oprogramowania w Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Najlepsze praktyki bezpieczeństwa podstawowego

Implementacje MCP dziedziczą i rozbudowują istniejącą postawę bezpieczeństwa organizacji. Wzmocnienie podstawowych praktyk bezpieczeństwa znacznie poprawia ogólne bezpieczeństwo systemów AI i wdrożeń MCP.

### Podstawowe zasady bezpieczeństwa

#### **Bezpieczne praktyki tworzenia oprogramowania**
- **Zgodność z OWASP**: Ochrona przed [10 największymi błędami OWASP](https://owasp.org/www-project-top-ten/) w aplikacjach webowych
- **Ochrony specyficzne dla AI**: Wprowadzanie kontroli dla [OWASP Top 10 dla LLM](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Bezpieczne zarządzanie sekretami**: Używanie dedykowanych magazynów dla tokenów, kluczy API i poufnych danych konfiguracyjnych
- **Szyfrowanie end-to-end**: Zapewnienie bezpiecznej komunikacji we wszystkich komponentach aplikacji i przepływach danych
- **Walidacja wejścia**: Rygorystyczna walidacja wszystkich danych wejściowych użytkownika, parametrów API i źródeł danych

#### **Umacnianie infrastruktury**
- **Uwierzytelnianie wieloskładnikowe**: Obowiązkowe MFA dla wszystkich kont administracyjnych i kont usług
- **Zarządzanie poprawkami**: Automatyczne i terminowe stosowanie poprawek dla systemów operacyjnych, frameworków i zależności  
- **Integracja dostawców tożsamości**: Centralne zarządzanie tożsamością przez dostawców tożsamości korporacyjnych (Microsoft Entra ID, Active Directory)
- **Segmentacja sieci**: Logiczna izolacja komponentów MCP ograniczająca możliwość ruchu bocznego
- **Zasada najmniejszego uprzywilejowania**: Minimalne wymagane uprawnienia dla wszystkich komponentów systemu i kont

#### **Monitorowanie i wykrywanie zagrożeń**
- **Szczegółowe logowanie**: Dokładne logowanie działań aplikacji AI, w tym interakcji klient-serwer MCP
- **Integracja SIEM**: Centralne zarządzanie informacjami o bezpieczeństwie i zdarzeniami w celu wykrywania anomalii
- **Analiza behawioralna**: Monitorowanie wspierane przez AI do wykrywania nietypowych wzorców w zachowaniu systemu i użytkowników
- **Wywiad zagrożeń**: Integracja z zewnętrznymi źródłami informacji o zagrożeniach i wskaźnikami kompromitacji (IOC)
- **Reakcja na incydenty**: Starannie zdefiniowane procedury wykrywania, reagowania i odzyskiwania po incydentach bezpieczeństwa

#### **Architektura Zero Trust**
- **Nigdy nie ufaj, zawsze weryfikuj**: Ciągła weryfikacja użytkowników, urządzeń i połączeń sieciowych
- **Mikrosegmentacja**: Granularna kontrola sieci izolująca poszczególne obciążenia i usługi
- **Bezpieczeństwo oparte na tożsamości**: Polityki bezpieczeństwa oparte na zweryfikowanych tożsamościach, a nie lokalizacji sieciowej
- **Ciągła ocena ryzyka**: Dynamiczna ocena postawy bezpieczeństwa bazująca na aktualnym kontekście i zachowaniu
- **Dostęp warunkowy**: Kontrole dostępu adaptujące się na podstawie czynników ryzyka, lokalizacji i zaufania do urządzenia

### Wzorce integracji korporacyjnej

#### **Integracja z ekosystemem bezpieczeństwa Microsoft**
- **Microsoft Defender for Cloud**: Kompleksowe zarządzanie postawą bezpieczeństwa chmury
- **Azure Sentinel**: Natywne w chmurze funkcjonalności SIEM i SOAR dla ochrony obciążeń AI
- **Microsoft Entra ID**: Zarządzanie tożsamością i dostępem przedsiębiorstwa z politykami dostępu warunkowego
- **Azure Key Vault**: Centralne zarządzanie sekretami z modułem sprzętowym HSM
- **Microsoft Purview**: Zarządzanie danymi i zgodnością dla źródeł danych AI i przepływów pracy

#### **Zgodność i zarządzanie**
- **Wyrównanie regulacyjne**: Zapewnienie, że implementacje MCP spełniają branżowe wymagania zgodności (GDPR, HIPAA, SOC 2)

- **Klasyfikacja danych**: Właściwa kategoryzacja i obsługa wrażliwych danych przetwarzanych przez systemy AI
- **Ślady audytu**: Kompleksowe logowanie dla zgodności regulacyjnej i dochodzeń kryminalistycznych
- **Kontrole prywatności**: Wdrażanie zasad prywatności zgodnie z designem w architekturze systemów AI
- **Zarządzanie zmianami**: Formalne procesy przeglądów bezpieczeństwa modyfikacji systemów AI

Te podstawowe praktyki tworzą solidną bazę bezpieczeństwa, która zwiększa skuteczność specyficznych dla MCP kontroli bezpieczeństwa i zapewnia kompleksową ochronę aplikacji opartych na AI.

## Kluczowe wnioski dotyczące bezpieczeństwa

- **Wielowarstwowe podejście do bezpieczeństwa**: Łącz podstawowe praktyki bezpieczeństwa (bezpieczne kodowanie, najmniejsze uprawnienia, weryfikacja łańcucha dostaw, ciągły monitoring) ze specyficznymi kontrolami AI dla kompleksowej ochrony

- **Specyficzne zagrożenia AI**: Systemy MCP napotykają unikalne ryzyka, takie jak wstrzykiwanie promptów, zatruwanie narzędzi, przejmowanie sesji, problemy z confused deputy, podatności na przekazywanie tokenów i nadmierne uprawnienia, które wymagają specjalistycznych środków zaradczych

- **Doskonałość uwierzytelniania i autoryzacji**: Wdrażaj solidne uwierzytelnianie z wykorzystaniem zewnętrznych dostawców tożsamości (Microsoft Entra ID), egzekwuj właściwą walidację tokenów i nigdy nie akceptuj tokenów niewydanych wyraźnie dla twojego serwera MCP

- **Zapobieganie atakom AI**: Stosuj Microsoft Prompt Shields i Azure Content Safety, by bronić się przed pośrednim wstrzykiwaniem promptów i atakami zatruwania narzędzi, jednocześnie weryfikując metadane narzędzi i monitorując zmiany dynamiczne

- **Bezpieczeństwo sesji i transportu**: Używaj kryptograficznie bezpiecznych, niedeterministycznych identyfikatorów sesji powiązanych z tożsamościami użytkowników, wdrażaj poprawne zarządzanie cyklem życia sesji i nigdy nie używaj sesji do uwierzytelniania

- **Najlepsze praktyki bezpieczeństwa OAuth**: Zapobiegaj atakom confused deputy przez wyraźną zgodę użytkownika dla dynamicznie rejestrowanych klientów, właściwą implementację OAuth 2.1 z PKCE oraz rygorystyczną walidację URI przekierowania  

- **Zasady bezpieczeństwa tokenów**: Unikaj antywzorów przekazywania tokenów, waliduj deklaracje odbiorców tokenów, stosuj krótkotrwałe tokeny z bezpieczną rotacją oraz utrzymuj wyraźne granice zaufania

- **Kompleksowe bezpieczeństwo łańcucha dostaw**: Traktuj wszystkie komponenty ekosystemu AI (modele, embeddingi, dostawców kontekstu, zewnętrzne API) z równie wysokim rygorem bezpieczeństwa, jak tradycyjne zależności oprogramowania

- **Ciągła ewolucja**: Bądź na bieżąco z szybko rozwijającymi się specyfikacjami MCP, uczestnicz w tworzeniu standardów społeczności bezpieczeństwa i utrzymuj adaptacyjny profil bezpieczeństwa w miarę dojrzewania protokołu

- **Integracja bezpieczeństwa Microsoft**: Wykorzystuj kompleksowy ekosystem bezpieczeństwa Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) dla zwiększonej ochrony wdrożeń MCP

## Kompleksowe zasoby

### **Oficjalna dokumentacja bezpieczeństwa MCP**
- [Specyfikacja MCP (Aktualna: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [Najlepsze praktyki bezpieczeństwa MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [Specyfikacja autoryzacji MCP](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [Repozytorium MCP na GitHub](https://github.com/modelcontextprotocol)

### **Zasoby bezpieczeństwa OWASP MCP**
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) - Kompleksowy przewodnik OWASP MCP Top 10 z wdrożeniem na platformie Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Oficjalne zagrożenia bezpieczeństwa OWASP MCP
- [Warsztat MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/) - Praktyczne szkolenie z bezpieczeństwa MCP na platformie Azure

### **Standardy bezpieczeństwa i najlepsze praktyki**
- [Najlepsze praktyki bezpieczeństwa OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 bezpieczeństwa aplikacji webowych](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 dla dużych modeli językowych](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digital Defense Report](https://aka.ms/mddr)

### **Badania i analizy bezpieczeństwa AI**
- [Wstrzykiwanie promptów w MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Ataki zatruwania narzędzi (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [Briefing badań bezpieczeństwa MCP (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Rozwiązania bezpieczeństwa Microsoft**
- [Dokumentacja Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Usługa Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Security](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Najlepsze praktyki zarządzania tokenami w Azure](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Przewodniki wdrożeniowe i samouczki**
- [Azure API Management jako brama uwierzytelniania MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Uwierzytelnianie Microsoft Entra ID z serwerami MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Bezpieczne przechowywanie i szyfrowanie tokenów (wideo)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **Bezpieczeństwo DevOps i łańcucha dostaw**
- [Bezpieczeństwo Azure DevOps](https://azure.microsoft.com/products/devops)
- [Bezpieczeństwo Azure Repos](https://azure.microsoft.com/products/devops/repos/)
- [Podróż Microsoft w zakresie bezpieczeństwa łańcucha dostaw](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Dodatkowa dokumentacja bezpieczeństwa**

Dla kompleksowych wskazówek dotyczących bezpieczeństwa odnieś się do tych specjalistycznych dokumentów w tej sekcji:

- **[Przykład autoryzacji CIMD i DCR](./samples/cimd-dcr-auth/README.md)** - Działający serwer zasobów MCP `2026-07-28` w TypeScript porównujący preferowane dokumenty metadanych Client ID z wycofanym fallbackiem Dynamic Client Registration
- **[Najlepsze praktyki bezpieczeństwa MCP](./mcp-security-best-practices.md)** - Kompletny zestaw najlepszych praktyk bezpieczeństwa dla implementacji MCP
- **[Implementacja Azure Content Safety](./azure-content-safety-implementation.md)** - Praktyczne przykłady integracji Azure Content Safety  
- **[Kontrole bezpieczeństwa MCP](./mcp-security-controls.md)** - Najnowsze techniki i kontrole bezpieczeństwa dla wdrożeń MCP
- **[Szybka ściąga najlepszych praktyk MCP](./mcp-best-practices.md)** - Szybki przewodnik po kluczowych praktykach bezpieczeństwa MCP
- **[BlueHat 2026: Zabezpieczanie przyszłości AI: zabezpieczenie MCP poprzez wzorce obrony w głębi](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Wzorce obrony w głębi od Microsoft Security Response Center (MSRC)

### **Praktyczne szkolenia z bezpieczeństwa**

- **[Warsztat MCP Security Summit (Sherpa)](https://azure-samples.github.io/sherpa/)** - Kompleksowy warsztat praktyczny zabezpieczania serwerów MCP w Azure, z postępującymi obozami od Base Camp do Summit
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - Architektura referencyjna i wskazówki wdrożeniowe dla wszystkich zagrożeń OWASP MCP Top 10

---

## Co dalej

Następny: [Rozdział 3: Rozpoczęcie pracy](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->