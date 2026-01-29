# AGENTS.md

## ပရောဂျက်အကျဉ်းချုပ်

**MCP for Beginners** သည် Model Context Protocol (MCP) ကိုလေ့လာရန်အတွက် AI မော်ဒယ်များနှင့် client အက်ပလီကေးရှင်းများအကြား အပြန်အလှန်ဆက်သွယ်မှုများအတွက် စံသတ်မှတ်ထားသော framework တစ်ခုဖြစ်သည်။ ဤ repository သည် အမျိုးမျိုးသော programming language များတွင် လက်တွေ့ကိုင်တွယ်နိုင်သော code နမူနာများနှင့်အတူ လေ့လာရေးအထောက်အကူပြု ပစ္စည်းများကို ပြည့်စုံစွာပေးထားသည်။

### အဓိကနည်းပညာများ

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

- **11 Core Modules (00-11)**: အခြေခံမှစ၍ အဆင့်မြင့်အထိ လေ့လာရေးလမ်းကြောင်း
- **Hands-on Labs**: လက်တွေ့လုပ်ဆောင်မှုများနှင့် အမျိုးမျိုးသော programming language များအတွက် ဖြေရှင်းချက် code များ
- **Sample Projects**: MCP server နှင့် client အကောင်အထည်ဖော်မှုများ
- **Translation System**: GitHub Actions workflow ကို အသုံးပြု၍ ဘာသာစကားများစွာကို အလိုအလျောက် ဘာသာပြန်ပေးခြင်း
- **Image Assets**: ဘာသာပြန်ထားသော ဓာတ်ပုံများကို စုစည်းထားသော directory

## Setup Commands

ဤ repository သည် documentation အဓိကထားသော repository ဖြစ်သည်။ အများဆုံး setup များကို individual sample projects နှင့် labs တွင်လုပ်ဆောင်ရမည်။

### Repository Setup

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Sample Projects နှင့်အလုပ်လုပ်ခြင်း

Sample projects များကို အောက်ပါနေရာများတွင် ရှာနိုင်သည်။
- `03-GettingStarted/samples/` - ဘာသာစကားအလိုက် နမူနာများ
- `03-GettingStarted/01-first-server/solution/` - ပထမဆုံး server အကောင်အထည်ဖော်မှုများ
- `03-GettingStarted/02-client/solution/` - Client အကောင်အထည်ဖော်မှုများ
- `11-MCPServerHandsOnLabs/` - Database integration labs များ

Sample project တစ်ခုစီတွင် setup လုပ်ရန် လမ်းညွှန်ချက်များပါဝင်သည်။

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

