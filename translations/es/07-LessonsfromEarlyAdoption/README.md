<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "344a126b620ff7997158542fd31be6a4",
  "translation_date": "2025-05-19T17:44:08+00:00",
  "source_file": "07-LessonsfromEarlyAdoption/README.md",
  "language_code": "es"
}
-->
# Lessons from Early Adoprters

## Overview

Esta lección explora cómo los primeros adoptantes han aprovechado el Model Context Protocol (MCP) para resolver desafíos reales e impulsar la innovación en diversas industrias. A través de estudios de caso detallados y proyectos prácticos, verás cómo MCP permite una integración de IA estandarizada, segura y escalable, conectando grandes modelos de lenguaje, herramientas y datos empresariales en un marco unificado. Obtendrás experiencia práctica diseñando y construyendo soluciones basadas en MCP, aprenderás de patrones de implementación comprobados y descubrirás las mejores prácticas para desplegar MCP en entornos de producción. La lección también destaca tendencias emergentes, direcciones futuras y recursos de código abierto para ayudarte a mantenerte a la vanguardia de la tecnología MCP y su ecosistema en evolución.

## Learning Objectives

- Analizar implementaciones reales de MCP en distintas industrias  
- Diseñar y construir aplicaciones completas basadas en MCP  
- Explorar tendencias emergentes y direcciones futuras en la tecnología MCP  
- Aplicar mejores prácticas en escenarios reales de desarrollo  

## Real-world MCP Implementations

### Case Study 1: Enterprise Customer Support Automation

Una corporación multinacional implementó una solución basada en MCP para estandarizar las interacciones de IA en sus sistemas de soporte al cliente. Esto les permitió:

- Crear una interfaz unificada para múltiples proveedores de LLM  
- Mantener una gestión consistente de prompts entre departamentos  
- Implementar controles robustos de seguridad y cumplimiento  
- Cambiar fácilmente entre diferentes modelos de IA según necesidades específicas  

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

**Results:** Reducción del 30% en costos de modelos, mejora del 45% en la consistencia de respuestas y mayor cumplimiento en operaciones globales.

### Case Study 2: Healthcare Diagnostic Assistant

Un proveedor de salud desarrolló una infraestructura MCP para integrar múltiples modelos médicos especializados de IA, asegurando que los datos sensibles de los pacientes permanecieran protegidos:

- Cambio fluido entre modelos médicos generalistas y especialistas  
- Controles estrictos de privacidad y registros de auditoría  
- Integración con sistemas existentes de Electronic Health Record (EHR)  
- Ingeniería de prompts consistente para terminología médica  

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

**Results:** Mejora en las sugerencias diagnósticas para médicos, cumplimiento total con HIPAA y reducción significativa en cambios de contexto entre sistemas.

### Case Study 3: Financial Services Risk Analysis

Una institución financiera implementó MCP para estandarizar sus procesos de análisis de riesgo en distintos departamentos:

- Creación de una interfaz unificada para modelos de riesgo crediticio, detección de fraude y riesgo de inversión  
- Implementación de controles estrictos de acceso y versionado de modelos  
- Garantía de auditabilidad en todas las recomendaciones de IA  
- Mantenimiento de un formato de datos consistente en sistemas diversos  

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

**Results:** Mejor cumplimiento regulatorio, ciclos de despliegue de modelos un 40% más rápidos y mayor consistencia en la evaluación de riesgos.

### Case Study 4: Microsoft Playwright MCP Server for Browser Automation

