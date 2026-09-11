# AGENTS.md

## Project Overview

**MCP for Beginners** na open-source educational curriculum wey dem take learn Model Context Protocol (MCP) - na standardized framework for interactions between AI models and client applications. Dis repository dey provide comprehensive learning materials with hands-on code examples for plenty programming languages dem.

### Key Technologies

- **Programming Languages**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworks & SDKs**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Databases**: PostgreSQL with pgvector extension
- **Cloud Platforms**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Build Tools**: npm, Maven, pip, Cargo
- **Documentation**: Markdown with automated multi-language translation (48+ languages)

### Architecture

- **11 Core Modules (00-11)**: Sequential learning path from fundamentals to advanced topics
- **Hands-on Labs**: Practical exercises with complete solution code in multiple languages
- **Sample Projects**: Working MCP server and client implementations
- **Translation System**: Automated GitHub Actions workflow for multi-language support
- **Image Assets**: Centralized images directory with translated versions

## Setup Commands

Dis na documentation-focused repository. Most setup dey happen inside individual sample projects and labs.

### Repository Setup

```bash
# Make you copy di repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Working with Sample Projects

Sample projects dey for:
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
# or
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
- [x] **Build/test/lint commands with exact flags**:
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
- [x] **One realistic workflow that can become an MCP tool**:
  `validate_curriculum_change`
- [x] **Inputs/outputs are explicit** (see specification below).
- [x] **Permissions and failure modes are documented** (see specification below).
- [x] **CI testability is explicit** (deterministic commands, explicit
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

- Read workspace files and write tool-generated artifacts (e.g., lint
  reports, test logs) only; no writes to `translations/` or
  `translated_images/`.
- Execute local shell commands.
- Optional network access only for package restore (`npm ci`,
  `python -m pip install`, `mvn` dependency resolution).
- No permission to push, merge, or modify `translations/` or
  `translated_images/`.

##### Failure modes

- `E_NO_INPUT_PATHS`: `changed_paths` empty.
- `E_INVALID_PATH`: input path dey escape repository root.
- `E_LINT_FAILED`: markdown lint exit with non-zero.
- `E_LINK_AUDIT_FAILED`: link audit command exit with non-zero.
- `E_SAMPLE_TEST_FAILED`: sample test/build exit with non-zero.
- `E_TIMEOUT`: command pass the configured timeout.

##### Recommended CI contract

To automate validation, configure one CI job wey:

- Dey trigger for pull requests wey touch `*.md`, sample code, or dis file.
- Dey run all di exact commands wey dem talk for up.
- Dey save logs as artifacts.
- Dey fail the job if any non-zero exit code happen.

#### If you deploy one MCP server from this repo

- [ ] Read the final MCP `2026-07-28` changelog:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] Verify say the SDK release wey you choose support MCP `2026-07-28`:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] Remove session and handshake assumptions; treat every request as
  self-contained:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] Send `Mcp-Method` and `Mcp-Name` headers for raw HTTP requests:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] Audit hardcoded error codes (`missing resource` don move from `-32002` to `-32602`).
- [ ] Migrate deprecated Roots, Sampling, Logging, and Dynamic Client
  Registration:
  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] Migrate off the experimental `2025-11-25` Tasks API:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] Review authorization for OAuth and OpenID Connect hardening:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### Documentation Structure

- **Modules 00-11**: Core curriculum content in sequential order
- **translations/**: Language-specific versions (auto-generated, no edit direct)
- **translated_images/**: Localized image versions (auto-generated)
- **images/**: Source images and diagrams

### Making Documentation Changes

1. Edit only the English markdown files for root module directories (00-11)
2. Update images for `images/` directory if e need
3. The co-op-translator GitHub Action go automatically generate translations
4. Translations dey regenerate every time una push to main branch

### Working with Translations

- **Automated Translation**: GitHub Actions workflow dey handle all translations
- **No manually edit** files for `translations/` directory
- Translation metadata dey inside every translated file
- Supported languages: 48+ languages like Arabic, Chinese, French, German, Hindi, Japanese, Korean, Portuguese, Russian, Spanish, and many others

## Testing Instructions

### Documentation Validation

Since dis na main documentation repository, testing dey focus on:

1. **Link Pattern Audit**: List Markdown links for review

   ```bash
   # List Markdown links (patin audit)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Code Sample Validation**: Test say code examples dey compile/run

   ```bash
   # Go waka go particular sample and run dia tests
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown Linting**: Check formatting consistency

   ```bash
   # Use markdownlint if you need am
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
- Include code examples for multiple languages where e fit
- Follow markdown best practices:
  - Use ATX-style headers (`#` syntax)
  - Use fenced code blocks with language identifiers
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
- Use type hints where e dey necessary
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

