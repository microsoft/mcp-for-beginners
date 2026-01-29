# MCP Security: Kompleksowa ochrona systemów AI

[![MCP Security Best Practices](../../../translated_images/pl/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(Kliknij powyższy obraz, aby obejrzeć wideo z tej lekcji)_

Bezpieczeństwo jest fundamentem projektowania systemów AI, dlatego traktujemy je jako naszą drugą sekcję. Jest to zgodne z zasadą Microsoftu **Secure by Design** z [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Model Context Protocol (MCP) wprowadza potężne nowe możliwości do aplikacji napędzanych AI, jednocześnie stawiając unikalne wyzwania bezpieczeństwa wykraczające poza tradycyjne ryzyka oprogramowania. Systemy MCP muszą radzić sobie zarówno z ustalonymi zagrożeniami bezpieczeństwa (bezpieczne kodowanie, zasada najmniejszych uprawnień, bezpieczeństwo łańcucha dostaw), jak i nowymi zagrożeniami specyficznymi dla AI, w tym wstrzykiwaniem promptów, zatruwaniem narzędzi, przejmowaniem sesji, atakami typu confused deputy, lukami w przekazywaniu tokenów oraz dynamiczną modyfikacją uprawnień.

Ta lekcja omawia najważniejsze ryzyka bezpieczeństwa w implementacjach MCP — obejmując uwierzytelnianie, autoryzację, nadmierne uprawnienia, pośrednie wstrzykiwanie promptów, bezpieczeństwo sesji, problemy confused deputy, zarządzanie tokenami oraz podatności łańcucha dostaw. Nauczysz się praktycznych środków kontroli i najlepszych praktyk, które pomogą złagodzić te ryzyka, wykorzystując rozwiązania Microsoft takie jak Prompt Shields, Azure Content Safety i GitHub Advanced Security, aby wzmocnić wdrożenie MCP.

## Cele nauki

Po zakończeniu tej lekcji będziesz potrafił:

- **Identyfikować zagrożenia specyficzne dla MCP**: Rozpoznawać unikalne ryzyka bezpieczeństwa w systemach MCP, w tym wstrzykiwanie promptów, zatruwanie narzędzi, nadmierne uprawnienia, przejmowanie sesji, problemy confused deputy, luki w przekazywaniu tokenów oraz ryzyka łańcucha dostaw
- **Stosować środki bezpieczeństwa**: Wdrażać skuteczne środki zaradcze, w tym solidne uwierzytelnianie, dostęp na zasadzie najmniejszych uprawnień, bezpieczne zarządzanie tokenami, kontrolę bezpieczeństwa sesji oraz weryfikację łańcucha dostaw
- **Wykorzystywać rozwiązania Microsoft w zakresie bezpieczeństwa**: Rozumieć i wdrażać Microsoft Prompt Shields, Azure Content Safety oraz GitHub Advanced Security do ochrony obciążeń MCP
- **Weryfikować bezpieczeństwo narzędzi**: Rozpoznawać znaczenie walidacji metadanych narzędzi, monitorowania dynamicznych zmian oraz obrony przed pośrednimi atakami wstrzykiwania promptów
- **Integracja najlepszych praktyk**: Łączyć ustalone fundamenty bezpieczeństwa (bezpieczne kodowanie, wzmacnianie serwerów, zero trust) z kontrolami specyficznymi dla MCP dla kompleksowej ochrony

# Architektura i Kontrole Bezpieczeństwa MCP

Nowoczesne implementacje MCP wymagają wielowarstwowych podejść do bezpieczeństwa, które adresują zarówno tradycyjne zagrożenia oprogramowania, jak i specyficzne dla AI. Szybko ewoluująca specyfikacja MCP stale rozwija swoje środki kontroli bezpieczeństwa, umożliwiając lepszą integrację z architekturami bezpieczeństwa przedsiębiorstw i ustalonymi najlepszymi praktykami.

Badania z [Microsoft Digital Defense Report](https://aka.ms/mddr) pokazują, że **98% zgłoszonych naruszeń można by zapobiec dzięki solidnej higienie bezpieczeństwa**. Najskuteczniejsza strategia ochrony łączy podstawowe praktyki bezpieczeństwa z kontrolami specyficznymi dla MCP — sprawdzone środki bazowe pozostają najbardziej efektywne w redukcji ogólnego ryzyka bezpieczeństwa.

## Aktualny krajobraz bezpieczeństwa

> **Uwaga:** Informacje te odzwierciedlają standardy bezpieczeństwa MCP na dzień **18 grudnia 2025**. Protokół MCP nadal szybko się rozwija, a przyszłe implementacje mogą wprowadzać nowe wzorce uwierzytelniania i rozszerzone kontrole. Zawsze odwołuj się do aktualnej [Specyfikacji MCP](https://spec.modelcontextprotocol.io/), [repozytorium MCP na GitHub](https://github.com/modelcontextprotocol) oraz [dokumentacji najlepszych praktyk bezpieczeństwa](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) dla najnowszych wytycznych.

### Ewolucja uwierzytelniania MCP

Specyfikacja MCP znacznie się rozwinęła w podejściu do uwierzytelniania i autoryzacji:

- **Pierwotne podejście**: Wczesne specyfikacje wymagały od deweloperów implementacji własnych serwerów uwierzytelniania, przy czym serwery MCP działały jako serwery autoryzacji OAuth 2.0 zarządzające bezpośrednio uwierzytelnianiem użytkowników
- **Aktualny standard (2025-11-25)**: Zaktualizowana specyfikacja pozwala serwerom MCP delegować uwierzytelnianie do zewnętrznych dostawców tożsamości (takich jak Microsoft Entra ID), poprawiając postawę bezpieczeństwa i zmniejszając złożoność implementacji
- **Transport Layer Security**: Ulepszone wsparcie dla bezpiecznych mechanizmów transportu z odpowiednimi wzorcami uwierzytelniania zarówno dla połączeń lokalnych (STDIO), jak i zdalnych (Streamable HTTP)

## Bezpieczeństwo uwierzytelniania i autoryzacji

### Aktualne wyzwania bezpieczeństwa

Nowoczesne implementacje MCP napotykają na kilka wyzwań związanych z uwierzytelnianiem i autoryzacją:

### Ryzyka i wektory zagrożeń

- **Błędna logika autoryzacji**: Wadliwa implementacja autoryzacji w serwerach MCP może ujawniać wrażliwe dane i nieprawidłowo stosować kontrole dostępu
- **Kompromitacja tokenów OAuth**: Kradzież tokenów lokalnego serwera MCP umożliwia atakującym podszywanie się pod serwery i dostęp do usług downstream
- **Luki w przekazywaniu tokenów**: Nieprawidłowe zarządzanie tokenami tworzy obejścia kontroli bezpieczeństwa i luki w rozliczalności
- **Nadmierne uprawnienia**: Nadmiernie uprzywilejowane serwery MCP naruszają zasadę najmniejszych uprawnień i rozszerzają powierzchnię ataku

#### Przekazywanie tokenów: krytyczny antywzorzec

**Przekazywanie tokenów jest wyraźnie zabronione** w obecnej specyfikacji autoryzacji MCP ze względu na poważne implikacje bezpieczeństwa:

##### Obejście kontroli bezpieczeństwa
- Serwery MCP i API downstream implementują krytyczne kontrole bezpieczeństwa (ograniczenia szybkości, walidacja żądań, monitorowanie ruchu), które zależą od prawidłowej walidacji tokenów
- Bezpośrednie użycie tokenów klienta do API omija te niezbędne zabezpieczenia, podważając architekturę bezpieczeństwa

##### Problemy z rozliczalnością i audytem  
- Serwery MCP nie mogą rozróżnić klientów używających tokenów wydanych upstream, co łamie ścieżki audytu
- Logi serwerów zasobów downstream pokazują mylące pochodzenie żądań zamiast faktycznych pośredników MCP
- Dochodzenia incydentów i audyty zgodności stają się znacznie trudniejsze

##### Ryzyko wycieku danych
- Niewalidowane roszczenia tokenów umożliwiają złośliwym aktorom z kradzionymi tokenami używanie serwerów MCP jako proxy do wycieku danych
- Naruszenia granic zaufania pozwalają na nieautoryzowane wzorce dostępu omijające zamierzone kontrole bezpieczeństwa

##### Wektory ataków wielousługowych
- Kompromitowane tokeny akceptowane przez wiele usług umożliwiają ruch boczny w sieci połączonych systemów
- Założenia zaufania między usługami mogą zostać naruszone, gdy pochodzenie tokenów nie może być zweryfikowane

### Kontrole bezpieczeństwa i środki zaradcze

**Krytyczne wymagania bezpieczeństwa:**

> **OBOWIĄZKOWE**: Serwery MCP **NIE MOGĄ** akceptować żadnych tokenów, które nie zostały wyraźnie wydane dla serwera MCP

#### Kontrole uwierzytelniania i autoryzacji

- **Rygorystyczny przegląd autoryzacji**: Przeprowadzaj kompleksowe audyty logiki autoryzacji serwerów MCP, aby zapewnić dostęp do wrażliwych zasobów tylko dla zamierzonych użytkowników i klientów
  - **Przewodnik wdrożeniowy**: [Azure API Management jako brama uwierzytelniania dla serwerów MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integracja tożsamości**: [Użycie Microsoft Entra ID do uwierzytelniania serwerów MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Bezpieczne zarządzanie tokenami**: Wdrażaj [zalecane praktyki Microsoft dotyczące walidacji i cyklu życia tokenów](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Waliduj roszczenia audience tokenów, aby odpowiadały tożsamości serwera MCP
  - Wdrażaj odpowiednie polityki rotacji i wygasania tokenów
  - Zapobiegaj atakom powtórzeniowym tokenów i nieautoryzowanemu użyciu

- **Chronione przechowywanie tokenów**: Zabezpiecz przechowywanie tokenów szyfrowaniem zarówno w spoczynku, jak i w tranzycie
  - **Najlepsze praktyki**: [Wytyczne dotyczące bezpiecznego przechowywania i szyfrowania tokenów](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Wdrażanie kontroli dostępu

- **Zasada najmniejszych uprawnień**: Przyznawaj serwerom MCP tylko minimalne uprawnienia niezbędne do zamierzonej funkcjonalności
  - Regularne przeglądy i aktualizacje uprawnień, aby zapobiegać narastaniu przywilejów
  - **Dokumentacja Microsoft**: [Bezpieczny dostęp na zasadzie najmniejszych uprawnień](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Kontrola dostępu oparta na rolach (RBAC)**: Wdrażaj precyzyjne przypisania ról
  - Ograniczaj role do konkretnych zasobów i działań
  - Unikaj szerokich lub niepotrzebnych uprawnień, które rozszerzają powierzchnię ataku

- **Ciągły monitoring uprawnień**: Wdrażaj stały audyt i monitorowanie dostępu
  - Monitoruj wzorce użycia uprawnień pod kątem anomalii
  - Szybko usuwaj nadmierne lub nieużywane uprawnienia

## Zagrożenia bezpieczeństwa specyficzne dla AI

### Ataki wstrzykiwania promptów i manipulacji narzędziami

Nowoczesne implementacje MCP napotykają zaawansowane wektory ataków specyficznych dla AI, których tradycyjne środki bezpieczeństwa nie są w stanie w pełni zaadresować:

#### **Pośrednie wstrzykiwanie promptów (Cross-Domain Prompt Injection)**

**Pośrednie wstrzykiwanie promptów** to jedno z najpoważniejszych zagrożeń w systemach AI z MCP. Atakujący osadzają złośliwe instrukcje w zewnętrznych treściach — dokumentach, stronach internetowych, e-mailach lub źródłach danych — które systemy AI następnie przetwarzają jako legalne polecenia.

**Scenariusze ataków:**
- **Wstrzykiwanie w dokumentach**: Złośliwe instrukcje ukryte w przetwarzanych dokumentach, które wywołują niezamierzone działania AI
- **Wykorzystanie treści internetowych**: Zainfekowane strony internetowe zawierające osadzone promptsy manipulujące zachowaniem AI podczas scrapowania
- **Ataki e-mailowe**: Złośliwe promptsy w e-mailach powodujące wycieki informacji lub nieautoryzowane działania asystentów AI
- **Zanieczyszczenie źródeł danych**: Kompromitowane bazy danych lub API dostarczające skażone treści do systemów AI

**Realny wpływ**: Ataki te mogą prowadzić do wycieku danych, naruszeń prywatności, generowania szkodliwych treści oraz manipulacji interakcjami użytkowników. Szczegółową analizę znajdziesz w [Prompt Injection w MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/pl/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **Ataki zatruwania narzędzi**

**Zatruwanie narzędzi** atakuje metadane definiujące narzędzia MCP, wykorzystując sposób, w jaki modele LLM interpretują opisy narzędzi i parametry do podejmowania decyzji o wykonaniu.

**Mechanizmy ataku:**
- **Manipulacja metadanymi**: Atakujący wstrzykują złośliwe instrukcje do opisów narzędzi, definicji parametrów lub przykładów użycia
- **Niewidoczne instrukcje**: Ukryte promptsy w metadanych narzędzi, które są przetwarzane przez modele AI, ale niewidoczne dla użytkowników
- **Dynamiczna modyfikacja narzędzi („Rug Pulls”)**: Narzędzia zatwierdzone przez użytkowników są później modyfikowane, aby wykonywać złośliwe działania bez ich wiedzy
- **Wstrzykiwanie parametrów**: Złośliwe treści osadzone w schematach parametrów narzędzi wpływające na zachowanie modelu

**Ryzyka serwerów hostowanych**: Zdalne serwery MCP niosą podwyższone ryzyko, ponieważ definicje narzędzi mogą być aktualizowane po początkowej akceptacji użytkownika, tworząc scenariusze, w których wcześniej bezpieczne narzędzia stają się złośliwe. Kompleksową analizę znajdziesz w [Ataki zatruwania narzędzi (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/pl/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **Dodatkowe wektory ataków AI**

- **Cross-Domain Prompt Injection (XPIA)**: Zaawansowane ataki wykorzystujące treści z wielu domen do obejścia kontroli bezpieczeństwa
- **Dynamiczna modyfikacja możliwości**: Zmiany w czasie rzeczywistym w możliwościach narzędzi, które unikają początkowych ocen bezpieczeństwa
- **Zatrucie okna kontekstu**: Ataki manipulujące dużymi oknami kontekstu, aby ukryć złośliwe instrukcje
- **Ataki dezorientujące modele**: Wykorzystywanie ograniczeń modeli do tworzenia nieprzewidywalnych lub niebezpiecznych zachowań

### Wpływ ryzyka bezpieczeństwa AI

**Konsekwencje o wysokim wpływie:**
- **Wycieki danych**: Nieautoryzowany dostęp i kradzież wrażliwych danych przedsiębiorstwa lub danych osobowych
- **Naruszenia prywatności**: Ujawnienie danych osobowych (PII) i poufnych informacji biznesowych  
- **Manipulacja systemami**: Niezamierzone modyfikacje krytycznych systemów i procesów
- **Kradzież poświadczeń**: Kompromitacja tokenów uwierzytelniających i poświadczeń usług
- **Ruch boczny**: Wykorzystanie skompromitowanych systemów AI jako punktów przesiadkowych do szerszych ataków sieciowych

### Rozwiązania Microsoft w zakresie bezpieczeństwa AI

#### **AI Prompt Shields: Zaawansowana ochrona przed atakami wstrzykiwania**

Microsoft **AI Prompt Shields** zapewniają kompleksową obronę przed bezpośrednimi i pośrednimi atakami wstrzykiwania promptów poprzez wielowarstwowe zabezpieczenia:

##### **Podstawowe mechanizmy ochrony:**

1. **Zaawansowane wykrywanie i filtrowanie**
   - Algorytmy uczenia maszynowego i techniki NLP wykrywają złośliwe instrukcje w zewnętrznych treściach
   - Analiza w czasie rzeczywistym dokumentów, stron internetowych, e-maili i źródeł danych pod kątem osadzonych zagrożeń
   - Kontekstowe rozróżnianie legalnych i złośliwych wzorców promptów

2. **Techniki spotlightingu**  
   - Rozróżnia zaufane instrukcje systemowe od potencjalnie skompromitowanych danych zewnętrznych
   - Metody transformacji tekstu zwiększające relewantność modelu przy izolowaniu złośliwych treści
   - Pomaga systemom AI utrzymać właściwą hierarchię instrukcji i ignorować wstrzyknięte polecenia

3. **Systemy delimiterów i znakowania danych**
   - Wyraźne definiowanie granic między zaufanymi komunikatami systemowymi a zewnętrznym tekstem wejściowym
   - Specjalne znaczniki podkreślające granice między zaufanymi i niezaufanymi źródłami danych
   - Jasne oddzielenie zapobiega pomyłkom instrukcji i nieautoryzowanemu wykonywaniu poleceń

4. **Ciągła inteligencja zagrożeń**
   - Microsoft stale monitoruje pojawiające się wzorce ataków i aktualizuje mechanizmy obronne
   - Proaktywne polowanie na nowe techniki wstrzykiwania i wektory ataków
   - Regularne aktualizacje modeli bezpieczeństwa dla utrzymania skuteczności wobec ewoluujących zagrożeń

5. **Integracja z Azure Content Safety**
   - Część kompleksowego pakietu Azure AI Content Safety
   - Dodatkowe wykrywanie prób jailbreaków, szkodliwych treści i naruszeń polityk bezpieczeństwa
   - Zunifikowane kontrole bezpieczeństwa w komponentach aplikacji AI

**Zasoby wdrożeniowe**: [Dokumentacja Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/pl/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## Zaawansowane zagrożenia bezpieczeństwa MCP

### Luki w przejmowaniu sesji

**Przejęcie sesji** to krytyczny wektor ataku w stanowych implementacjach MCP, gdzie nieuprawnione podmioty uzyskują i wykorzystują prawidłowe identyfikatory sesji do podszywania się pod klientów i wykonywania nieautoryzowanych działań.

#### **Scenariusze ataków i ryzyka**

- **Wstrzykiwanie promptów przez przejęcie sesji**: Atakujący z kradzionymi identyfikatorami sesji wstrzykują złośliwe zdarzenia do serwerów współdzielących stan sesji, potencjalnie wywołując szkodliwe działania lub uzyskując dostęp do wrażliwych danych
- **Bezpośrednie podszywanie się**: Skradzione identyfikatory sesji umożliwiają bezpośrednie wywołania serwera MCP, omijając uwierzytelnianie i traktując atakujących jak prawowitych użytkowników
- **Skompromitowane strumienie z możliwością wznowienia**: Atakujący mogą przedwcześnie zakończyć żądania, powodując, że prawowici klienci wznawiają sesje z potencjalnie złośliwą zawartością

#### **Kontrole bezpieczeństwa zarządzania sesjami**

**Krytyczne wymagania:**
- **Weryfikacja autoryzacji**: Serwery MCP implementujące autoryzację **MUSZĄ** weryfikować WSZYSTKIE przychodzące żądania i **NIE MOGĄ** polegać na sesjach do uwierzytelniania  
- **Bezpieczne generowanie sesji**: Używaj kryptograficznie bezpiecznych, niedeterministycznych identyfikatorów sesji generowanych za pomocą bezpiecznych generatorów liczb losowych  
- **Powiązanie z użytkownikiem**: Powiąż identyfikatory sesji z informacjami specyficznymi dla użytkownika, używając formatów takich jak `<user_id>:<session_id>`, aby zapobiec nadużyciom sesji między użytkownikami  
- **Zarządzanie cyklem życia sesji**: Wdrażaj odpowiednie wygasanie, rotację i unieważnianie, aby ograniczyć okna podatności  
- **Bezpieczeństwo transportu**: Obowiązkowe HTTPS dla całej komunikacji, aby zapobiec przechwyceniu identyfikatorów sesji  

### Problem zdezorientowanego pełnomocnika

**Problem zdezorientowanego pełnomocnika** występuje, gdy serwery MCP działają jako proxy uwierzytelniające między klientami a usługami stron trzecich, tworząc możliwości obejścia autoryzacji poprzez wykorzystanie statycznych identyfikatorów klienta.

#### **Mechanika ataku i ryzyka**

- **Obejście zgody oparte na ciasteczkach**: Poprzednie uwierzytelnienie użytkownika tworzy ciasteczka zgody, które atakujący wykorzystują poprzez złośliwe żądania autoryzacji z przygotowanymi URI przekierowań  
- **Kradzież kodu autoryzacyjnego**: Istniejące ciasteczka zgody mogą spowodować, że serwery autoryzacji pominą ekrany zgody, przekierowując kody do punktów kontrolowanych przez atakującego  
- **Nieautoryzowany dostęp do API**: Skradzione kody autoryzacyjne umożliwiają wymianę tokenów i podszywanie się pod użytkownika bez wyraźnej zgody  

#### **Strategie łagodzenia**

**Wymagane kontrole:**  
- **Wymagania dotyczące wyraźnej zgody**: Serwery proxy MCP używające statycznych identyfikatorów klienta **MUSZĄ** uzyskać zgodę użytkownika dla każdego dynamicznie rejestrowanego klienta  
- **Implementacja bezpieczeństwa OAuth 2.1**: Stosuj aktualne najlepsze praktyki bezpieczeństwa OAuth, w tym PKCE (Proof Key for Code Exchange) dla wszystkich żądań autoryzacji  
- **Ścisła walidacja klienta**: Wdrażaj rygorystyczną walidację URI przekierowań i identyfikatorów klienta, aby zapobiec wykorzystaniu  

### Luki w przekazywaniu tokenów  

**Przekazywanie tokenów** to wyraźny antywzorzec, w którym serwery MCP akceptują tokeny klienta bez odpowiedniej walidacji i przekazują je do dalszych API, naruszając specyfikacje autoryzacji MCP.

#### **Implikacje bezpieczeństwa**

- **Ominięcie kontroli**: Bezpośrednie użycie tokenów klienta do API omija krytyczne ograniczenia szybkości, walidację i kontrole monitoringu  
- **Uszkodzenie ścieżki audytu**: Tokeny wydane upstream uniemożliwiają identyfikację klienta, co utrudnia dochodzenia incydentów  
- **Eksfiltracja danych przez proxy**: Niezwalidowane tokeny umożliwiają złośliwym aktorom używanie serwerów jako proxy do nieautoryzowanego dostępu do danych  
- **Naruszenia granic zaufania**: Założenia zaufania usług downstream mogą zostać naruszone, gdy pochodzenie tokenów nie może być zweryfikowane  
- **Rozszerzenie ataków na wiele usług**: Skompromitowane tokeny akceptowane w wielu usługach umożliwiają ruch boczny  

#### **Wymagane kontrole bezpieczeństwa**

**Wymagania niepodlegające negocjacjom:**  
- **Walidacja tokenów**: Serwery MCP **NIE MOGĄ** akceptować tokenów niewydanych wyraźnie dla serwera MCP  
- **Weryfikacja odbiorcy**: Zawsze weryfikuj, czy roszczenia odbiorcy tokena odpowiadają tożsamości serwera MCP  
- **Prawidłowy cykl życia tokenów**: Wdrażaj krótkotrwałe tokeny dostępu z bezpiecznymi praktykami rotacji  

## Bezpieczeństwo łańcucha dostaw dla systemów AI

Bezpieczeństwo łańcucha dostaw rozwinęło się poza tradycyjne zależności oprogramowania, obejmując cały ekosystem AI. Nowoczesne implementacje MCP muszą rygorystycznie weryfikować i monitorować wszystkie komponenty związane z AI, ponieważ każdy z nich wprowadza potencjalne podatności mogące zagrozić integralności systemu.

### Rozszerzone komponenty łańcucha dostaw AI

**Tradycyjne zależności oprogramowania:**  
- Biblioteki i frameworki open-source  
- Obrazy kontenerów i systemy bazowe  
- Narzędzia deweloperskie i pipeline’y budowania  
- Komponenty infrastruktury i usługi  

**Elementy specyficzne dla łańcucha dostaw AI:**  
- **Modele bazowe**: Wstępnie wytrenowane modele od różnych dostawców wymagające weryfikacji pochodzenia  
- **Usługi osadzania**: Zewnętrzne usługi wektoryzacji i wyszukiwania semantycznego  
- **Dostawcy kontekstu**: Źródła danych, bazy wiedzy i repozytoria dokumentów  
- **API stron trzecich**: Zewnętrzne usługi AI, pipeline’y ML i punkty przetwarzania danych  
- **Artefakty modeli**: Wagi, konfiguracje i warianty modeli dostrajanych  
- **Źródła danych treningowych**: Zbiory danych używane do trenowania i dostrajania modeli  

### Kompleksowa strategia bezpieczeństwa łańcucha dostaw

#### **Weryfikacja komponentów i zaufanie**  
- **Weryfikacja pochodzenia**: Sprawdzaj pochodzenie, licencjonowanie i integralność wszystkich komponentów AI przed integracją  
- **Ocena bezpieczeństwa**: Przeprowadzaj skanowanie podatności i przeglądy bezpieczeństwa modeli, źródeł danych i usług AI  
- **Analiza reputacji**: Oceń historię bezpieczeństwa i praktyki dostawców usług AI  
- **Weryfikacja zgodności**: Zapewnij, że wszystkie komponenty spełniają wymagania bezpieczeństwa i regulacyjne organizacji  

#### **Bezpieczne pipeline’y wdrożeniowe**  
- **Automatyczne skanowanie CI/CD**: Integruj skanowanie bezpieczeństwa w całych zautomatyzowanych pipeline’ach wdrożeniowych  
- **Integralność artefaktów**: Wdrażaj kryptograficzną weryfikację wszystkich wdrażanych artefaktów (kod, modele, konfiguracje)  
- **Wdrożenia etapowe**: Stosuj progresywne strategie wdrożeń z walidacją bezpieczeństwa na każdym etapie  
- **Zaufane repozytoria artefaktów**: Wdrażaj tylko z weryfikowanych, bezpiecznych rejestrów i repozytoriów artefaktów  

#### **Ciągły monitoring i reakcja**  
- **Skanowanie zależności**: Stały monitoring podatności wszystkich zależności oprogramowania i komponentów AI  
- **Monitoring modeli**: Ciągła ocena zachowania modeli, dryfu wydajności i anomalii bezpieczeństwa  
- **Śledzenie stanu usług**: Monitoruj dostępność, incydenty bezpieczeństwa i zmiany polityk zewnętrznych usług AI  
- **Integracja wywiadu zagrożeń**: Uwzględniaj kanały informacji o zagrożeniach specyficzne dla bezpieczeństwa AI i ML  

#### **Kontrola dostępu i zasada najmniejszych uprawnień**  
- **Uprawnienia na poziomie komponentów**: Ogranicz dostęp do modeli, danych i usług zgodnie z potrzebami biznesowymi  
- **Zarządzanie kontami usług**: Wdrażaj dedykowane konta usług z minimalnymi wymaganymi uprawnieniami  
- **Segmentacja sieci**: Izoluj komponenty AI i ogranicz dostęp sieciowy między usługami  
- **Kontrole bramki API**: Używaj scentralizowanych bramek API do kontroli i monitorowania dostępu do zewnętrznych usług AI  

#### **Reakcja na incydenty i odzyskiwanie**  
- **Procedury szybkiej reakcji**: Ustanowione procesy łatania lub wymiany skompromitowanych komponentów AI  
- **Rotacja poświadczeń**: Zautomatyzowane systemy rotacji sekretów, kluczy API i poświadczeń usług  
- **Możliwości wycofania**: Możliwość szybkiego powrotu do poprzednich, znanych dobrych wersji komponentów AI  
- **Odzyskiwanie po naruszeniach łańcucha dostaw**: Specyficzne procedury reagowania na kompromitacje usług AI upstream  

### Narzędzia i integracja bezpieczeństwa Microsoft

**GitHub Advanced Security** zapewnia kompleksową ochronę łańcucha dostaw, w tym:  
- **Skanowanie sekretów**: Automatyczne wykrywanie poświadczeń, kluczy API i tokenów w repozytoriach  
- **Skanowanie zależności**: Ocena podatności zależności open-source i bibliotek  
- **Analiza CodeQL**: Statyczna analiza kodu pod kątem podatności i problemów z kodowaniem  
- **Wgląd w łańcuch dostaw**: Widoczność stanu zdrowia i bezpieczeństwa zależności  

**Integracja z Azure DevOps i Azure Repos:**  
- Bezproblemowa integracja skanowania bezpieczeństwa w platformach deweloperskich Microsoft  
- Automatyczne kontrole bezpieczeństwa w Azure Pipelines dla obciążeń AI  
- Egzekwowanie polityk bezpiecznego wdrażania komponentów AI  

**Praktyki wewnętrzne Microsoft:**  
Microsoft wdraża rozległe praktyki bezpieczeństwa łańcucha dostaw we wszystkich produktach. Poznaj sprawdzone podejścia w [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).  

## Najlepsze praktyki bezpieczeństwa fundamentów

Implementacje MCP dziedziczą i rozwijają istniejącą postawę bezpieczeństwa Twojej organizacji. Wzmocnienie podstawowych praktyk bezpieczeństwa znacząco zwiększa ogólne bezpieczeństwo systemów AI i wdrożeń MCP.

### Podstawowe fundamenty bezpieczeństwa

#### **Bezpieczne praktyki rozwoju**  
- **Zgodność z OWASP**: Ochrona przed [OWASP Top 10](https://owasp.org/www-project-top-ten/) podatnościami aplikacji webowych  
- **Ochrona specyficzna dla AI**: Wdrażaj kontrole dla [OWASP Top 10 dla LLM](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- **Bezpieczne zarządzanie sekretami**: Używaj dedykowanych sejfów na tokeny, klucze API i wrażliwe dane konfiguracyjne  
- **Szyfrowanie end-to-end**: Zapewnij bezpieczną komunikację we wszystkich komponentach aplikacji i przepływach danych  
- **Walidacja wejścia**: Rygorystyczna walidacja wszystkich danych wejściowych użytkownika, parametrów API i źródeł danych  

#### **Wzmacnianie infrastruktury**  
- **Uwierzytelnianie wieloskładnikowe**: Obowiązkowe MFA dla wszystkich kont administracyjnych i usługowych  
- **Zarządzanie poprawkami**: Automatyczne, terminowe łatanie systemów operacyjnych, frameworków i zależności  
- **Integracja dostawcy tożsamości**: Centralne zarządzanie tożsamością przez dostawców korporacyjnych (Microsoft Entra ID, Active Directory)  
- **Segmentacja sieci**: Logiczna izolacja komponentów MCP w celu ograniczenia potencjału ruchu bocznego  
- **Zasada najmniejszych uprawnień**: Minimalne wymagane uprawnienia dla wszystkich komponentów systemu i kont  

#### **Monitorowanie i wykrywanie zagrożeń**  
- **Kompleksowe logowanie**: Szczegółowe logi aktywności aplikacji AI, w tym interakcji klient-serwer MCP  
- **Integracja SIEM**: Centralne zarządzanie informacjami i zdarzeniami bezpieczeństwa do wykrywania anomalii  
- **Analiza behawioralna**: Monitorowanie oparte na AI do wykrywania nietypowych wzorców zachowań systemu i użytkowników  
- **Wywiad zagrożeń**: Integracja z zewnętrznymi kanałami informacji o zagrożeniach i wskaźnikami kompromitacji (IOC)  
- **Reakcja na incydenty**: Dobrze zdefiniowane procedury wykrywania, reagowania i odzyskiwania po incydentach bezpieczeństwa  

#### **Architektura Zero Trust**  
- **Nigdy nie ufaj, zawsze weryfikuj**: Ciągła weryfikacja użytkowników, urządzeń i połączeń sieciowych  
- **Mikrosegmentacja**: Szczegółowe kontrole sieci izolujące pojedyncze obciążenia i usługi  
- **Bezpieczeństwo oparte na tożsamości**: Polityki bezpieczeństwa oparte na zweryfikowanych tożsamościach, a nie lokalizacji sieciowej  
- **Ciągła ocena ryzyka**: Dynamiczna ocena postawy bezpieczeństwa na podstawie aktualnego kontekstu i zachowań  
- **Dostęp warunkowy**: Kontrole dostępu dostosowujące się do czynników ryzyka, lokalizacji i zaufania do urządzenia  

### Wzorce integracji korporacyjnej

#### **Integracja ekosystemu bezpieczeństwa Microsoft**  
- **Microsoft Defender for Cloud**: Kompleksowe zarządzanie postawą bezpieczeństwa chmury  
- **Azure Sentinel**: Natywne w chmurze SIEM i SOAR do ochrony obciążeń AI  
- **Microsoft Entra ID**: Korporacyjne zarządzanie tożsamością i dostępem z politykami dostępu warunkowego  
- **Azure Key Vault**: Centralne zarządzanie sekretami z wsparciem modułu bezpieczeństwa sprzętowego (HSM)  
- **Microsoft Purview**: Zarządzanie danymi i zgodnością dla źródeł danych i przepływów AI  

#### **Zgodność i zarządzanie**  
- **Zgodność regulacyjna**: Zapewnij, że implementacje MCP spełniają wymagania branżowe (GDPR, HIPAA, SOC 2)  
- **Klasyfikacja danych**: Właściwa kategoryzacja i obsługa danych wrażliwych przetwarzanych przez systemy AI  
- **Ścieżki audytu**: Kompleksowe logowanie dla zgodności regulacyjnej i dochodzeń kryminalistycznych  
- **Kontrole prywatności**: Wdrażanie zasad prywatności od podstaw w architekturze systemów AI  
- **Zarządzanie zmianami**: Formalne procesy przeglądu bezpieczeństwa modyfikacji systemów AI  

Te podstawowe praktyki tworzą solidną bazę bezpieczeństwa, która zwiększa skuteczność specyficznych kontroli MCP i zapewnia kompleksową ochronę aplikacji opartych na AI.

## Kluczowe wnioski dotyczące bezpieczeństwa

- **Wielowarstwowe podejście do bezpieczeństwa**: Łącz podstawowe praktyki bezpieczeństwa (bezpieczne kodowanie, zasada najmniejszych uprawnień, weryfikacja łańcucha dostaw, ciągły monitoring) z kontrolami specyficznymi dla AI dla kompleksowej ochrony  

- **Specyficzny krajobraz zagrożeń AI**: Systemy MCP stoją przed unikalnymi ryzykami, takimi jak wstrzykiwanie promptów, zatruwanie narzędzi, przejmowanie sesji, problemy zdezorientowanego pełnomocnika, luki w przekazywaniu tokenów i nadmierne uprawnienia, które wymagają specjalistycznych środków zaradczych  

- **Doskonałość uwierzytelniania i autoryzacji**: Wdrażaj solidne uwierzytelnianie z użyciem zewnętrznych dostawców tożsamości (Microsoft Entra ID), egzekwuj właściwą walidację tokenów i nigdy nie akceptuj tokenów niewydanych wyraźnie dla Twojego serwera MCP  

- **Zapobieganie atakom na AI**: Wdrażaj Microsoft Prompt Shields i Azure Content Safety, aby bronić się przed pośrednim wstrzykiwaniem promptów i atakami zatruwania narzędzi, jednocześnie weryfikując metadane narzędzi i monitorując dynamiczne zmiany  

- **Bezpieczeństwo sesji i transportu**: Używaj kryptograficznie bezpiecznych, niedeterministycznych identyfikatorów sesji powiązanych z tożsamościami użytkowników, wdrażaj właściwe zarządzanie cyklem życia sesji i nigdy nie używaj sesji do uwierzytelniania  

- **Najlepsze praktyki bezpieczeństwa OAuth**: Zapobiegaj atakom zdezorientowanego pełnomocnika poprzez wyraźną zgodę użytkownika dla dynamicznie rejestrowanych klientów, właściwą implementację OAuth 2.1 z PKCE oraz ścisłą walidację URI przekierowań  

- **Zasady bezpieczeństwa tokenów**: Unikaj antywzorca przekazywania tokenów, waliduj roszczenia odbiorcy tokenów, wdrażaj krótkotrwałe tokeny z bezpieczną rotacją i utrzymuj jasne granice zaufania  

- **Kompleksowe bezpieczeństwo łańcucha dostaw**: Traktuj wszystkie komponenty ekosystemu AI (modele, osadzenia, dostawcy kontekstu, zewnętrzne API) z taką samą rygorystyczną dbałością o bezpieczeństwo jak tradycyjne zależności oprogramowania  

- **Ciągła ewolucja**: Bądź na bieżąco z szybko ewoluującymi specyfikacjami MCP, wnoś wkład do standardów społeczności bezpieczeństwa i utrzymuj adaptacyjną postawę bezpieczeństwa w miarę dojrzewania protokołu  

- **Integracja bezpieczeństwa Microsoft**: Wykorzystuj kompleksowy ekosystem bezpieczeństwa Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) dla zwiększonej ochrony wdrożeń MCP  

## Kompleksowe zasoby

### **Oficjalna dokumentacja bezpieczeństwa MCP**  
- [Specyfikacja MCP (Aktualna: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [Najlepsze praktyki bezpieczeństwa MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)  
- [Specyfikacja autoryzacji MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)  
- [Repozytorium MCP na GitHub](https://github.com/modelcontextprotocol)  

### **Standardy bezpieczeństwa i najlepsze praktyki**  
- [Najlepsze praktyki bezpieczeństwa OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)  
- [OWASP Top 10 bezpieczeństwa aplikacji webowych](https://owasp.org/www-project-top-ten/)  
- [OWASP Top 10 dla dużych modeli językowych](https://genai.owasp.org/download/43299/?tmstv=1731900559)  
- [Microsoft Digital Defense Report](https://aka.ms/mddr)  

### **Badania i analizy bezpieczeństwa AI**  
- [Wstrzykiwanie promptów w MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)  
- [Ataki zatruwania narzędzi (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)  
- [MCP Security Research Briefing (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft Security Solutions**
- [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety Service](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Security](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure Token Management Best Practices](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Implementation Guides & Tutorials**
- [Azure API Management as MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID Authentication with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Secure Token Storage and Encryption (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps & Supply Chain Security**
- [Azure DevOps Security](https://azure.microsoft.com/products/devops)
- [Azure Repos Security](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft Supply Chain Security Journey](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Dodatkowa dokumentacja dotycząca bezpieczeństwa**

Aby uzyskać kompleksowe wskazówki dotyczące bezpieczeństwa, zapoznaj się z tymi specjalistycznymi dokumentami w tej sekcji:

- **[MCP Security Best Practices 2025](./mcp-security-best-practices-2025.md)** - Kompleksowe najlepsze praktyki bezpieczeństwa dla implementacji MCP
- **[Azure Content Safety Implementation](./azure-content-safety-implementation.md)** - Praktyczne przykłady implementacji integracji Azure Content Safety  
- **[MCP Security Controls 2025](./mcp-security-controls-2025.md)** - Najnowsze kontrole i techniki bezpieczeństwa dla wdrożeń MCP
- **[MCP Best Practices Quick Reference](./mcp-best-practices.md)** - Szybki przewodnik po podstawowych praktykach bezpieczeństwa MCP

---

## Co dalej

Następny: [Rozdział 3: Pierwsze kroki](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->