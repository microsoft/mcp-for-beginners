# 🚀 10 serwerów Microsoft MCP, które zmieniają produktywność programistów

## 🎯 Czego nauczysz się z tego przewodnika

Ten praktyczny przewodnik przedstawia dziesięć serwerów Microsoft MCP, które aktywnie zmieniają sposób pracy programistów z asystentami AI. Zamiast tylko wyjaśniać, co serwery MCP *mogą* robić, pokażemy Ci serwery, które już teraz realnie wpływają na codzienne procesy tworzenia oprogramowania w Microsoft i poza nim.

Każdy serwer w tym przewodniku został wybrany na podstawie rzeczywistego zastosowania i opinii programistów. Dowiesz się nie tylko, co robi każdy serwer, ale także dlaczego jest ważny i jak najlepiej wykorzystać go w swoich projektach. Niezależnie od tego, czy dopiero zaczynasz z MCP, czy chcesz rozbudować swoje obecne środowisko, te serwery to jedne z najbardziej praktycznych i efektywnych narzędzi dostępnych w ekosystemie Microsoft.

> **💡 Szybka wskazówka na start**
> 
> Jesteś nowy w MCP? Spokojnie! Ten przewodnik jest przyjazny dla początkujących. Wyjaśnimy pojęcia na bieżąco, a w razie potrzeby zawsze możesz wrócić do naszych modułów [Wprowadzenie do MCP](../00-Introduction/README.md) i [Podstawowe koncepcje](../01-CoreConcepts/README.md) dla głębszego zrozumienia.

## Przegląd

Ten obszerny przewodnik omawia dziesięć serwerów Microsoft MCP, które rewolucjonizują sposób, w jaki programiści współpracują z asystentami AI i narzędziami zewnętrznymi. Od zarządzania zasobami Azure po przetwarzanie dokumentów – te serwery pokazują moc Model Context Protocol w tworzeniu płynnych i efektywnych procesów programistycznych.

## Cele nauki

Po zakończeniu tego przewodnika będziesz:
- Rozumieć, jak serwery MCP zwiększają produktywność programistów
- Poznawać najważniejsze implementacje serwerów MCP Microsoftu
- Odkrywać praktyczne zastosowania każdego serwera
- Wiedzieć, jak skonfigurować te serwery w VS Code i Visual Studio
- Poznawać szerszy ekosystem MCP i jego przyszłe kierunki

## 🔧 Zrozumienie serwerów MCP: przewodnik dla początkujących

### Czym są serwery MCP?

Jako początkujący w Model Context Protocol (MCP) możesz się zastanawiać: „Czym dokładnie jest serwer MCP i dlaczego miałbym się tym interesować?” Zacznijmy od prostego porównania.

Pomyśl o serwerach MCP jak o wyspecjalizowanych asystentach, którzy pomagają Twojemu AI wspomagającemu kodowanie (np. GitHub Copilot) łączyć się z zewnętrznymi narzędziami i usługami. Tak jak na telefonie używasz różnych aplikacji do różnych zadań – jedna do pogody, inna do nawigacji, jeszcze inna do bankowości – tak serwery MCP dają Twojemu asystentowi AI możliwość interakcji z różnymi narzędziami i usługami programistycznymi.

### Problem, który rozwiązują serwery MCP

Przed pojawieniem się serwerów MCP, jeśli chciałeś:
- Sprawdzić zasoby Azure
- Utworzyć zgłoszenie na GitHubie
- Wykonać zapytanie do bazy danych
- Przeszukać dokumentację

musiałeś przerwać kodowanie, otworzyć przeglądarkę, wejść na odpowiednią stronę i wykonać te czynności ręcznie. Ciągłe przełączanie kontekstu przerywało Twój flow i obniżało produktywność.

### Jak serwery MCP zmieniają Twoje doświadczenie programistyczne

Dzięki serwerom MCP możesz pozostać w swoim środowisku programistycznym (VS Code, Visual Studio itp.) i po prostu poprosić asystenta AI o wykonanie tych zadań. Na przykład:

**Zamiast tradycyjnego procesu:**
1. Przestań kodować
2. Otwórz przeglądarkę
3. Wejdź na portal Azure
4. Sprawdź szczegóły konta magazynu
5. Wróć do VS Code
6. Kontynuuj kodowanie

**Możesz teraz zrobić to tak:**
1. Zapytaj AI: „Jaki jest status moich kont magazynu Azure?”
2. Kontynuuj kodowanie, mając potrzebne informacje

### Kluczowe korzyści dla początkujących

#### 1. 🔄 **Pozostań w stanie flow**
- Koniec z przełączaniem się między wieloma aplikacjami
- Skup się na pisaniu kodu
- Zmniejsz obciążenie umysłowe związane z zarządzaniem różnymi narzędziami

#### 2. 🤖 **Używaj języka naturalnego zamiast skomplikowanych poleceń**
- Zamiast pamiętać składnię SQL, opisz, jakich danych potrzebujesz
- Zamiast znać polecenia Azure CLI, wyjaśnij, co chcesz osiągnąć
- Pozwól AI zająć się technicznymi szczegółami, a Ty skup się na logice

#### 3. 🔗 **Łącz różne narzędzia**
- Twórz potężne procesy, łącząc różne usługi
- Przykład: „Pobierz wszystkie ostatnie zgłoszenia z GitHub i utwórz odpowiadające im zadania w Azure DevOps”
- Buduj automatyzację bez pisania skomplikowanych skryptów

#### 4. 🌐 **Korzystaj z rosnącego ekosystemu**
- Wykorzystuj serwery tworzone przez Microsoft, GitHub i inne firmy
- Łącz narzędzia różnych dostawców bezproblemowo
- Dołącz do ustandaryzowanego ekosystemu działającego z różnymi asystentami AI