- **Modules 00-11**: အဓိက curriculum အကြောင်းအရာများကို အစဉ်လိုက်
- **translations/**: ဘာသာစကားအလိုက် version များ (auto-generated, မပြင်ပါ)
- **translated_images/**: ဘာသာပြန်ထားသော ဓာတ်ပုံ version များ (auto-generated)
- **images/**: အရင်းအမြစ် ဓာတ်ပုံများနှင့် အကြမ်းဖျင်းပုံများ

### Documentation Changes ပြုလုပ်ခြင်း

1. Root module directories (00-11) တွင် English markdown ဖိုင်များကိုသာ ပြင်ဆင်ပါ
2. `images/` directory တွင် ဓာတ်ပုံများကို update လုပ်ပါ (လိုအပ်ပါက)
3. co-op-translator GitHub Action သည် ဘာသာပြန်မှုများကို အလိုအလျောက် ပြုလုပ်မည်
4. Main branch သို့ push လုပ်သောအခါ ဘာသာပြန်မှုများကို ပြန်လည်ဖန်တီးမည်

### Translations နှင့်အလုပ်လုပ်ခြင်း

- **Automated Translation**: GitHub Actions workflow သည် ဘာသာပြန်မှုများကို စီမံခန့်ခွဲသည်
- `translations/` directory တွင် ဖိုင်များကို လက်ဖြင့် မပြင်ပါ
- Translation metadata သည် translated ဖိုင်တစ်ခုစီတွင် embed လုပ်ထားသည်
- Supported languages: 48+ ဘာသာစကားများ (Arabic, Chinese, French, German, Hindi, Japanese, Korean, Portuguese, Russian, Spanish, စသည်တို့)

## Testing Instructions

### Documentation Validation

ဤ repository သည် documentation အဓိကထားသော repository ဖြစ်သဖြင့် အောက်ပါအချက်များကို စစ်ဆေးရမည်။

1. **Link Validation**: Internal links အားလုံးအလုပ်လုပ်မှုရှိမရှိ စစ်ဆေးပါ
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Code Sample Validation**: Code နမူနာများ compile/run ဖြစ်နိုင်မရှိ စစ်ဆေးပါ
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Markdown Linting**: Formatting consistency ကို စစ်ဆေးပါ
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Sample Project Testing

ဘာသာစကားအလိုက် sample တစ်ခုစီတွင် testing လုပ်ရန် လမ်းညွှန်ချက်များပါဝင်သည်။

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

- ရိုးရှင်းပြီး စတင်လေ့လာသူများအတွက် သင့်လျော်သော ဘာသာစကားကို အသုံးပြုပါ
- လိုအပ်သောနေရာတွင် ဘာသာစကားအမျိုးမျိုးဖြင့် code နမူနာများ ထည့်ပါ
- Markdown အကောင်းဆုံးအလေ့အကျင့်များကို လိုက်နာပါ။
  - ATX-style headers (`#` syntax) ကို အသုံးပြုပါ
  - Fenced code blocks ကို language identifiers ဖြင့် အသုံးပြုပါ
  - ဓာတ်ပုံများအတွက် ဖော်ပြချက် alt text ထည့်ပါ
  - Line length များကို သင့်တော်စွာ ထိန်းသိမ်းပါ (တိတိကျကျ hard limit မရှိသော်လည်း)

### Code Sample Style

#### TypeScript/JavaScript
- ES modules (`import`/`export`) ကို အသုံးပြုပါ
- TypeScript strict mode conventions ကို လိုက်နာပါ
- Type annotations ထည့်ပါ
- ES2022 ကို target လုပ်ပါ

#### Python
- PEP 8 style guidelines ကို လိုက်နာပါ
- Type hints ကို သင့်တော်သောနေရာတွင် အသုံးပြုပါ
- Functions နှင့် classes အတွက် docstrings ထည့်ပါ
- Modern Python features (3.8+) ကို အသုံးပြုပါ

#### Java
- Spring Boot conventions ကို လိုက်နာပါ
- Java 21 features ကို အသုံးပြုပါ
- Standard Maven project structure ကို လိုက်နာပါ
- Javadoc comments ထည့်ပါ

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

Repository သည် GitHub Pages သို့မဟုတ် အခြားတူညီသော platform များကို documentation hosting အတွက် အသုံးပြုသည် (လိုအပ်ပါက)။ Main branch သို့ ပြောင်းလဲမှုများသည် အောက်ပါအဆင့်များကို trigger လုပ်သည်။

1. Translation workflow (`.github/workflows/co-op-translator.yml`)
2. English markdown ဖိုင်များအားလုံးကို အလိုအလျောက် ဘာသာပြန်ခြင်း
3. လိုအပ်သောနေရာတွင် ဓာတ်ပုံ localization

### No Build Process Required

ဤ repository သည် အဓိကအား markdown documentation ကိုသာ ပါဝင်သည်။ Core curriculum အကြောင်းအရာအတွက် compilation သို့မဟုတ် build အဆင့်မလိုအပ်ပါ။

### Sample Project Deployment

Individual sample projects တွင် deployment လုပ်ရန် လမ်းညွှန်ချက်များပါဝင်နိုင်သည်။
- `03-GettingStarted/09-deployment/` တွင် MCP server deployment လမ်းညွှန်ချက်များကို ကြည့်ပါ
- Azure Container Apps deployment နမူနာများကို `11-MCPServerHandsOnLabs/` တွင် ရှာပါ

## Contributing Guidelines

### Pull Request Process

1. **Fork and Clone**: Repository ကို fork လုပ်ပြီး local မှာ clone လုပ်ပါ
2. **Create a Branch**: ဖော်ပြချက် branch name များကို အသုံးပြုပါ (ဥပမာ - `fix/typo-module-3`, `add/python-example`)
3. **Make Changes**: English markdown ဖိုင်များကိုသာ ပြင်ဆင်ပါ (translations မဟုတ်)
4. **Test Locally**: Markdown render မှန်ကန်မှုရှိမရှိ စစ်ဆေးပါ
5. **Submit PR**: PR title နှင့် description ကို ရှင်းလင်းစွာရေးပါ
6. **CLA**: Microsoft Contributor License Agreement ကို လိုအပ်ပါက လက်မှတ်ရေးပါ

### PR Title Format

ရှင်းလင်းသော title များကို အသုံးပြုပါ။
- `[Module XX] Brief description` - module-specific ပြောင်းလဲမှုများအတွက်
- `[Samples] Description` - sample code ပြောင်းလဲမှုများအတွက်
- `[Docs] Description` - general documentation ပြောင်းလဲမှုများအတွက်

### ဘာကို Contribute လုပ်ရမည်

- Documentation သို့မဟုတ် code နမူနာများတွင် bug fix
- အပို programming language များအတွက် code နမူနာအသစ်များ
- ရှိပြီးသားအကြောင်းအရာများကို ရှင်းလင်းမှုနှင့် တိုးတက်မှုများ
- Practical examples သို့မဟုတ် case studies အသစ်များ
- မမှန်ကန်သောအကြောင်းအရာများအတွက် issue report

### ဘာကို မလုပ်သင့်

- `translations/` directory တွင် ဖိုင်များကို မပြင်ပါ
- `translated_images/` directory ကို မပြင်ပါ
- ကြီးမားသော binary ဖိုင်များကို မထည့်ပါ (ညှိနှိုင်းမှုမရှိပါက)
- Translation workflow ဖိုင်များကို coordination မရှိဘဲ မပြောင်းပါ

## အပိုအချက်များ

### Repository Maintenance

- **Changelog**: `changelog.md` တွင် အရေးကြီးသော ပြောင်းလဲမှုများကို မှတ်တမ်းတင်ထားသည်
- **Study Guide**: `study_guide.md` ကို curriculum navigation အတွက် အသုံးပြုပါ
- **Issue Templates**: Bug report နှင့် feature request များအတွက် GitHub issue templates ကို အသုံးပြုပါ
- **Code of Conduct**: Microsoft Open Source Code of Conduct ကို လိုက်နာရမည်

### Learning Path

Modules (00-11) ကို အစဉ်လိုက် လေ့လာပါ။
1. **00-02**: အခြေခံ (Introduction, Core Concepts, Security)
2. **03**: လက်တွေ့အကောင်အထည်ဖော်မှု
3. **04-05**: လက်တွေ့အကောင်အထည်ဖော်မှုနှင့် အဆင့်မြင့်အကြောင်းအရာများ
4. **06-10**: Community, အကောင်းဆုံးအလေ့အကျင့်များနှင့် အမှန်တကယ်အသုံးချမှုများ
5. **11**: Comprehensive database integration labs (13 sequential labs)

### Support Resources

- **Documentation**: https://modelcontextprotocol.io/
- **Specification**: https://spec.modelcontextprotocol.io/
- **Community**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Azure AI Foundry Discord server
- **Related Courses**: README.md တွင် Microsoft learning paths အခြားများကို ကြည့်ပါ

### Common Troubleshooting

**Q: My PR is failing the translation check**
A: Root module directories တွင် English markdown ဖိုင်များကိုသာ ပြင်ဆင်ထားကြောင်း သေချာပါ။

**Q: How do I add a new language?**
A: Language support ကို co-op-translator workflow မှ စီမံသည်။ ဘာသာစကားအသစ်ထည့်ရန်အတွက် issue တစ်ခုဖွင့်ပါ။

**Q: Code samples aren't working**
A: Specific sample ရဲ့ README တွင် setup လုပ်ရန် လမ်းညွှန်ချက်များကို လိုက်နာထားကြောင်း သေချာပါ။ Dependency များ၏ version မှန်ကန်မှုကို စစ်ဆေးပါ။

**Q: Images aren't displaying**
A: Image paths သည် relative ဖြစ်ကြောင်းနှင့် forward slashes ကို အသုံးပြုထားကြောင်း သေချာပါ။ ဓာတ်ပုံများသည် `images/` directory သို့မဟုတ် `translated_images/` တွင် ရှိရမည်။

### Performance Considerations

- Translation workflow သည် မိနစ်အနည်းငယ်ကြာနိုင်သည်
- ကြီးမားသော ဓာတ်ပုံများကို commit မလုပ်မီ optimize လုပ်ပါ
- Individual markdown ဖိုင်များကို အဓိကအကြောင်းအရာများအတွက် သင့်တော်စွာ ထိန်းသိမ်းပါ
- Relative links ကို အသုံးပြုပါ

### Project Governance

ဤပရောဂျက်သည် Microsoft open source လုပ်ထုံးလုပ်နည်းများကို လိုက်နာသည်။
- MIT License for code and documentation
- Microsoft Open Source Code of Conduct
- CLA လိုအပ်သော contribution များအတွက်
- Security issues: SECURITY.md လမ်းညွှန်ချက်များကို လိုက်နာပါ
- Support: SUPPORT.md တွင် အထောက်အကူပေးသော resources များကို ကြည့်ပါ

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။