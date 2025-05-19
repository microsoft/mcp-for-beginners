<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "344a126b620ff7997158542fd31be6a4",
  "translation_date": "2025-05-19T18:31:42+00:00",
  "source_file": "07-LessonsfromEarlyAdoption/README.md",
  "language_code": "fi"
}
-->
# Lessons from Early Adoprters

## Overview

Tässä oppitunnissa tarkastellaan, miten varhaiset omaksujat ovat hyödyntäneet Model Context Protocolia (MCP) ratkaistakseen käytännön haasteita ja edistääkseen innovaatiota eri toimialoilla. Yksityiskohtaisten tapaustutkimusten ja käytännön projektien kautta näet, miten MCP mahdollistaa standardoidun, turvallisen ja skaalautuvan tekoälyn integroinnin – yhdistäen suuria kielimalleja, työkaluja ja yrityksen dataa yhtenäiseen kehykseen. Saat käytännön kokemusta MCP-pohjaisten ratkaisujen suunnittelusta ja rakentamisesta, opit toimivista toteutusmalleista sekä parhaista käytännöistä MCP:n käyttöönotossa tuotantoympäristöissä. Oppitunti käsittelee myös nousevia trendejä, tulevia suuntia ja avoimen lähdekoodin resursseja, jotka auttavat pysymään MCP-teknologian ja sen kehittyvän ekosysteemin kärjessä.

## Learning Objectives

- Analysoida MCP:n käytännön toteutuksia eri toimialoilla
- Suunnitella ja rakentaa kokonaisia MCP-pohjaisia sovelluksia
- Tutkia MCP-teknologian nousevia trendejä ja tulevia suuntia
- Soveltaa parhaita käytäntöjä todellisissa kehitystilanteissa

## Real-world MCP Implementations

### Case Study 1: Enterprise Customer Support Automation

Monikansallinen yritys otti käyttöön MCP-pohjaisen ratkaisun standardoidakseen tekoälyvuorovaikutukset asiakastukijärjestelmissään. Tämä mahdollisti:

- Yhtenäisen käyttöliittymän useille LLM-toimittajille
- Johdonmukaisen kehotteiden hallinnan eri osastojen välillä
- Vahvat turvallisuus- ja vaatimustenmukaisuuden valvontamekanismit
- Helpon siirtymisen eri tekoälymallien välillä tarpeen mukaan

**Technical Implementation:**  
```python
# Python MCP server implementation for customer support
import logging
import asyncio
from modelcontextprotocol import create_server, ServerConfig
from modelcontextprotocol.server import MCPServer
from modelcontextprotocol.transports import create_http_transport
from modelcontextprotocol.resources import ResourceDefinition
from modelcontextprotocol.prompts import PromptDefinition
from modelcontextprotocol.tool import ToolDefinition

# Configure logging
logging.basicConfig(level=logging.INFO)

async def main():
    # Create server configuration
    config = ServerConfig(
        name="Enterprise Customer Support Server",
        version="1.0.0",
        description="MCP server for handling customer support inquiries"
    )
    
    # Initialize MCP server
    server = create_server(config)
    
    # Register knowledge base resources
    server.resources.register(
        ResourceDefinition(
            name="customer_kb",
            description="Customer knowledge base documentation"
        ),
        lambda params: get_customer_documentation(params)
    )
    
    # Register prompt templates
    server.prompts.register(
        PromptDefinition(
            name="support_template",
            description="Templates for customer support responses"
        ),
        lambda params: get_support_templates(params)
    )
    
    # Register support tools
    server.tools.register(
        ToolDefinition(
            name="ticketing",
            description="Create and update support tickets"
        ),
        handle_ticketing_operations
    )
    
    # Start server with HTTP transport
    transport = create_http_transport(port=8080)
    await server.run(transport)

if __name__ == "__main__":
    asyncio.run(main())
```

**Results:** 30 % kustannussäästöt malleissa, 45 % parannus vastausten johdonmukaisuudessa ja parannettu vaatimustenmukaisuus globaalissa toiminnassa.