Microsoft desarrolló el [Playwright MCP server](https://github.com/microsoft/playwright-mcp) para habilitar la automatización de navegadores de forma segura y estandarizada mediante el Model Context Protocol. Esta solución permite que agentes de IA y LLMs interactúen con navegadores web de manera controlada, auditable y extensible, habilitando casos de uso como pruebas web automatizadas, extracción de datos y flujos de trabajo de extremo a extremo.

- Expone capacidades de automatización de navegador (navegación, llenado de formularios, captura de pantalla, etc.) como herramientas MCP  
- Implementa controles estrictos de acceso y sandboxing para prevenir acciones no autorizadas  
- Proporciona registros detallados de auditoría para todas las interacciones con el navegador  
- Soporta integración con Azure OpenAI y otros proveedores de LLM para automatización impulsada por agentes  

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
- Habilitó automatización programática segura de navegadores para agentes de IA y LLMs  
- Redujo el esfuerzo en pruebas manuales y mejoró la cobertura de pruebas para aplicaciones web  
- Proporcionó un marco reutilizable y extensible para integración de herramientas basadas en navegador en entornos empresariales  

**References:**  
- [Playwright MCP Server GitHub Repository](https://github.com/microsoft/playwright-mcp)  
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)  

### Case Study 5: Azure MCP – Enterprise-Grade Model Context Protocol as a Service

Azure MCP ([https://aka.ms/azmcp](https://aka.ms/azmcp)) es la implementación gestionada y de nivel empresarial del Model Context Protocol de Microsoft, diseñada para ofrecer capacidades escalables, seguras y conformes de servidores MCP como servicio en la nube. Azure MCP permite a las organizaciones desplegar, administrar e integrar rápidamente servidores MCP con servicios de Azure AI, datos y seguridad, reduciendo la carga operativa y acelerando la adopción de IA.

- Hospedaje totalmente gestionado de servidores MCP con escalado, monitoreo y seguridad integrados  
- Integración nativa con Azure OpenAI, Azure AI Search y otros servicios de Azure  
- Autenticación y autorización empresarial mediante Microsoft Entra ID  
- Soporte para herramientas personalizadas, plantillas de prompts y conectores de recursos  
- Cumplimiento con requisitos de seguridad y regulaciones empresariales  

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
- Reducción del tiempo para obtener valor en proyectos de IA empresarial gracias a una plataforma MCP lista para usar y conforme  
- Simplificación en la integración de LLMs, herramientas y fuentes de datos empresariales  
- Mejora en seguridad, observabilidad y eficiencia operativa para cargas MCP  

**References:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [Azure AI Services](https://azure.microsoft.com/en-us/products/ai-services/)  

## Case Study 6: NLWeb  
MCP (Model Context Protocol) es un protocolo emergente para que chatbots y asistentes de IA interactúen con herramientas. Cada instancia de NLWeb es también un servidor MCP que soporta un método principal, ask, utilizado para hacer preguntas a un sitio web en lenguaje natural. La respuesta devuelta utiliza schema.org, un vocabulario ampliamente usado para describir datos web. En términos generales, MCP es para NLWeb lo que HTTP es para HTML. NLWeb combina protocolos, formatos schema.org y código de ejemplo para ayudar a los sitios a crear rápidamente estos endpoints, beneficiando tanto a humanos mediante interfaces conversacionales como a máquinas mediante interacciones naturales entre agentes.

NLWeb consta de dos componentes distintos:  
- Un protocolo, muy simple al principio, para interactuar con un sitio en lenguaje natural y un formato que usa json y schema.org para la respuesta. Consulta la documentación sobre la REST API para más detalles.  
- Una implementación sencilla de (1) que aprovecha el marcado existente, para sitios que pueden abstraerse como listas de ítems (productos, recetas, atracciones, reseñas, etc.). Junto con un conjunto de widgets de interfaz de usuario, los sitios pueden ofrecer fácilmente interfaces conversacionales para su contenido. Consulta la documentación sobre Life of a chat query para más detalles sobre su funcionamiento.  

**References:**  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [NLWeb](https://github.com/microsoft/NlWeb)  

## Hands-on Projects

### Project 1: Build a Multi-Provider MCP Server

**Objective:** Crear un servidor MCP que pueda enrutar solicitudes a múltiples proveedores de modelos de IA según criterios específicos.

**Requirements:**  
- Soportar al menos tres proveedores diferentes de modelos (por ejemplo, OpenAI, Anthropic, modelos locales)  
- Implementar un mecanismo de enrutamiento basado en metadatos de la solicitud  
- Crear un sistema de configuración para gestionar credenciales de proveedores  
- Añadir caché para optimizar rendimiento y costos  
- Construir un panel sencillo para monitorear el uso  

**Implementation Steps:**  
1. Configurar la infraestructura básica del servidor MCP  
2. Implementar adaptadores para cada servicio de modelo de IA  
3. Crear la lógica de enrutamiento basada en atributos de la solicitud  
4. Añadir mecanismos de caché para solicitudes frecuentes  
5. Desarrollar el panel de monitoreo  
6. Probar con distintos patrones de solicitud  

**Technologies:** Elige entre Python (.NET/Java/Python según preferencia), Redis para caché y un framework web sencillo para el panel.

### Project 2: Enterprise Prompt Management System

**Objective:** Desarrollar un sistema basado en MCP para gestionar, versionar y desplegar plantillas de prompts en toda una organización.

**Requirements:**  
- Crear un repositorio centralizado para plantillas de prompts  
- Implementar versionado y flujos de trabajo de aprobación  
- Construir capacidades de prueba de plantillas con entradas de ejemplo  
- Desarrollar controles de acceso basados en roles  
- Crear una API para recuperación y despliegue de plantillas  

**Implementation Steps:**  
1. Diseñar el esquema de base de datos para almacenamiento de plantillas  
2. Crear la API principal para operaciones CRUD de plantillas  
3. Implementar el sistema de versionado  
4. Construir el flujo de trabajo de aprobación  
5. Desarrollar el marco de pruebas  
6. Crear una interfaz web sencilla para la gestión  
7. Integrar con un servidor MCP  

**Technologies:** Elige tu framework backend preferido, base de datos SQL o NoSQL y framework frontend para la interfaz de gestión.

### Project 3: MCP-Based Content Generation Platform

**Objective:** Construir una plataforma de generación de contenido que aproveche MCP para ofrecer resultados consistentes en diferentes tipos de contenido.

**Requirements:**  
- Soportar múltiples formatos de contenido (posts de blog, redes sociales, textos de marketing)  
- Implementar generación basada en plantillas con opciones de personalización  
- Crear un sistema de revisión y retroalimentación de contenido  
- Rastrear métricas de rendimiento del contenido  
- Soportar versionado e iteración del contenido  

**Implementation Steps:**  
1. Configurar la infraestructura del cliente MCP  
2. Crear plantillas para diferentes tipos de contenido  
3. Construir la canalización de generación de contenido  
4. Implementar el sistema de revisión  
5. Desarrollar el sistema de seguimiento de métricas  
6. Crear una interfaz para gestión de plantillas y generación de contenido  

**Technologies:** Lenguaje de programación, framework web y sistema de base de datos de tu preferencia.

## Future Directions for MCP Technology

### Emerging Trends

1. **Multi-Modal MCP**  
   - Expansión de MCP para estandarizar interacciones con modelos de imagen, audio y video  
   - Desarrollo de capacidades de razonamiento cruzado entre modalidades  
   - Formatos de prompt estandarizados para diferentes modalidades  

2. **Federated MCP Infrastructure**  
   - Redes MCP distribuidas que pueden compartir recursos entre organizaciones  
   - Protocolos estandarizados para compartir modelos de forma segura  
   - Técnicas de computación que preservan la privacidad  

3. **MCP Marketplaces**  
   - Ecosistemas para compartir y monetizar plantillas y plugins MCP  
   - Procesos de aseguramiento de calidad y certificación  
   - Integración con marketplaces de modelos  

4. **MCP for Edge Computing**  
   - Adaptación de estándares MCP para dispositivos edge con recursos limitados  
   - Protocolos optimizados para entornos de baja banda ancha  
   - Implementaciones especializadas MCP para ecosistemas IoT  

5. **Regulatory Frameworks**  
   - Desarrollo de extensiones MCP para cumplimiento regulatorio  
   - Registros de auditoría estandarizados e interfaces de explicabilidad  
   - Integración con marcos emergentes de gobernanza de IA  

### MCP Solutions from Microsoft  

Microsoft y Azure han desarrollado varios repositorios de código abierto para ayudar a los desarrolladores a implementar MCP en diversos escenarios:

#### Microsoft Organization  
1. [playwright-mcp](https://github.com/microsoft/playwright-mcp) - Servidor Playwright MCP para automatización y pruebas de navegador  
2. [files-mcp-server](https://github.com/microsoft/files-mcp-server) - Implementación de servidor MCP para OneDrive, para pruebas locales y contribución comunitaria  
3. [NLWeb](https://github.com/microsoft/NlWeb) - Colección de protocolos abiertos y herramientas open source enfocadas en establecer una capa fundamental para la Web de IA  

#### Azure-Samples Organization  
1. [mcp](https://github.com/Azure-Samples/mcp) - Enlaces a ejemplos, herramientas y recursos para construir e integrar servidores MCP en Azure usando varios lenguajes  
2. [mcp-auth-servers](https://github.com/Azure-Samples/mcp-auth-servers) - Servidores MCP de referencia que demuestran autenticación con la especificación actual del Model Context Protocol  
3. [remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions) - Página principal para implementaciones de Remote MCP Server en Azure Functions con enlaces a repositorios por lenguaje  
4. [remote-mcp-functions-python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Plantilla rápida para construir y desplegar servidores MCP remotos personalizados usando Azure Functions con Python  
5. [remote-mcp-functions-dotnet](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Plantilla rápida para construir y desplegar servidores MCP remotos personalizados usando Azure Functions con .NET/C#  
6. [remote-mcp-functions-typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Plantilla rápida para construir y desplegar servidores MCP remotos personalizados usando Azure Functions con TypeScript  
7. [remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) - Azure API Management como AI Gateway para servidores MCP remotos usando Python  
8. [AI-Gateway](https://github.com/Azure-Samples/AI-Gateway) - Experimentos APIM ❤️ AI incluyendo capacidades MCP, integrando Azure OpenAI y AI Foundry  

Estos repositorios ofrecen diversas implementaciones, plantillas y recursos para trabajar con el Model Context Protocol en distintos lenguajes de programación y servicios de Azure. Cubren casos de uso desde implementaciones básicas de servidores hasta autenticación, despliegue en la nube e integración empresarial.

#### MCP Resources Directory  

El [directorio MCP Resources](https://github.com/microsoft/mcp/tree/main/Resources) en el repositorio oficial de Microsoft MCP ofrece una colección seleccionada de recursos de ejemplo, plantillas de prompts y definiciones de herramientas para usar con servidores Model Context Protocol. Este directorio está diseñado para ayudar a los desarrolladores a comenzar rápidamente con MCP, ofreciendo bloques reutilizables y ejemplos de mejores prácticas para:

- **Prompt Templates:** Plantillas listas para usar en tareas y escenarios comunes de IA, que pueden adaptarse para tus propias implementaciones MCP.  
- **Tool Definitions:** Esquemas de herramientas de ejemplo y metadatos para estandarizar la integración e invocación de herramientas en diferentes servidores MCP.  
- **Resource Samples:** Definiciones de recursos de ejemplo para conectar fuentes de datos, APIs y servicios externos dentro del marco MCP.  
- **Reference Implementations:** Ejemplos prácticos que muestran cómo estructurar y organizar recursos, prompts y herramientas en proyectos MCP reales.  

Estos recursos aceleran el desarrollo, promueven la estandarización y ayudan a asegurar las mejores prácticas al construir y desplegar soluciones basadas en MCP.

#### MCP Resources Directory  
- [MCP Resources (Sample Prompts, Tools, and Resource Definitions)](https://github.com/microsoft/mcp/tree/main/Resources)  

### Research Opportunities

- Técnicas eficientes de optimización de prompts dentro de frameworks MCP  
- Modelos de seguridad para despliegues MCP multi-tenant  
- Benchmarking de rendimiento entre diferentes implementaciones MCP  
- Métodos de verificación formal para servidores MCP  

## Conclusion

El Model Context Protocol (MCP) está moldeando rápidamente el futuro de la integración de IA estandarizada, segura e interoperable en diversas industrias. A través de los estudios de caso y proyectos prácticos de esta lección, has visto cómo los primeros adoptantes, incluyendo Microsoft y Azure, están aprovechando MCP para resolver desafíos reales, acelerar la adopción de IA y garantizar cumplimiento, seguridad y escalabilidad. El enfoque modular de MCP permite a las organizaciones conectar grandes modelos de lenguaje, herramientas y datos empresariales en un marco unificado y auditable. A medida que MCP sigue evolucionando, mantenerse activo en la comunidad, explorar recursos de código abierto y aplicar las mejores prácticas será clave para construir soluciones de IA robustas y preparadas para el futuro.

## Additional Resources

- [MCP GitHub Repository (Microsoft)](https://github.com/microsoft/mcp)  
- [MCP Resources Directory (Sample Prompts, Tools, and Resource Definitions)](https://github.com/microsoft/mcp/tree/main/Resources)  
- [MCP Community & Documentation](https://modelcontextprotocol.io/introduction)  
- [Azure MCP Documentation](https://aka.ms/azmcp)  
- [Playwright MCP Server GitHub Repository](https://github.com/microsoft/playwright-mcp)  
- [Files MCP Server (OneDrive)](https://github.com/microsoft/files-mcp-server)  
- [Azure-Samples MCP](https://github.com/Azure-Samples/mcp)  
- [MCP Auth Servers (Azure-Samples)](https://github.com/Azure-Samples/mcp-auth-servers)  
- [Remote MCP Functions (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions)
- [Remote MCP Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-python)
- [Remote MCP Functions .NET (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)
- [Remote MCP Functions TypeScript (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-functions-typescript)
- [Remote MCP APIM Functions Python (Azure-Samples)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
- [AI-Gateway (Azure-Samples)](https://github.com/Azure-Samples/AI-Gateway)
- [Microsoft AI and Automation Solutions](https://azure.microsoft.com/en-us/products/ai-services/)

## Ejercicios

1. Analiza uno de los estudios de caso y propone un enfoque alternativo de implementación.
2. Elige una de las ideas de proyecto y crea una especificación técnica detallada.
3. Investiga una industria no cubierta en los estudios de caso y describe cómo MCP podría abordar sus desafíos específicos.
4. Explora una de las direcciones futuras y crea un concepto para una nueva extensión de MCP que la soporte.

Siguiente: [Best Practices](../08-BestPractices/README.md)

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.