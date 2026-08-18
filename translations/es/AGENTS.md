# AGENTS.md

## Descripción general del proyecto

**MCP para principiantes** es un currículo educativo de código abierto para aprender el Protocolo de Contexto del Modelo (MCP), un marco estandarizado para las interacciones entre modelos de IA y aplicaciones cliente. Este repositorio proporciona materiales completos de aprendizaje con ejemplos prácticos de código en varios lenguajes de programación.

### Tecnologías clave

- **Lenguajes de programación**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworks y SDKs**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Bases de datos**: PostgreSQL con extensión pgvector
- **Plataformas en la nube**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Herramientas de construcción**: npm, Maven, pip, Cargo
- **Documentación**: Markdown con traducción automática en múltiples idiomas (más de 48 idiomas)

### Arquitectura

- **11 Módulos principales (00-11)**: Ruta de aprendizaje secuencial desde fundamentos hasta temas avanzados
- **Laboratorios prácticos**: Ejercicios prácticos con código de solución completo en varios idiomas
- **Proyectos de ejemplo**: Implementaciones funcionales de servidor y cliente MCP
- **Sistema de traducción**: Flujo de trabajo automatizado con GitHub Actions para soporte multi-idioma
- **Recursos de imágenes**: Directorio centralizado de imágenes con versiones traducidas

## Comandos de configuración

Este es un repositorio enfocado en documentación. La mayoría de las configuraciones ocurren dentro de proyectos de ejemplo individuales y laboratorios.

### Configuración del repositorio

```bash
# Clonar el repositorio
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Trabajando con proyectos de ejemplo

Los proyectos de ejemplo están ubicados en:
- `03-GettingStarted/samples/` - Ejemplos específicos por lenguaje
- `03-GettingStarted/01-first-server/solution/` - Primeras implementaciones del servidor
- `03-GettingStarted/02-client/solution/` - Implementaciones de cliente
- `11-MCPServerHandsOnLabs/` - Laboratorios completos de integración con base de datos

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

## Flujo de trabajo de desarrollo

### Preparación para MCP 7-28

#### Lista de verificación de preparación del repositorio

- [x] **Claridad para nuevos colaboradores**: Este archivo define el propósito del repositorio,
  estructura, reglas de contribución y rutas de configuración de ejemplo.
- [x] **Comandos de compilación/prueba/lint con flags exactos**:
  - Lint de documentación del repositorio:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Auditoría de patrones de enlaces en la documentación del repositorio:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validación de ejemplo TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validación de ejemplo Python:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validación de ejemplo Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Un flujo de trabajo realista que puede convertirse en una herramienta MCP**:
  `validate_curriculum_change`
- [x] **Entradas/salidas son explícitas** (ver especificación abajo).
- [x] **Permisos y modos de fallo están documentados** (ver especificación abajo).
- [x] **Testabilidad CI es explícita** (comandos deterministas, códigos de salida explícitos,
  y salidas legibles por máquina).

#### Flujo de trabajo candidato para herramienta MCP: `validate_curriculum_change`

##### Objetivo

Validar cambios en la documentación del currículo y en el código de muestra representativo
antes de hacer merge.

##### Entradas

- `changed_paths: string[]` (requerido) - rutas relativas modificadas en el PR.
- `run_docs_lint: boolean` (por defecto `true`)
- `run_links_audit: boolean` (por defecto `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (por defecto todos en `false`)

##### Salidas

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Permisos

- Leer archivos del espacio de trabajo y escribir artefactos generados por la herramienta (por ejemplo, reportes de lint,
  logs de prueba) solamente; no escribir en `translations/` ni en
  `translated_images/`.
- Ejecutar comandos shell locales.
- Acceso de red opcional solo para restauración de paquetes (`npm ci`,
  `python -m pip install`, resolución de dependencias `mvn`).
- Sin permiso para hacer push, merge o modificar `translations/` ni
  `translated_images/`.

##### Modos de fallo

- `E_NO_INPUT_PATHS`: `changed_paths` está vacío.
- `E_INVALID_PATH`: ruta de entrada escapa del raíz del repositorio.
- `E_LINT_FAILED`: el lint de markdown terminó con código distinto de cero.
- `E_LINK_AUDIT_FAILED`: el comando de auditoría de enlaces terminó con código distinto de cero.
- `E_SAMPLE_TEST_FAILED`: la prueba/compilación del ejemplo terminó con código distinto de cero.
- `E_TIMEOUT`: el comando excedió el tiempo de espera configurado.

