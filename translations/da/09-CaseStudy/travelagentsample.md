# Case Study: Azure AI Travel Agents – Reference Implementation

## Oversigt

[Azure AI Travel Agents](https://github.com/Azure-Samples/azure-ai-travel-agents) er en omfattende reference-løsning udviklet af Microsoft, som viser, hvordan man bygger en multi-agent, AI-drevet rejseplanlægningsapplikation ved hjælp af Model Context Protocol (MCP), Azure OpenAI og Azure AI Search. Dette projekt demonstrerer bedste praksis for orkestrering af flere AI-agenter, integration af virksomhedens data og levering af en sikker, udvidelsesvenlig platform til virkelige scenarier.

## Nøglefunktioner
- **Multi-Agent Orkestrering:** Anvender MCP til at koordinere specialiserede agenter (f.eks. fly-, hotel- og rejseplanlægningsagenter), som samarbejder om at løse komplekse rejseplanlægningsopgaver.
- **Integration af Virksomhedsdata:** Forbinder til Azure AI Search og andre virksomhedskilder for at levere opdaterede og relevante oplysninger til rejseanbefalinger.
- **Sikker og Skalerbar Arkitektur:** Udnytter Azure-tjenester til autentificering, autorisation og skalerbar udrulning, i overensstemmelse med virksomhedens sikkerhedspraksis.
- **Udvidelsesvenlige Værktøjer:** Implementerer genanvendelige MCP-værktøjer og promptskabeloner, som muliggør hurtig tilpasning til nye domæner eller forretningsbehov.
- **Brugeroplevelse:** Tilbyder en samtalebaseret grænseflade, hvor brugere kan interagere med rejseagenterne, drevet af Azure OpenAI og MCP.

## Arkitektur
![Architecture](https://raw.githubusercontent.com/Azure-Samples/azure-ai-travel-agents/main/docs/ai-travel-agents-architecture-diagram.png)

### Beskrivelse af Arkitekturdiagrammet

Azure AI Travel Agents-løsningen er designet med fokus på modularitet, skalerbarhed og sikker integration af flere AI-agenter og virksomhedens datakilder. Hovedkomponenterne og dataflowet er som følger:

- **Brugergrænseflade:** Brugere interagerer med systemet via en samtalegrænseflade (som en webchat eller Teams-bot), der sender brugerforespørgsler og modtager rejseanbefalinger.
- **MCP Server:** Fungerer som den centrale orkestrator, der modtager brugerinput, håndterer kontekst og koordinerer handlingerne hos specialiserede agenter (f.eks. FlightAgent, HotelAgent, ItineraryAgent) via Model Context Protocol.
- **AI-agenter:** Hver agent er ansvarlig for et specifikt område (fly, hoteller, rejseplaner) og er implementeret som et MCP-værktøj. Agenterne bruger promptskabeloner og logik til at behandle forespørgsler og generere svar.
- **Azure OpenAI Service:** Tilbyder avanceret naturlig sprogforståelse og -generering, som gør det muligt for agenterne at tolke brugerens hensigt og generere samtalesvar.
- **Azure AI Search & Virksomhedsdata:** Agenterne forespørger Azure AI Search og andre virksomhedskilder for at hente opdaterede oplysninger om fly, hoteller og rejsemuligheder.
- **Autentificering & Sikkerhed:** Integreres med Microsoft Entra ID for sikker autentificering og anvender mindst-privilegium adgangskontrol til alle ressourcer.
- **Udrulning:** Designet til udrulning på Azure Container Apps, hvilket sikrer skalerbarhed, overvågning og operationel effektivitet.

Denne arkitektur muliggør problemfri orkestrering af flere AI-agenter, sikker integration med virksomhedens data og en robust, udvidelsesvenlig platform til at bygge domænespecifikke AI-løsninger.

## Trin-for-trin Forklaring af Arkitekturdiagrammet
Forestil dig, at du planlægger en stor rejse og har et team af eksperthjælpere, der hjælper dig med alle detaljer. Azure AI Travel Agents-systemet fungerer på samme måde, hvor forskellige dele (som teammedlemmer) hver har en særlig opgave. Sådan hænger det hele sammen:

### Brugergrænseflade (UI):
Tænk på dette som din rejseagents reception. Her stiller du spørgsmål eller fremsætter ønsker, som “Find mig en flybillet til Paris.” Det kan være et chatvindue på en hjemmeside eller en beskedapp.

### MCP Server (Koordinatoren):
MCP Serveren er som lederen, der lytter til din forespørgsel ved receptionen og beslutter, hvilken specialist der skal håndtere hver del. Den holder styr på samtalen og sørger for, at alt forløber glat.

### AI-agenter (Specialistassistenter):
Hver agent er ekspert inden for et bestemt område – en kender alt til fly, en anden til hoteller, og en tredje til rejseplanlægning. Når du beder om en rejse, sender MCP Serveren din forespørgsel til den eller de rette agenter. Disse agenter bruger deres viden og værktøjer til at finde de bedste muligheder for dig.

### Azure OpenAI Service (Sprogeksperten):
Dette er som at have en sprogekspert, der forstår præcis, hvad du spørger om, uanset hvordan du formulerer det. Den hjælper agenterne med at forstå dine forespørgsler og svare i et naturligt, samtalebaseret sprog.

### Azure AI Search & Virksomhedsdata (Informationsbiblioteket):
Forestil dig et kæmpe, opdateret bibliotek med al den nyeste rejseinformation – flytider, hoteltilgængelighed og mere. Agenterne søger i dette bibliotek for at finde de mest præcise svar til dig.

### Autentificering & Sikkerhed (Vagten):
Ligesom en sikkerhedsvagt tjekker, hvem der må komme ind i bestemte områder, sikrer denne del, at kun autoriserede personer og agenter kan få adgang til følsomme oplysninger. Den holder dine data sikre og private.

### Udrulning på Azure Container Apps (Bygningen):
Alle disse assistenter og værktøjer arbejder sammen inde i en sikker, skalerbar bygning (skyen). Det betyder, at systemet kan håndtere mange brugere samtidig og altid er tilgængeligt, når du har brug for det.

## Hvordan det hele fungerer sammen:

Du starter med at stille et spørgsmål ved receptionen (UI).  
Lederen (MCP Server) finder ud af, hvilken specialist (agent) der skal hjælpe dig.  
Specialisten bruger sprogeksperten (OpenAI) til at forstå din forespørgsel og biblioteket (AI Search) til at finde det bedste svar.  
Vagten (Autentificering) sikrer, at alt foregår sikkert.  
Alt dette sker inde i en pålidelig, skalerbar bygning (Azure Container Apps), så din oplevelse bliver glat og sikker.  
Dette teamwork gør det muligt for systemet hurtigt og sikkert at hjælpe dig med at planlægge din rejse, ligesom et team af ekspertrejseagenter, der arbejder sammen på et moderne kontor!

## Teknisk Implementering
- **MCP Server:** Værts for den centrale orkestreringslogik, eksponerer agentværktøjer og håndterer kontekst til flertrins rejseplanlægningsarbejdsgange.
- **Agenter:** Hver agent (f.eks. FlightAgent, HotelAgent) er implementeret som et MCP-værktøj med egne promptskabeloner og logik.
- **Azure Integration:** Bruger Azure OpenAI til naturlig sprogforståelse og Azure AI Search til datahentning.
- **Sikkerhed:** Integreres med Microsoft Entra ID til autentificering og anvender mindst-privilegium adgangskontrol til alle ressourcer.
- **Udrulning:** Understøtter udrulning til Azure Container Apps for skalerbarhed og operationel effektivitet.

## Resultater og Indvirkning
- Demonstrerer, hvordan MCP kan bruges til at orkestrere flere AI-agenter i et virkeligt, produktionsklart scenarie.
- Fremskynder udviklingen af løsninger ved at tilbyde genanvendelige mønstre til agentkoordinering, dataintegration og sikker udrulning.
- Tjener som en skabelon til at bygge domænespecifikke, AI-drevne applikationer ved hjælp af MCP og Azure-tjenester.

## Referencer
- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)
- [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.