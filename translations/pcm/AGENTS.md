# AGENTS.md

## Project Overview

**MCP for Beginners** na open-source edukeshon curriculum wey dem create for learn Model Context Protocol (MCP) - na standardized framework wey dey for interactions between AI models and client applications. Dis repository dey provide full learning materials plus hands-on code examples wey cover plenti programming languages.

### Key Technologies

- **Programming Languages**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworks & SDKs**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Databases**: PostgreSQL wit pgvector extension
- **Cloud Platforms**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Build Tools**: npm, Maven, pip, Cargo
- **Documentation**: Markdown wit automated multi-language translation (48+ languages)

### Architecture

- **11 Core Modules (00-11)**: Sequential learning path from fundamentals go advanced topics
- **Hands-on Labs**: Practical exercises plus complete solution code for multiple languages
- **Sample Projects**: Working MCP server and client implementations
- **Translation System**: Automated GitHub Actions workflow for multi-language support
- **Image Assets**: Centralized images folder wit translated versions

## Setup Commands

Dis na documentation-focused repository. Most setup dey happen for individual sample projects and labs.

### Repository Setup

```bash
# Make you duplicate di repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Working with Sample Projects

Sample projects dey located for:
- `03-GettingStarted/samples/` - Language-specific examples
- `03-GettingStarted/01-first-server/solution/` - First server implementations
- `03-GettingStarted/02-client/solution/` - Client implementations
- `11-MCPServerHandsOnLabs/` - Comprehensive database integration labs

Each sample project get im own setup instructions:

#### TypeScript/JavaScript Projects
```bash
cd <project-directory>
npm install
npm start
```

#### Python Projects
```bash
cd <project-directory>
pip install -r requirements.txt
# or  (dis one fit still mean di same in pidgin)
pip install -e .
python main.py
```

#### Java Projects
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Development Workflow

### MCP 7-28 Readiness

#### Repo readiness checklist

- [x] **New contributor clarity**: Dis file dey define repository purpose,
  structure, contribution rules, and sample setup paths.
- [x] **Build/test/lint commands wey get exact flags**:
  - Repository docs lint:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Repository docs link pattern audit:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - TypeScript sample validation:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Python sample validation:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Java sample validation:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **One realistic workflow wey fit become MCP tool**:
  `validate_curriculum_change`
- [x] **Inputs/outputs dey explicit** (see specification below).
- [x] **Permissions and failure modes dey documented** (see specification below).
- [x] **CI testability dey explicit** (deterministic commands, explicit
  exit codes, and machine-readable outputs).

#### Candidate MCP tool workflow: `validate_curriculum_change`

##### Goal

Validate curriculum documentation changes and representative sample code
health before merge.

##### Inputs

- `changed_paths: string[]` (required) - relative paths wey change for PR.
- `run_docs_lint: boolean` (default `true`)
- `run_links_audit: boolean` (default `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (default all `false`)

##### Outputs

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Permissions

- Read workspace files and write tool-generated artifacts (like lint
  reports, test logs) only; no writes to `translations/` or
  `translated_images/`.
- Execute local shell commands.
- Optional network access only for package restore (`npm ci`,
  `python -m pip install`, `mvn` dependency resolution).
- No permission to push, merge, or modify `translations/` or
  `translated_images/`.

##### Failure modes

- `E_NO_INPUT_PATHS`: `changed_paths` empty.
- `E_INVALID_PATH`: input path run waka comot from repository root.
- `E_LINT_FAILED`: markdown lint exit non-zero.
- `E_LINK_AUDIT_FAILED`: link audit command exit non-zero.
- `E_SAMPLE_TEST_FAILED`: sample test/build exit non-zero.
- `E_TIMEOUT`: command pass im configured timeout.

##### Recommended CI contract

To automatically do validation, configure a CI job wey:

- Triggers on pull requests wey touch `*.md`, sample code, or dis file.
- Runs the exact commands wey dey listed above.
- Persists logs as artifacts.
- Fail the job if any non-zero exit code show.

#### If you dey ship MCP server from dis repo

- [ ] Read the draft changelog for MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Run your server against SDK betas:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Remove session and handshake assumptions; treat each request as
  self-contained:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Send `Mcp-Method` and `Mcp-Name` headers for raw HTTP requests:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Audit hardcoded error codes (`missing resource` move from `-32002` go `-32602`).
- [ ] Flag and plan migration for deprecated roots, sampling, and
  logging:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Migrate off the experimental `2025-11-25` Tasks API:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Review authorization for OAuth and OpenID Connect hardening:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Documentation Structure