### Case Study 2: Healthcare Diagnostic Assistant

Terveydenhuollon palveluntarjoaja kehitti MCP-infrastruktuurin integroidakseen useita erikoistuneita lääketieteellisiä tekoälymalleja samalla varmistaen, että arkaluonteiset potilastiedot pysyivät suojattuina:

- Saumaton vaihto yleislääketieteen ja erikoismallien välillä
- Tiukat tietosuojaohjeet ja auditointijäljet
- Integrointi olemassa oleviin potilastietojärjestelmiin (EHR)
- Johdonmukainen kehotteiden suunnittelu lääketieteelliseen terminologiaan

**Technical Implementation:**  
```csharp
// C# MCP host application implementation in healthcare application
using Microsoft.Extensions.DependencyInjection;
using ModelContextProtocol.SDK.Client;
using ModelContextProtocol.SDK.Security;
using ModelContextProtocol.SDK.Resources;

public class DiagnosticAssistant
{
    private readonly MCPHostClient _mcpClient;
    private readonly PatientContext _patientContext;
    
    public DiagnosticAssistant(PatientContext patientContext)
    {
        _patientContext = patientContext;
        
        // Configure MCP client with healthcare-specific settings
        var clientOptions = new ClientOptions
        {
            Name = "Healthcare Diagnostic Assistant",
            Version = "1.0.0",
            Security = new SecurityOptions
            {
                Encryption = EncryptionLevel.Medical,
                AuditEnabled = true
            }
        };
        
        _mcpClient = new MCPHostClientBuilder()
            .WithOptions(clientOptions)
            .WithTransport(new HttpTransport("https://healthcare-mcp.example.org"))
            .WithAuthentication(new HIPAACompliantAuthProvider())
            .Build();
    }
    
    public async Task<DiagnosticSuggestion> GetDiagnosticAssistance(
        string symptoms, string patientHistory)
    {
        // Create request with appropriate resources and tool access
        var resourceRequest = new ResourceRequest
        {
            Name = "patient_records",
            Parameters = new Dictionary<string, object>
            {
                ["patientId"] = _patientContext.PatientId,
                ["requestingProvider"] = _patientContext.ProviderId
            }
        };
        
        // Request diagnostic assistance using appropriate prompt
        var response = await _mcpClient.SendPromptRequestAsync(
            promptName: "diagnostic_assistance",
            parameters: new Dictionary<string, object>
            {
                ["symptoms"] = symptoms,
                patientHistory = patientHistory,
                relevantGuidelines = _patientContext.GetRelevantGuidelines()
            });
            
        return DiagnosticSuggestion.FromMCPResponse(response);
    }
}
```

**Results:** Parantuneet diagnoosiehdotukset lääkäreille, täydellinen HIPAA-vaatimusten noudattaminen ja merkittävä kontekstinvaihdon vähennys järjestelmien välillä.

### Case Study 3: Financial Services Risk Analysis

Rahoituslaitos otti MCP:n käyttöön standardoidakseen riskianalyysiprosessinsa eri osastoilla:

- Yhtenäinen käyttöliittymä luottoriskin, petosten tunnistuksen ja sijoitusriskimallien hallintaan
- Tiukat käyttöoikeudet ja malliversioiden hallinta
- Kaikkien tekoälysuositusten auditointimahdollisuus
- Johdonmukainen datan muotoilu eri järjestelmien välillä

**Technical Implementation:**  
```java
// Java MCP server for financial risk assessment
import org.mcp.server.*;
import org.mcp.security.*;

public class FinancialRiskMCPServer {
    public static void main(String[] args) {
        // Create MCP server with financial compliance features
        MCPServer server = new MCPServerBuilder()
            .withModelProviders(
                new ModelProvider("risk-assessment-primary", new AzureOpenAIProvider()),
                new ModelProvider("risk-assessment-audit", new LocalLlamaProvider())
            )
            .withPromptTemplateDirectory("./compliance/templates")
            .withAccessControls(new SOCCompliantAccessControl())
            .withDataEncryption(EncryptionStandard.FINANCIAL_GRADE)
            .withVersionControl(true)
            .withAuditLogging(new DatabaseAuditLogger())
            .build();
            
        server.addRequestValidator(new FinancialDataValidator());
        server.addResponseFilter(new PII_RedactionFilter());
        
        server.start(9000);
        
        System.out.println("Financial Risk MCP Server running on port 9000");
    }
}
```

