# 🚀 10 serwerów Microsoft MCP, które zmieniają produktywność programistów

## 🎯 Czego nauczysz się z tego przewodnika

Ten praktyczny przewodnik prezentuje dziesięć serwerów Microsoft MCP, które aktywnie zmieniają sposób pracy programistów z asystentami AI. Zamiast tylko wyjaśniać, co serwery MCP *mogą* robić, pokażemy serwery, które już mają realny wpływ na codzienne workflow programistyczne w Microsoft i poza nim.

Każdy serwer w tym przewodniku został wybrany na podstawie rzeczywistego użytkowania i opinii programistów. Dowiesz się nie tylko, co robi każdy serwer, ale także dlaczego jest to ważne i jak wykorzystać go najlepiej w swoich projektach. Niezależnie od tego, czy jesteś całkiem nowy w MCP, czy chcesz rozszerzyć swoją istniejącą konfigurację, te serwery reprezentują najpraktyczniejsze i najbardziej wpływowe narzędzia dostępne w ekosystemie Microsoft.

> **💡 Szybka wskazówka na start**
>
> Jesteś nowy w MCP? Nie martw się! Ten przewodnik jest przyjazny dla początkujących. Wyjaśnimy koncepcje w trakcie lektury, a zawsze możesz wrócić do naszych modułów [Wprowadzenie do MCP](../00-Introduction/README.md) i [Podstawowe koncepcje](../01-CoreConcepts/README.md), by uzyskać głębsze tło.

## Przegląd

Ten kompleksowy przewodnik bada dziesięć serwerów Microsoft MCP, które rewolucjonizują sposób, w jaki programiści współpracują z asystentami AI i narzędziami zewnętrznymi. Od zarządzania zasobami Azure po przetwarzanie dokumentów, te serwery demonstrują moc Model Context Protocol w tworzeniu płynnych i produktywnych workflow programistycznych.

## Cele nauki

Po zakończeniu tego przewodnika będziesz:
- Rozumieć, jak serwery MCP zwiększają produktywność programistów
- Poznawać najbardziej wpływowe implementacje serwerów MCP Microsoft
- Odkrywać praktyczne zastosowania każdego serwera
- Wiedzieć, jak skonfigurować i uruchomić te serwery w VS Code i Visual Studio
- Eksplorować szerszy ekosystem MCP i kierunki rozwoju

## 🔧 Zrozumienie serwerów MCP: przewodnik dla początkujących

### Czym są serwery MCP?

Jako początkujący w Model Context Protocol (MCP) możesz się zastanawiać: „Czym dokładnie jest serwer MCP i dlaczego powinno mnie to interesować?” Zacznijmy od prostej analogii.

Pomyśl o serwerach MCP jak o wyspecjalizowanych asystentach, którzy pomagają twojemu AI asystentowi kodowania (np. GitHub Copilot) łączyć się z zewnętrznymi narzędziami i usługami. Podobnie jak używasz różnych aplikacji na telefonie do różnych zadań — jednej do pogody, innej do nawigacji, kolejnej do bankowości — serwery MCP dają twojemu AI asystentowi możliwość interakcji z różnymi narzędziami i usługami programistycznymi.

### Problem, który rozwiązują serwery MCP

Przed serwerami MCP, jeśli chciałeś:
- Sprawdzić swoje zasoby Azure
- Utworzyć zgłoszenie na GitHubie
- Wykonać zapytanie do bazy danych
- Przeszukać dokumentację

Musiałeś przerwać kodowanie, otworzyć przeglądarkę, przejść na odpowiednią stronę i ręcznie wykonać te zadania. To ciągłe przełączanie kontekstu przerywa twój rytm i zmniejsza produktywność.

### Jak serwery MCP zmieniają twoje doświadczenie programistyczne

Dzięki serwerom MCP możesz pozostać w swoim środowisku programistycznym (VS Code, Visual Studio itd.) i po prostu poprosić swojego asystenta AI o wykonanie tych zadań. Na przykład:

**Zamiast tradycyjnego workflow:**
1. Przestań kodować
2. Otwórz przeglądarkę
3. Przejdź do portalu Azure
4. Sprawdź szczegóły konta magazynu
5. Wróć do VS Code
6. Kontynuuj kodowanie

**Możesz teraz zrobić to tak:**
1. Zapytaj AI: „Jaki jest status moich kont magazynu Azure?”
2. Kontynuuj kodowanie z dostarczonymi informacjami

### Kluczowe korzyści dla początkujących

#### 1. 🔄 **Pozostań w swoim stanie przepływu pracy**
- Koniec z przełączaniem się między wieloma aplikacjami
- Skoncentruj się na kodzie, który piszesz
- Zmniejsz obciążenie umysłowe związane z zarządzaniem różnymi narzędziami

#### 2. 🤖 **Używaj naturalnego języka zamiast skomplikowanych poleceń**
- Zamiast uczyć się składni SQL, opisz, jakich danych potrzebujesz
- Zamiast pamiętać polecenia Azure CLI, opowiedz, co chcesz osiągnąć
- Pozwól AI zająć się szczegółami technicznymi, a sam skup się na logice

#### 3. 🔗 **Łącz wiele narzędzi razem**
- Twórz potężne workflow przez łączenie różnych usług
- Przykład: „Pobierz wszystkie ostatnie zgłoszenia na GitHubie i utwórz odpowiadające im elementy pracy w Azure DevOps”
- Buduj automatyzację bez pisania skomplikowanych skryptów

#### 4. 🌐 **Dostęp do rosnącego ekosystemu**
- Korzystaj z serwerów tworzonych przez Microsoft, GitHub i inne firmy
- Swobodnie łącz narzędzia od różnych dostawców
- Dołącz do ustandaryzowanego ekosystemu działającego z różnymi asystentami AI