- **Modules 00-11**: Core curriculum content in sequential order
- **translations/**: Language-specific versions (auto-generated, no edit directly)
- **translated_images/**: Localized image versions (auto-generated)
- **images/**: Source images and diagrams

### Making Documentation Changes

1. Edit only English markdown files for root module directories (00-11)
2. Update images for `images/` directory if you need
3. co-op-translator GitHub Action go automatically generate translations
4. Translations go regenerate when push to main branch

### Working with Translations

- **Automated Translation**: GitHub Actions workflow dey handle all translations
- **No manually edit** files for `translations/` directory
- Translation metadata go dey inside each translated file
- Supported languages: 48+ languages including Arabic, Chinese, French, German, Hindi, Japanese, Korean, Portuguese, Russian, Spanish, and many more

## Testing Instructions

### Documentation Validation

Since dis one na mostly documentation repository, the testing dey focus on:

1. **Link Pattern Audit**: List Markdown links for review

   ```bash
   # List Markdown links (pattern audit)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Code Sample Validation**: Test say code examples fit compile/run

   ```bash
   # Go find dat one sample and run e tests
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown Linting**: Check formatting consistency

   ```bash
   # Use markdownlint if e need be
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Sample Project Testing

Each language-specific sample get im own testing method:

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

## Code Style Guidelines

### Documentation Style

- Use clear, beginner-friendly language
- Include code examples for multiple languages if e fit
- Follow markdown better practices:
  - Use ATX-style headers (`#` syntax)
  - Use fenced code blocks wit language identifiers
  - Include descriptive alt text for images
  - Keep line lengths reasonable (no hard limit, but be sensible)

### Code Sample Style

#### TypeScript/JavaScript
- Use ES modules (`import`/`export`)
- Follow TypeScript strict mode conventions
- Include type annotations
- Target ES2022

#### Python
- Follow PEP 8 style guidelines
- Use type hints where necessary
- Include docstrings for functions and classes
- Use modern Python features (3.8+)

#### Java
- Follow Spring Boot conventions
- Use Java 21 features
- Follow standard Maven project structure
- Include Javadoc comments

### File Organization

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

## Build and Deployment

### Documentation Deployment

The repository dey use GitHub Pages or wetin similar for documentation hosting (if e dey). Changes to the main branch go trigger:

1. Translation workflow (`.github/workflows/co-op-translator.yml`)
2. Automated translation of all English markdown files
3. Image localization if e need

### No Build Process Required

Dis repository mainly get markdown documentation. No compilation or build step dey needed for the core curriculum content.

### Sample Project Deployment

Individual sample projects fit get deployment instructions:
- See `03-GettingStarted/09-deployment/` for MCP server deployment guidance
- Azure Container Apps deployment examples dey `11-MCPServerHandsOnLabs/`

## Contributing Guidelines

### Pull Request Process

1. **Fork and Clone**: Fork di repository and clone your fork for local machine
2. **Create a Branch**: Use descriptive branch names (for example, `fix/typo-module-3`, `add/python-example`)
3. **Make Changes**: Edit only English markdown files (no touch translations)
4. **Test Locally**: Make sure markdown dey render well
5. **Submit PR**: Use clear titles and descriptions for PR
6. **CLA**: Sign Microsoft Contributor License Agreement when e ask you

### PR Title Format

Use clear, descriptive titles:
- `[Module XX] Short description` for module-specific changes
- `[Samples] Description` for sample code changes
- `[Docs] Description` for general documentation updates

### Wetin to Contribute

- Bug fixes for documentation or code samples
- New code examples for different languages
- Clarifications and improvements for existing content
- New case studies or practical examples
- Issue reports for unclear or incorrect content

### Wetin NOT to Do

- No directly edit files for `translations/` directory
- No edit `translated_images/` directory
- No add big big binary files without talk first
- No change translation workflow files without coordination

## Additional Notes

### Repository Maintenance

- **Changelog**: All important changes dem dey document for `changelog.md`
- **Study Guide**: Use `study_guide.md` for curriculum navigation overview
- **Issue Templates**: Use GitHub issue templates for bug reports and feature requests
- **Code of Conduct**: All contributors gats follow Microsoft Open Source Code of Conduct

### Learning Path

Follow modules in order (00-11) to learn well well:
1. **00-02**: Fundamentals (Introduction, Core Concepts, Security)
2. **03**: Getting Started with hands-on implementation
3. **04-05**: Practical implementation and advanced topics
4. **06-10**: Community, best practices, and real-world applications
5. **11**: Comprehensive database integration labs (13 sequential labs)

### Support Resources

- **Documentation**: https://modelcontextprotocol.io/
- **Specification**: https://spec.modelcontextprotocol.io/
- **Community**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord server
- **Related Courses**: See README.md for other Microsoft learning paths

### Common Troubleshooting

**Q: My PR dey fail translation check**
A: Make sure say you only edit English markdown files for root module folders, no change translated versions.

**Q: How I go take add new language?**
A: Language support dey handled through co-op-translator workflow. Open issue to talk about how to add new languages.

**Q: Code samples no dey work**

A: Make sure say you don follow di setup instructions for di specific sample README. Check say di versions of dependencies wey you get na correct one.

**Q: Images no dey show**
A: Confirm say di image paths na relative and di dem dey use forward slashes. Images suppose dey for di `images/` directory or `translated_images/` for localized versions.

### Performance Considerations

- Translation workflow fit carry plenty minutes to complete
- Big-big images suppose optimize before you commit
- Make individual markdown files dey focused and dey reasonable size
- Use relative links to make am easy to move

### Project Governance

Dis project dey follow Microsoft open source practices:
- MIT License for code and documentation
- Microsoft Open Source Code of Conduct
- CLA dey required for contributions
- Security issues: Follow SECURITY.md guidelines
- Support: See SUPPORT.md for help resources

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->