**Results:** Parannettu sääntelynmukaisuus, 40 % nopeammat mallien käyttöönottoajat ja parempi riskinarvioinnin johdonmukaisuus osastojen välillä.

### Case Study 4: Microsoft Playwright MCP Server for Browser Automation

Microsoft kehitti [Playwright MCP serverin](https://github.com/microsoft/playwright-mcp) mahdollistamaan turvallisen ja standardoidun selaimen automaation Model Context Protocolin avulla. Tämä ratkaisu mahdollistaa tekoälyagenttien ja LLM:ien vuorovaikutuksen verkkoselainten kanssa hallitulla, auditoitavalla ja laajennettavalla tavalla – mahdollistaen käyttötapauksia kuten automaattinen verkkotestaus, datan poiminta ja end-to-end-työnkulut.

- Tarjoaa selaimen automaatiotoiminnot (navigointi, lomakkeiden täyttö, kuvakaappaukset jne.) MCP-työkaluina
- Toteuttaa tiukat pääsynvalvonnat ja hiekkalaatikkotoiminnot luvattomien toimintojen estämiseksi
- Tarjoaa yksityiskohtaiset auditointilokit kaikista selaimen toiminnoista
- Tukee integraatiota Azure OpenAI:n ja muiden LLM-toimittajien kanssa agenttiohjattuun automaatioon

**Technical Implementation:**  
```typescript
// TypeScript: Registering Playwright browser automation tools in an MCP server
import { createServer, ToolDefinition } from 'modelcontextprotocol';
import { launch } from 'playwright';

const server = createServer({
  name: 'Playwright MCP Server',
  version: '1.0.0',
  description: 'MCP server for browser automation using Playwright'
});

// Register a tool for navigating to a URL and capturing a screenshot
server.tools.register(
  new ToolDefinition({
    name: 'navigate_and_screenshot',
    description: 'Navigate to a URL and capture a screenshot',
    parameters: {
      url: { type: 'string', description: 'The URL to visit' }
    }
  }),
  async ({ url }) => {
    const browser = await launch();
    const page = await browser.newPage();
    await page.goto(url);
    const screenshot = await page.screenshot();
    await browser.close();
    return { screenshot };
  }
);

// Start the MCP server
server.listen(8080);
```

**Results:**  
- Mahdollisti turvallisen, ohjelmallisen selaimen automaation tekoälyagenteille ja LLM:ille  
- Vähensi manuaalisen testauksen tarvetta ja paransi testikattavuutta web-sovelluksissa  
- Tarjosi uudelleenkäytettävän ja laajennettavan kehyksen selaimen työkalujen integrointiin yritysympäristöissä

**References:**  
- [Playwright MCP Server GitHub Repository](https://github.com/microsoft/playwright-mcp)  
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

### Case Study 5: Azure MCP – Enterprise-Grade Model Context Protocol as a Service

Azure MCP ([https://aka.ms/azmcp](https://aka.ms/azmcp)) on Microsoftin hallinnoitu, yritystason toteutus Model Context Protocolista, joka tarjoaa skaalautuvat, turvalliset ja vaatimustenmukaiset MCP-palvelinominaisuudet pilvipalveluna. Azure MCP mahdollistaa organisaatioiden nopean käyttöönoton, hallinnan ja MCP-palvelimien integroinnin Azure AI-, data- ja tietoturvapalveluihin, vähentäen operatiivista kuormaa ja nopeuttaen tekoälyn käyttöönottoa.

- Täysin hallinnoitu MCP-palvelin, jossa sisäänrakennettu skaalaus, valvonta ja tietoturva  
- Natiivisti integroitu Azure OpenAI:n, Azure AI Searchin ja muiden Azuren palveluiden kanssa  
- Yritystason tunnistus ja valtuutus Microsoft Entra ID:n kautta  
- Tuki räätälöidyille työkaluilla, kehotepohjille ja resurssien liittimille  
- Vaatimustenmukaisuus yrityksen tietoturva- ja sääntelyvaatimusten kanssa

**Technical Implementation:**  
```yaml
# Example: Azure MCP server deployment configuration (YAML)
apiVersion: mcp.microsoft.com/v1
kind: McpServer
metadata:
  name: enterprise-mcp-server
spec:
  modelProviders:
    - name: azure-openai
      type: AzureOpenAI
      endpoint: https://<your-openai-resource>.openai.azure.com/
      apiKeySecret: <your-azure-keyvault-secret>
  tools:
    - name: document_search
      type: AzureAISearch
      endpoint: https://<your-search-resource>.search.windows.net/
      apiKeySecret: <your-azure-keyvault-secret>
  authentication:
    type: EntraID
    tenantId: <your-tenant-id>
  monitoring:
    enabled: true
    logAnalyticsWorkspace: <your-log-analytics-id>
```

**Results:**  
- Lyhensi yritysten tekoälyprojektien aika-arvoa tarjoamalla valmiin, vaatimustenmukaisen MCP-palvelinalustan  
- Yksinkertaisti LLM:ien, työkalujen ja yritysdatan lähteiden integrointia  
- Paransi tietoturvaa, näkyvyyttä ja operatiivista tehokkuutta MCP-kuormissa

**References:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [Azure AI Services](https://azure.microsoft.com/en-us/products/ai-services/)

## Case Study 6: NLWeb  
MCP (Model Context Protocol) on nouseva protokolla chatboteille ja tekoälyavustajille työkaluilla vuorovaikutukseen. Jokainen NLWeb-instanssi toimii myös MCP-palvelimena, joka tukee yhtä ydintoimintoa, ask-metodia, jolla voi esittää verkkosivustolle kysymyksiä luonnollisella kielellä. Palautettu vastaus hyödyntää schema.org-standardia, joka on laajasti käytetty sanasto verkkodatan kuvaamiseen. Vapaasti ilmaistuna MCP on NLWebin suhde Http:hen HTML:ssä. NLWeb yhdistää protokollat, Schema.org-muodot ja esimerkkikoodin auttaakseen sivustoja luomaan nopeasti tällaisia päätepisteitä, hyödyttäen sekä ihmisiä keskustelukäyttöliittymien kautta että koneita luonnollisen agentti-agentti-vuorovaikutuksen kautta.

NLWeb koostuu kahdesta erillisestä osasta:  
- Protokolla, joka on aluksi hyvin yksinkertainen, ja jonka avulla voi kommunikoida sivuston kanssa luonnollisella kielellä sekä formaatti, joka hyödyntää jsonia ja schema.org:ia vastauksen kuvaamiseen. Katso REST API -dokumentaatio lisätietoja varten.  
- Yksinkertainen toteutus (1), joka hyödyntää olemassa olevaa merkintää, sivustoille jotka voidaan abstraktoida kohdelistoiksi (tuotteet, reseptit, nähtävyydet, arvostelut jne.). Yhdessä käyttöliittymäwidgettien kanssa sivustot voivat helposti tarjota keskustelupohjaisia käyttöliittymiä sisällölleen. Katso dokumentaatio Life of a chat query -osiosta lisätietoja toimintaperiaatteesta.

**References:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [NLWeb](https://github.com/microsoft/NlWeb)

## Hands-on Projects

### Project 1: Build a Multi-Provider MCP Server

**Objective:** Luo MCP-palvelin, joka osaa ohjata pyyntöjä useille tekoälymallien tarjoajille tiettyjen kriteerien perusteella.

**Requirements:**  
- Tuki vähintään kolmelle eri mallitoimittajalle (esim. OpenAI, Anthropic, paikalliset mallit)  
- Reititysmekanismi pyyntöjen metatietojen perusteella  
- Konfigurointijärjestelmä toimittajien tunnistetietojen hallintaan  
- Välimuisti suorituskyvyn ja kustannusten optimointiin  
- Yksinkertainen hallintapaneeli käytön seurantaan

**Implementation Steps:**  
1. Perusta MCP-palvelininfrastruktuuri  
2. Toteuta toimittajien adapterit kullekin tekoälymallipalvelulle  
3. Luo reitityslogiikka pyyntöjen ominaisuuksien perusteella  
4. Lisää välimuistimekanismit usein toistuviin pyyntöihin  
5. Kehitä valvontapaneeli  
6. Testaa erilaisilla pyyntökuvioilla

**Technologies:** Valitse Python (.NET/Java/Python mieltymyksesi mukaan), Redis välimuistiksi ja kevyt web-kehys hallintapaneelille.

### Project 2: Enterprise Prompt Management System

**Objective:** Kehitä MCP-pohjainen järjestelmä kehotepohjien hallintaan, versiointiin ja käyttöönottoon organisaation sisällä.

**Requirements:**  
- Keskitetty arkisto kehotepohjille  
- Versiointi- ja hyväksymisprosessit  
- Testausmahdollisuudet esimerkkisyötteillä  
- Roolipohjaiset käyttöoikeudet  
- API kehotepohjien hakemiseen ja käyttöönottoon

**Implementation Steps:**  
1. Suunnittele tietokantakaavio pohjien tallennukselle  
2. Luo ydintoiminnot pohjien CRUD-käyttöön  
3. Toteuta versiointijärjestelmä  
4. Rakenna hyväksymisprosessi  
5. Kehitä testauskehys  
6. Luo yksinkertainen web-käyttöliittymä hallintaan  
7. Integroi MCP-palvelimeen

**Technologies:** Valitse haluamasi backend-kehys, SQL- tai NoSQL-tietokanta ja frontend-kehys hallintaliittymälle.

### Project 3: MCP-Based Content Generation Platform

**Objective:** Rakenna sisällöntuotantoalusta, joka hyödyntää MCP:tä tarjotakseen johdonmukaisia tuloksia eri sisältötyypeille.

**Requirements:**  
- Tuki useille sisältömuodoille (blogikirjoitukset, some, markkinointitekstit)  
- Mallipohjainen generointi muokkausmahdollisuuksilla  
- Sisällön arviointi- ja palautteenantojärjestelmä  
- Sisällön suorituskykymittarien seuranta  
- Sisältöjen versiointi ja iterointi

**Implementation Steps:**  
1. Perusta MCP-asiakasinfrastruktuuri  
2. Luo pohjat eri sisältötyypeille  
3. Rakenna sisällöntuotantoputki  
4. Toteuta arviointijärjestelmä  
5. Kehitä mittariseurantajärjestelmä  
6. Luo käyttöliittymä pohjien hallintaan ja sisällöntuotantoon

**Technologies:** Valitse oma suosikkiohjelmointikielesi, web-kehys ja tietokanta.

## Future Directions for MCP Technology

### Emerging Trends

1. **Multi-Modal MCP**  
   - MCP:n laajentaminen vakioimaan vuorovaikutukset kuvan, äänen ja videon mallien kanssa  
   - Monimodaalisen päättelyn kehitys  
   - Standardoidut kehotemuodot eri modaliteeteille

2. **Federated MCP Infrastructure**  
   - Hajautetut MCP-verkostot, jotka voivat jakaa resursseja organisaatioiden välillä  
   - Standardoidut protokollat turvalliseen mallien jakamiseen  
   - Tietosuojaa parantavat laskentamenetelmät

3. **MCP Marketplaces**  
   - Ekosysteemit MCP-kehotepohjien ja lisäosien jakamiseen ja kaupallistamiseen  
   - Laadunvarmistus- ja sertifiointiprosessit  
   - Integraatio mallimarkkinoiden kanssa

4. **MCP for Edge Computing**  
   - MCP-standardien sovittaminen resurssirajoitteisille reunalaitteille  
   - Optimoidut protokollat vähäkaistaisiin ympäristöihin  
   - Erityiset MCP-toteutukset IoT-ekosysteemeille

5. **Regulatory Frameworks**  
   - MCP-laajennusten kehitys sääntelyn noudattamiseen  
   - Standardoidut auditointijäljet ja selitettävyyden rajapinnat  
   - Integraatio nousevien tekoälyn hallintakehysten kanssa

### MCP Solutions from Microsoft 

Microsoft ja Azure ovat kehittäneet useita avoimen lähdekoodin repositorioita auttamaan kehittäjiä MCP:n toteutuksissa eri käyttötapauksissa:

#### Microsoft Organization  
1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) – Playwright MCP -palvelin selaimen automaatioon ja testaukseen  
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) – OneDrive MCP -palvelin paikalliseen testaukseen ja yhteisön panokseen  
3. [NLWeb](https://github.com/microsoft/NlWeb) – Kokoelma avoimia protokollia ja työkaluja, joiden pääpaino on tekoälyverkon perustan luomisessa  

#### Azure-Samples Organization  
1. [mcp](https://github.com/Azure-Samples/mcp) – Esimerkkejä, työkaluja ja resursseja MCP-palvelimien rakentamiseen ja integrointiin Azurella eri kielillä  
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) – Referenssipalvelimia MCP:n autentikointiesimerkeillä  
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) – Etä-MCP-palvelinten toteutuksia Azure Functions -ympäristössä  
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) – Pika-aloitusmalli etä-MCP-palvelimille Pythonilla Azure Functions -ympäristössä  
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) – Pika-aloitusmalli etä-MCP-palvelimille .NET/C#-kielellä Azure Functions -ympäristössä  
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) – Pika-aloitusmalli etä-MCP-palvelimille TypeScriptillä Azure Functions -ympäristössä  
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) – Azure API Management tekoälyporttina etä-MCP-palvelimille Pythonilla  
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) – APIM ❤️ AI -kokeiluja MCP-ominaisuuksilla, integroitu Azure OpenAI:hin ja AI Foundryyn