#### 5. 🛠️ **Ucz się praktycznie**
- Zacznij od gotowych serwerów, by zrozumieć koncepcje
- Stopniowo buduj własne serwery, gdy poczujesz się pewniej
- Korzystaj z dostępnych SDK i dokumentacji, by kierować swoją nauką

### Przykład z prawdziwego świata dla początkujących

Załóżmy, że zaczynasz z web developmentem i pracujesz nad pierwszym projektem. Oto jak serwery MCP mogą pomóc:

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

### Przewaga standardu branżowego Enterprise

MCP staje się standardem w całej branży, co oznacza:
- **Spójność**: podobne doświadczenia w różnych narzędziach i firmach
- **Interoperacyjność**: serwery od różnych dostawców współpracują ze sobą
- **Przyszłościowa odporność**: umiejętności i konfiguracje przenoszą się między asystentami AI
- **Społeczność**: duży ekosystem wspólnej wiedzy i zasobów

### Rozpoczęcie: Czego się nauczysz

W tym przewodniku zapoznasz się z 10 serwerami Microsoft MCP szczególnie przydatnymi dla programistów na każdym poziomie. Każdy serwer został zaprojektowany, aby:
- Rozwiązać typowe wyzwania programistyczne
- Zmniejszyć powtarzalne zadania
- Poprawić jakość kodu
- Zwiększyć możliwości nauki