##### Contrato recomendado para CI

Para automatizar la validación, configure un job de CI que:

- Se active en pull requests que afecten a `*.md`, código de muestra o este archivo.
- Ejecute los comandos exactos listados arriba.
- Mantenga los logs como artefactos.
- Falla el job con cualquier código de salida distinto de cero.

#### Si distribuyes un servidor MCP de este repo

- [ ] Lee el borrador del registro de cambios para MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Ejecuta tu servidor contra las betas del SDK:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Elimina las suposiciones sobre sesión y handshake; trata cada solicitud como
  autocontenida:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Envía los encabezados `Mcp-Method` y `Mcp-Name` para solicitudes HTTP en crudo:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Audita los códigos de error codificados (el error `missing resource` se movió de `-32002` a `-32602`).

- [ ] Marcar y planificar la migración para raíces, muestreo y
  registro obsoletos:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Migrar de la API experimental `2025-11-25` de Tareas:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Revisar la autorización para el endurecimiento de OAuth y OpenID Connect:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Estructura de la documentación

- **Módulos 00-11**: Contenido del currículo principal en orden secuencial
- **translations/**: Versiones específicas por idioma (autogeneradas, no editar directamente)
- **translated_images/**: Versiones localizadas de imágenes (autogeneradas)
- **images/**: Imágenes y diagramas fuente

### Cómo realizar cambios en la documentación

1. Editar solo los archivos markdown en inglés en los directorios raíz de los módulos (00-11)
2. Actualizar imágenes en el directorio `images/` si es necesario
3. La acción de GitHub co-op-translator generará automáticamente las traducciones
4. Las traducciones se regeneran al hacer push a la rama principal

### Trabajando con traducciones

- **Traducción automatizada**: El flujo de trabajo de GitHub Actions maneja todas las traducciones
- **No editar manualmente** los archivos en el directorio `translations/`
- Los metadatos de traducción están incrustados en cada archivo traducido
- Idiomas soportados: más de 48 idiomas incluyendo árabe, chino, francés, alemán, hindi, japonés, coreano, portugués, ruso, español y muchos más

## Instrucciones para pruebas

### Validación de documentación

Dado que este es principalmente un repositorio de documentación, las pruebas se centran en:

1. **Auditoría de patrones de enlaces**: Listar enlaces Markdown para revisión

   ```bash
   # Enumerar enlaces Markdown (auditoría de patrones)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Validación de ejemplos de código**: Probar que los ejemplos de código compilen/ejecuten

   ```bash
   # Navegar a la muestra específica y ejecutar sus pruebas
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Linting de Markdown**: Verificar consistencia en el formato

   ```bash
   # Usa markdownlint si es necesario
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Pruebas de proyectos de muestra

Cada muestra específica por idioma incluye su propio enfoque de pruebas:

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

## Guías de estilo de código

### Estilo de documentación

- Usar un lenguaje claro y amigable para principiantes
- Incluir ejemplos de código en varios idiomas cuando sea aplicable
- Seguir las mejores prácticas de markdown:
  - Usar encabezados estilo ATX (sintaxis `#`)
  - Usar bloques de código delimitados con identificadores de idioma
  - Incluir texto alternativo descriptivo para imágenes
  - Mantener una longitud razonable de las líneas (sin límite estricto, pero con sentido)

### Estilo de ejemplos de código

#### TypeScript/JavaScript
- Usar módulos ES (`import`/`export`)
- Seguir las convenciones del modo estricto de TypeScript
- Incluir anotaciones de tipo
- Apuntar a ES2022

#### Python
- Seguir las pautas de estilo PEP 8
- Usar hints de tipo cuando corresponda
- Incluir docstrings para funciones y clases
- Usar características modernas de Python (3.8+)

#### Java
- Seguir las convenciones de Spring Boot
- Usar características de Java 21
- Seguir la estructura estándar de proyectos Maven
- Incluir comentarios Javadoc

### Organización de archivos

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

## Construcción y despliegue

### Despliegue de documentación

El repositorio utiliza GitHub Pages o similar para hospedaje de documentación (si aplica). Los cambios en la rama principal desencadenan:

1. Flujo de trabajo de traducción (`.github/workflows/co-op-translator.yml`)
2. Traducción automática de todos los archivos markdown en inglés
3. Localización de imágenes según sea necesario

### No se requiere proceso de compilación

Este repositorio contiene principalmente documentación en markdown. No se necesita paso de compilación para el contenido del currículo principal.

### Despliegue de proyectos de muestra

Proyectos de muestra individuales pueden tener instrucciones de despliegue:
- Ver `03-GettingStarted/09-deployment/` para guía de despliegue del servidor MCP
- Ejemplos de despliegue de Azure Container Apps en `11-MCPServerHandsOnLabs/`

## Guías para contribuir

### Proceso de pull request

1. **Fork y clonación**: Haz fork del repositorio y clona tu fork localmente
2. **Crear rama**: Usar nombres descriptivos para las ramas (ej. `fix/typo-module-3`, `add/python-example`)
3. **Realizar cambios**: Editar solo archivos markdown en inglés (no las traducciones)
4. **Probar localmente**: Verificar que el markdown se renderice correctamente
5. **Enviar PR**: Usar títulos y descripciones claras para el PR
6. **CLA**: Firmar el Acuerdo de Licencia de Contribuidor de Microsoft cuando sea solicitado

### Formato del título del PR

Usar títulos claros y descriptivos:
- `[Module XX] Breve descripción` para cambios específicos de módulos
- `[Samples] Descripción` para cambios en ejemplos de código
- `[Docs] Descripción` para actualizaciones generales de documentación

### Qué contribuir

- Correcciones de errores en documentación o ejemplos de código
- Nuevos ejemplos de código en idiomas adicionales
- Aclaraciones y mejoras al contenido existente
- Nuevos estudios de caso o ejemplos prácticos
- Reportes de problemas por contenido poco claro o incorrecto

### Qué NO hacer

- No editar directamente archivos en el directorio `translations/`
- No editar el directorio `translated_images/`
- No agregar archivos binarios grandes sin discusión previa
- No cambiar archivos del flujo de trabajo de traducción sin coordinación

## Notas adicionales

### Mantenimiento del repositorio

- **Registro de cambios**: Todos los cambios significativos se documentan en `changelog.md`
- **Guía de estudio**: Usar `study_guide.md` para una vista general de navegación del currículo
- **Plantillas de issues**: Usar plantillas de issues de GitHub para reportes de errores y solicitudes de funciones
- **Código de conducta**: Todos los contribuidores deben cumplir el Código de Conducta de código abierto de Microsoft

### Ruta de aprendizaje

Seguir los módulos en orden secuencial (00-11) para un aprendizaje óptimo:
1. **00-02**: Fundamentos (Introducción, Conceptos básicos, Seguridad)
2. **03**: Primeros pasos con implementación práctica
3. **04-05**: Implementación práctica y temas avanzados
4. **06-10**: Comunidad, mejores prácticas y aplicaciones del mundo real
5. **11**: Laboratorios integrales de base de datos (13 laboratorios secuenciales)

### Recursos de soporte

- **Documentación**: https://modelcontextprotocol.io/
- **Especificación**: https://spec.modelcontextprotocol.io/
- **Comunidad**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Servidor Discord Microsoft Foundry
- **Cursos relacionados**: Ver README.md para otras rutas de aprendizaje de Microsoft

### Solución común de problemas

**P: Mi PR está fallando la verificación de traducción**
R: Asegúrate de haber editado solo archivos markdown en inglés en los directorios raíz de los módulos, no versiones traducidas.

**P: ¿Cómo agrego un nuevo idioma?**
R: El soporte de idiomas se gestiona mediante el flujo de trabajo co-op-translator. Abre un issue para discutir agregar nuevos idiomas.

**P: Los ejemplos de código no funcionan**

R: Asegúrate de haber seguido las instrucciones de configuración en el README de la muestra específica. Verifica que tienes instaladas las versiones correctas de las dependencias.

**P: Las imágenes no se muestran**
R: Verifica que las rutas de las imágenes sean relativas y usen barras inclinadas hacia adelante. Las imágenes deben estar en el directorio `images/` o en `translated_images/` para las versiones localizadas.

### Consideraciones de Rendimiento

- El flujo de trabajo de traducción puede tardar varios minutos en completarse
- Las imágenes grandes deben optimizarse antes de hacer commit
- Mantén los archivos markdown individuales enfocados y de tamaño razonable
- Usa enlaces relativos para mejor portabilidad

### Gobernanza del Proyecto

Este proyecto sigue las prácticas de código abierto de Microsoft:
- Licencia MIT para código y documentación
- Código de Conducta de Código Abierto de Microsoft
- CLA requerida para contribuciones
- Problemas de seguridad: Sigue las pautas de SECURITY.md
- Soporte: Consulta SUPPORT.md para recursos de ayuda

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->