Nämä repositoriot tarjoavat erilaisia toteutuksia, malleja ja resursseja MCP:n käyttöön eri ohjelmointikielillä ja Azuren palveluissa. Ne kattavat peruspalvelinratkaisuista autentikointiin, pilvikäyttöön ja yritysintegrointiin.

#### MCP Resources Directory

Virallisen Microsoft MCP -varaston [MCP Resources -hakemisto](https://github.com/microsoft/mcp/tree/main/Resources) tarjoaa valikoiman esimerkkiresursseja, kehotepohjia ja työkalumäärittelyjä MCP-palvelimien käyttöön. Tämä hakemisto on suunniteltu auttamaan kehittäjiä pääsemään nopeasti alkuun MCP:n kanssa tarjo
- [Remote MCP Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-python)
- [Remote MCP Functions .NET (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
- [Remote MCP Functions TypeScript (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-typescript)
- [Remote MCP APIM Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
- [AI-Gateway (Azure-Samples)](https://github.com/Azure-Samples/AI-Gateway)
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

## Harjoitukset

1. Analysoi yksi tapaustutkimuksista ja ehdota vaihtoehtoinen toteutustapa.
2. Valitse yksi projektiehdotus ja laadi yksityiskohtainen tekninen määrittely.
3. Tutki toimiala, jota ei ole käsitelty tapaustutkimuksissa, ja hahmottele, miten MCP voisi ratkaista sen erityisiä haasteita.
4. Tutki yhtä tulevaisuuden suuntausta ja luo konsepti uudelle MCP-laajennukselle sen tukemiseksi.

Seuraava: [Best Practices](../08-BestPractices/README.md)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää auktoritatiivisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virhetulkinnoista.