#### 5. 🛠️ **Ucz się przez praktykę**
- Zacznij od gotowych serwerów, by zrozumieć koncepcje
- Stopniowo twórz własne serwery, gdy nabierzesz pewności
- Korzystaj z dostępnych SDK i dokumentacji, które pomogą Ci w nauce

### Przykład z życia dla początkujących

Załóżmy, że dopiero zaczynasz z web developmentem i pracujesz nad pierwszym projektem. Oto jak serwery MCP mogą pomóc:

**Tradycyjne podejście:**
```
1. Code a feature
2. Open browser → Navigate to GitHub
3. Create an issue for testing
4. Open another tab → Check Azure docs for deployment
5. Open third tab → Look up database connection examples
6. Return to VS Code
7. Try to remember what you were doing
```

**Z serwerami MCP:**
```
1. Code a feature
2. Ask AI: "Create a GitHub issue for testing this login feature"
3. Ask AI: "How do I deploy this to Azure according to the docs?"
4. Ask AI: "Show me the best way to connect to my database"
5. Continue coding with all the information you need
```

### Przewaga standardu korporacyjnego

MCP staje się standardem branżowym, co oznacza:
- **Spójność**: Podobne doświadczenie w różnych narzędziach i firmach
- **Współpraca**: Serwery różnych dostawców działają razem
- **Przyszłościowość**: Umiejętności i konfiguracje przenoszą się między różnymi asystentami AI
- **Społeczność**: Duży ekosystem dzielący się wiedzą i zasobami

### Od czego zacząć: czego się nauczysz

W tym przewodniku omówimy 10 serwerów Microsoft MCP, które są szczególnie przydatne dla programistów na każdym poziomie. Każdy serwer został zaprojektowany, by:
- Rozwiązywać typowe wyzwania programistyczne
- Redukować powtarzalne zadania
- Poprawiać jakość kodu
- Zwiększać możliwości nauki

