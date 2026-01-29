# AGENTS.md

## Project Overview

**MCP for Beginners** na open-source curriculum wey dey teach Model Context Protocol (MCP) - na one standard framework wey dey help AI models and client apps dey interact well. Dis repository get full learning materials wey include code examples for different programming languages.

### Key Technologies

- **Programming Languages**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworks & SDKs**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Databases**: PostgreSQL wey get pgvector extension
- **Cloud Platforms**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Build Tools**: npm, Maven, pip, Cargo
- **Documentation**: Markdown wey fit translate automatically to 48+ languages

### Architecture

- **11 Core Modules (00-11)**: Step-by-step learning from basics to advanced topics
- **Hands-on Labs**: Practical exercises wey get solution code for different languages
- **Sample Projects**: MCP server and client wey dey work well
- **Translation System**: GitHub Actions workflow wey dey translate to different languages
- **Image Assets**: Centralized image folder wey get translated versions

## Setup Commands

Dis repository na mainly for documentation. Most setup dey happen inside the sample projects and labs.

### Repository Setup

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Working with Sample Projects

Sample projects dey for:
- `03-GettingStarted/samples/` - Examples for different languages
- `03-GettingStarted/01-first-server/solution/` - First server implementations
- `03-GettingStarted/02-client/solution/` - Client implementations
- `11-MCPServerHandsOnLabs/` - Labs wey dey show how database dey work

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

### Documentation Structure

- **Modules 00-11**: Main curriculum content wey dey follow order
- **translations/**: Versions for different languages (auto-generated, no touch am)
- **translated_images/**: Localized image versions (auto-generated)
- **images/**: Original images and diagrams

### Making Documentation Changes

1. Edit only the English markdown files wey dey root module folders (00-11)
2. Update images for `images/` folder if e need am
3. GitHub Action wey be co-op-translator go generate translations automatically
4. Translations go update anytime you push to main branch

### Working with Translations

- **Automated Translation**: GitHub Actions dey handle translations
- **No touch manually** files wey dey `translations/` folder
- Translation metadata dey inside each translated file
- Supported languages: 48+ languages like Arabic, Chinese, French, German, Hindi, Japanese, Korean, Portuguese, Russian, Spanish, and plenty others

## Testing Instructions

### Documentation Validation

Since dis repository na mainly documentation, testing dey focus on:

1. **Link Validation**: Make sure all internal links dey work
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Code Sample Validation**: Test say code examples dey compile/run well
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Markdown Linting**: Check say formatting dey consistent
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
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

- Use simple language wey beginners go understand
- Add code examples for different languages if e dey possible
- Follow markdown best practices:
  - Use ATX-style headers (`#` syntax)
  - Use fenced code blocks wey get language identifiers
  - Add descriptive alt text for images
  - Make line length reasonable (no hard limit, but e no go too long)

### Code Sample Style

#### TypeScript/JavaScript
- Use ES modules (`import`/`export`)
- Follow TypeScript strict mode rules
- Add type annotations
- Target ES2022

#### Python
- Follow PEP 8 style rules
- Use type hints if e dey possible
- Add docstrings for functions and classes
- Use modern Python features (3.8+)

#### Java
- Follow Spring Boot rules
- Use Java 21 features
- Follow standard Maven project structure
- Add Javadoc comments

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

Dis repository dey use GitHub Pages or similar platform for documentation hosting (if e dey applicable). Changes wey dey main branch go trigger:

1. Translation workflow (`.github/workflows/co-op-translator.yml`)
2. Automatic translation of all English markdown files
3. Image localization if e dey needed

### No Build Process Required

Dis repository na mainly markdown documentation. No need to compile or build the main curriculum content.

### Sample Project Deployment

Individual sample projects fit get deployment instructions:
- Check `03-GettingStarted/09-deployment/` for MCP server deployment guide
- Azure Container Apps deployment examples dey `11-MCPServerHandsOnLabs/`

## Contributing Guidelines

### Pull Request Process

1. **Fork and Clone**: Fork the repository and clone am for your computer
2. **Create a Branch**: Use branch names wey dey descriptive (e.g., `fix/typo-module-3`, `add/python-example`)
3. **Make Changes**: Edit only English markdown files (no touch translations)
4. **Test Locally**: Check say markdown dey render well
5. **Submit PR**: Use clear PR titles and descriptions
6. **CLA**: Sign Microsoft Contributor License Agreement if dem ask you

### PR Title Format

Use clear, descriptive titles:
- `[Module XX] Brief description` for module-specific changes
- `[Samples] Description` for sample code changes
- `[Docs] Description` for general documentation updates

### Wetin You Fit Contribute

- Fix bugs for documentation or code samples
- Add new code examples for more languages
- Make existing content clearer or better
- Add new case studies or practical examples
- Report issues for unclear or wrong content

### Wetin You No Go Do

- No edit files wey dey `translations/` folder
- No touch `translated_images/` folder
- No add big binary files without discussion
- No change translation workflow files without agreement

## Additional Notes

### Repository Maintenance

- **Changelog**: All big changes dey documented for `changelog.md`
- **Study Guide**: Use `study_guide.md` to navigate curriculum
- **Issue Templates**: Use GitHub issue templates for bug reports and feature requests
- **Code of Conduct**: All contributors must follow Microsoft Open Source Code of Conduct

### Learning Path

Follow modules step-by-step (00-11) for better learning:
1. **00-02**: Basics (Introduction, Core Concepts, Security)
2. **03**: Getting Started with practical implementation
3. **04-05**: Practical implementation and advanced topics
4. **06-10**: Community, best practices, and real-world applications
5. **11**: Full database integration labs (13 step-by-step labs)

### Support Resources

- **Documentation**: https://modelcontextprotocol.io/
- **Specification**: https://spec.modelcontextprotocol.io/
- **Community**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Azure AI Foundry Discord server
- **Related Courses**: Check README.md for other Microsoft learning paths

### Common Troubleshooting

**Q: My PR dey fail translation check**
A: Make sure say you only edit English markdown files wey dey root module folders, no touch translated versions.

**Q: How I go add new language?**
A: Language support dey managed through co-op-translator workflow. Open issue to discuss am.

**Q: Code samples no dey work**
A: Make sure say you follow setup instructions wey dey specific sample README. Check say you install correct versions of dependencies.

**Q: Images no dey show**
A: Confirm say image paths dey relative and use forward slashes. Images suppose dey `images/` folder or `translated_images/` for localized versions.

### Performance Considerations

- Translation workflow fit take some minutes to complete
- Big images suppose dey optimized before you commit am
- Make markdown files dey focused and no too big
- Use relative links for better portability

### Project Governance

Dis project dey follow Microsoft open source rules:
- MIT License for code and documentation
- Microsoft Open Source Code of Conduct
- CLA dey required for contributions
- Security issues: Follow SECURITY.md guidelines
- Support: Check SUPPORT.md for help resources

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleto service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even though we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey you go fit trust. For important mata, e good make you use professional human translation. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->