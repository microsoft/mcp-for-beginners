# AGENTS.md

## Resumen del Proyecto

**MCP para Principiantes** es un currículo educativo de código abierto para aprender el Protocolo de Contexto de Modelo (MCP), un marco estandarizado para interacciones entre modelos de IA y aplicaciones cliente. Este repositorio ofrece materiales de aprendizaje completos con ejemplos prácticos de código en varios lenguajes de programación.

### Tecnologías Clave

- **Lenguajes de Programación**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworks y SDKs**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Bases de Datos**: PostgreSQL con extensión pgvector
- **Plataformas en la Nube**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Herramientas de Construcción**: npm, Maven, pip, Cargo
- **Documentación**: Markdown con traducción automática a múltiples idiomas (48+ idiomas)

### Arquitectura

- **11 Módulos Principales (00-11)**: Ruta de aprendizaje secuencial desde fundamentos hasta temas avanzados
- **Laboratorios Prácticos**: Ejercicios prácticos con código de solución completo en varios lenguajes
- **Proyectos de Ejemplo**: Implementaciones funcionales de servidor y cliente MCP
- **Sistema de Traducción**: Flujo de trabajo automatizado de GitHub Actions para soporte multilingüe
- **Recursos Gráficos**: Directorio centralizado de imágenes con versiones traducidas

## Comandos de Configuración

Este es un repositorio enfocado en documentación. La mayoría de las configuraciones se realizan dentro de los proyectos de ejemplo y laboratorios individuales.

### Configuración del Repositorio

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Trabajando con Proyectos de Ejemplo

Los proyectos de ejemplo se encuentran en:
- `03-GettingStarted/samples/` - Ejemplos específicos por lenguaje
- `03-GettingStarted/01-first-server/solution/` - Implementaciones del primer servidor
- `03-GettingStarted/02-client/solution/` - Implementaciones de cliente
- `11-MCPServerHandsOnLabs/` - Laboratorios integrales de integración de bases de datos

Cada proyecto de ejemplo contiene sus propias instrucciones de configuración:

#### Proyectos en TypeScript/JavaScript
```bash
cd <project-directory>
npm install
npm start
```

#### Proyectos en Python
```bash
cd <project-directory>
pip install -r requirements.txt
# or
pip install -e .
python main.py
```

#### Proyectos en Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Flujo de Trabajo de Desarrollo

### Estructura de la Documentación