> **💡 Wskazówka do nauki**
> 
> Jeśli jesteś całkowicie nowy w MCP, zacznij od naszych modułów [Wprowadzenie do MCP](../00-Introduction/README.md) i [Podstawowe koncepcje](../01-CoreConcepts/README.md). Następnie wróć tutaj, aby zobaczyć te koncepcje w praktyce na przykładach narzędzi Microsoft.
>
> Dla dodatkowego kontekstu na temat znaczenia MCP, zobacz wpis Marii Naggagi: [Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## Rozpoczęcie pracy z MCP w VS Code i Visual Studio 🚀

Konfiguracja tych serwerów MCP jest prosta, jeśli korzystasz z Visual Studio Code lub Visual Studio 2022 z GitHub Copilot.

### Konfiguracja VS Code

Oto podstawowy proces dla VS Code:

1. **Włącz tryb agenta**: W VS Code przełącz się na tryb agenta w oknie Copilot Chat
2. **Skonfiguruj serwery MCP**: Dodaj konfiguracje serwerów do pliku settings.json w VS Code
3. **Uruchom serwery**: Kliknij przycisk „Start” przy każdym serwerze, którego chcesz używać
4. **Wybierz narzędzia**: Wybierz, które serwery MCP mają być aktywne w bieżącej sesji

Szczegółowe instrukcje konfiguracji znajdziesz w [dokumentacji MCP dla VS Code](https://code.visualstudio.com/docs/copilot/copilot-mcp).

> **💡 Profesjonalna wskazówka: zarządzaj serwerami MCP jak ekspert!**
> 
> Widok rozszerzeń VS Code zawiera teraz [wygodny interfejs do zarządzania zainstalowanymi serwerami MCP](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)! Masz szybki dostęp do uruchamiania, zatrzymywania i zarządzania dowolnym serwerem MCP za pomocą przejrzystego i prostego interfejsu. Wypróbuj!

### Konfiguracja Visual Studio 2022

Dla Visual Studio 2022 (wersja 17.14 lub nowsza):

1. **Włącz tryb agenta**: Kliknij rozwijane menu „Ask” w oknie GitHub Copilot Chat i wybierz „Agent”
2. **Utwórz plik konfiguracyjny**: Stwórz plik `.mcp.json` w katalogu rozwiązania (zalecane miejsce: `<SOLUTIONDIR>\.mcp.json`)
3. **Skonfiguruj serwery**: Dodaj konfiguracje serwerów MCP w standardowym formacie MCP
4. **Zatwierdź narzędzia**: Po wyświetleniu monitu zatwierdź narzędzia, których chcesz używać, nadając odpowiednie uprawnienia

Szczegółowe instrukcje konfiguracji Visual Studio znajdziesz w [dokumentacji MCP dla Visual Studio](https://learn.microsoft.com/visualstudio/ide/mcp-servers).

Każdy serwer MCP ma własne wymagania konfiguracyjne (łańcuchy połączeń, uwierzytelnianie itp.), ale schemat konfiguracji jest spójny w obu środowiskach.

## Lekcje wyniesione z serwerów Microsoft MCP 🛠️

### 1. 📚 Serwer Microsoft Learn Docs MCP

[![Zainstaluj w VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Zainstaluj w VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Co robi**: Serwer Microsoft Learn Docs MCP to usługa hostowana w chmurze, która zapewnia asystentom AI dostęp w czasie rzeczywistym do oficjalnej dokumentacji Microsoft za pośrednictwem Model Context Protocol. Łączy się z `https://learn.microsoft.com/api/mcp` i umożliwia semantyczne wyszukiwanie w Microsoft Learn, dokumentacji Azure, Microsoft 365 oraz innych oficjalnych źródłach Microsoft.

**Dlaczego jest przydatny**: Choć może się wydawać, że to „tylko dokumentacja”, ten serwer jest kluczowy dla każdego programisty korzystającego z technologii Microsoft. Jedną z największych skarg programistów .NET na asystentów AI jest to, że nie są oni na bieżąco z najnowszymi wersjami .NET i C#. Serwer Microsoft Learn Docs MCP rozwiązuje ten problem, zapewniając dostęp w czasie rzeczywistym do najnowszej dokumentacji, referencji API i najlepszych praktyk. Niezależnie od tego, czy pracujesz z najnowszymi SDK Azure, eksplorujesz nowe funkcje C# 13, czy wdrażasz nowatorskie wzorce .NET Aspire, ten serwer gwarantuje, że Twój asystent AI ma dostęp do autorytatywnych, aktualnych informacji potrzebnych do generowania dokładnego i nowoczesnego kodu.

**Zastosowanie w praktyce**: „Jakie są polecenia az cli do utworzenia aplikacji kontenerowej Azure zgodnie z oficjalną dokumentacją Microsoft Learn?” lub „Jak skonfigurować Entity Framework z dependency injection w ASP.NET Core?” A może „Przejrzyj ten kod, aby upewnić się, że spełnia zalecenia dotyczące wydajności z dokumentacji Microsoft Learn.” Serwer zapewnia kompleksowe pokrycie Microsoft Learn, dokumentacji Azure i Microsoft 365, wykorzystując zaawansowane wyszukiwanie semantyczne, by znaleźć najbardziej kontekstowo odpowiednie informacje. Zwraca do 10 wysokiej jakości fragmentów treści z tytułami artykułów i linkami, zawsze korzystając z najnowszej dokumentacji Microsoft, gdy tylko zostanie opublikowana.

**Przykład**: Serwer udostępnia narzędzie `microsoft_docs_search`, które wykonuje wyszukiwanie semantyczne w oficjalnej dokumentacji technicznej Microsoft. Po konfiguracji możesz zadawać pytania typu „Jak zaimplementować uwierzytelnianie JWT w ASP.NET Core?” i otrzymywać szczegółowe, oficjalne odpowiedzi z linkami do źródeł. Jakość wyszukiwania jest wyjątkowa, ponieważ rozumie kontekst – pytanie o „kontenery” w kontekście Azure zwróci dokumentację Azure Container Instances, podczas gdy to samo słowo w kontekście .NET zwróci informacje o kolekcjach C#.

To szczególnie przydatne w przypadku szybko zmieniających się lub niedawno zaktualizowanych bibliotek i zastosowań. Na przykład w ostatnich projektach kodowania chciałem wykorzystać funkcje najnowszych wydań .NET Aspire i Microsoft.Extensions.AI. Dzięki dołączeniu serwera Microsoft Learn Docs MCP mogłem korzystać nie tylko z dokumentacji API, ale także z przewodników i instrukcji, które właśnie zostały opublikowane.
> **💡 Przydatna wskazówka**
> 
> Nawet modele przyjazne narzędziom potrzebują zachęty do korzystania z narzędzi MCP! Rozważ dodanie systemowego promptu lub [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) w stylu: „Masz dostęp do `microsoft.docs.mcp` – używaj tego narzędzia, aby wyszukiwać najnowszą oficjalną dokumentację Microsoft podczas rozwiązywania pytań dotyczących technologii Microsoft, takich jak C#, Azure, ASP.NET Core czy Entity Framework.”
>
> Aby zobaczyć świetny przykład takiego zastosowania, sprawdź [tryb czatu C# .NET Janitor](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) z repozytorium Awesome GitHub Copilot. Ten tryb wykorzystuje serwer Microsoft Learn Docs MCP, aby pomóc w oczyszczaniu i modernizacji kodu C# z użyciem najnowszych wzorców i najlepszych praktyk.
### 2. ☁️ Azure MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Co robi**: Azure MCP Server to kompleksowy zestaw ponad 15 wyspecjalizowanych konektorów do usług Azure, które integrują cały ekosystem Azure z Twoim workflow AI. To nie jest tylko pojedynczy serwer – to potężna kolekcja obejmująca zarządzanie zasobami, łączność z bazami danych (PostgreSQL, SQL Server), analizę logów Azure Monitor za pomocą KQL, integrację z Cosmos DB i wiele więcej.

**Dlaczego jest przydatny**: Poza samym zarządzaniem zasobami Azure, ten serwer znacząco poprawia jakość kodu podczas pracy z Azure SDK. Korzystając z Azure MCP w trybie Agent, nie tylko pomaga pisać kod – pomaga pisać *lepszy* kod Azure, który stosuje aktualne wzorce uwierzytelniania, najlepsze praktyki obsługi błędów i wykorzystuje najnowsze funkcje SDK. Zamiast otrzymywać ogólny kod, który może działać, dostajesz kod zgodny z zalecanymi wzorcami Azure dla środowisk produkcyjnych.

**Kluczowe moduły obejmują**:
- **🗄️ Konektory baz danych**: Bezpośredni dostęp w naturalnym języku do Azure Database for PostgreSQL i SQL Server
- **📊 Azure Monitor**: Analiza logów i wgląd operacyjny z wykorzystaniem KQL
- **🌐 Zarządzanie zasobami**: Pełne zarządzanie cyklem życia zasobów Azure
- **🔐 Uwierzytelnianie**: Wzorce DefaultAzureCredential i managed identity
- **📦 Usługi storage**: Operacje na Blob Storage, Queue Storage i Table Storage
- **🚀 Usługi kontenerowe**: Zarządzanie Azure Container Apps, Container Instances i AKS
- **I wiele innych wyspecjalizowanych konektorów**

**Przykłady zastosowań w praktyce**: „Wypisz moje konta storage w Azure”, „Zapytaj moje Log Analytics o błędy z ostatniej godziny” lub „Pomóż mi zbudować aplikację Azure w Node.js z poprawnym uwierzytelnianiem”.

**Pełny scenariusz demonstracyjny**: Oto kompletny przewodnik pokazujący moc połączenia Azure MCP z rozszerzeniem GitHub Copilot for Azure w VS Code. Gdy masz oba zainstalowane i wpiszesz:

> „Utwórz skrypt w Pythonie, który przesyła plik do Azure Blob Storage, używając uwierzytelniania DefaultAzureCredential. Skrypt powinien połączyć się z moim kontem storage o nazwie 'mycompanystorage', przesłać plik do kontenera 'documents', utworzyć plik testowy z aktualnym znacznikiem czasu do przesłania, obsłużyć błędy w sposób łagodny i zapewnić informacyjne wyjście, stosować najlepsze praktyki Azure dotyczące uwierzytelniania i obsługi błędów, zawierać komentarze wyjaśniające działanie uwierzytelniania DefaultAzureCredential oraz być dobrze zorganizowany z odpowiednimi funkcjami i dokumentacją.”

Azure MCP Server wygeneruje kompletny, gotowy do produkcji skrypt w Pythonie, który:
- Używa najnowszego SDK Azure Blob Storage z właściwymi wzorcami asynchronicznymi
- Implementuje DefaultAzureCredential z wyczerpującym wyjaśnieniem łańcucha awaryjnego
- Zawiera solidną obsługę błędów z uwzględnieniem specyficznych typów wyjątków Azure
- Stosuje najlepsze praktyki Azure SDK dotyczące zarządzania zasobami i połączeniami
- Zapewnia szczegółowe logowanie i informacyjne wyjście na konsolę
- Tworzy dobrze zorganizowany skrypt z funkcjami, dokumentacją i wskazówkami typów

Co jest wyjątkowe, to fakt, że bez Azure MCP mógłbyś otrzymać ogólny kod do blob storage, który działa, ale nie stosuje aktualnych wzorców Azure. Z Azure MCP dostajesz kod wykorzystujący najnowsze metody uwierzytelniania, obsługujący specyficzne scenariusze błędów Azure i zgodny z zaleceniami Microsoftu dla aplikacji produkcyjnych.

**Przykład z życia**: Miałem problem z zapamiętaniem konkretnych poleceń `az` i `azd` do ad-hoc użycia. Zawsze to był dla mnie proces dwustopniowy: najpierw sprawdzenie składni, potem uruchomienie polecenia. Często po prostu wchodziłem na portal i klikałem, bo nie chciałem przyznać, że nie pamiętam składni CLI. Możliwość opisania tego, co chcę zrobić, jest niesamowita, a jeszcze lepiej móc to zrobić bez wychodzenia z IDE!

W repozytorium [Azure MCP](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server) znajdziesz świetną listę przypadków użycia, które pomogą Ci zacząć. Kompleksowe przewodniki instalacji i zaawansowane opcje konfiguracji znajdziesz w [oficjalnej dokumentacji Azure MCP](https://learn.microsoft.com/azure/developer/azure-mcp-server/).

### 3. 🐙 GitHub MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**Co robi**: Oficjalny GitHub MCP Server zapewnia płynną integrację z całym ekosystemem GitHub, oferując zarówno zdalny dostęp hostowany, jak i lokalne wdrożenie przez Dockera. To nie tylko podstawowe operacje na repozytoriach – to kompleksowe narzędzie obejmujące zarządzanie GitHub Actions, workflow pull requestów, śledzenie issue, skanowanie bezpieczeństwa, powiadomienia i zaawansowaną automatyzację.

**Dlaczego jest przydatny**: Ten serwer zmienia sposób, w jaki korzystasz z GitHub, przenosząc pełne doświadczenie platformy bezpośrednio do Twojego środowiska programistycznego. Zamiast ciągłego przełączania się między VS Code a GitHub.com w celu zarządzania projektami, przeglądu kodu i monitorowania CI/CD, możesz wszystko obsługiwać za pomocą poleceń w naturalnym języku, pozostając skupionym na kodzie.

> **ℹ️ Note: Różne typy „Agentów”**
> 
> Nie myl tego GitHub MCP Server z GitHub Coding Agent (agentem AI, któremu można przypisywać issue do automatycznych zadań kodowania). GitHub MCP Server działa w trybie Agent w VS Code, zapewniając integrację z API GitHub, podczas gdy GitHub Coding Agent to osobna funkcja tworząca pull requesty po przypisaniu do issue.

**Kluczowe możliwości obejmują**:
- **⚙️ GitHub Actions**: Kompleksowe zarządzanie pipeline CI/CD, monitorowanie workflow i obsługa artefaktów
- **🔀 Pull Requests**: Tworzenie, przegląd, scalanie i zarządzanie PR z pełnym śledzeniem statusu
- **🐛 Issues**: Pełne zarządzanie cyklem życia issue, komentowanie, etykietowanie i przypisywanie
- **🔒 Bezpieczeństwo**: Alerty skanowania kodu, wykrywanie sekretów i integracja z Dependabot
- **🔔 Powiadomienia**: Inteligentne zarządzanie powiadomieniami i kontrola subskrypcji repozytoriów
- **📁 Zarządzanie repozytoriami**: Operacje na plikach, zarządzanie gałęziami i administracja repozytorium
- **👥 Współpraca**: Wyszukiwanie użytkowników i organizacji, zarządzanie zespołami i kontrola dostępu

**Przykłady zastosowań w praktyce**: „Utwórz pull request z mojej gałęzi feature”, „Pokaż wszystkie nieudane uruchomienia CI w tym tygodniu”, „Wypisz otwarte alerty bezpieczeństwa dla moich repozytoriów” lub „Znajdź wszystkie issue przypisane do mnie w moich organizacjach”.

**Pełny scenariusz demonstracyjny**: Oto potężny workflow pokazujący możliwości GitHub MCP Server:

> „Muszę przygotować się do przeglądu sprintu. Pokaż mi wszystkie pull requesty, które utworzyłem w tym tygodniu, sprawdź status naszych pipeline’ów CI/CD, stwórz podsumowanie alertów bezpieczeństwa, które musimy rozwiązać, i pomóż mi przygotować notatki do wydania na podstawie scalonych PR z etykietą 'feature'.”

GitHub MCP Server:
- Pobierze Twoje ostatnie pull requesty z szczegółowymi informacjami o statusie
- Przeanalizuje uruchomienia workflow i wyróżni wszelkie błędy lub problemy z wydajnością
- Skonsoliduje wyniki skanowania bezpieczeństwa i priorytetyzuje krytyczne alerty
- Wygeneruje kompleksowe notatki do wydania, wyciągając informacje ze scalonych PR
- Zaproponuje konkretne kroki do planowania sprintu i przygotowania wydania

**Przykład z życia**: Uwielbiam używać tego do workflow przeglądu kodu. Zamiast przeskakiwać między VS Code, powiadomieniami GitHub i stronami pull requestów, mogę powiedzieć „Pokaż mi wszystkie PR czekające na moją recenzję”, a potem „Dodaj komentarz do PR #123 z pytaniem o obsługę błędów w metodzie uwierzytelniania.” Serwer obsługuje wywołania API GitHub, utrzymuje kontekst dyskusji i pomaga tworzyć bardziej konstruktywne komentarze recenzji.

**Opcje uwierzytelniania**: Serwer obsługuje zarówno OAuth (bezproblemowo w VS Code), jak i Personal Access Tokens, z konfigurowalnym zestawem narzędzi, aby włączyć tylko potrzebną funkcjonalność GitHub. Możesz uruchomić go jako usługę zdalną dla szybkiej konfiguracji lub lokalnie przez Dockera, aby mieć pełną kontrolę.

> **💡 Pro Tip**
> 
> Włączaj tylko te zestawy narzędzi, których potrzebujesz, konfigurując parametr `--toolsets` w ustawieniach MCP, aby zmniejszyć rozmiar kontekstu i poprawić dobór narzędzi AI. Na przykład dodaj `"--toolsets", "repos,issues,pull_requests,actions"` do argumentów konfiguracji MCP dla podstawowych workflow deweloperskich lub użyj `"--toolsets", "notifications, security"`, jeśli głównie chcesz monitorować GitHub.

### 4. 🔄 Azure DevOps MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**Co robi**: Łączy się z usługami Azure DevOps, oferując kompleksowe zarządzanie projektami, śledzenie elementów pracy, zarządzanie pipeline’ami buildów oraz operacje na repozytoriach.

**Dlaczego jest przydatny**: Dla zespołów korzystających z Azure DevOps jako głównej platformy DevOps, ten MCP server eliminuje konieczność ciągłego przełączania się między środowiskiem programistycznym a interfejsem webowym Azure DevOps. Możesz zarządzać elementami pracy, sprawdzać status buildów, przeszukiwać repozytoria i realizować zadania projektowe bezpośrednio z poziomu asystenta AI.

**Przykłady zastosowań w praktyce**: „Pokaż mi wszystkie aktywne elementy pracy w bieżącym sprincie dla projektu WebApp”, „Utwórz raport błędu dotyczący problemu z logowaniem, który właśnie znalazłem” lub „Sprawdź status naszych pipeline’ów buildów i pokaż ostatnie niepowodzenia”.

**Przykład z życia**: Łatwo sprawdzisz status bieżącego sprintu zespołu za pomocą prostego zapytania, np. „Pokaż mi wszystkie aktywne elementy pracy w bieżącym sprincie dla projektu WebApp” lub „Utwórz raport błędu dotyczący problemu z logowaniem, który właśnie znalazłem” bez wychodzenia ze środowiska programistycznego.

### 5. 📝 MarkItDown MCP Server
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**Co robi**: MarkItDown to kompleksowy serwer konwersji dokumentów, który przekształca różne formaty plików w wysokiej jakości Markdown, zoptymalizowany pod kątem wykorzystania przez LLM oraz procesy analizy tekstu.

**Dlaczego jest przydatny**: Niezbędny w nowoczesnych procesach dokumentacyjnych! MarkItDown obsługuje imponujący zakres formatów plików, jednocześnie zachowując kluczową strukturę dokumentu, taką jak nagłówki, listy, tabele i linki. W przeciwieństwie do prostych narzędzi do ekstrakcji tekstu, skupia się na zachowaniu semantycznego znaczenia i formatowania, które są wartościowe zarówno dla przetwarzania AI, jak i czytelności dla ludzi.

**Obsługiwane formaty plików**:
- **Dokumenty biurowe**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **Pliki multimedialne**: Obrazy (z metadanymi EXIF i OCR), Audio (z metadanymi EXIF i transkrypcją mowy)
- **Zawartość internetowa**: HTML, kanały RSS, adresy URL YouTube, strony Wikipedii
- **Formaty danych**: CSV, JSON, XML, pliki ZIP (przetwarzane rekurencyjnie)
- **Formaty publikacji**: EPub, notatniki Jupyter (.ipynb)
- **E-mail**: wiadomości Outlook (.msg)
- **Zaawansowane**: integracja z Azure Document Intelligence dla ulepszonego przetwarzania PDF

**Zaawansowane możliwości**: MarkItDown wspiera opisy obrazów generowane przez LLM (gdy dostępny jest klient OpenAI), Azure Document Intelligence dla lepszego przetwarzania PDF, transkrypcję audio dla treści mówionych oraz system wtyczek do rozszerzania obsługi dodatkowych formatów plików.

**Przykłady zastosowań w praktyce**: „Przekonwertuj tę prezentację PowerPoint na Markdown dla naszej strony dokumentacji”, „Wyodrębnij tekst z tego PDF zachowując odpowiednią strukturę nagłówków” lub „Przekształć ten arkusz Excel w czytelny format tabeli”.

**Przykład z dokumentacji**: Cytując [MarkItDown docs](https://github.com/microsoft/markitdown#why-markdown):

> Markdown jest bardzo zbliżony do zwykłego tekstu, z minimalnym markupem lub formatowaniem, ale nadal pozwala na przedstawienie ważnej struktury dokumentu. Popularne LLM, takie jak GPT-4o od OpenAI, natywnie „mówią” Markdownem i często włączają Markdown do swoich odpowiedzi bez wyraźnego polecenia. Sugeruje to, że były trenowane na ogromnych ilościach tekstu sformatowanego w Markdown i dobrze go rozumieją. Dodatkowo, konwencje Markdown są bardzo efektywne pod względem tokenów.

MarkItDown świetnie zachowuje strukturę dokumentu, co jest ważne dla procesów AI. Na przykład podczas konwersji prezentacji PowerPoint zachowuje organizację slajdów z odpowiednimi nagłówkami, wyodrębnia tabele jako tabele Markdown, dodaje tekst alternatywny do obrazów, a nawet przetwarza notatki prelegenta. Wykresy są konwertowane na czytelne tabele danych, a wynikowy Markdown utrzymuje logiczny przepływ oryginalnej prezentacji. To czyni go idealnym do przekazywania zawartości prezentacji do systemów AI lub tworzenia dokumentacji na podstawie istniejących slajdów.

### 6. 🗃️ SQL Server MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Co robi**: Umożliwia konwersacyjne korzystanie z baz danych SQL Server (lokalnych, Azure SQL lub Fabric)

**Dlaczego jest przydatny**: Podobny do serwera PostgreSQL, ale dla ekosystemu Microsoft SQL. Połącz się za pomocą prostego connection string i zacznij zadawać zapytania w naturalnym języku – koniec z przełączaniem kontekstu!

**Przykłady zastosowań w praktyce**: „Znajdź wszystkie zamówienia, które nie zostały zrealizowane w ciągu ostatnich 30 dni” jest tłumaczone na odpowiednie zapytania SQL i zwraca sformatowane wyniki.

**Przykład z życia**: Po skonfigurowaniu połączenia z bazą danych możesz od razu zacząć rozmawiać ze swoimi danymi. W poście na blogu pokazano to na prostym pytaniu: „z jaką bazą danych jesteś połączony?” Serwer MCP odpowiada, wywołując odpowiednie narzędzie bazodanowe, łącząc się z instancją SQL Server i zwracając szczegóły aktualnego połączenia – wszystko bez pisania ani jednej linii SQL. Serwer obsługuje kompleksowe operacje na bazie danych, od zarządzania schematem po manipulację danymi, wszystko za pomocą poleceń w naturalnym języku. Pełne instrukcje konfiguracji i przykłady z VS Code i Claude Desktop znajdziesz tutaj: [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).

### 7. 🎭 Playwright MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**Co robi**: Umożliwia agentom AI interakcję ze stronami internetowymi w celach testowania i automatyzacji

> **ℹ️ Napędza GitHub Copilot**
> 
> Playwright MCP Server zasila Coding Agent GitHub Copilot, dając mu możliwości przeglądania stron internetowych! [Dowiedz się więcej o tej funkcji](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**Dlaczego jest przydatny**: Idealny do automatycznych testów opartych na opisach w naturalnym języku. AI może nawigować po stronach, wypełniać formularze i wyciągać dane za pomocą ustrukturyzowanych zrzutów dostępności – to naprawdę potężne narzędzie!

**Przykłady zastosowań w praktyce**: „Przetestuj proces logowania i sprawdź, czy pulpit ładuje się poprawnie” lub „Wygeneruj test, który wyszukuje produkty i weryfikuje stronę wyników” – wszystko bez potrzeby dostępu do kodu źródłowego aplikacji.

**Przykład z życia**: Moja koleżanka Debbie O'Brien ostatnio robi niesamowitą robotę z Playwright MCP Server! Na przykład pokazała, jak można wygenerować kompletne testy Playwright bez dostępu do kodu źródłowego aplikacji. W jej scenariuszu poprosiła Copilota o stworzenie testu dla aplikacji do wyszukiwania filmów: przejdź na stronę, wyszukaj „Garfield” i sprawdź, czy film pojawia się w wynikach. MCP uruchomił sesję przeglądarki, zbadał strukturę strony za pomocą zrzutów DOM, znalazł odpowiednie selektory i wygenerował w pełni działający test w TypeScript, który przeszedł za pierwszym razem.

Co czyni to naprawdę potężnym, to fakt, że łączy instrukcje w naturalnym języku z wykonywalnym kodem testowym. Tradycyjne podejścia wymagają albo ręcznego pisania testów, albo dostępu do kodu źródłowego dla kontekstu. Dzięki Playwright MCP możesz testować zewnętrzne strony, aplikacje klienckie lub pracować w scenariuszach testów black-box, gdzie dostęp do kodu nie jest możliwy.

### 8. 💻 Dev Box MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Co robi**: Zarządza środowiskami Microsoft Dev Box za pomocą naturalnego języka

**Dlaczego jest przydatny**: Znacznie upraszcza zarządzanie środowiskami deweloperskimi! Twórz, konfiguruj i zarządzaj środowiskami bez konieczności pamiętania konkretnych poleceń.

**Przykłady zastosowań w praktyce**: „Utwórz nowy Dev Box z najnowszym .NET SDK i skonfiguruj go pod nasz projekt”, „Sprawdź status wszystkich moich środowisk deweloperskich” lub „Stwórz ustandaryzowane środowisko demo na prezentacje zespołowe”.

**Przykład z życia**: Jestem wielkim fanem korzystania z Dev Box do pracy osobistej. Moment olśnienia miałem, gdy James Montemagno wyjaśnił, jak świetny jest Dev Box do prezentacji na konferencjach, ponieważ ma superszybkie połączenie ethernetowe, niezależnie od sieci konferencyjnej, hotelowej czy samolotowej, z której korzystam. Właściwie niedawno ćwiczyłem demo konferencyjne, gdy mój laptop był podłączony do hotspotu telefonu podczas jazdy autobusem z Brugii do Antwerpii! Moim kolejnym krokiem jest zarządzanie wieloma środowiskami zespołowymi i ustandaryzowanymi środowiskami demo. Kolejnym popularnym zastosowaniem, o którym słyszałem od klientów i współpracowników, jest używanie Dev Box do prekonfigurowanych środowisk deweloperskich. W obu przypadkach korzystanie z MCP do konfiguracji i zarządzania Dev Boxami pozwala na interakcję w naturalnym języku, pozostając cały czas w środowisku deweloperskim.

### 9. 🤖 Azure AI Foundry MCP Server
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_AI_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_AI_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**Co robi**: Azure AI Foundry MCP Server zapewnia deweloperom kompleksowy dostęp do ekosystemu AI Azure, w tym katalogów modeli, zarządzania wdrożeniami, indeksowania wiedzy za pomocą Azure AI Search oraz narzędzi do oceny. Ten eksperymentalny serwer łączy rozwój AI z potężną infrastrukturą AI Azure, ułatwiając budowanie, wdrażanie i ocenę aplikacji AI.

**Dlaczego jest przydatny**: Ten serwer zmienia sposób pracy z usługami Azure AI, wprowadzając zaawansowane możliwości AI bezpośrednio do Twojego środowiska deweloperskiego. Zamiast przełączać się między portalem Azure, dokumentacją i IDE, możesz odkrywać modele, wdrażać usługi, zarządzać bazami wiedzy i oceniać wydajność AI za pomocą poleceń w naturalnym języku. Jest szczególnie przydatny dla deweloperów tworzących aplikacje RAG (Retrieval-Augmented Generation), zarządzających wdrożeniami wielu modeli lub implementujących kompleksowe procesy oceny AI.

**Kluczowe możliwości dla deweloperów**:
- **🔍 Odkrywanie i wdrażanie modeli**: Przeglądaj katalog modeli Azure AI Foundry, uzyskuj szczegółowe informacje o modelach wraz z przykładami kodu i wdrażaj modele do usług Azure AI
- **📚 Zarządzanie wiedzą**: Twórz i zarządzaj indeksami Azure AI Search, dodawaj dokumenty, konfiguruj indeksatory i buduj zaawansowane systemy RAG
- **⚡ Integracja agentów AI**: Łącz się z agentami Azure AI, zapytuj istniejące agenty i oceniaj ich wydajność w scenariuszach produkcyjnych
- **📊 Ramy oceny**: Przeprowadzaj kompleksowe oceny tekstowe i agentów, generuj raporty w formacie markdown oraz wdrażaj kontrolę jakości aplikacji AI
- **🚀 Narzędzia do prototypowania**: Otrzymuj instrukcje konfiguracji dla prototypowania opartego na GitHub oraz dostęp do Azure AI Foundry Labs z najnowszymi modelami badawczymi

**Przykłady zastosowań w praktyce**: „Wdroż model Phi-4 do usług Azure AI dla mojej aplikacji”, „Utwórz nowy indeks wyszukiwania dla mojego systemu RAG dokumentacji”, „Oceń odpowiedzi mojego agenta względem metryk jakości” lub „Znajdź najlepszy model rozumowania do moich złożonych zadań analitycznych”.

**Pełny scenariusz demonstracyjny**: Oto potężny workflow rozwoju AI:


> „Tworzę agenta wsparcia klienta. Pomóż mi znaleźć dobry model rozumowania w katalogu, wdrożyć go do usług Azure AI, stworzyć bazę wiedzy z naszej dokumentacji, skonfigurować ramy oceny do testowania jakości odpowiedzi, a następnie pomóż mi prototypować integrację z tokenem GitHub do testów.”

Azure AI Foundry MCP Server:
- Zapytuje katalog modeli, aby polecić optymalne modele rozumowania na podstawie Twoich wymagań
- Dostarcza polecenia wdrożenia i informacje o limitach dla wybranego regionu Azure
- Konfiguruje indeksy Azure AI Search z odpowiednim schematem dla Twojej dokumentacji
- Ustawia pipeline’y oceny z metrykami jakości i kontrolami bezpieczeństwa
- Generuje kod prototypowy z uwierzytelnianiem GitHub do natychmiastowego testowania
- Zapewnia kompleksowe przewodniki konfiguracji dostosowane do Twojego stosu technologicznego

**Przykład z życia**: Jako deweloper miałem problem z nadążaniem za różnymi modelami LLM. Znam kilka głównych, ale czułem, że tracę na produktywności i efektywności. Tokeny i limity są stresujące i trudne do zarządzania – nigdy nie wiem, czy wybieram odpowiedni model do zadania, czy marnuję budżet. Usłyszałem o tym MCP Server od Jamesa Montemagno, gdy pytałem kolegów o rekomendacje, i jestem podekscytowany, by go wypróbować! Możliwości odkrywania modeli wyglądają szczególnie imponująco dla kogoś takiego jak ja, kto chce wyjść poza standardowe modele i znaleźć te zoptymalizowane do konkretnych zadań. Ramy oceny pomogą mi zweryfikować, czy faktycznie osiągam lepsze wyniki, a nie tylko próbuję czegoś nowego dla samego eksperymentu.

> **ℹ️ Status eksperymentalny**
> 
> Ten MCP server jest eksperymentalny i jest aktywnie rozwijany. Funkcje i API mogą ulec zmianie. Idealny do eksploracji możliwości Azure AI i tworzenia prototypów, ale należy zweryfikować stabilność przed użyciem produkcyjnym.

### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**Co robi**: Dostarcza deweloperom niezbędne narzędzia do tworzenia agentów AI i aplikacji integrujących się z Microsoft 365 i Microsoft 365 Copilot, w tym walidację schematów, pobieranie przykładowego kodu oraz pomoc w rozwiązywaniu problemów.

**Dlaczego jest przydatny**: Tworzenie dla Microsoft 365 i Copilot wymaga pracy z złożonymi schematami manifestów i specyficznymi wzorcami rozwoju. Ten MCP server wprowadza kluczowe zasoby deweloperskie bezpośrednio do Twojego środowiska kodowania, pomagając w walidacji schematów, znajdowaniu przykładów kodu i rozwiązywaniu typowych problemów bez konieczności ciągłego odwoływania się do dokumentacji.

**Przykłady zastosowań w praktyce**: „Zweryfikuj manifest deklaratywnego agenta i napraw błędy schematu”, „Pokaż przykładowy kod implementacji wtyczki Microsoft Graph API” lub „Pomóż rozwiązać problemy z uwierzytelnianiem aplikacji Teams”.

**Przykład z życia**: Skontaktowałem się z moim znajomym Johnem Millerem po rozmowie na Build o M365 Agents i polecił mi ten MCP. To może być świetne dla deweloperów nowych w M365 Agents, ponieważ oferuje szablony, przykładowy kod i szkielet do szybkiego startu bez ton dokumentacji. Funkcje walidacji schematów wydają się szczególnie przydatne, by uniknąć błędów w strukturze manifestu, które mogą powodować godziny debugowania.

> **💡 Pro Tip**
> 
> Używaj tego serwera razem z Microsoft Learn Docs MCP Server, aby uzyskać kompleksowe wsparcie w rozwoju M365 – jeden dostarcza oficjalną dokumentację, a ten oferuje praktyczne narzędzia i pomoc w rozwiązywaniu problemów.

## Co dalej? 🔮

## 📋 Podsumowanie

Model Context Protocol (MCP) zmienia sposób, w jaki deweloperzy współpracują z asystentami AI i narzędziami zewnętrznymi. Te 10 serwerów Microsoft MCP pokazuje siłę standaryzowanej integracji AI, umożliwiając płynne workflow, które pozwalają deweloperom pozostać w stanie pełnej koncentracji, korzystając z potężnych zewnętrznych funkcji.

Od kompleksowej integracji ekosystemu Azure po specjalistyczne narzędzia, takie jak Playwright do automatyzacji przeglądarki czy MarkItDown do przetwarzania dokumentów, te serwery pokazują, jak MCP może zwiększyć produktywność w różnych scenariuszach rozwojowych. Standaryzowany protokół zapewnia, że narzędzia te współpracują bezproblemowo, tworząc spójne doświadczenie deweloperskie.

W miarę rozwoju ekosystemu MCP, aktywne uczestnictwo w społeczności, eksploracja nowych serwerów i tworzenie własnych rozwiązań będą kluczowe dla maksymalizacji efektywności pracy. Otwartość standardu MCP pozwala łączyć narzędzia od różnych dostawców, tworząc idealny workflow dopasowany do indywidualnych potrzeb.

## 🔗 Dodatkowe zasoby

- [Official Microsoft MCP Repository](https://github.com/microsoft/mcp)
- [MCP Community & Documentation](https://modelcontextprotocol.io/introduction)
- [VS Code MCP Documentation](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP Documentation](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP Documentation](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Let's Learn – MCP Events](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Awesome GitHub Copilot Customizations](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days Live 29th/30th July or watch on Demand ](https://aka.ms/mcpdevdays)

## 🎯 Ćwiczenia

1. **Instalacja i konfiguracja**: Skonfiguruj jeden z serwerów MCP w swoim środowisku VS Code i przetestuj podstawową funkcjonalność.
2. **Integracja workflow**: Zaprojektuj workflow rozwojowy łączący co najmniej trzy różne serwery MCP.
3. **Planowanie własnego serwera**: Zidentyfikuj zadanie w codziennej pracy deweloperskiej, które mogłoby skorzystać na własnym serwerze MCP i stwórz jego specyfikację.
4. **Analiza wydajności**: Porównaj efektywność korzystania z serwerów MCP z tradycyjnymi metodami dla typowych zadań deweloperskich.
5. **Ocena bezpieczeństwa**: Oceń implikacje bezpieczeństwa korzystania z serwerów MCP w Twoim środowisku i zaproponuj najlepsze praktyki.

Next:[Best Practices](../08-BestPractices/README.md)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do jak największej dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.