# Studium przypadku: Azure AI Travel Agents – implementacja referencyjna

## Przegląd

[Azure AI Travel Agents](https://github.com/Azure-Samples/azure-ai-travel-agents) to kompleksowe rozwiązanie referencyjne opracowane przez Microsoft, które pokazuje, jak zbudować wieloagentową aplikację do planowania podróży wspieraną przez AI, wykorzystując Model Context Protocol (MCP), Azure OpenAI oraz Azure AI Search. Projekt ten prezentuje najlepsze praktyki w zakresie koordynacji wielu agentów AI, integracji danych korporacyjnych oraz zapewnienia bezpiecznej i rozszerzalnej platformy do zastosowań w rzeczywistych scenariuszach.

## Kluczowe funkcje
- **Orkiestracja wieloagentowa:** Wykorzystuje MCP do koordynacji wyspecjalizowanych agentów (np. agentów lotów, hoteli i planów podróży), którzy współpracują, aby realizować złożone zadania związane z planowaniem podróży.
- **Integracja danych korporacyjnych:** Łączy się z Azure AI Search oraz innymi źródłami danych korporacyjnych, aby dostarczać aktualne i istotne informacje do rekomendacji podróży.
- **Bezpieczna, skalowalna architektura:** Wykorzystuje usługi Azure do uwierzytelniania, autoryzacji oraz skalowalnego wdrażania, zgodnie z najlepszymi praktykami bezpieczeństwa w przedsiębiorstwach.
- **Rozszerzalne narzędzia:** Implementuje wielokrotnego użytku narzędzia MCP oraz szablony promptów, umożliwiając szybkie dostosowanie do nowych dziedzin lub wymagań biznesowych.
- **Doświadczenie użytkownika:** Zapewnia konwersacyjny interfejs, dzięki któremu użytkownicy mogą wchodzić w interakcję z agentami podróży, wspierany przez Azure OpenAI i MCP.

## Architektura
![Architecture](https://raw.githubusercontent.com/Azure-Samples/azure-ai-travel-agents/main/docs/ai-travel-agents-architecture-diagram.png)

### Opis diagramu architektury

Rozwiązanie Azure AI Travel Agents zostało zaprojektowane z myślą o modułowości, skalowalności oraz bezpiecznej integracji wielu agentów AI i źródeł danych korporacyjnych. Główne komponenty i przepływ danych przedstawiają się następująco:

- **Interfejs użytkownika:** Użytkownicy wchodzą w interakcję z systemem za pomocą konwersacyjnego UI (np. czatu na stronie internetowej lub bota w Teams), który wysyła zapytania użytkownika i odbiera rekomendacje podróży.
- **MCP Server:** Pełni rolę centralnego koordynatora, odbierając dane wejściowe od użytkownika, zarządzając kontekstem i koordynując działania wyspecjalizowanych agentów (np. FlightAgent, HotelAgent, ItineraryAgent) za pomocą Model Context Protocol.
- **Agenci AI:** Każdy agent odpowiada za konkretną dziedzinę (loty, hotele, plany podróży) i jest zaimplementowany jako narzędzie MCP. Agenci korzystają z szablonów promptów i logiki do przetwarzania zapytań i generowania odpowiedzi.
- **Azure OpenAI Service:** Zapewnia zaawansowane rozumienie i generowanie języka naturalnego, umożliwiając agentom interpretację intencji użytkownika i tworzenie konwersacyjnych odpowiedzi.
- **Azure AI Search i dane korporacyjne:** Agenci wyszukują w Azure AI Search oraz innych źródłach danych korporacyjnych, aby uzyskać aktualne informacje o lotach, hotelach i opcjach podróży.
- **Uwierzytelnianie i bezpieczeństwo:** Integruje się z Microsoft Entra ID w celu bezpiecznego uwierzytelniania oraz stosuje zasady minimalnych uprawnień do wszystkich zasobów.
- **Wdrożenie:** Zaprojektowane do wdrożenia na Azure Container Apps, co zapewnia skalowalność, monitorowanie i efektywność operacyjną.

Ta architektura umożliwia płynną orkiestrację wielu agentów AI, bezpieczną integrację z danymi korporacyjnymi oraz solidną, rozszerzalną platformę do tworzenia rozwiązań AI dedykowanych konkretnym dziedzinom.

## Szczegółowe wyjaśnienie diagramu architektury
Wyobraź sobie, że planujesz dużą podróż i masz zespół ekspertów, którzy pomagają Ci w każdym szczególe. System Azure AI Travel Agents działa podobnie, wykorzystując różne elementy (jak członków zespołu), z których każdy ma swoje specjalne zadanie. Oto jak to wszystko działa razem:

### Interfejs użytkownika (UI):
Pomyśl o tym jak o recepcji twojego agenta podróży. To miejsce, gdzie Ty (użytkownik) zadajesz pytania lub składasz prośby, np. „Znajdź mi lot do Paryża.” Może to być okno czatu na stronie internetowej lub aplikacji do komunikacji.

### MCP Server (koordynator):
MCP Server to jak menedżer, który słucha twojej prośby na recepcji i decyduje, który specjalista powinien się nią zająć. Śledzi przebieg rozmowy i dba, aby wszystko przebiegało sprawnie.

### Agenci AI (specjalistyczni asystenci):
Każdy agent to ekspert w swojej dziedzinie – jeden zna się na lotach, inny na hotelach, a jeszcze inny na planowaniu trasy podróży. Gdy prosisz o wyjazd, MCP Server przekazuje twoje zapytanie odpowiednim agentom. Agenci korzystają ze swojej wiedzy i narzędzi, aby znaleźć dla Ciebie najlepsze opcje.

### Azure OpenAI Service (ekspert językowy):
To jak ekspert językowy, który dokładnie rozumie, o co pytasz, niezależnie od tego, jak sformułujesz swoje pytanie. Pomaga agentom zrozumieć twoje prośby i odpowiadać w naturalnym, konwersacyjnym języku.

### Azure AI Search i dane korporacyjne (biblioteka informacji):
Wyobraź sobie ogromną, aktualną bibliotekę z najnowszymi informacjami o podróżach – rozkładami lotów, dostępnością hoteli i innymi danymi. Agenci przeszukują tę bibliotekę, aby znaleźć dla Ciebie najdokładniejsze odpowiedzi.

### Uwierzytelnianie i bezpieczeństwo (ochroniarz):
Tak jak ochroniarz sprawdza, kto może wejść do określonych miejsc, ta część systemu dba, aby tylko upoważnione osoby i agenci mieli dostęp do wrażliwych informacji. Chroni Twoje dane i prywatność.

### Wdrożenie na Azure Container Apps (budynek):
Wszyscy ci asystenci i narzędzia działają razem w bezpiecznym, skalowalnym „budynku” (chmurze). Oznacza to, że system może obsłużyć wielu użytkowników jednocześnie i jest zawsze dostępny, gdy go potrzebujesz.

## Jak to wszystko działa razem:

Zaczynasz od zadania pytania na recepcji (UI).  
Menedżer (MCP Server) ustala, który specjalista (agent) powinien Ci pomóc.  
Specjalista korzysta z eksperta językowego (OpenAI), aby zrozumieć Twoją prośbę, oraz z biblioteki (AI Search), aby znaleźć najlepszą odpowiedź.  
Ochroniarz (uwierzytelnianie) dba o bezpieczeństwo całego procesu.  
Wszystko to dzieje się w niezawodnym, skalowalnym „budynku” (Azure Container Apps), dzięki czemu Twoje doświadczenie jest płynne i bezpieczne.  
Ta współpraca pozwala systemowi szybko i bezpiecznie pomóc Ci zaplanować podróż, niczym zespół ekspertów pracujących razem w nowoczesnym biurze!

## Implementacja techniczna
- **MCP Server:** Hostuje główną logikę orkiestracji, udostępnia narzędzia agentów i zarządza kontekstem dla wieloetapowych procesów planowania podróży.
- **Agenci:** Każdy agent (np. FlightAgent, HotelAgent) jest zaimplementowany jako narzędzie MCP z własnymi szablonami promptów i logiką.
- **Integracja z Azure:** Wykorzystuje Azure OpenAI do rozumienia języka naturalnego oraz Azure AI Search do pobierania danych.
- **Bezpieczeństwo:** Integruje się z Microsoft Entra ID w celu uwierzytelniania i stosuje zasady minimalnych uprawnień do wszystkich zasobów.
- **Wdrożenie:** Obsługuje wdrożenie na Azure Container Apps dla zapewnienia skalowalności i efektywności operacyjnej.

## Wyniki i wpływ
- Pokazuje, jak MCP może być używany do koordynacji wielu agentów AI w rzeczywistym, produkcyjnym scenariuszu.
- Przyspiesza rozwój rozwiązań, dostarczając wielokrotnego użytku wzorce koordynacji agentów, integracji danych i bezpiecznego wdrażania.
- Służy jako wzorzec do budowy dedykowanych aplikacji AI z wykorzystaniem MCP i usług Azure.

## Źródła
- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)
- [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.