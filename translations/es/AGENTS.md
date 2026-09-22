# AGENTS.md

## Descripción del Proyecto

**MCP para Principiantes** es un currículo educativo de código abierto para aprender el Model Context Protocol (MCP) - un marco estandarizado para las interacciones entre modelos de IA y aplicaciones cliente. Este repositorio proporciona materiales de aprendizaje completos con ejemplos prácticos de código en múltiples lenguajes de programación.

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
- **Documentación**: Markdown con traducción automatizada en múltiples idiomas (más de 48 idiomas)

### Arquitectura

- **11 Módulos Principales (00-11)**: Ruta de aprendizaje secuencial desde fundamentos hasta temas avanzados
- **Laboratorios Prácticos**: Ejercicios prácticos con código completo de solución en varios lenguajes
- **Proyectos de Ejemplo**: Implementaciones funcionales de servidores y clientes MCP
- **Sistema de Traducción**: Flujo de trabajo automatizado con GitHub Actions para soporte multilingüe
- **Recursos de imágenes**: Directorio centralizado de imágenes con versiones traducidas

## Comandos de Configuración

Este es un repositorio enfocado en la documentación. La configuración principal ocurre dentro de proyectos de ejemplo y laboratorios individuales.

### Configuración del Repositorio

```bash
# Clonar el repositorio
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Trabajando con Proyectos de Ejemplo

Los proyectos de ejemplo se encuentran en:
- `03-GettingStarted/samples/` - Ejemplos específicos para cada lenguaje
- `03-GettingStarted/01-first-server/solution/` - Implementaciones del primer servidor
- `03-GettingStarted/02-client/solution/` - Implementaciones de cliente
- `11-MCPServerHandsOnLabs/` - Laboratorios integrales de integración con bases de datos

Cada proyecto de ejemplo contiene sus propias instrucciones de configuración:

#### Proyectos TypeScript/JavaScript
```bash
cd <project-directory>
npm install
npm start
```

#### Proyectos Python
```bash
cd <project-directory>
pip install -r requirements.txt
# o
pip install -e .
python main.py
```

#### Proyectos Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Flujo de Trabajo de Desarrollo

### Preparación para MCP 7-28

#### Lista de verificación para preparación del repo

- [x] **Claridad para nuevos contribuyentes**: Este archivo define el propósito del repositorio,
  estructura, reglas de contribución y rutas de configuración de ejemplo.
- [x] **Comandos de construcción/prueba/lint con banderas exactas**:
  - Lint de documentación del repositorio:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Auditoría de patrones de enlaces en la documentación:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validación de ejemplo TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validación de ejemplo Python:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validación de ejemplo Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Un flujo de trabajo realista que puede convertirse en una herramienta MCP**:
  `validate_curriculum_change`
- [x] **Entradas/salidas explícitas** (ver especificación abajo).
- [x] **Permisos y modos de falla documentados** (ver especificación abajo).
- [x] **Pruebas CI explícitas** (comandos determinísticos, códigos de salida explícitos
  y salidas legibles por máquina).

#### Flujo de trabajo candidato para herramienta MCP: `validate_curriculum_change`

##### Objetivo

Validar la salud de los cambios en documentación del currículo y código de ejemplo
antes de hacer merge.

##### Entradas

- `changed_paths: string[]` (obligatorio) - rutas relativas modificadas en el PR.
- `run_docs_lint: boolean` (por defecto `true`)
- `run_links_audit: boolean` (por defecto `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (por defecto todo `false`)

##### Salidas

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Permisos

- Leer archivos del espacio de trabajo y escribir artefactos generados por la herramienta (por ejemplo, reportes de lint,
  logs de prueba) solamente; no se permiten escrituras en `translations/` ni
  `translated_images/`.
- Ejecutar comandos locales en shell.
- Acceso a red opcional solamente para restaurar paquetes (`npm ci`,
  `python -m pip install`, resolución de dependencias `mvn`).
- Sin permiso para hacer push, merge o modificar `translations/` ni
  `translated_images/`.

##### Modos de falla

- `E_NO_INPUT_PATHS`: `changed_paths` está vacío.
- `E_INVALID_PATH`: la ruta de entrada escapa la raíz del repositorio.
- `E_LINT_FAILED`: lint markdown termina con código distinto de cero.
- `E_LINK_AUDIT_FAILED`: comando de auditoría de enlaces termina con código distinto de cero.
- `E_SAMPLE_TEST_FAILED`: prueba/construcción de ejemplo termina con código distinto de cero.
- `E_TIMEOUT`: el comando excedió el tiempo de espera configurado.

