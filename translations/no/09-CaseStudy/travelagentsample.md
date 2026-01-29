# Case Study: Azure AI Travel Agents – Referanseimplementering

## Oversikt

[Azure AI Travel Agents](https://github.com/Azure-Samples/azure-ai-travel-agents) er en omfattende referanseløsning utviklet av Microsoft som viser hvordan man kan bygge en fleragent-basert, AI-drevet reiseplanleggingsapplikasjon ved bruk av Model Context Protocol (MCP), Azure OpenAI og Azure AI Search. Dette prosjektet demonstrerer beste praksis for å orkestrere flere AI-agenter, integrere bedriftsdata og tilby en sikker, utvidbar plattform for virkelige scenarier.

## Nøkkelfunksjoner
- **Fleragent-orkestrering:** Bruker MCP for å koordinere spesialiserte agenter (f.eks. fly-, hotell- og reiseplanleggingsagenter) som samarbeider for å løse komplekse reiseplanleggingsoppgaver.
- **Integrasjon av bedriftsdata:** Knytter til Azure AI Search og andre bedriftsdatakilder for å gi oppdatert og relevant informasjon til reiseanbefalinger.
- **Sikker og skalerbar arkitektur:** Utnytter Azure-tjenester for autentisering, autorisasjon og skalerbar distribusjon, i tråd med beste praksis for bedriftsikkerhet.
- **Utvidbare verktøy:** Implementerer gjenbrukbare MCP-verktøy og promptmaler, som muliggjør rask tilpasning til nye domener eller forretningsbehov.
- **Brukeropplevelse:** Tilbyr et samtalebasert grensesnitt hvor brukere kan samhandle med reiseagentene, drevet av Azure OpenAI og MCP.

## Arkitektur
![Architecture](https://raw.githubusercontent.com/Azure-Samples/azure-ai-travel-agents/main/docs/ai-travel-agents-architecture-diagram.png)

### Beskrivelse av arkitekturdiagrammet

Azure AI Travel Agents-løsningen er designet for modularitet, skalerbarhet og sikker integrasjon av flere AI-agenter og bedriftsdatakilder. Hovedkomponentene og dataflyten er som følger:

- **Brukergrensesnitt:** Brukere samhandler med systemet gjennom et samtalegrensesnitt (som en webchat eller Teams-bot), som sender brukerforespørsler og mottar reiseanbefalinger.
- **MCP Server:** Fungerer som den sentrale orkestratoren, mottar brukerinput, håndterer kontekst og koordinerer handlingene til spesialiserte agenter (f.eks. FlightAgent, HotelAgent, ItineraryAgent) via Model Context Protocol.
- **AI-agenter:** Hver agent har ansvar for et spesifikt område (fly, hotell, reiserute) og er implementert som et MCP-verktøy. Agentene bruker promptmaler og logikk for å behandle forespørsler og generere svar.
- **Azure OpenAI Service:** Tilbyr avansert naturlig språkforståelse og generering, som gjør det mulig for agentene å tolke brukerens intensjon og generere samtalesvar.
- **Azure AI Search & bedriftsdata:** Agentene søker i Azure AI Search og andre bedriftsdatakilder for å hente oppdatert informasjon om fly, hoteller og reisealternativer.
- **Autentisering og sikkerhet:** Integreres med Microsoft Entra ID for sikker autentisering og anvender prinsippet om minste privilegium for tilgangskontroll til alle ressurser.
- **Distribusjon:** Designet for distribusjon på Azure Container Apps, som sikrer skalerbarhet, overvåking og driftseffektivitet.

Denne arkitekturen muliggjør sømløs orkestrering av flere AI-agenter, sikker integrasjon med bedriftsdata og en robust, utvidbar plattform for å bygge domene-spesifikke AI-løsninger.

## Trinnvis forklaring av arkitekturdiagrammet
Tenk deg at du planlegger en stor reise og har et team av eksperthjelpere som bistår deg med alle detaljer. Azure AI Travel Agents-systemet fungerer på samme måte, med ulike deler (som teammedlemmer) som hver har en spesiell oppgave. Slik henger det hele sammen:

### Brukergrensesnitt (UI):
Tenk på dette som resepsjonen hos reisebyrået ditt. Her stiller du spørsmål eller legger inn forespørsler, som «Finn en flyreise til Paris». Dette kan være et chatte-vindu på en nettside eller en meldingsapp.

### MCP Server (Koordinatoren):
MCP Server er som lederen som lytter til forespørselen din i resepsjonen og bestemmer hvilken spesialist som skal håndtere hver del. Den holder oversikt over samtalen og sørger for at alt går smidig.

### AI-agenter (Spesialisteksperter):
Hver agent er ekspert på et bestemt område – en kjenner alt om flyreiser, en annen om hoteller, og en tredje om å planlegge reiseruten. Når du ber om en reise, sender MCP Server forespørselen til riktig(e) agent(er). Disse bruker sin kunnskap og verktøy for å finne de beste alternativene for deg.

### Azure OpenAI Service (Språkekspert):
Dette er som å ha en språkekspert som forstår nøyaktig hva du spør om, uansett hvordan du formulerer det. Den hjelper agentene med å forstå forespørslene dine og svare på en naturlig, samtalebasert måte.

### Azure AI Search & bedriftsdata (Informasjonsbibliotek):
Tenk deg et enormt, oppdatert bibliotek med all den nyeste reiseinformasjonen – flytider, hotelltilgjengelighet og mer. Agentene søker i dette biblioteket for å finne de mest nøyaktige svarene til deg.

### Autentisering og sikkerhet (Vekter):
Akkurat som en vekter sjekker hvem som får adgang til visse områder, sørger denne delen for at bare autoriserte personer og agenter får tilgang til sensitiv informasjon. Den holder dataene dine trygge og private.

### Distribusjon på Azure Container Apps (Bygningen):
Alle disse hjelperne og verktøyene jobber sammen inne i en sikker, skalerbar bygning (skyen). Det betyr at systemet kan håndtere mange brukere samtidig og alltid er tilgjengelig når du trenger det.

## Hvordan det hele fungerer sammen:

Du starter med å stille et spørsmål i resepsjonen (UI).  
Lederen (MCP Server) finner ut hvilken spesialist (agent) som skal hjelpe deg.  
Spesialisten bruker språkeksperten (OpenAI) for å forstå forespørselen din og biblioteket (AI Search) for å finne det beste svaret.  
Vekteren (Autentisering) sørger for at alt er trygt.  
Alt dette skjer inne i en pålitelig, skalerbar bygning (Azure Container Apps), slik at opplevelsen din blir smidig og sikker.  
Dette samarbeidet gjør at systemet raskt og trygt kan hjelpe deg med å planlegge reisen, akkurat som et team av ekspertreiseagenter som jobber sammen på et moderne kontor!

## Teknisk implementering
- **MCP Server:** Huser kjernelogikken for orkestrering, eksponerer agentverktøy og håndterer kontekst for flertrinns reiseplanleggingsarbeidsflyter.
- **Agenter:** Hver agent (f.eks. FlightAgent, HotelAgent) er implementert som et MCP-verktøy med egne promptmaler og logikk.
- **Azure-integrasjon:** Bruker Azure OpenAI for naturlig språkforståelse og Azure AI Search for datainnhenting.
- **Sikkerhet:** Integreres med Microsoft Entra ID for autentisering og anvender prinsippet om minste privilegium for tilgangskontroll til alle ressurser.
- **Distribusjon:** Støtter distribusjon til Azure Container Apps for skalerbarhet og driftseffektivitet.

## Resultater og betydning
- Viser hvordan MCP kan brukes til å orkestrere flere AI-agenter i et virkelighetsnært, produksjonsklart scenario.
- Fremskynder utvikling av løsninger ved å tilby gjenbrukbare mønstre for agentkoordinering, dataintegrasjon og sikker distribusjon.
- Fungerer som en mal for å bygge domene-spesifikke, AI-drevne applikasjoner ved bruk av MCP og Azure-tjenester.

## Referanser
- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)
- [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.