The repository dey use GitHub Pages or similar for documentation hosting (if e dey applicable). Changes for the main branch go trigger:

1. Translation workflow (`.github/workflows/co-op-translator.yml`)
2. Automated translation for all English markdown files
3. Image localization when e need

### No Build Process Required

Dis repository mainly get markdown documentation. No compilation or build step dey necessary for the core curriculum content.

### Sample Project Deployment

Individual sample projects fit get deployment instructions:
- See `03-GettingStarted/09-deployment/` for MCP server deployment guidance
- Azure Container Apps deployment examples for `11-MCPServerHandsOnLabs/`

## Contributing Guidelines

### Pull Request Process

1. **Fork and Clone**: Fork di repository and clone your fork locally
2. **Create a Branch**: Use descriptive branch names (e.g., `fix/typo-module-3`, `add/python-example`)
3. **Make Changes**: Edit only English markdown files (no translations)
4. **Test Locally**: Check say markdown dey render well
5. **Submit PR**: Use clear PR titles and descriptions
6. **CLA**: Sign the Microsoft Contributor License Agreement as e come up

### PR Title Format

Use clear, descriptive titles:
- `[Module XX] Brief description` for module-specific changes
- `[Samples] Description` for sample code changes
- `[Docs] Description` for general documentation updates

### Wetin to Contribute

- Bug fixes for documentation or code samples
- New code examples for more languages
- Clarifications and improvements to existing content
- New case studies or practical examples
- Issue reports for unclear or wrong content

### Wetin NOT to Do

- No direct edit of files for `translations/` directory
- No edit for `translated_images/` directory
- No add big binary files without talk am first
- No change translation workflow files without arrangement

## Additional Notes

### Repository Maintenance

- **Changelog**: All important changes dey documented for `changelog.md`
- **Study Guide**: Use `study_guide.md` for curriculum navigation overview
- **Issue Templates**: Use GitHub issue templates for bug reports and feature requests
- **Code of Conduct**: All contributors must follow Microsoft Open Source Code of Conduct

### Learning Path

Follow modules inside sequential order (00-11) to get better learning:
1. **00-02**: Fundamentals (Introduction, Core Concepts, Security)
2. **03**: Getting Started with hands-on implementation
3. **04-05**: Practical implementation and advanced topics
4. **06-10**: Community, best practices, and real-world applications
5. **11**: Comprehensive database integration labs (13 sequential labs)

### Support Resources

- **Documentation**: https://modelcontextprotocol.io/
- **Specification**: https://modelcontextprotocol.io/specification/2026-07-28/
- **Community**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord server
- **Related Courses**: See README.md for other Microsoft learning paths

### Common Troubleshooting

**Q: My PR dey fail the translation check**
A: Make sure say you only edit English markdown files for root module directories, no be translated versions.

**Q: How I fit add new language?**
A: Language support dey managed by the co-op-translator workflow. Open issue to discuss how to add new languages.

**Q: Code samples no dey work**
A: Make sure say you don follow setup instructions for the specific sample README. Check if you get correct versions of dependencies install.

**Q: Images no dey show**

A: Make sure sey image paths dey relative and dem dey use forward slashes. Images suppose dey inside di `images/` folder or for `translated_images/` if na localized versions.

### Performance Considerations

- Translation workflow fit take plenty minute make e complete
- Big images suppose dem go optimize dem before dem commit am
- Make sure make individual markdown files dey focused and no too big
- Use relative links make e better to carry go another place

### Project Governance

Dis project dey follow Microsoft open source way dem:
- MIT License dey for code and documentation
- Microsoft Open Source Code of Conduct dey
- CLA dem dey need for contribution
- Security issues: Make you follow SECURITY.md guideline dem
- Support: Check SUPPORT.md for help resources

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->