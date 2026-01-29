# Case Study: Opdatering af Azure DevOps-elementer med data fra YouTube ved hjælp af MCP

> **Disclaimer:** Der findes allerede online værktøjer og rapporter, som kan automatisere processen med at opdatere Azure DevOps-elementer med data fra platforme som YouTube. Det følgende scenarie er udelukkende et eksempel på, hvordan MCP-værktøjer kan anvendes til automatisering og integration.

## Oversigt

Denne case study viser et eksempel på, hvordan Model Context Protocol (MCP) og dets værktøjer kan bruges til at automatisere opdateringen af Azure DevOps (ADO) arbejdsopgaver med information hentet fra online platforme som YouTube. Det beskrevne scenarie er blot en illustration af de bredere muligheder med disse værktøjer, som kan tilpasses mange lignende automatiseringsbehov.

I dette eksempel følger en Advocate online sessioner ved hjælp af ADO-elementer, hvor hvert element indeholder en YouTube-video-URL. Ved at bruge MCP-værktøjer kan Advocaten holde ADO-elementerne opdaterede med de nyeste videometre, såsom antal visninger, på en gentagelig og automatiseret måde. Denne tilgang kan generaliseres til andre tilfælde, hvor information fra online kilder skal integreres i ADO eller andre systemer.

## Scenarie

En Advocate har ansvaret for at følge op på effekten af online sessioner og community-engagement. Hver session registreres som en ADO arbejdsopgave i projektet 'DevRel', og arbejdsopgaven indeholder et felt til YouTube-videoens URL. For at kunne rapportere sessionens rækkevidde præcist, skal Advocaten opdatere ADO-elementet med det aktuelle antal videovisninger og datoen for, hvornår denne information blev hentet.

## Brugte værktøjer

- [Azure DevOps MCP](https://github.com/microsoft/azure-devops-mcp): Muliggør programmatisk adgang til og opdatering af ADO arbejdsopgaver via MCP.
- [Playwright MCP](https://github.com/microsoft/playwright-mcp): Automatiserer browserhandlinger for at hente live data fra websider, såsom YouTube-videoers statistik.

## Trin-for-trin workflow

1. **Identificer ADO-elementet**: Start med ADO arbejdsopgave-ID'et (f.eks. 1234) i projektet 'DevRel'.
2. **Hent YouTube-URL'en**: Brug Azure DevOps MCP-værktøjet til at få YouTube-URL'en fra arbejdsopgaven.
3. **Udtræk videovisninger**: Brug Playwright MCP-værktøjet til at navigere til YouTube-URL'en og hente det aktuelle antal visninger.
4. **Opdater ADO-elementet**: Skriv det seneste antal visninger og datoen for hentningen ind i sektionen 'Impact and Learnings' i ADO-arbejdsopgaven ved hjælp af Azure DevOps MCP-værktøjet.

## Eksempel på prompt

```bash
- Work with the ADO Item ID: 1234
- The project is '2025-Awesome'
- Get the YouTube URL for the ADO item
- Use Playwright to get the current views from the YouTube video
- Update the ADO item with the current video views and the updated date of the information
```

## Mermaid flowchart

```mermaid
flowchart TD
    A[Start: Advocate identifies ADO Item ID] --> B[Get YouTube URL from ADO Item using Azure DevOps MCP]
    B --> C[Extract current video views using Playwright MCP]
    C --> D[Update ADO Item's Impact and Learnings section with view count and date]
    D --> E[End]
```

## Teknisk implementering

- **MCP Orkestrering**: Workflowet styres af en MCP-server, som koordinerer brugen af både Azure DevOps MCP og Playwright MCP-værktøjerne.
- **Automatisering**: Processen kan trigges manuelt eller planlægges til at køre med faste intervaller for at holde ADO-elementerne opdaterede.
- **Udvidelsesmuligheder**: Samme mønster kan bruges til at opdatere ADO-elementer med andre online metrikker (f.eks. likes, kommentarer) eller fra andre platforme.

## Resultater og effekt

- **Effektivitet**: Mindsker manuelt arbejde for Advocates ved at automatisere indhentning og opdatering af videometre.
- **Nøjagtighed**: Sikrer, at ADO-elementer afspejler de mest aktuelle data fra online kilder.
- **Gentagelighed**: Tilbyder en genanvendelig workflow til lignende scenarier med andre datakilder eller metrikker.

## Referencer

- [Azure DevOps MCP](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP](https://github.com/microsoft/playwright-mcp)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.