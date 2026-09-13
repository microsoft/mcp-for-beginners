# Studium przypadku: Publikowanie w mediach społecznościowych z agenta za pomocą zdalnego serwera MCP

> **Zastrzeżenie:** Kilka usług i projektów open-source potrafi publikować w sieciach społecznościowych, a zespół może również integrować API każdej sieci bezpośrednio. Poniższy scenariusz jest jednym z przykładów pokazujących, jak można zaprojektować i korzystać z **zdalnego serwera MCP z możliwością zapisu**. Publora to usługa komercyjna z darmowym planem; wzorce opisane tutaj mają zastosowanie do każdego serwera MCP realizującego nieodwracalne działania w imieniu użytkownika.

## Przegląd

Agenci dobrze radzą sobie z tworzeniem szkiców treści, ale słabo z jej publikacją. Model może napisać ogłoszenie prasowe w kilka sekund, a potem praca się zatrzymuje: publikacja oznacza API dla każdej sieci, aplikację OAuth dla każdej sieci i różny zestaw zasad dotyczących mediów dla każdej z nich. Większość zespołów rozwiązuje to, kopiując tekst ręcznie do przeglądarki.

To studium przypadku pokazuje, jak ten ostatni krok można zamknąć za pomocą pojedynczego zdalnego serwera MCP i — co ważniejsze dla każdego budującego taki serwer — jakie decyzje projektowe musi podjąć **serwer z możliwością zapisu**. Odczyt danych jest wyrozumiały. Publikacja nie: błędne wywołanie narzędzia jest widoczne dla odbiorców i nie może być cofnięte.

## Scenariusz

Mały zespół ds. relacji z deweloperami tworzy szkice postów wewnątrz agenta (Claude, VS Code, Cursor — klient nie ma znaczenia). Chcą, aby agent:

- zobaczył, które konta społecznościowe zespół ma połączone,
- utworzył szkic posta i przechował go jako szkic do zatwierdzenia przez człowieka,
- dołączył obraz,
- zaplanował publikację w kilku sieciach na wybrany czas,
- a później raportował wyniki.

Co najważniejsze, chcą, aby agent *nie mógł* przypadkowo opublikować podczas gdy są jeszcze w fazie eksperymentów.

## Użyte narzędzia