##### Contrato recomendado para CI

Para automatizar la validación, configure un trabajo CI que:

- Se active en pull requests que modifiquen `*.md`, código de ejemplo o este archivo.
- Ejecute los comandos exactos listados arriba.
- Persista logs como artefactos.
- Falla el trabajo ante cualquier código de salida distinto de cero.

#### Si distribuyes un servidor MCP desde este repo

- [ ] Lee el changelog final de MCP `2026-07-28`:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] Verifica que la versión del SDK seleccionada soporte MCP `2026-07-28`:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] Elimina suposiciones de sesión y handshake; trata cada petición como
  autocontenida:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] Envía cabeceras `Mcp-Method` y `Mcp-Name` para peticiones HTTP sin procesar:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] Revisa códigos de error codificados (por ejemplo, `missing resource` cambió de `-32002` a `-32602`).

- [ ] Migrar Roots, Muestreo, Registro y Cliente Dinámico obsoletos
  Registro:
  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] Migrar fuera de la API experimental `2025-11-25` de Tareas:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] Revisar autorización para el endurecimiento de OAuth y OpenID Connect:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### Estructura de la Documentación

- **Módulos 00-11**: Contenido principal del currículo en orden secuencial
- **translations/**: Versiones específicas de idioma (auto-generadas, no editar directamente)
- **translated_images/**: Versiones localizadas de imágenes (auto-generadas)
- **images/**: Imágenes y diagramas fuente

### Realizar Cambios en la Documentación

1. Editar sólo los archivos markdown en inglés en los directorios raíz de módulo (00-11)
2. Actualizar imágenes en el directorio `images/` si es necesario
3. La acción de GitHub co-op-translator generará automáticamente las traducciones
4. Las traducciones se regeneran al hacer push a la rama main

### Trabajando con Traducciones

- **Traducción Automatizada**: El flujo de trabajo de GitHub Actions gestiona todas las traducciones
- **NO editar manualmente** los archivos en el directorio `translations/`
- Los metadatos de traducción están incrustados en cada archivo traducido
- Idiomas soportados: más de 48 idiomas incluyendo árabe, chino, francés, alemán, hindi, japonés, coreano, portugués, ruso, español y muchos más

## Instrucciones de Prueba

### Validación de la Documentación

Dado que esto es principalmente un repositorio de documentación, las pruebas se enfocan en:

1. **Auditoría de Patrones de Enlaces**: Listar enlaces en Markdown para revisión

   ```bash
   # Listar enlaces Markdown (auditoría de patrones)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Validación de Ejemplos de Código**: Probar que los ejemplos de código compilan/ejecutan

   ```bash
   # Navegar a una muestra específica y ejecutar sus pruebas
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Linting de Markdown**: Verificar la consistencia del formato

   ```bash
   # Usa markdownlint si es necesario
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Pruebas de Proyectos de Ejemplo

Cada muestra específica de idioma incluye su propio enfoque de prueba:

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

## Guías de Estilo de Código

### Estilo de Documentación

- Usar un lenguaje claro y amigable para principiantes
- Incluir ejemplos de código en varios lenguajes cuando sea aplicable
- Seguir las mejores prácticas de Markdown:
  - Usar encabezados estilo ATX (sintaxis con `#`)
  - Usar bloques de código con lenguajes identificados
  - Incluir texto alternativo descriptivo para las imágenes
  - Mantener longitudes de línea razonables (sin límite estricto, pero con sentido)

### Estilo de Ejemplos de Código

#### TypeScript/JavaScript
- Usar módulos ES (`import`/`export`)
- Seguir las convenciones en modo estricto de TypeScript
- Incluir anotaciones de tipos
- Orientado a ES2022

#### Python
- Seguir las pautas de estilo PEP 8
- Usar hints de tipo cuando sea adecuado
- Incluir docstrings para funciones y clases
- Usar características modernas de Python (3.8+)

#### Java
- Seguir las convenciones de Spring Boot
- Usar características de Java 21
- Seguir estructura estándar de proyectos Maven
- Incluir comentarios Javadoc

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

## Compilación y Despliegue

### Despliegue de Documentación

El repositorio usa GitHub Pages o similar para alojar la documentación (si aplica). Los cambios en la rama principal disparan:

1. Flujo de trabajo de traducción (`.github/workflows/co-op-translator.yml`)
2. Traducción automatizada de todos los archivos markdown en inglés
3. Localización de imágenes según sea necesario

### No se requiere proceso de compilación

Este repositorio contiene principalmente documentación markdown. No se necesita compilación ni paso de construcción para el contenido principal del currículo.

### Despliegue de Proyectos de Ejemplo

Los proyectos de ejemplo individuales pueden tener instrucciones de despliegue:
- Ver `03-GettingStarted/09-deployment/` para guía de despliegue del servidor MCP
- Ejemplos de despliegue con Azure Container Apps en `11-MCPServerHandsOnLabs/`

## Guías para Contribuir

### Proceso de Pull Request

1. **Fork y Clona**: Haz fork del repositorio y clona tu fork localmente
2. **Crear una Rama**: Usa nombres descriptivos para las ramas (e.g., `fix/typo-module-3`, `add/python-example`)
3. **Realiza Cambios**: Edita sólo los archivos markdown en inglés (no las traducciones)
4. **Prueba Localmente**: Verifica que markdown se renderice correctamente
5. **Envía el PR**: Usa títulos y descripciones claras para el PR
6. **CLA**: Firma el Acuerdo de Licencia de Contribución de Microsoft cuando se solicite

### Formato del Título del PR

Usa títulos claros y descriptivos:
- `[Módulo XX] Breve descripción` para cambios específicos de módulo
- `[Ejemplos] Descripción` para cambios en código de muestra
- `[Docs] Descripción` para actualizaciones generales de documentación

### Qué Contribuir

- Correcciones de errores en documentación o ejemplos de código
- Nuevos ejemplos de código en lenguajes adicionales
- Aclaraciones y mejoras al contenido existente
- Nuevos estudios de caso o ejemplos prácticos
- Reportes de problemas por contenido poco claro o incorrecto

### Qué NO hacer

- No editar directamente archivos en el directorio `translations/`
- No editar el directorio `translated_images/`
- No agregar archivos binarios grandes sin discusión previa
- No cambiar archivos del flujo de trabajo de traducción sin coordinación

## Notas Adicionales

### Mantenimiento del Repositorio

- **Registro de Cambios**: Todos los cambios significativos están documentados en `changelog.md`
- **Guía de Estudio**: Usa `study_guide.md` para la navegación general del currículo
- **Plantillas de Issues**: Usa plantillas de GitHub para reportes de bugs y solicitudes de características
- **Código de Conducta**: Todos los contribuyentes deben seguir el Código de Conducta de código abierto de Microsoft

### Ruta de Aprendizaje

Sigue los módulos en orden secuencial (00-11) para un aprendizaje óptimo:
1. **00-02**: Fundamentos (Introducción, Conceptos Clave, Seguridad)
2. **03**: Introducción con implementación práctica
3. **04-05**: Implementación práctica y temas avanzados
4. **06-10**: Comunidad, mejores prácticas y aplicaciones del mundo real
5. **11**: Laboratorios completos de integración de base de datos (13 laboratorios secuenciales)

### Recursos de Soporte

- **Documentación**: https://modelcontextprotocol.io/
- **Especificación**: https://modelcontextprotocol.io/specification/2026-07-28/
- **Comunidad**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Servidor Discord de Microsoft Foundry
- **Cursos Relacionados**: Ver README.md para otras rutas de aprendizaje de Microsoft

### Problemas Comunes y Soluciones

**P: Mi PR falla la comprobación de traducción**
R: Asegúrate de haber editado sólo archivos markdown en inglés en los directorios raíz de los módulos, no versiones traducidas.

**P: ¿Cómo agrego un nuevo idioma?**
R: El soporte de idiomas se gestiona mediante el flujo de trabajo co-op-translator. Abre un issue para discutir agregar nuevos idiomas.

**P: Los ejemplos de código no funcionan**
R: Asegúrate de seguir las instrucciones de configuración en el README específico de la muestra. Verifica que tengas las versiones correctas de las dependencias instaladas.


**P: Las imágenes no se muestran**

A: Verifique que las rutas de las imágenes sean relativas y usen barras inclinadas hacia adelante. Las imágenes deben estar en el directorio `images/` o en `translated_images/` para versiones localizadas.

### Consideraciones de rendimiento

- El flujo de trabajo de traducción puede tardar varios minutos en completarse
- Las imágenes grandes deben optimizarse antes de ser confirmadas
- Mantenga los archivos markdown individuales enfocados y de tamaño razonable
- Use enlaces relativos para mejor portabilidad

### Gobernanza del proyecto

Este proyecto sigue las prácticas de código abierto de Microsoft:
- Licencia MIT para código y documentación
- Código de Conducta de Código Abierto de Microsoft
- CLA requerida para contribuciones
- Problemas de seguridad: Siga las directrices de SECURITY.md
- Soporte: Consulte SUPPORT.md para recursos de ayuda

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->