> **💡 Wskazówka do nauki**
>
> Jeśli jesteś całkiem nowy w MCP, zacznij od naszych modułów [Wprowadzenie do MCP](../00-Introduction/README.md) i [Podstawowe koncepcje](../01-CoreConcepts/README.md). Potem wróć tutaj, aby zobaczyć te koncepcje w działaniu z rzeczywistymi narzędziami Microsoft.
>
> Dla dodatkowego kontekstu ważności MCP, zapoznaj się z postem Marii Naggaga: [Połącz raz, integruj wszędzie dzięki MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## Rozpoczęcie pracy z MCP w VS Code i Visual Studio 🚀

Konfiguracja tych serwerów MCP jest prosta, jeśli używasz Visual Studio Code lub Visual Studio 2022 z GitHub Copilot.

### Konfiguracja VS Code

Oto podstawowy proces dla VS Code:

1. **Włącz tryb Agenta**: W VS Code przełącz się na tryb Agenta w oknie czatu Copilot
2. **Skonfiguruj serwery MCP**: Dodaj konfiguracje serwerów do swojego pliku settings.json w VS Code
3. **Uruchom serwery**: Kliknij przycisk "Start" dla każdego serwera, którego chcesz używać
4. **Wybierz narzędzia**: Wybierz, które serwery MCP włączyć dla swojej aktualnej sesji

Szczegółowe instrukcje konfiguracji znajdziesz w [dokumentacji VS Code MCP](https://code.visualstudio.com/docs/copilot/copilot-mcp).

> **💡 Profesjonalna wskazówka: Zarządzaj serwerami MCP jak profesjonalista!**
>
> Widok rozszerzeń VS Code teraz zawiera [wygodny nowy interfejs do zarządzania zainstalowanymi serwerami MCP](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)! Masz szybki dostęp do uruchamiania, zatrzymywania i zarządzania dowolnym zainstalowanym serwerem MCP za pomocą jasnego i prostego interfejsu. Wypróbuj to!

### Konfiguracja Visual Studio 2022

Dla Visual Studio 2022 (wersja 17.14 lub nowsza):

1. **Włącz tryb Agenta**: Kliknij rozwijane menu "Zapytaj" w oknie GitHub Copilot Chat i wybierz "Agent"
2. **Utwórz plik konfiguracyjny**: Utwórz plik `.mcp.json` w katalogu rozwiązania (zalecane miejsce: `<SOLUTIONDIR>\.mcp.json`)
3. **Skonfiguruj serwery**: Dodaj konfiguracje serwerów MCP w standardowym formacie MCP
4. **Zatwierdzenie narzędzi**: Po pojawieniu się monitu zatwierdź narzędzia, których chcesz używać, nadając im odpowiednie uprawnienia zakresu

Szczegółowe instrukcje konfiguracji Visual Studio znajdziesz w [dokumentacji Visual Studio MCP](https://learn.microsoft.com/visualstudio/ide/mcp-servers).

Każdy serwer MCP ma własne wymagania konfiguracyjne (np. łańcuchy połączenia, uwierzytelnianie), ale wzorzec konfiguracji jest spójny w obu IDE.

## Lekcje wyniesione z serwerów Microsoft MCP 🛠️

### 1. 📚 Serwer Microsoft Learn Docs MCP

[![Zainstaluj w VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Zainstaluj w VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Co robi**: Serwer Microsoft Learn Docs MCP to usługa hostowana w chmurze, która zapewnia asystentom AI dostęp w czasie rzeczywistym do oficjalnej dokumentacji Microsoft poprzez Model Context Protocol. Łączy się z `https://learn.microsoft.com/api/mcp` i umożliwia semantyczne wyszukiwanie w Microsoft Learn, dokumentacji Azure, dokumentacji Microsoft 365 i innych oficjalnych źródłach Microsoft.

**Dlaczego jest przydatny**: Choć może się wydawać, że to „tylko dokumentacja”, ten serwer jest kluczowy dla każdego programisty korzystającego z technologii Microsoft. Jedną z największych skarg deweloperów .NET na asystentów AI jest to, że nie są oni na bieżąco z najnowszymi wersjami .NET i C#. Serwer Microsoft Learn Docs MCP rozwiązuje ten problem, zapewniając dostęp w czasie rzeczywistym do najnowszej dokumentacji, referencji API i najlepszych praktyk. Niezależnie czy pracujesz z najnowszymi SDK Azure, eksplorujesz nowe funkcje C# 13, czy wdrażasz nowoczesne wzorce Aspire, ten serwer zapewnia, że asystent AI ma dostęp do autorytatywnych, aktualnych informacji potrzebnych do generowania dokładnego, nowoczesnego kodu.

**Zastosowanie w praktyce**: „Jakie są polecenia az cli do utworzenia aplikacji kontenerowej Azure zgodnie z oficjalną dokumentacją Microsoft Learn?” lub „Jak skonfigurować Entity Framework z dependency injection w ASP.NET Core?” A może „Przejrzyj ten kod, aby upewnić się, że odpowiada zaleceniom dotyczącym wydajności z dokumentacji Microsoft Learn.” Serwer oferuje kompleksowe pokrycie Microsoft Learn, dokumentacji Azure i Microsoft 365, wykorzystując zaawansowane wyszukiwanie semantyczne do znalezienia najbardziej kontekstowo odpowiednich informacji. Zwraca do 10 wysokiej jakości fragmentów treści z tytułami artykułów i URL-ami, zawsze uzyskując dostęp do najnowszej dokumentacji Microsoft w momencie jej publikacji.

**Przykład**: Serwer udostępnia narzędzie `microsoft_docs_search`, które wykonuje wyszukiwanie semantyczne w oficjalnej dokumentacji technicznej Microsoft. Po konfiguracji możesz zadawać pytania typu „Jak zaimplementować uwierzytelnianie JWT w ASP.NET Core?” i otrzymywać szczegółowe, oficjalne odpowiedzi z linkami do źródeł. Jakość wyszukiwania jest wyjątkowa, ponieważ rozumie kontekst – pytanie o „kontenery” w kontekście Azure zwróci dokumentację Azure Container Instances, podczas gdy to samo słowo w kontekście .NET zwróci odpowiednie informacje o kolekcjach C#.

To szczególnie pomocne przy szybko zmieniających się lub niedawno zaktualizowanych bibliotekach i przypadkach użycia. Na przykład, w niektórych ostatnich projektach kodowania chciałem wykorzystać funkcje w najnowszych wydaniach Aspire i Microsoft.Extensions.AI. Dzięki włączeniu serwera Microsoft Learn Docs MCP mogłem korzystać nie tylko z dokumentacji API, ale też z przewodników i instrukcji właśnie opublikowanych.

> **💡 Profesjonalna wskazówka**
>
> Nawet modele przyjazne narzędziom potrzebują zachęty, aby używać narzędzi MCP! Rozważ dodanie systemowego promptu lub [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) w stylu: „Masz dostęp do `microsoft.docs.mcp` – używaj tego narzędzia do wyszukiwania najnowszej oficjalnej dokumentacji Microsoft przy odpowiadaniu na pytania dotyczące technologii Microsoft jak C#, Azure, ASP.NET Core czy Entity Framework.”
>
> Świetny przykład tego w praktyce znajdziesz w [trybie czatu C# .NET Janitor](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) w repozytorium Awesome GitHub Copilot. Ten tryb specjalnie wykorzystuje serwer Microsoft Learn Docs MCP, aby pomóc w oczyszczeniu i unowocześnieniu kodu C# korzystając z najnowszych wzorców i najlepszych praktyk.
### 2. ☁️ Serwer Azure MCP


[![Zainstaluj w VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Zainstaluj w VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Co robi**: Serwer Azure MCP to kompleksowy zestaw ponad 15 wyspecjalizowanych konektorów usług Azure, który wnosi cały ekosystem Azure do Twojego przepływu pracy AI. To nie tylko pojedynczy serwer – to potężna kolekcja zawierająca zarządzanie zasobami, łączność z bazami danych (PostgreSQL, SQL Server), analizę logów Azure Monitor z użyciem KQL, integrację Cosmos DB i wiele więcej.

**Dlaczego jest przydatny**: Poza samo zarządzaniem zasobami Azure, ten serwer znacznie poprawia jakość kodu przy pracy z SDK Azure. Gdy używasz Azure MCP w trybie Agenta, nie tylko pomaga pisać kod – pomaga pisać *lepszy* kod Azure zgodny z aktualnymi wzorcami uwierzytelniania, najlepszymi praktykami obsługi błędów i wykorzystujący najnowsze funkcje SDK. Zamiast otrzymać generyczny kod, który może działać, dostajesz kod zgodny z zalecanymi wzorcami Azure dla środowisk produkcyjnych.

**Kluczowe moduły obejmują**:
- **🗄️ Konektory baz danych**: Bezpośredni dostęp w języku naturalnym do Azure Database dla PostgreSQL i SQL Server
- **📊 Azure Monitor**: Analiza logów oparta na KQL i wgląd operacyjny
- **🌐 Zarządzanie zasobami**: Pełny cykl życia zasobów Azure
- **🔐 Uwierzytelnianie**: Wzorce DefaultAzureCredential i zarządzanej tożsamości
- **📦 Usługi magazynowania**: Operacje na Blob Storage, Queue Storage i Table Storage
- **🚀 Usługi kontenerowe**: Azure Container Apps, Container Instances i zarządzanie AKS
- **I wiele innych wyspecjalizowanych konektorów**

**Zastosowania w praktyce**: "Wyświetl moje konta magazynowe Azure", "Zqueryj moje Log Analytics workspace pod kątem błędów z ostatniej godziny" lub "Pomóż mi zbudować aplikację Azure w Node.js z właściwym uwierzytelnianiem"

**Pełny scenariusz demonstracyjny**: Oto kompletny przewodnik pokazujący moc połączenia Azure MCP z rozszerzeniem GitHub Copilot dla Azure w VS Code. Gdy masz zainstalowane oba i wpisujesz:

> "Utwórz skrypt Python, który przesyła plik do Azure Blob Storage używając uwierzytelniania DefaultAzureCredential. Skrypt ma połączyć się z moim kontem magazynowym Azure o nazwie 'mycompanystorage', przesłać do kontenera 'documents', utworzyć plik testowy z aktualnym znacznikiem czasu do przesłania, obsłużyć błędy w sposób łagodny i dostarczyć informacyjne wyjście, stosować najlepsze praktyki Azure dla uwierzytelnienia i obsługi błędów, zawierać komentarze wyjaśniające działanie uwierzytelniania DefaultAzureCredential oraz być dobrze zorganizowanym ze stosownymi funkcjami i dokumentacją."

Serwer Azure MCP wygeneruje kompletny, gotowy do produkcji skrypt Python, który:
- Używa najnowszego SDK Azure Blob Storage z właściwymi wzorcami asynchronicznymi
- Implementuje DefaultAzureCredential z wyczerpującym wyjaśnieniem łańcucha zastępczego
- Zawiera solidną obsługę błędów ze specyficznymi typami wyjątków Azure
- Stosuje najlepsze praktyki SDK Azure dla zarządzania zasobami i połączeniami
- Zapewnia szczegółowe logowanie i informacyjne wyjście do konsoli
- Tworzy właściwie zorganizowany skrypt z funkcjami, dokumentacją i podpowiedziami typów

Co jest szczególnie warte zauważenia, to fakt, że bez Azure MCP moglibyśmy otrzymać generyczny kod do blob storage, który działa, ale nie stosuje aktualnych wzorców Azure. Z Azure MCP otrzymujesz kod wykorzystujący najnowsze metody uwierzytelniania, obsługujący scenariusze błędów specyficzne dla Azure i zgodny z zalecanymi przez Microsoft praktykami produkcyjnymi.

**Przykład z życia**: Miałem problem z zapamiętaniem konkretnych poleceń `az` i `azd` CLI do ad-hoc użycia. Zawsze to dla mnie dwustopniowy proces: najpierw sprawdzam składnię, potem wykonuję polecenie. Często wchodzę po prostu na portal i klikanie, bo nie chcę się przyznać, że zapomniałem składnię CLI. Możliwość po prostu opisania tego, czego chcę, jest niesamowita, a jeszcze lepsze, że mogę to zrobić bez wychodzenia z IDE!

W [repozytorium Azure MCP](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server) jest świetna lista przypadków użycia, aby zacząć. Aby uzyskać kompleksowe przewodniki dotyczące konfiguracji i zaawansowanych opcji, sprawdź [oficjalną dokumentację Azure MCP](https://learn.microsoft.com/azure/developer/azure-mcp-server/).

### 3. 🐙 Serwer GitHub MCP

[![Zainstaluj w VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Zainstaluj w VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**Co robi**: Oficjalny serwer GitHub MCP zapewnia bezproblemową integrację z całym ekosystemem GitHub, oferując zarówno zdalny dostęp hostowany, jak i lokalne opcje wdrożenia Docker. To nie tylko podstawowe operacje na repozytoriach – to kompleksowy zestaw narzędzi zawierający zarządzanie GitHub Actions, przepływami pracy pull requestów, śledzeniem issue, skanowaniem bezpieczeństwa, powiadomieniami i zaawansowanymi możliwościami automatyzacji.

**Dlaczego jest przydatny**: Ten serwer zmienia sposób interakcji z GitHub, wprowadzając pełne doświadczenie platformy bezpośrednio do Twojego środowiska programistycznego. Zamiast ciągłego przełączania się między VS Code a GitHub.com w celu zarządzania projektami, przeglądu kodu i monitorowania CI/CD, możesz wszystko obsługiwać za pomocą poleceń w języku naturalnym, pozostając skoncentrowanym na kodzie.

> **ℹ️ Uwaga: Różne typy "Agentów"**
> 
> Nie myl tego serwera GitHub MCP z GitHub Coding Agent (agent AI, którego możesz przypisać do issue w celu automatycznych zadań programistycznych). Serwer GitHub MCP działa w trybie Agenta VS Code, by zapewnić integrację API GitHub, natomiast GitHub Coding Agent to osobna funkcja tworząca pull requesty, gdy jest przypisany do issue na GitHub.

**Kluczowe możliwości obejmują**:
- **⚙️ GitHub Actions**: Kompleksowe zarządzanie pipeline CI/CD, monitorowanie przepływów pracy i obsługa artefaktów
- **🔀 Pull Requesty**: Tworzenie, przeglądanie, scalanie i zarządzanie PR z pełnym śledzeniem statusu
- **🐛 Issues**: Pełny cykl życia issue, komentowanie, etykietowanie i przypisywanie
- **🔒 Bezpieczeństwo**: Alerty skanowania kodu, wykrywanie sekretów i integracja Dependabot
- **🔔 Powiadomienia**: Inteligentne zarządzanie powiadomieniami i kontrola subskrypcji repozytorium
- **📁 Zarządzanie repozytorium**: Operacje na plikach, zarządzanie gałęziami i administracja repozytorium
- **👥 Współpraca**: Wyszukiwanie użytkowników i organizacji, zarządzanie zespołami i kontrola dostępu

**Zastosowania w praktyce**: "Utwórz pull request z mojej gałęzi funkcji", "Pokaż wszystkie nieudane przebiegi CI w tym tygodniu", "Lista otwartych alertów bezpieczeństwa dla moich repozytoriów" lub "Znajdź wszystkie przypisane do mnie issue w moich organizacjach"

**Pełny scenariusz demonstracyjny**: Oto potężny przepływ pracy pokazujący możliwości serwera GitHub MCP:

> "Muszę się przygotować do przeglądu sprintu. Pokaż mi wszystkie pull requesty, które utworzyłem w tym tygodniu, sprawdź status naszych pipeline CI/CD, utwórz podsumowanie alertów bezpieczeństwa, które trzeba rozwiązać, i pomóż mi stworzyć notatki wydania na podstawie scalonych PR z etykietą 'feature'."

Serwer GitHub MCP:
- Zapytuje o Twoje ostatnie pull requesty ze szczegółowymi informacjami o statusie
- Analizuje przebiegi workflow i wyróżnia wszelkie błędy lub problemy z wydajnością
- Kompiluje wyniki skanowania bezpieczeństwa i priorytetyzuje krytyczne alerty
- Generuje kompleksowe notatki wydania poprzez ekstrakcję informacji ze scalonych PR
- Dostarcza wykonalne kolejne kroki do planowania sprintu i przygotowań wydania

**Przykład z życia**: Uwielbiam używać tego do przepływów pracy przeglądu kodu. Zamiast przełączać się między VS Code, powiadomieniami GitHub i stronami pull requestów, mogę powiedzieć "Pokaż mi wszystkie PR oczekujące na moją recenzję", a potem "Dodaj komentarz do PR #123 pytający o obsługę błędów w metodzie uwierzytelniania". Serwer obsługuje wywołania API GitHub, utrzymuje kontekst dyskusji i pomaga tworzyć konstruktywne komentarze do recenzji.

**Opcje uwierzytelniania**: Serwer obsługuje zarówno OAuth (bezproblemowo w VS Code), jak i osobiste tokeny dostępu, z konfigurowalnym zestawem narzędzi pozwalającym włączyć tylko potrzebną funkcjonalność GitHub. Możesz uruchomić go jako usługę zdalną z natychmiastową konfiguracją lub lokalnie przez Dockera dla pełnej kontroli.

> **💡 Porada eksperta**
> 
> Włącz tylko potrzebne zestawy narzędzi, konfigurując parametr `--toolsets` w ustawieniach serwera MCP, by zmniejszyć rozmiar kontekstu i poprawić wybór narzędzi AI. Na przykład dodaj `"--toolsets", "repos,issues,pull_requests,actions"` do argumentów konfiguracji MCP dla głównych przepływów deweloperskich lub użyj `"--toolsets", "notifications, security"`, jeśli głównie potrzebujesz monitorowania GitHub.
### 4. 🔄 Serwer Azure DevOps MCP

[![Zainstaluj w VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Zainstaluj w VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**Co robi**: Łączy się z usługami Azure DevOps, oferując kompleksowe zarządzanie projektami, śledzenie work itemów, zarządzanie pipeline’ami buildów i operacje na repozytoriach.

**Dlaczego jest przydatny**: Dla zespołów korzystających z Azure DevOps jako głównej platformy DevOps, ten serwer MCP eliminuje ciągłe przełączanie się między środowiskiem programistycznym a interfejsem webowym Azure DevOps. Możesz zarządzać work itemami, sprawdzać statusy buildów, wyszukiwać w repozytoriach i obsługiwać zadania zarządzania projektami bezpośrednio z asystenta AI.

**Zastosowania w praktyce**: "Pokaż mi wszystkie aktywne work itemy w bieżącym sprincie dla projektu WebApp", "Utwórz zgłoszenie błędu dla problemu z logowaniem, który właśnie znalazłem" lub "Sprawdź status naszych pipeline’ów buildów i pokaż ostatnie niepowodzenia"

**Przykład z życia**: Łatwo możesz sprawdzić status bieżącego sprintu swego zespołu prostym zapytaniem jak "Pokaż mi wszystkie aktywne work itemy w bieżącym sprincie dla projektu WebApp" lub "Utwórz zgłoszenie błędu dla problemu z logowaniem, który właśnie znalazłem" bez wychodzenia ze środowiska programistycznego.

### 5. 📝 Serwer MarkItDown MCP


[![Zainstaluj w VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Zainstaluj w VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**Co robi**: MarkItDown to kompleksowy serwer konwersji dokumentów, który przekształca różne formaty plików na wysokiej jakości Markdown, zoptymalizowany pod kątem wykorzystania w LLM i przepływów analizy tekstu.

**Dlaczego jest użyteczny**: Niezbędny w nowoczesnych przepływach pracy z dokumentacją! MarkItDown obsługuje imponujący zakres formatów plików, zachowując jednocześnie kluczową strukturę dokumentu, taką jak nagłówki, listy, tabele oraz linki. W przeciwieństwie do prostych narzędzi do ekstrakcji tekstu, skupia się na zachowaniu znaczenia semantycznego i formatowania, które są wartościowe zarówno dla przetwarzania AI, jak i czytelności dla ludzi.

**Obsługiwane formaty plików**:
- **Dokumenty biurowe**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **Pliki multimedialne**: Obrazy (z metadanymi EXIF i OCR), audio (z metadanymi EXIF i transkrypcją mowy)
- **Zawartość internetowa**: HTML, kanały RSS, adresy URL YouTube, strony Wikipedii
- **Formaty danych**: CSV, JSON, XML, pliki ZIP (rekurencyjna analiza zawartości)
- **Formaty publikacji**: EPub, notatniki Jupyter (.ipynb)
- **E-mail**: wiadomości Outlook (.msg)
- **Zaawansowane**: integracja Azure Document Intelligence dla rozszerzonego przetwarzania PDF

**Zaawansowane możliwości**: MarkItDown obsługuje opisy obrazów wspierane przez LLM (gdy jest dostępny klient OpenAI), Azure Document Intelligence do rozszerzonego przetwarzania PDF, transkrypcję audio dla treści mówionych oraz system wtyczek pozwalający na rozszerzenie na dodatkowe formaty plików.

**Zastosowania w praktyce**: "Przekształć tę prezentację PowerPoint do formatu Markdown na naszą stronę dokumentacji", "Wydobądź tekst z tego PDF z zachowaniem właściwej struktury nagłówków", lub "Przekształć ten arkusz Excel w czytelny format tabeli"

**Przykład z dokumentacji**: Cytując [dokumentację MarkItDown](https://github.com/microsoft/markitdown#why-markdown):

> Markdown jest niezwykle bliski prostemu tekstowi, z minimalnym markupem lub formatowaniem, ale wciąż oferuje sposób reprezentacji ważnej struktury dokumentu. Popularne LLM, takie jak GPT-4o od OpenAI, natywnie "posługują się" Markdownem i często bez podpowiedzi włączają Markdown w swoich odpowiedziach. Sugeruje to, że zostały wytrenowane na ogromnej ilości tekstu sformatowanego Markdownem i dobrze go rozumieją. Jako dodatkowa korzyść, konwencje Markdown są także bardzo efektywne pod względem tokenów.

MarkItDown doskonale zachowuje strukturę dokumentu, co jest ważne w przepływach AI. Na przykład przy konwersji prezentacji PowerPoint utrzymuje organizację slajdów z właściwymi nagłówkami, ekstrahuje tabele jako tabele Markdown, dodaje tekst alternatywny do obrazów, a nawet przetwarza notatki prelegenta. Wykresy są konwertowane na czytelne tabele danych, a wynikowy Markdown zachowuje logiczny przebieg oryginalnej prezentacji. Czyni to narzędzie idealnym do zasilania treści prezentacji w systemy AI lub tworzenia dokumentacji ze slajdów.
### 6. 🗃️ SQL Server MCP Server

[![Zainstaluj w VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Zainstaluj w VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**Co robi**: Umożliwia konwersacyjne korzystanie z baz danych SQL Server (lokalnie, Azure SQL lub Fabric)

**Dlaczego jest użyteczny**: Podobny do serwera PostgreSQL, ale dla ekosystemu Microsoft SQL. Połącz się prostym łańcuchem połączenia i zacznij zadawać pytania w języku naturalnym – koniec z przełączaniem kontekstu!

**Zastosowania w praktyce**: "Znajdź wszystkie zamówienia, które nie zostały zrealizowane w ostatnich 30 dniach" jest tłumaczone na odpowiednie zapytania SQL i zwraca sformatowane wyniki

**Przykład z życia**: Po skonfigurowaniu połączenia z bazą możesz od razu zacząć rozmawiać ze swoimi danymi. W poście na blogu pokazano to na prostym pytaniu: "Z którą bazą danych jesteś połączony?" Serwer MCP reaguje, wywołując odpowiednie narzędzie bazy danych, łączy się z instancją SQL Server i zwraca szczegóły bieżącego połączenia – wszystko bez konieczności pisania linii SQL. Serwer wspiera kompleksowe operacje na bazie danych od zarządzania schematem po manipulację danymi, wszystko za pomocą naturalnych poleceń w języku. Pełne instrukcje konfiguracji i przykłady dla VS Code i Claude Desktop znajdziesz tutaj: [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).


### 7. 🎭 Playwright MCP Server

[![Zainstaluj w VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Zainstaluj w VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**Co robi**: Umożliwia agentom AI interakcję ze stronami internetowymi do testowania i automatyzacji

> **ℹ️ Napędza GitHub Copilot**
> 
> Serwer Playwright MCP zasila Agenta Kodującego GitHub Copilot, dając mu możliwości przeglądania stron internetowych! [Dowiedz się więcej o tej funkcji](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**Dlaczego jest użyteczny**: Idealny do automatycznych testów opartych na opisach w języku naturalnym. AI może nawigować po stronach, wypełniać formularze i wyciągać dane za pomocą ustrukturyzowanych snapshotów dostępności – to niezwykle potężne narzędzie!

**Zastosowania w praktyce**: "Przetestuj proces logowania i zweryfikuj, czy dashboard ładuje się poprawnie" lub "Wygeneruj test, który wyszukuje produkty i sprawdza stronę wyników" – wszystko bez potrzeby posiadania kodu źródłowego aplikacji

**Przykład z życia**: Moja koleżanka Debbie O'Brien ostatnio wyróżniła się niesamowitą pracą z serwerem Playwright MCP! Na przykład pokazała niedawno, jak można wygenerować kompletne testy Playwright bez dostępu do kodu źródłowego aplikacji. W swoim scenariuszu poprosiła Copilota o stworzenie testu dla aplikacji wyszukiwania filmów: przejdź do strony, wyszukaj "Garfield" i zweryfikuj, czy film pojawia się w wynikach. MCP uruchomił sesję przeglądarki, zbadał strukturę strony za pomocą snapshotów DOM, znalazł właściwe selektory i wygenerował w pełni działający test w TypeScript, który przeszedł przy pierwszym uruchomieniu.

To, co jest naprawdę potężne, to fakt, że łączy instrukcje w języku naturalnym z wykonywalnym kodem testów. Tradycyjne metody wymagają ręcznego pisania testów lub dostępu do kodu źródłowego dla kontekstu. Z Playwright MCP można testować zewnętrzne strony, aplikacje klienckie lub działać w scenariuszach testowania czarnej skrzynki, gdzie dostęp do kodu nie jest możliwy.


### 8. 💻 Dev Box MCP Server

[![Zainstaluj w VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Zainstaluj w VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**Co robi**: Zarządza środowiskami Microsoft Dev Box za pomocą języka naturalnego

**Dlaczego jest użyteczny**: Znacznie upraszcza zarządzanie środowiskami deweloperskimi! Twórz, konfiguruj i zarządzaj środowiskami programistycznymi bez konieczności pamiętania konkretnych poleceń.

**Zastosowania w praktyce**: "Utwórz nowy Dev Box z najnowszym .NET SDK i skonfiguruj go dla naszego projektu", "Sprawdź status wszystkich moich środowisk developerskich" lub "Stwórz zunifikowane środowisko demo na prezentacje zespołowe"

**Przykład z życia**: Jestem wielkim fanem używania Dev Box do rozwoju osobistego. Moment olśnienia miałem, gdy James Montemagno wyjaśnił, jak świetny jest Dev Box na konferencyjne dema, ponieważ oferuje bardzo szybkie połączenie ethernetowe, niezależnie od konferencji/hotelu/sieci Wi-Fi w samolocie, z której korzystam w danym momencie. W rzeczywistości ostatnio ćwiczyłem demo na konferencję mając laptop podłączony do hotspota telefonu w trakcie jazdy autobusem z Brugii do Antwerpii! Następnym krokiem jest zarządzanie zespołem wieloma środowiskami developerskimi i zunifikowanymi środowiskami demo. Kolejnym dużym zastosowaniem, o którym słyszałem od klientów i współpracowników, jest wykorzystywanie Dev Box do wstępnie skonfigurowanych środowisk programistycznych. W obu przypadkach używanie MCP do konfigurowania i zarządzania Dev Boxami pozwala korzystać z interakcji w języku naturalnym, pozostając jednocześnie w środowisku deweloperskim.

### 9. 🤖 Microsoft Foundry MCP Server


[![Zainstaluj w VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Zainstaluj w VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**Co robi**: Serwer Microsoft Foundry MCP zapewnia programistom kompleksowy dostęp do ekosystemu AI Azure, w tym katalogów modeli, zarządzania wdrożeniami, indeksowania wiedzy za pomocą Azure AI Search oraz narzędzi oceny. Ten eksperymentalny serwer mostkuje lukę między tworzeniem AI a potężną infrastrukturą AI Azure, ułatwiając budowanie, wdrażanie i ocenianie aplikacji AI.

**Dlaczego jest przydatny**: Ten serwer rewolucjonizuje sposób pracy z usługami Azure AI, wprowadzając klasy korporacyjne możliwości AI bezpośrednio do twojego środowiska deweloperskiego. Zamiast przełączać się między portalem Azure, dokumentacją a IDE, możesz odkrywać modele, wdrażać usługi, zarządzać bazami wiedzy oraz oceniać wydajność AI przy użyciu poleceń w naturalnym języku. Jest szczególnie przydatny dla programistów tworzących aplikacje RAG (Retrieval-Augmented Generation), zarządzających wielomodelowymi wdrożeniami lub implementujących kompleksowe pipeline-y oceny AI.

**Kluczowe możliwości dla programistów**:
- **🔍 Odkrywanie modeli i wdrażanie**: Przeglądaj katalog modeli Microsoft Foundry, uzyskuj szczegółowe informacje o modelach z przykładami kodu i wdrażaj modele do usług Azure AI
- **📚 Zarządzanie wiedzą**: Twórz i zarządzaj indeksami Azure AI Search, dodawaj dokumenty, konfiguruj indeksatory i buduj zaawansowane systemy RAG
- **⚡ Integracja agentów AI**: Łącz się z agentami Azure AI, wyszukuj istniejące agenty i oceniaj ich wydajność w scenariuszach produkcyjnych
- **📊 Framework oceny**: Przeprowadzaj kompleksowe oceny tekstu i agentów, generuj raporty w markdown i wdrażaj kontrolę jakości aplikacji AI
- **🚀 Narzędzia prototypowania**: Uzyskaj instrukcje konfiguracji dla prototypowania opartego na GitHub oraz dostęp do Microsoft Foundry Labs z nowatorskimi modelami badawczymi

**Przykład użycia w praktyce**: "Wdroż model Phi-4 do usług Azure AI dla mojej aplikacji", "Stwórz nowy indeks wyszukiwania dla mojego systemu RAG dokumentacji", "Oceń odpowiedzi mojego agenta względem wskaźników jakości" lub "Znajdź najlepszy model rozumowania dla moich złożonych zadań analitycznych"

**Pełny scenariusz demonstracyjny**: Oto potężny workflow tworzenia AI:

> "Buduję agenta wsparcia klienta. Pomóż mi znaleźć dobry model rozumowania z katalogu, wdrożyć go do usług Azure AI, stworzyć bazę wiedzy z naszej dokumentacji, ustawić framework oceny do testowania jakości odpowiedzi, a następnie pomóż mi stworzyć prototyp integracji z tokenem GitHub do testów."

Serwer Microsoft Foundry MCP:
- Wyszuka w katalogu modeli optymalne modele rozumowania na podstawie twoich wymagań
- Dostarczy polecenia wdrożenia i informacje o limitach dla wybranego regionu Azure
- Ustawi indeksy Azure AI Search z odpowiednim schematem dla twojej dokumentacji
- Skonfiguruje pipeline-y oceny z metrykami jakości i zabezpieczeniami
- Wygeneruje kod prototypowania z uwierzytelnieniem GitHub do natychmiastowych testów
- Zapewni kompleksowe przewodniki konfiguracji dostosowane do twojego stacku technologicznego

**Przykład z życia**: Jako programista miałem trudności, by nadążyć za różnymi modelami LLM dostępnymi na rynku. Znam kilka głównych, ale czułem, że tracę potencjalne korzyści w produktywności i wydajności. Tokeny i limity są stresujące i trudne do zarządzania – nigdy nie wiem, czy wybieram właściwy model do odpowiedniego zadania, czy nie marnuję budżetu. Usłyszałem o tym serwerze MCP od Jamesa Montemagno, gdy pytałem współpracowników o rekomendacje do tego wpisu i jestem podekscytowany, by go wypróbować! Możliwości odkrywania modeli wyglądają na wyjątkowo imponujące dla kogoś takiego jak ja, kto chce eksplorować poza utartymi ścieżkami i znaleźć modele zoptymalizowane pod konkretne zadania. Framework oceny powinien pomóc mi potwierdzić, że faktycznie uzyskuję lepsze wyniki, a nie tylko testuję coś nowego dla samego testowania.

> **ℹ️ Status eksperymentalny**
> 
> Ten serwer MCP jest eksperymentalny i jest w aktywnym rozwoju. Funkcje i API mogą ulegać zmianom. Idealny do eksploracji możliwości Azure AI i budowy prototypów, ale należy zweryfikować stabilność do użycia produkcyjnego.
### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Zainstaluj w VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Zainstaluj w VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**Co robi**: Dostarcza programistom niezbędne narzędzia do tworzenia agentów AI i aplikacji integrujących się z Microsoft 365 oraz Microsoft 365 Copilot, w tym walidację schematów, pobieranie przykładowego kodu i pomoc w rozwiązywaniu problemów.

**Dlaczego jest przydatny**: Tworzenie dla Microsoft 365 i Copilot obejmuje złożone schematy manifestów i specyficzne wzorce rozwoju. Ten serwer MCP wprowadza kluczowe zasoby rozwojowe bezpośrednio do twojego środowiska kodowania, pomagając walidować schematy, znaleźć przykładowy kod i rozwiązywać typowe problemy bez ciągłego odwoływania się do dokumentacji.

**Przykłady praktycznego zastosowania**: „Zweryfikuj mój deklaratywny manifest agenta i napraw błędy schematu”, „Pokaż przykładowy kod implementacji wtyczki Microsoft Graph API” lub „Pomóż rozwiązać problemy z uwierzytelnianiem mojej aplikacji Teams”.

**Przykład z życia**: Skontaktowałem się z moim przyjacielem Johnem Millerem po rozmowie z nim na konferencji Build o agentach M365 i polecił ten MCP. To może być świetne dla programistów początkujących z agentami M365, ponieważ dostarcza szablony, przykładowy kod i strukturę startową bez konieczności nurkowania w dokumentacji. Funkcje walidacji schematów wyglądają na szczególnie użyteczne, by unikać błędów struktury manifestu, które mogą powodować godziny debugowania.

> **💡 Profesjonalna wskazówka**
> 
> Używaj tego serwera równolegle z Microsoft Learn Docs MCP Server dla kompleksowego wsparcia rozwoju M365 – jeden dostarcza oficjalną dokumentację, a ten oferuje praktyczne narzędzia rozwojowe i pomoc w rozwiązywaniu problemów.


## Co dalej? 🔮

## 📋 Podsumowanie

Protokoły Model Context Protocol (MCP) zmieniają sposób, w jaki programiści współdziałają z asystentami AI i narzędziami zewnętrznymi. Te 10 serwerów Microsoft MCP pokazuje moc standaryzowanej integracji AI, umożliwiając płynne procesy pracy, które pozwalają programistom pozostać w stanie flow, korzystając z potężnych zewnętrznych możliwości.

Od kompleksowej integracji ekosystemu Azure po specjalistyczne narzędzia jak Playwright do automatyzacji przeglądarki czy MarkItDown do przetwarzania dokumentów, serwery te prezentują, jak MCP może zwiększyć produktywność w różnych scenariuszach rozwojowych. Standaryzowany protokół zapewnia, że narzędzia te współpracują bezproblemowo, tworząc spójne doświadczenie deweloperskie.

W miarę jak ekosystem MCP będzie się rozwijać, pozostawanie zaangażowanym w społeczność, eksplorowanie nowych serwerów i budowanie niestandardowych rozwiązań będzie kluczem do maksymalizacji produktywności programistycznej. Otwarta natura standardu MCP oznacza, że możesz łączyć narzędzia od różnych dostawców, tworząc idealny proces pracy dostosowany do twoich potrzeb.

## 🔗 Dodatkowe zasoby

- [Oficjalne Repozytorium Microsoft MCP](https://github.com/microsoft/mcp)
- [Społeczność MCP i Dokumentacja](https://modelcontextprotocol.io/introduction)
- [Dokumentacja MCP dla VS Code](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Dokumentacja MCP dla Visual Studio](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Dokumentacja MCP dla Azure](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Let's Learn – Wydarzenia MCP](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Niesamowite dostosowania GitHub Copilot](https://github.com/awesome-copilot)
- [SDK MCP dla C#](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days na żywo 29/30 lipca lub dostęp na żądanie](https://aka.ms/mcpdevdays)

## 🎯 Ćwiczenia

1. **Instalacja i konfiguracja**: Skonfiguruj jeden z serwerów MCP w swoim środowisku VS Code i przetestuj podstawową funkcjonalność.
2. **Integracja workflow**: Zaprojektuj workflow rozwojowy łączący co najmniej trzy różne serwery MCP.
3. **Planowanie niestandardowego serwera**: Wybierz zadanie z codziennej pracy programistycznej, które mogłoby skorzystać z niestandardowego serwera MCP i stwórz jego specyfikację.
4. **Analiza wydajności**: Porównaj efektywność używania serwerów MCP w stosunku do tradycyjnych metod dla typowych zadań rozwojowych.
5. **Ocena bezpieczeństwa**: Oceń implikacje bezpieczeństwa korzystania z serwerów MCP w swoim środowisku i zaproponuj najlepsze praktyki.


Następny:[Najlepsze praktyki](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->