- [Publora MCP Server](https://github.com/publora/mcp-server) — zdalny serwer MCP (`streamable-http`) udostępniający narzędzia do publikacji, planowania, zarządzania mediami i analityki LinkedIn. Zarejestrowany w oficjalnym rejestrze MCP jako `com.publora/mcp-server`.

## Przebieg krok po kroku

1. **Podłącz serwer.** Klienci obsługujący OAuth przechodzą przepływ autoryzacji kodu z PKCE na ekranie zgody serwera; klienci bez takiej obsługi, np. CLI bez interfejsu, używają klucza API Publora w nagłówku. Obie ścieżki są obsługiwane, a jaką dostaniesz, zależy od klienta, nie od serwera.
2. **Wyświetl połączenia.** Agent wywołuje `list_connections` i otrzymuje połączone konta wraz z ich identyfikatorami.
3. **Tworzenie szkicu.** Agent wywołuje `create_post` *bez* ustawiania daty publikacji. Post jest zapisywany jako szkic — nic nie jest publikowane.
4. **Dodawanie mediów.** Publiczne URL-e obrazów są przesyłane w tym samym wywołaniu; serwer je pobiera i weryfikuje.
5. **Planowanie.** Po zatwierdzeniu przez człowieka `update_post` ustawia status na zaplanowany z datą w formacie ISO 8601.
6. **Pomiar.** Dla LinkedIn `linkedin_post_stats` zwraca zaangażowanie, gdy post jest już opublikowany.

## Przykładowe polecenie

```text
Which social accounts do I have connected?
Draft a post announcing our new changelog page, attach the screenshot at
https://example.com/changelog.png, and keep it as a draft — do not publish it.
Once I approve, schedule it to LinkedIn and Bluesky for tomorrow at 09:00 UTC.
```

## Schemat Mermaid

```mermaid
flowchart TD
    A[Polecenie użytkownika w kliencie MCP] --> B[Klient wykonuje OAuth z serwerem]
    B --> C[list_connections]
    C --> D{Czy docelowe sieci są połączone?}
    D -- No --> E[Agent zgłasza, które z nich brakują]
    D -- Yes --> F[create_post bez scheduledTime -> szkic]
    F --> G[Człowiek przegląda szkic]
    G -- Approved --> H[update_post: status=scheduled]
    G -- Rejected --> I[delete_post]
    H --> J[Serwer publikuje o zaplanowanym czasie]
    J --> K[linkedin_post_stats dla zaangażowania]
```

## Implementacja techniczna

Lekcje poniżej to przenośna część tego studium przypadku.

### Otwarta odkrywalność, uwierzytelnione wykonywanie

`tools/list` jest dostępne bez poświadczeń; każde `tools/call` wymaga tokenu
i w przeciwnym wypadku zwraca `401` z nagłówkiem `WWW-Authenticate` wskazującym na
metadane chronionego zasobu. Starszy endpoint serwera także odpowiada
na niezweryfikowane `initialize` dla klientów protokołów sprzed
`2026-07-28`; obecni klienci nie używają tego handshake.

Ten podział specyficzny dla serwera umożliwia rejestrom, katalogom i klientom inspekcję nazw narzędzi,
schematów i adnotacji bez sekretu, jednocześnie zapobiegając anonimowemu
wykonaniu. Otwarta odkrywalność to decyzja wdrożeniowa, nie wymóg MCP; wdrożenie
chronione może też wymagać autoryzacji dla `tools/list`.

### Rejestracja: dynamiczna rejestracja klienta i co ją zastępuje

Serwer udostępnia `/.well-known/oauth-protected-resource` oraz `/.well-known/oauth-authorization-server` i obsługuje przepływ autoryzacji kodu z PKCE (`S256`), tokeny odświeżania i **dynamiczną rejestrację klienta**.

Dynamiczna rejestracja usunęła ręczny krok dla klientów starszych: bez niej
każdy klient potrzebował wcześniej wydanego `client_id` od dostawcy.

Traktuj to raczej jako zachowanie kompatybilności niż wzorzec do kopiowania. Wersja specyfikacji z `2026-07-28` wycofuje dynamiczną rejestrację klienta na rzecz Dokumentów Metadanych Klienta (Client ID Metadata Documents), gdzie klient hostuje dokument metadanych pod stabilnym URL HTTPS, a ten URL *jest* `client_id`. Dynamiczna rejestracja dalej działa, ale serwer budowany dziś powinien planować CIMD i utrzymywać dynamiczną rejestrację tylko dla starszych klientów.

### Adnotacje narzędzi to nie dekoracja

Każde narzędzie zawiera `title` oraz odpowiednie wskazówki: `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`.

Są dwa powody, by w nie inwestować. Po pierwsze, klienci korzystają ze wskazówek, by zdecydować, co potwierdzić z użytkownikiem — klient może automatycznie wykonać zapytanie tylko do odczytu i zatrzymać się przed usunięciem do zatwierdzenia. Specyfikacja wyraźnie mówi, że adnotacje to niesprawdzone wskazówki, a nie mechanizm autoryzacji: kształtują, co klient chce zrobić, ale niczego na serwerze nie blokują, a serwer musi i tak egzekwować własne reguły. Po drugie, główne katalogi konektorów teraz *wymagają* ich do przeglądu; serwer bez tytułów i wskazówek dla narzędzi zostanie odrzucony bez względu na jakość działania.

### Spraw, aby identyfikatory nie były wymyślne

Identyfikatory platform to nieprzezroczyste ciągi tekstowe zwracane przez `list_connections`, a opis schematu wyraźnie mówi, że muszą być kopiowane dosłownie i nigdy nie można ich zgadywać. Serwer odrzuca wszystko inne.

Modele są biegłymi zgadywaczami. Każdy serwer z możliwością zapisu powinien zakładać, że identyfikator ostatecznie zostanie zahalucynowany i niech ta ścieżka kończy się głośnym i wczesnym błędem, a nie akcją na wartości, która wygląda wiarygodnie.

### Zakończ przed publikacją z komunikatem możliwym do działania

Niektóre sieci odrzucają posty tylko z tekstem i wymagają obrazu lub wideo. Walidacja następuje podczas planowania, a błąd wskazuje platformę i brakujące wymaganie.

Agent może naprawić sytuację „Instagram wymaga mediów — dołącz obraz lub wideo” bez kolejnej wymiany z serwerem. Nie może się jednak ustabilizować po ogólnym błędzie `400`.

### Uczyń ponawianie bezpiecznym

Dwa narzędzia tworzące treść, `create_post` i `update_post`, akceptują klucz idempotencji: ponowne użycie go z identycznym żądaniem powtarza oryginalną odpowiedź zamiast tworzyć drugi post. Runtime agentów ponawia na timeouty; bez idempotencji wolna odpowiedź staje się podwójną publikacją. Pozostałe narzędzia zapisujące — usuwanie, etapy mediów, reakcje i komentarze LinkedIn — takiego klucza nie przyjmują, więc ponawianie tam nie jest automatycznie bezpieczne. Warto wiedzieć, które własne mutacje są chronione, a które nie.

### Zapewnij sposób na testowanie, które nic nie publikuje


Serwer akceptuje zarezerwowany cel, `publora-playground`, który jest weryfikowany i potwierdzany jak prawdziwy cel, a następnie odrzucany — nic nie trafia do aktywnego konta. Jest to opisane w samym schemacie narzędzia, który każdy klient może odczytać bez uwierzytelnienia: pole `platforms` w `create_post` dokumentuje to jako "cel testu połączenia, który nie wymaga rzeczywistego połączenia — post jest potwierdzany i odrzucany, nic nie jest publikowane". Wywołaj go, przekazując jako jedyny wpis: `platforms: ["publora-playground"]`.

Okazało się, że jest to jeden z najbardziej użytecznych szczegółów całej powierzchni. Recenzenci katalogów konektorów, współtwórcy i CI mogą przetestować pełną ścieżkę zapisu od początku do końca bez ryzyka dla prawdziwej publiczności. Każdy serwer MCP, wykonujący działania nieodwracalne, korzysta z dokumentowanego celu no-op.

## Wyniki i Wpływ

- Krok publikacji przesunięto z przeglądarki do tej samej konwersacji, w której tworzona jest treść, a nawyk rozpoczynania od szkicu utrzymuje człowieka w pętli. Bądź precyzyjny, czym to jest: szkic jest konwencją, a nie granicą. Ten sam kredensjał może zaplanować lub opublikować, więc każdy, kto potrzebuje prawdziwego zatwierdzenia, musi to wymusić poza interfejsem narzędzia — oddzielne kredensjały lub warstwa polityki przed serwerem.
- Różnice między sieciami — wymagania mediów, wątki, kontrola odpowiedzi — są obsługiwane raz na serwerze, a nie w każdym agencie, który się z nim komunikuje.
- Ten sam serwer wspiera kilku klientów MCP bez wcześniejszych kredensjałów.
    Obecne klienty mogą korzystać z Dokumentów Metadanych Client ID; DCR pozostaje zapasem
    dla starszych klientów.
- Powyższe ograniczenia projektowe były formowane zarówno przez recenzje katalogu konektorów, jak i przez użytkowników: adnotacje, OAuth i bezpieczny cel testowy były wymagane przynajmniej przez jednego z nich.

## Odniesienia

- [Publora MCP Server (źródło)](https://github.com/publora/mcp-server)
- [Dokumentacja Publora API i MCP](https://docs.publora.com)
- [Wpis w rejestrze MCP: `com.publora/mcp-server`](https://registry.modelcontextprotocol.io/v0/servers?search=com.publora/mcp-server)
- [Specyfikacja MCP — Autoryzacja](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [Specyfikacja MCP — Adnotacje narzędzi](https://modelcontextprotocol.io/docs/concepts/tools)

## Co Dalej

- Weź serwer MCP, który budujesz i sprawdź trzy najtańsze usprawnienia tutaj: adnotacje na każdym narzędziu, klucz idempotencji na każdym zapisie oraz udokumentowany cel no-op.
- Wypróbuj podział otwartego odkrywania: wywołaj `tools/list` na publicznym zdalnym serwerze bez uwierzytelnienia, a następnie wywołaj narzędzie i sprawdź wyzwanie `401`.
- Zastanów się, co oznacza „cofnij” w twojej domenie. Publikowanie ma szkice i usuwanie; jeśli twoje akcje nie mają odpowiednika, potwierdzenie należy umieścić w projekcie narzędzia, a nie w monicie.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->