- **Módulos 00-11**: Contenido principal del currículo en orden secuencial
- **translations/**: Versiones en idiomas específicos (generadas automáticamente, no editar directamente)
- **translated_images/**: Versiones localizadas de imágenes (generadas automáticamente)
- **images/**: Imágenes y diagramas fuente

### Realizando Cambios en la Documentación

1. Edita solo los archivos markdown en inglés en los directorios raíz de los módulos (00-11)
2. Actualiza las imágenes en el directorio `images/` si es necesario
3. La acción de GitHub co-op-translator generará automáticamente las traducciones
4. Las traducciones se regeneran al hacer push a la rama principal

### Trabajando con Traducciones

- **Traducción Automática**: El flujo de trabajo de GitHub Actions maneja todas las traducciones
- **NO editar manualmente** los archivos en el directorio `translations/`
- Los metadatos de traducción están incrustados en cada archivo traducido
- Idiomas soportados: Más de 48 idiomas, incluyendo árabe, chino, francés, alemán, hindi, japonés, coreano, portugués, ruso, español y muchos más

## Instrucciones de Pruebas

### Validación de Documentación

Dado que este es principalmente un repositorio de documentación, las pruebas se centran en:

1. **Validación de Enlaces**: Asegúrate de que todos los enlaces internos funcionen
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Validación de Ejemplos de Código**: Prueba que los ejemplos de código se compilen/ejecuten
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Linting de Markdown**: Verifica la consistencia del formato
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Pruebas de Proyectos de Ejemplo

Cada ejemplo específico por lenguaje incluye su propio enfoque de pruebas:

#### TypeScript/JavaScript
```bash
npm test
npm run build
```

#### Python
```bash
pytest
python -m pytest tests/
```

#### Java
```bash
mvn test
mvn verify
```

## Directrices de Estilo de Código

### Estilo de Documentación

- Usa lenguaje claro y amigable para principiantes
- Incluye ejemplos de código en varios lenguajes cuando sea aplicable
- Sigue las mejores prácticas de markdown:
  - Usa encabezados estilo ATX (`#` sintaxis)
  - Usa bloques de código delimitados con identificadores de lenguaje
  - Incluye texto alternativo descriptivo para imágenes
  - Mantén las líneas de texto razonablemente cortas (sin límite estricto, pero sé sensato)

### Estilo de Ejemplos de Código

#### TypeScript/JavaScript
- Usa módulos ES (`import`/`export`)
- Sigue las convenciones de modo estricto de TypeScript
- Incluye anotaciones de tipo
- Apunta a ES2022

#### Python
- Sigue las directrices de estilo PEP 8
- Usa sugerencias de tipo cuando sea apropiado
- Incluye docstrings para funciones y clases
- Usa características modernas de Python (3.8+)

#### Java
- Sigue las convenciones de Spring Boot
- Usa características de Java 21
- Sigue la estructura estándar de proyectos Maven
- Incluye comentarios Javadoc

### Organización de Archivos

```
<module-number>-<ModuleName>/
├── README.md              # Main module content
├── samples/               # Code examples (if applicable)
│   ├── typescript/
│   ├── python/
│   ├── java/
│   └── ...
└── solution/              # Complete working solutions
    └── <language>/
```

## Construcción y Despliegue

### Despliegue de Documentación

El repositorio utiliza GitHub Pages o similar para alojar la documentación (si aplica). Los cambios en la rama principal activan:

1. Flujo de trabajo de traducción (`.github/workflows/co-op-translator.yml`)
2. Traducción automática de todos los archivos markdown en inglés
3. Localización de imágenes según sea necesario

### No se Requiere Proceso de Construcción

Este repositorio contiene principalmente documentación en markdown. No se necesita compilación ni paso de construcción para el contenido principal del currículo.

### Despliegue de Proyectos de Ejemplo

Los proyectos de ejemplo individuales pueden tener instrucciones de despliegue:
- Consulta `03-GettingStarted/09-deployment/` para orientación sobre el despliegue de servidores MCP
- Ejemplos de despliegue en Azure Container Apps en `11-MCPServerHandsOnLabs/`

## Directrices para Contribuir

### Proceso de Pull Request

1. **Fork y Clonar**: Haz un fork del repositorio y clona tu fork localmente
2. **Crea una Rama**: Usa nombres de rama descriptivos (por ejemplo, `fix/typo-module-3`, `add/python-example`)
3. **Realiza Cambios**: Edita solo los archivos markdown en inglés (no las traducciones)
4. **Prueba Localmente**: Verifica que el markdown se renderice correctamente
5. **Envía el PR**: Usa títulos y descripciones claras en el PR
6. **CLA**: Firma el Acuerdo de Licencia de Contribuidor de Microsoft cuando se te solicite

### Formato de Títulos de PR

Usa títulos claros y descriptivos:
- `[Module XX] Breve descripción` para cambios específicos de módulos
- `[Samples] Descripción` para cambios en ejemplos de código
- `[Docs] Descripción` para actualizaciones generales de documentación

### Qué Contribuir

- Corrección de errores en documentación o ejemplos de código
- Nuevos ejemplos de código en lenguajes adicionales
- Clarificaciones y mejoras al contenido existente
- Nuevos estudios de caso o ejemplos prácticos
- Reportes de problemas sobre contenido poco claro o incorrecto

### Qué NO Hacer

- No edites directamente los archivos en el directorio `translations/`
- No edites el directorio `translated_images/`
- No agregues archivos binarios grandes sin discusión previa
- No cambies los archivos de flujo de trabajo de traducción sin coordinación

## Notas Adicionales

### Mantenimiento del Repositorio

- **Changelog**: Todos los cambios significativos se documentan en `changelog.md`
- **Guía de Estudio**: Usa `study_guide.md` para una visión general de la navegación del currículo
- **Plantillas de Issues**: Usa las plantillas de GitHub para reportes de errores y solicitudes de características
- **Código de Conducta**: Todos los contribuyentes deben seguir el Código de Conducta de Código Abierto de Microsoft

### Ruta de Aprendizaje

Sigue los módulos en orden secuencial (00-11) para un aprendizaje óptimo:
1. **00-02**: Fundamentos (Introducción, Conceptos Básicos, Seguridad)
2. **03**: Introducción con implementación práctica
3. **04-05**: Implementación práctica y temas avanzados
4. **06-10**: Comunidad, mejores prácticas y aplicaciones reales
5. **11**: Laboratorios integrales de integración de bases de datos (13 laboratorios secuenciales)

### Recursos de Soporte

- **Documentación**: https://modelcontextprotocol.io/
- **Especificación**: https://spec.modelcontextprotocol.io/
- **Comunidad**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Servidor de Discord de Microsoft Azure AI Foundry
- **Cursos Relacionados**: Consulta README.md para otros caminos de aprendizaje de Microsoft

### Solución de Problemas Comunes

**P: Mi PR está fallando en la verificación de traducción**  
R: Asegúrate de haber editado solo los archivos markdown en inglés en los directorios raíz de los módulos, no las versiones traducidas.

**P: ¿Cómo agrego un nuevo idioma?**  
R: El soporte de idiomas se gestiona a través del flujo de trabajo co-op-translator. Abre un issue para discutir la adición de nuevos idiomas.

**P: Los ejemplos de código no funcionan**  
R: Asegúrate de haber seguido las instrucciones de configuración en el README específico del ejemplo. Verifica que tengas instaladas las versiones correctas de las dependencias.

**P: Las imágenes no se muestran**  
R: Verifica que las rutas de las imágenes sean relativas y usen barras diagonales. Las imágenes deben estar en el directorio `images/` o `translated_images/` para versiones localizadas.

### Consideraciones de Rendimiento

- El flujo de trabajo de traducción puede tardar varios minutos en completarse
- Las imágenes grandes deben optimizarse antes de ser comprometidas
- Mantén los archivos markdown individuales enfocados y de tamaño razonable
- Usa enlaces relativos para mejor portabilidad

### Gobernanza del Proyecto

Este proyecto sigue las prácticas de código abierto de Microsoft:
- Licencia MIT para código y documentación
- Código de Conducta de Código Abierto de Microsoft
- CLA requerido para contribuciones
- Problemas de seguridad: Sigue las directrices de SECURITY.md
- Soporte: Consulta SUPPORT.md para recursos de ayuda

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.