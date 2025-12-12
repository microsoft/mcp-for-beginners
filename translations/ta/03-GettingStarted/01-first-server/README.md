<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8fdac7600a5f4722643d0f14e15ac259",
  "translation_date": "2025-12-11T08:50:42+00:00",
  "source_file": "03-GettingStarted/01-first-server/README.md",
  "language_code": "ta"
}
-->
# MCP உடன் துவக்கம்

Model Context Protocol (MCP) உடன் உங்கள் முதல் படிகளுக்கு வரவேற்கிறோம்! நீங்கள் MCP-க்கு புதியவராக இருந்தாலும் அல்லது உங்கள் புரிதலை ஆழப்படுத்த விரும்பினாலும், இந்த வழிகாட்டி முக்கியமான அமைப்பு மற்றும் மேம்பாட்டு செயல்முறையை வழிநடத்தும். MCP எப்படி AI மாதிரிகள் மற்றும் பயன்பாடுகளுக்கு இடையேயான ஒருங்கிணைப்பை எளிதாக்குகிறது என்பதை நீங்கள் கண்டுபிடிப்பீர்கள், மேலும் MCP-ஆல் இயக்கப்படும் தீர்வுகளை உருவாக்கி சோதிக்க உங்கள் சூழலை விரைவாக தயார் செய்வது எப்படி என்பதை கற்றுக்கொள்வீர்கள்.

> TLDR; நீங்கள் AI பயன்பாடுகளை உருவாக்கினால், உங்கள் LLM (பெரிய மொழி மாதிரி) க்கு கருவிகள் மற்றும் பிற வளங்களை சேர்க்க முடியும் என்பதை நீங்கள் அறிவீர்கள், இதனால் LLM அதிக அறிவார்ந்ததாக மாறும். ஆனால் அந்த கருவிகள் மற்றும் வளங்களை ஒரு சர்வரில் வைக்கும்போது, அந்த பயன்பாடு மற்றும் சர்வர் திறன்கள் எந்தவொரு கிளையண்டுக்கும் LLM உடன் அல்லது இல்லாமல் பயன்படுத்தக்கூடியதாக இருக்கும்.

## கண்ணோட்டம்

இந்த பாடம் MCP சூழல்களை அமைப்பது மற்றும் உங்கள் முதல் MCP பயன்பாடுகளை உருவாக்குவது பற்றி நடைமுறை வழிகாட்டுதலை வழங்குகிறது. தேவையான கருவிகள் மற்றும் கட்டமைப்புகளை அமைப்பது, அடிப்படை MCP சர்வர்களை உருவாக்குவது, ஹோஸ்ட் பயன்பாடுகளை உருவாக்குவது மற்றும் உங்கள் செயல்பாடுகளை சோதிப்பது எப்படி என்பதை நீங்கள் கற்றுக்கொள்வீர்கள்.

Model Context Protocol (MCP) என்பது பயன்பாடுகள் LLM களுக்கு (பெரிய மொழி மாதிரிகளுக்கு) சூழலை வழங்கும் முறையை ஒருங்கிணைக்கும் திறந்த நெறிமுறை ஆகும். MCP ஐ AI பயன்பாடுகளுக்கான USB-C போர்ட்டாக நினைத்துக் கொள்ளுங்கள் - இது AI மாதிரிகளை வெவ்வேறு தரவுத் தளங்கள் மற்றும் கருவிகளுடன் இணைக்கும் ஒருங்கிணைந்த வழியை வழங்குகிறது.

## கற்றல் குறிக்கோள்கள்

இந்த பாடத்தின் முடிவில், நீங்கள்:

- C#, Java, Python, TypeScript மற்றும் Rust இல் MCP மேம்பாட்டு சூழல்களை அமைக்க முடியும்
- தனிப்பயன் அம்சங்களுடன் அடிப்படை MCP சர்வர்களை உருவாக்கி வெளியிட முடியும் (வளங்கள், தூண்டுதல்கள் மற்றும் கருவிகள்)
- MCP சர்வர்களுடன் இணைக்கும் ஹோஸ்ட் பயன்பாடுகளை உருவாக்க முடியும்
- MCP செயல்பாடுகளை சோதித்து பிழைத்திருத்தம் செய்ய முடியும்

## உங்கள் MCP சூழலை அமைத்தல்

MCP உடன் பணியாற்றத் தொடங்குவதற்கு முன், உங்கள் மேம்பாட்டு சூழலை தயார் செய்தல் மற்றும் அடிப்படை பணிச் செயல்முறையை புரிந்துகொள்வது முக்கியம். இந்த பகுதி MCP உடன் மென்மையான துவக்கத்திற்கான ஆரம்ப அமைப்பு படிகளை வழிநடத்தும்.

### முன் தேவைகள்

MCP மேம்பாட்டில் இறங்குவதற்கு முன், நீங்கள் கொண்டிருக்க வேண்டும்:

- **மேம்பாட்டு சூழல்**: உங்கள் தேர்ந்த மொழிக்கான (C#, Java, Python, TypeScript, அல்லது Rust)
- **IDE/எடிட்டர்**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm அல்லது எந்தவொரு நவீன குறியீட்டு எடிட்டரும்
- **பேக்கேஜ் மேலாளர்கள்**: NuGet, Maven/Gradle, pip, npm/yarn, அல்லது Cargo
- **API விசைகள்**: உங்கள் ஹோஸ்ட் பயன்பாடுகளில் பயன்படுத்த திட்டமிட்ட எந்த AI சேவைகளுக்குமான

## அடிப்படை MCP சர்வர் அமைப்பு

ஒரு MCP சர்வர் பொதுவாக கொண்டிருக்கும்:

- **சர்வர் கட்டமைப்பு**: போர்ட், அங்கீகாரம் மற்றும் பிற அமைப்புகளை அமைத்தல்
- **வளங்கள்**: LLM களுக்கு கிடைக்கும் தரவு மற்றும் சூழல்
- **கருவிகள்**: மாதிரிகள் அழைக்கக்கூடிய செயல்பாடுகள்
- **தூண்டுதல்கள்**: உரையை உருவாக்க அல்லது கட்டமைக்க மாதிரிகள்

TypeScript இல் ஒரு எளிய எடுத்துக்காட்டு இங்கே:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ஒரு MCP சேவையகத்தை உருவாக்கவும்
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// ஒரு கூட்டல் கருவியைச் சேர்க்கவும்
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ஒரு இயக்கக்கூடிய வரவேற்பு வளத்தைச் சேர்க்கவும்
server.resource(
  "file",
  // 'list' அளவுரு வளம் கிடைக்கும் கோப்புகளை எவ்வாறு பட்டியலிடுகிறது என்பதை கட்டுப்படுத்துகிறது. இதை undefined ஆக அமைத்தால் இந்த வளத்திற்கான பட்டியலிடல் முடக்கப்படும்.
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => ({
    contents: [{
      uri: uri.href,
      text: `File, ${path}!`
    }]
  })
);

// கோப்பு உள்ளடக்கங்களை வாசிக்கும் ஒரு கோப்பு வளத்தைச் சேர்க்கவும்
server.resource(
  "file",
  new ResourceTemplate("file://{path}", { list: undefined }),
  async (uri, { path }) => {
    let text;
    try {
      text = await fs.readFile(path, "utf8");
    } catch (err) {
      text = `Error reading file: ${err.message}`;
    }
    return {
      contents: [{
        uri: uri.href,
        text
      }]
    };
  }
);

server.prompt(
  "review-code",
  { code: z.string() },
  ({ code }) => ({
    messages: [{
      role: "user",
      content: {
        type: "text",
        text: `Please review this code:\n\n${code}`
      }
    }]
  })
);

// stdin இல் இருந்து செய்திகளை பெறத் தொடங்கி stdout இல் செய்திகளை அனுப்பவும்
const transport = new StdioServerTransport();
await server.connect(transport);
```

மேலே உள்ள குறியீட்டில் நாம்:

- MCP TypeScript SDK இலிருந்து தேவையான வகுப்புகளை இறக்குமதி செய்தோம்.
- புதிய MCP சர்வர் உதாரணத்தை உருவாக்கி கட்டமைத்தோம்.
- ஒரு தனிப்பயன் கருவி (`calculator`) ஐ ஹேண்ட்லர் செயல்பாட்டுடன் பதிவு செய்தோம்.
- வரும் MCP கோரிக்கைகளை கேட்க சர்வரை துவக்கியோம்.

## சோதனை மற்றும் பிழைத்திருத்தம்

உங்கள் MCP சர்வரை சோதிக்கத் தொடங்குவதற்கு முன், கிடைக்கும் கருவிகள் மற்றும் சிறந்த பிழைத்திருத்த நடைமுறைகளை புரிந்துகொள்வது முக்கியம். பயனுள்ள சோதனை உங்கள் சர்வர் எதிர்பார்த்தபடி செயல்படுவதை உறுதி செய்யும் மற்றும் பிரச்சனைகளை விரைவாக கண்டறிந்து தீர்க்க உதவும். கீழ்காணும் பகுதி உங்கள் MCP செயல்பாட்டை சரிபார்க்க பரிந்துரைக்கப்படும் அணுகுமுறைகளை விளக்குகிறது.

MCP உங்கள் சர்வர்களை சோதிக்க மற்றும் பிழைத்திருத்த உதவும் கருவிகளை வழங்குகிறது:

- **Inspector கருவி**, இந்த காட்சி இடைமுகம் உங்கள் சர்வருடன் இணைந்து உங்கள் கருவிகள், தூண்டுதல்கள் மற்றும் வளங்களை சோதிக்க அனுமதிக்கும்.
- **curl**, நீங்கள் curl போன்ற கட்டளை வரி கருவி அல்லது HTTP கட்டளைகளை உருவாக்கி இயக்கக்கூடிய பிற கிளையண்டுகளைப் பயன்படுத்தி உங்கள் சர்வருடன் இணைக்கலாம்.

### MCP Inspector பயன்படுத்துதல்

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) என்பது காட்சி சோதனை கருவி ஆகும், இது உங்களுக்கு உதவுகிறது:

1. **சர்வர் திறன்களை கண்டறிதல்**: கிடைக்கும் வளங்கள், கருவிகள் மற்றும் தூண்டுதல்களை தானாக கண்டறிதல்
2. **கருவி செயல்பாட்டை சோதனை செய்தல்**: வெவ்வேறு அளவுருக்களை முயற்சி செய்து நேரடி பதில்களை காண்பது
3. **சர்வர் மெட்டாடேட்டாவை பார்வையிடுதல்**: சர்வர் தகவல், திட்டங்கள் மற்றும் கட்டமைப்புகளை ஆய்வு செய்தல்

```bash
# உதாரணம் TypeScript, MCP இன்ஸ்பெக்டரை நிறுவுதல் மற்றும் இயக்குதல்
npx @modelcontextprotocol/inspector node build/index.js
```

மேலே உள்ள கட்டளைகளை இயக்கும் போது, MCP Inspector உங்கள் உலாவியில் உள்ளூர் வலை இடைமுகத்தை துவக்கும். நீங்கள் பதிவு செய்த MCP சர்வர்கள், அவற்றின் கிடைக்கும் கருவிகள், வளங்கள் மற்றும் தூண்டுதல்கள் காட்டப்படும் ஒரு டாஷ்போர்டை காண்பீர்கள். இந்த இடைமுகம் கருவி செயல்பாட்டை இடைமுகமாக சோதிக்க, சர்வர் மெட்டாடேட்டாவை ஆய்வு செய்ய மற்றும் நேரடி பதில்களை காண உதவுகிறது, இது உங்கள் MCP சர்வர் செயல்பாடுகளை சரிபார்க்கவும் பிழைத்திருத்தவும் எளிதாக்குகிறது.

இதோ அது எப்படி தோன்றும் என்பதற்கான ஒரு ஸ்கிரீன்ஷாட்:

![MCP Inspector server connection](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.ta.png)

## பொதுவான அமைப்பு பிரச்சனைகள் மற்றும் தீர்வுகள்

| பிரச்சனை | சாத்தியமான தீர்வு |
|-------|-------------------|
| இணைப்பு மறுக்கப்பட்டது | சர்வர் இயங்குகிறதா மற்றும் போர்ட் சரியானதா என சரிபார்க்கவும் |
| கருவி செயல்பாட்டு பிழைகள் | அளவுரு சரிபார்ப்பு மற்றும் பிழை கையாளுதலை பரிசீலிக்கவும் |
| அங்கீகாரம் தோல்விகள் | API விசைகள் மற்றும் அனுமதிகளை சரிபார்க்கவும் |
| திட்டம் சரிபார்ப்பு பிழைகள் | அளவுருக்கள் வரையறுக்கப்பட்ட திட்டத்துடன் பொருந்துகிறதா என உறுதி செய்யவும் |
| சர்வர் துவங்கவில்லை | போர்ட் மோதல்கள் அல்லது காணாமல் போன சார்புகளை சரிபார்க்கவும் |
| CORS பிழைகள் | குறுக்கு-மூலம் கோரிக்கைகளுக்கான சரியான CORS தலைப்புகளை அமைக்கவும் |
| அங்கீகாரம் பிரச்சனைகள் | டோக்கன் செல்லுபடியாகும் மற்றும் அனுமதிகள் சரிபார்க்கவும் |

## உள்ளூர் மேம்பாடு

உள்ளூர் மேம்பாடு மற்றும் சோதனைக்காக, நீங்கள் உங்கள் கணினியில் நேரடியாக MCP சர்வர்களை இயக்கலாம்:

1. **சர்வர் செயல்முறையை துவக்கவும்**: உங்கள் MCP சர்வர் பயன்பாட்டை இயக்கவும்
2. **பிணைய அமைப்பை கட்டமைக்கவும்**: சர்வர் எதிர்பார்க்கப்படும் போர்டில் அணுகக்கூடியதாக இருக்க வேண்டும்
3. **கிளையண்டுகளை இணைக்கவும்**: `http://localhost:3000` போன்ற உள்ளூர் இணைப்பு URL களை பயன்படுத்தவும்

```bash
# உதாரணம்: TypeScript MCP சர்வரை உள்ளூர் முறையில் இயக்குதல்
npm run start
# சர்வர் http://localhost:3000 இல் இயங்குகிறது
```

## உங்கள் முதல் MCP சர்வரை உருவாக்குதல்

நாம் முன்பு [முக்கிய கருத்துக்களை](/01-CoreConcepts/README.md) கற்றுக்கொண்டோம், இப்போது அந்த அறிவை செயல்படுத்த நேரம்.

### சர்வர் என்ன செய்ய முடியும்

குறியீடு எழுதத் தொடங்குவதற்கு முன், சர்வர் என்ன செய்ய முடியும் என்பதை நினைவூட்டிக் கொள்வோம்:

ஒரு MCP சர்வர் உதாரணமாக:

- உள்ளூர் கோப்புகள் மற்றும் தரவுத்தளங்களை அணுகலாம்
- தொலை API களுடன் இணைக்கலாம்
- கணக்கீடுகளை செய்யலாம்
- பிற கருவிகள் மற்றும் சேவைகளுடன் ஒருங்கிணைக்கலாம்
- தொடர்புக்கு பயனர் இடைமுகத்தை வழங்கலாம்

சரி, இப்போது நாம் என்ன செய்ய முடியும் என்பதை அறிந்தோம், குறியீடு எழுதத் தொடங்குவோம்.

## பயிற்சி: சர்வர் உருவாக்குதல்

ஒரு சர்வரை உருவாக்க, நீங்கள் பின்வரும் படிகளை பின்பற்ற வேண்டும்:

- MCP SDK ஐ நிறுவவும்.
- ஒரு திட்டத்தை உருவாக்கி திட்ட அமைப்பை அமைக்கவும்.
- சர்வர் குறியீட்டை எழுதவும்.
- சர்வரை சோதிக்கவும்.

### -1- திட்டம் உருவாக்குதல்

#### TypeScript

```sh
# திட்ட அடைவை உருவாக்கி npm திட்டத்தை துவங்கவும்
mkdir calculator-server
cd calculator-server
npm init -y
```

#### Python

```sh
# திட்ட அடைவை உருவாக்கவும்
mkdir calculator-server
cd calculator-server
# Visual Studio Code இல் கோப்புறையை திறக்கவும் - நீங்கள் வேறு IDE பயன்படுத்தினால் இதை தவிர்க்கவும்
code .
```

#### .NET

```sh
dotnet new console -n McpCalculatorServer
cd McpCalculatorServer
```

#### Java

Java க்கான Spring Boot திட்டத்தை உருவாக்கவும்:

```bash
curl https://start.spring.io/starter.zip \
  -d dependencies=web \
  -d javaVersion=21 \
  -d type=maven-project \
  -d groupId=com.example \
  -d artifactId=calculator-server \
  -d name=McpServer \
  -d packageName=com.microsoft.mcp.sample.server \
  -o calculator-server.zip
```

ஜிப் கோப்பை வெளியேற்றவும்:

```bash
unzip calculator-server.zip -d calculator-server
cd calculator-server
# விருப்பமாக பயன்படுத்தப்படாத சோதனையை அகற்றவும்
rm -rf src/test/java
```

*pom.xml* கோப்பில் பின்வரும் முழுமையான கட்டமைப்பை சேர்க்கவும்:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <!-- Spring Boot parent for dependency management -->
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.5.0</version>
        <relativePath />
    </parent>

    <!-- Project coordinates -->
    <groupId>com.example</groupId>
    <artifactId>calculator-server</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>Calculator Server</name>
    <description>Basic calculator MCP service for beginners</description>

    <!-- Properties -->
    <properties>
        <java.version>21</java.version>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
    </properties>

    <!-- Spring AI BOM for version management -->
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.ai</groupId>
                <artifactId>spring-ai-bom</artifactId>
                <version>1.0.0-SNAPSHOT</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <!-- Dependencies -->
    <dependencies>
        <dependency>
            <groupId>org.springframework.ai</groupId>
            <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
        <dependency>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-starter-test</artifactId>
         <scope>test</scope>
      </dependency>
    </dependencies>

    <!-- Build configuration -->
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <configuration>
                    <release>21</release>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <!-- Repositories for Spring AI snapshots -->
    <repositories>
        <repository>
            <id>spring-milestones</id>
            <name>Spring Milestones</name>
            <url>https://repo.spring.io/milestone</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
        <repository>
            <id>spring-snapshots</id>
            <name>Spring Snapshots</name>
            <url>https://repo.spring.io/snapshot</url>
            <releases>
                <enabled>false</enabled>
            </releases>
        </repository>
    </repositories>
</project>
```

#### Rust

```sh
mkdir calculator-server
cd calculator-server
cargo init
```

### -2- சார்புகளை சேர்க்கவும்

திட்டம் உருவாக்கப்பட்ட பிறகு, அடுத்ததாக சார்புகளை சேர்ப்போம்:

#### TypeScript

```sh
# ஏற்கனவே நிறுவப்படவில்லை என்றால், TypeScript ஐ உலகளாவியமாக நிறுவவும்
npm install typescript -g

# MCP SDK மற்றும் ஸ்கீமா சரிபார்ப்புக்காக Zod ஐ நிறுவவும்
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript
```

#### Python

```sh
# ஒரு மெய்நிகர் சூழலை உருவாக்கி சார்புகளை நிறுவுக
python -m venv venv
venv\Scripts\activate
pip install "mcp[cli]"
```

#### Java

```bash
cd calculator-server
./mvnw clean install -DskipTests
```

#### Rust

```sh
cargo add rmcp --features server,transport-io
cargo add serde
cargo add tokio --features rt-multi-thread
```

### -3- திட்ட கோப்புகளை உருவாக்குதல்

#### TypeScript

*package.json* கோப்பை திறந்து, சர்வரை கட்டி இயக்க நீங்கள் பின்வரும் உள்ளடக்கத்துடன் மாற்றவும்:

```json
{
  "name": "calculator-server",
  "version": "1.0.0",
  "main": "index.js",
  "type": "module",
  "scripts": {
    "build": "tsc",
    "start": "npm run build && node ./build/index.js",
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "A simple calculator server using Model Context Protocol",
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.16.0",
    "zod": "^3.25.76"
  },
  "devDependencies": {
    "@types/node": "^24.0.14",
    "typescript": "^5.8.3"
  }
}
```

*tsconfig.json* கோப்பை பின்வரும் உள்ளடக்கத்துடன் உருவாக்கவும்:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "Node16",
    "moduleResolution": "Node16",
    "outDir": "./build",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```

உங்கள் மூலக் குறியீட்டுக்கான அடைவை உருவாக்கவும்:

```sh
mkdir src
touch src/index.ts
```

#### Python

*server.py* என்ற கோப்பை உருவாக்கவும்

```sh
touch server.py
```

#### .NET

தேவையான NuGet பேக்கேஜ்களை நிறுவவும்:

```sh
dotnet add package ModelContextProtocol --prerelease
dotnet add package Microsoft.Extensions.Hosting
```

#### Java

Java Spring Boot திட்டங்களுக்கு, திட்ட அமைப்பு தானாக உருவாக்கப்படும்.

#### Rust

Rust இல், `cargo init` இயக்கும் போது *src/main.rs* கோப்பு இயல்பாக உருவாக்கப்படும். கோப்பை திறந்து இயல்புநிலை குறியீட்டை நீக்கவும்.

### -4- சர்வர் குறியீட்டை உருவாக்குதல்

#### TypeScript

*index.ts* என்ற கோப்பை உருவாக்கி பின்வரும் குறியீட்டை சேர்க்கவும்:

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
 
// ஒரு MCP சேவையகத்தை உருவாக்கவும்
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});
```

இப்போது உங்களிடம் ஒரு சர்வர் உள்ளது, ஆனால் அது அதிகம் செய்யவில்லை, அதை சரி செய்யலாம்.

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# ஒரு MCP சர்வரை உருவாக்கவும்
mcp = FastMCP("Demo")
```

#### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

// add features
```

#### Java

Java க்கான முக்கிய சர்வர் கூறுகளை உருவாக்கவும். முதலில், முக்கிய பயன்பாட்டு வகுப்பை மாற்றவும்:

*src/main/java/com/microsoft/mcp/sample/server/McpServerApplication.java*:

```java
package com.microsoft.mcp.sample.server;

import org.springframework.ai.tool.ToolCallbackProvider;
import org.springframework.ai.tool.method.MethodToolCallbackProvider;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import com.microsoft.mcp.sample.server.service.CalculatorService;

@SpringBootApplication
public class McpServerApplication {

    public static void main(String[] args) {
        SpringApplication.run(McpServerApplication.class, args);
    }
    
    @Bean
    public ToolCallbackProvider calculatorTools(CalculatorService calculator) {
        return MethodToolCallbackProvider.builder().toolObjects(calculator).build();
    }
}
```

கணக்கிடும் சேவையை உருவாக்கவும் *src/main/java/com/microsoft/mcp/sample/server/service/CalculatorService.java*:

```java
package com.microsoft.mcp.sample.server.service;

import org.springframework.ai.tool.annotation.Tool;
import org.springframework.stereotype.Service;

/**
 * Service for basic calculator operations.
 * This service provides simple calculator functionality through MCP.
 */
@Service
public class CalculatorService {

    /**
     * Add two numbers
     * @param a The first number
     * @param b The second number
     * @return The sum of the two numbers
     */
    @Tool(description = "Add two numbers together")
    public String add(double a, double b) {
        double result = a + b;
        return formatResult(a, "+", b, result);
    }

    /**
     * Subtract one number from another
     * @param a The number to subtract from
     * @param b The number to subtract
     * @return The result of the subtraction
     */
    @Tool(description = "Subtract the second number from the first number")
    public String subtract(double a, double b) {
        double result = a - b;
        return formatResult(a, "-", b, result);
    }

    /**
     * Multiply two numbers
     * @param a The first number
     * @param b The second number
     * @return The product of the two numbers
     */
    @Tool(description = "Multiply two numbers together")
    public String multiply(double a, double b) {
        double result = a * b;
        return formatResult(a, "*", b, result);
    }

    /**
     * Divide one number by another
     * @param a The numerator
     * @param b The denominator
     * @return The result of the division
     */
    @Tool(description = "Divide the first number by the second number")
    public String divide(double a, double b) {
        if (b == 0) {
            return "Error: Cannot divide by zero";
        }
        double result = a / b;
        return formatResult(a, "/", b, result);
    }

    /**
     * Calculate the power of a number
     * @param base The base number
     * @param exponent The exponent
     * @return The result of raising the base to the exponent
     */
    @Tool(description = "Calculate the power of a number (base raised to an exponent)")
    public String power(double base, double exponent) {
        double result = Math.pow(base, exponent);
        return formatResult(base, "^", exponent, result);
    }

    /**
     * Calculate the square root of a number
     * @param number The number to find the square root of
     * @return The square root of the number
     */
    @Tool(description = "Calculate the square root of a number")
    public String squareRoot(double number) {
        if (number < 0) {
            return "Error: Cannot calculate square root of a negative number";
        }
        double result = Math.sqrt(number);
        return String.format("√%.2f = %.2f", number, result);
    }

    /**
     * Calculate the modulus (remainder) of division
     * @param a The dividend
     * @param b The divisor
     * @return The remainder of the division
     */
    @Tool(description = "Calculate the remainder when one number is divided by another")
    public String modulus(double a, double b) {
        if (b == 0) {
            return "Error: Cannot divide by zero";
        }
        double result = a % b;
        return formatResult(a, "%", b, result);
    }

    /**
     * Calculate the absolute value of a number
     * @param number The number to find the absolute value of
     * @return The absolute value of the number
     */
    @Tool(description = "Calculate the absolute value of a number")
    public String absolute(double number) {
        double result = Math.abs(number);
        return String.format("|%.2f| = %.2f", number, result);
    }

    /**
     * Get help about available calculator operations
     * @return Information about available operations
     */
    @Tool(description = "Get help about available calculator operations")
    public String help() {
        return "Basic Calculator MCP Service\n\n" +
               "Available operations:\n" +
               "1. add(a, b) - Adds two numbers\n" +
               "2. subtract(a, b) - Subtracts the second number from the first\n" +
               "3. multiply(a, b) - Multiplies two numbers\n" +
               "4. divide(a, b) - Divides the first number by the second\n" +
               "5. power(base, exponent) - Raises a number to a power\n" +
               "6. squareRoot(number) - Calculates the square root\n" + 
               "7. modulus(a, b) - Calculates the remainder of division\n" +
               "8. absolute(number) - Calculates the absolute value\n\n" +
               "Example usage: add(5, 3) will return 5 + 3 = 8";
    }

    /**
     * Format the result of a calculation
     */
    private String formatResult(double a, String operator, double b, double result) {
        return String.format("%.2f %s %.2f = %.2f", a, operator, b, result);
    }
}
```

**உற்பத்தி தயாரான சேவைக்கான விருப்ப கூறுகள்:**

துவக்க கட்டமைப்பை உருவாக்கவும் *src/main/java/com/microsoft/mcp/sample/server/config/StartupConfig.java*:

```java
package com.microsoft.mcp.sample.server.config;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class StartupConfig {
    
    @Bean
    public CommandLineRunner startupInfo() {
        return args -> {
            System.out.println("\n" + "=".repeat(60));
            System.out.println("Calculator MCP Server is starting...");
            System.out.println("SSE endpoint: http://localhost:8080/sse");
            System.out.println("Health check: http://localhost:8080/actuator/health");
            System.out.println("=".repeat(60) + "\n");
        };
    }
}
```

ஆரோக்கிய கட்டுப்படுத்தியை உருவாக்கவும் *src/main/java/com/microsoft/mcp/sample/server/controller/HealthController.java*:

```java
package com.microsoft.mcp.sample.server.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Map;

@RestController
public class HealthController {
    
    @GetMapping("/health")
    public ResponseEntity<Map<String, Object>> healthCheck() {
        Map<String, Object> response = new HashMap<>();
        response.put("status", "UP");
        response.put("timestamp", LocalDateTime.now().toString());
        response.put("service", "Calculator MCP Server");
        return ResponseEntity.ok(response);
    }
}
```

விரிவான பிழை கையாளியை உருவாக்கவும் *src/main/java/com/microsoft/mcp/sample/server/exception/GlobalExceptionHandler.java*:

```java
package com.microsoft.mcp.sample.server.exception;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(IllegalArgumentException.class)
    public ResponseEntity<ErrorResponse> handleIllegalArgumentException(IllegalArgumentException ex) {
        ErrorResponse error = new ErrorResponse(
            "Invalid_Input", 
            "Invalid input parameter: " + ex.getMessage());
        return new ResponseEntity<>(error, HttpStatus.BAD_REQUEST);
    }

    public static class ErrorResponse {
        private String code;
        private String message;

        public ErrorResponse(String code, String message) {
            this.code = code;
            this.message = message;
        }

        // பெறுநர்கள்
        public String getCode() { return code; }
        public String getMessage() { return message; }
    }
}
```

தனிப்பயன் பேனரை உருவாக்கவும் *src/main/resources/banner.txt*:

```text
_____      _            _       _             
 / ____|    | |          | |     | |            
| |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| |___| (_| | | (__| |_| | | (_| | || (_) | |   
 \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                
Calculator MCP Server v1.0
Spring Boot MCP Application
```

</details>

#### Rust

*src/main.rs* கோப்பின் மேல் பாகத்தில் பின்வரும் குறியீட்டை சேர்க்கவும். இது உங்கள் MCP சர்வருக்கான தேவையான நூலகங்கள் மற்றும் தொகுதிகளை இறக்குமதி செய்கிறது.

```rust
use rmcp::{
    handler::server::{router::tool::ToolRouter, tool::Parameters},
    model::{ServerCapabilities, ServerInfo},
    schemars, tool, tool_handler, tool_router,
    transport::stdio,
    ServerHandler, ServiceExt,
};
use std::error::Error;
```

கணக்கிடும் சர்வர் எளிமையானது, இரண்டு எண்களை கூட்டும். கணக்கிடும் கோரிக்கையை பிரதிநிதித்துவப்படுத்த ஒரு struct உருவாக்குவோம்.

```rust
#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}
```

அடுத்து, கணக்கிடும் சர்வரை பிரதிநிதித்துவப்படுத்த ஒரு struct உருவாக்கவும். இந்த struct கருவி ரவுடரை வைத்திருக்கும், இது கருவிகளை பதிவு செய்ய பயன்படுத்தப்படுகிறது.

```rust
#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}
```

இப்போது, `Calculator` struct ஐ செயல்படுத்தி சர்வரின் புதிய உதாரணத்தை உருவாக்கி சர்வர் ஹேண்ட்லரை செயல்படுத்தலாம்.

```rust
#[tool_router]
impl Calculator {
    pub fn new() -> Self {
        Self {
            tool_router: Self::tool_router(),
        }
    }
}

#[tool_handler]
impl ServerHandler for Calculator {
    fn get_info(&self) -> ServerInfo {
        ServerInfo {
            instructions: Some("A simple calculator tool".into()),
            capabilities: ServerCapabilities::builder().enable_tools().build(),
            ..Default::default()
        }
    }
}
```

இறுதியாக, சர்வரை துவக்க முக்கிய செயல்பாட்டை செயல்படுத்த வேண்டும். இந்த செயல்பாடு `Calculator` struct உதாரணத்தை உருவாக்கி அதை நிலையான உள்ளீடு/வெளியீடு வழியாக சேவை செய்யும்.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

சர்வர் இப்போது தன்னுடைய அடிப்படை தகவலை வழங்க அமைக்கப்பட்டுள்ளது. அடுத்து, கூட்டல் செய்ய ஒரு கருவியை சேர்ப்போம்.

### -5- கருவி மற்றும் வளம் சேர்த்தல்

பின்வரும் குறியீட்டை சேர்த்து ஒரு கருவி மற்றும் வளத்தை சேர்க்கவும்:

#### TypeScript

```typescript
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

server.resource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);
```

உங்கள் கருவி `a` மற்றும் `b` என்ற அளவுருக்களை எடுத்துக் கொண்டு பின்வரும் வடிவில் பதிலை உருவாக்கும் செயல்பாட்டை இயக்குகிறது:

```typescript
{
  contents: [{
    type: "text", content: "some content"
  }]
}
```

உங்கள் வளம் "greeting" என்ற சரம் மூலம் அணுகப்படுகிறது, `name` என்ற அளவுருவை எடுத்துக் கொண்டு கருவி போலவே பதிலை உருவாக்குகிறது:

```typescript
{
  uri: "<href>",
  text: "a text"
}
```

#### Python

```python
# ஒரு கூட்டல் கருவியைச் சேர்க்கவும்
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ஒரு இயக்கமுள்ள வரவேற்பு வளத்தைச் சேர்க்கவும்
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

மேலே உள்ள குறியீட்டில் நாம்:

- `add` என்ற கருவியை வரையறுத்தோம், இது `a` மற்றும் `b` என்ற இரண்டு முழு எண்கள் அளவுருக்களை எடுத்துக் கொள்கிறது.
- `greeting` என்ற வளத்தை உருவாக்கினோம், இது `name` என்ற அளவுருவை எடுத்துக் கொள்கிறது.

#### .NET

இதை உங்கள் Program.cs கோப்பில் சேர்க்கவும்:

```csharp
[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

கருவிகள் முன்பு படியில் உருவாக்கப்பட்டுள்ளன.

#### Rust

`impl Calculator` தொகுதியில் புதிய கருவியை சேர்க்கவும்:

```rust
#[tool(description = "Adds a and b")]
async fn add(
    &self,
    Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
) -> String {
    (a + b).to_string()
}
```

### -6- இறுதி குறியீடு

சர்வர் துவங்குவதற்கு தேவையான கடைசி குறியீட்டை சேர்ப்போம்:

#### TypeScript

```typescript
// stdin இல் இருந்து செய்திகளை பெறத் தொடங்கி stdout இல் செய்திகளை அனுப்புதல்
const transport = new StdioServerTransport();
await server.connect(transport);
```

முழு குறியீடு இங்கே:

```typescript
// index.ts
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ஒரு MCP சேவையகத்தை உருவாக்கவும்
const server = new McpServer({
  name: "Calculator MCP Server",
  version: "1.0.0"
});

// ஒரு கூட்டல் கருவியைச் சேர்க்கவும்
server.tool(
  "add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ஒரு இயக்கக்கூடிய வரவேற்பு வளத்தைச் சேர்க்கவும்
server.resource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);

// stdin இல் இருந்து செய்திகளை பெறத் தொடங்கி stdout இல் செய்திகளை அனுப்பவும்
const transport = new StdioServerTransport();
server.connect(transport);
```

#### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# ஒரு MCP சேவையகத்தை உருவாக்கவும்
mcp = FastMCP("Demo")


# ஒரு கூட்டல் கருவியைச் சேர்க்கவும்
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ஒரு இயக்கக்கூடிய வரவேற்பு வளத்தைச் சேர்க்கவும்
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# முக்கிய செயலாக்க தொகுதி - சேவையகத்தை இயக்க இது அவசியம்
if __name__ == "__main__":
    mcp.run()
```

#### .NET

பின்வரும் உள்ளடக்கத்துடன் Program.cs கோப்பை உருவாக்கவும்:

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

#### Java

உங்கள் முழுமையான முக்கிய பயன்பாட்டு வகுப்பு இதுபோல் இருக்க வேண்டும்:

```java
// McpServerApplication.java
package com.microsoft.mcp.sample.server;

import org.springframework.ai.tool.ToolCallbackProvider;
import org.springframework.ai.tool.method.MethodToolCallbackProvider;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import com.microsoft.mcp.sample.server.service.CalculatorService;

@SpringBootApplication
public class McpServerApplication {

    public static void main(String[] args) {
        SpringApplication.run(McpServerApplication.class, args);
    }
    
    @Bean
    public ToolCallbackProvider calculatorTools(CalculatorService calculator) {
        return MethodToolCallbackProvider.builder().toolObjects(calculator).build();
    }
}
```

#### Rust

Rust சர்வருக்கான இறுதி குறியீடு இதுபோல் இருக்க வேண்டும்:

```rust
use rmcp::{
    ServerHandler, ServiceExt,
    handler::server::{router::tool::ToolRouter, tool::Parameters},
    model::{ServerCapabilities, ServerInfo},
    schemars, tool, tool_handler, tool_router,
    transport::stdio,
};
use std::error::Error;

#[derive(Debug, serde::Deserialize, schemars::JsonSchema)]
pub struct CalculatorRequest {
    pub a: f64,
    pub b: f64,
}

#[derive(Debug, Clone)]
pub struct Calculator {
    tool_router: ToolRouter<Self>,
}

#[tool_router]
impl Calculator {
    pub fn new() -> Self {
        Self {
            tool_router: Self::tool_router(),
        }
    }
    
    #[tool(description = "Adds a and b")]
    async fn add(
        &self,
        Parameters(CalculatorRequest { a, b }): Parameters<CalculatorRequest>,
    ) -> String {
        (a + b).to_string()
    }
}

#[tool_handler]
impl ServerHandler for Calculator {
    fn get_info(&self) -> ServerInfo {
        ServerInfo {
            instructions: Some("A simple calculator tool".into()),
            capabilities: ServerCapabilities::builder().enable_tools().build(),
            ..Default::default()
        }
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let service = Calculator::new().serve(stdio()).await?;
    service.waiting().await?;
    Ok(())
}
```

### -7- சர்வரை சோதனை செய்தல்

பின்வரும் கட்டளையுடன் சர்வரை துவக்கவும்:

#### TypeScript

```sh
npm run build
```

#### Python

```sh
mcp run server.py
```

> MCP Inspector ஐ பயன்படுத்த, `mcp dev server.py` ஐ பயன்படுத்தவும், இது தானாக Inspector ஐ துவக்கி தேவையான பிராக்சி அமர்வு டோக்கனை வழங்கும். `mcp run server.py` பயன்படுத்தினால், நீங்கள் கையேடு முறையில் Inspector ஐ துவக்கி இணைப்பை அமைக்க வேண்டும்.

#### .NET

உங்கள் திட்ட அடைவில் இருப்பதை உறுதி செய்யவும்:

```sh
cd McpCalculatorServer
dotnet run
```

#### Java

```bash
./mvnw clean install -DskipTests
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### Rust

சர்வரை வடிவமைத்து இயக்க பின்வரும் கட்டளைகளை இயக்கவும்:

```sh
cargo fmt
cargo run
```

### -8- Inspector மூலம் இயக்குதல்

Inspector என்பது ஒரு சிறந்த கருவி, இது உங்கள் சர்வரை துவக்கி அதுடன் தொடர்பு கொண்டு அது வேலை செய்கிறதா என்று சோதிக்க உதவுகிறது. அதை துவக்குவோம்:

> [!NOTE]
> "command" புலத்தில் அது வேறுபடலாம், ஏனெனில் அது உங்கள் குறிப்பிட்ட ரன்டைம் உடன் சர்வரை இயக்கும் கட்டளையை கொண்டிருக்கும்.

#### TypeScript

```sh
npx @modelcontextprotocol/inspector node build/index.js
```

அல்லது உங்கள் *package.json* இல் இதைப் போல சேர்க்கவும்: `"inspector": "npx @modelcontextprotocol/inspector node build/index.js"` பின்னர் `npm run inspector`
`Command` புலத்தில் `python` மற்றும் `Arguments` ஆக `server.py` அமைக்க வேண்டும் என்பதை உறுதிப்படுத்திக் கொள்ளுங்கள். இது ஸ்கிரிப்ட் சரியாக இயங்குவதை உறுதி செய்யும்.

#### .NET

உங்கள் திட்ட அடைவில் இருப்பதை உறுதிப்படுத்திக் கொள்ளுங்கள்:

```sh
cd McpCalculatorServer
npx @modelcontextprotocol/inspector dotnet run
```

#### Java

உங்கள் கால்குலேட்டர் சர்வர் இயங்குவதை உறுதிப்படுத்துங்கள்
பின்னர் இன்ஸ்பெக்டரை இயக்கவும்:

```cmd
npx @modelcontextprotocol/inspector
```

இன்ஸ்பெக்டர் வலை இடைமுகத்தில்:

1. "SSE" என்பதை போக்குவரத்து வகையாக தேர்ந்தெடுக்கவும்
2. URL ஐ இதுவரை அமைக்கவும்: `http://localhost:8080/sse`
3. "Connect" கிளிக் செய்யவும்

![Connect](../../../../translated_images/tool.163d33e3ee307e209ef146d8f85060d2f7e83e9f59b3b1699a77204ae0454ad2.ta.png)

**நீங்கள் இப்போது சர்வருடன் இணைக்கப்பட்டுள்ளீர்கள்**
**Java சர்வர் சோதனை பகுதி இப்போது முடிந்தது**

அடுத்த பகுதி சர்வருடன் தொடர்பு கொள்ளும் பற்றியது.

நீங்கள் பின்வரும் பயனர் இடைமுகத்தை காண வேண்டும்:

![Connect](../../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.ta.png)

1. Connect பொத்தானை தேர்ந்தெடுத்து சர்வருடன் இணைக்கவும்
  சர்வருடன் இணைந்தவுடன், பின்வரும் காண்பிக்கப்படும்:

  ![Connected](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.ta.png)

1. "Tools" மற்றும் "listTools" ஐ தேர்ந்தெடுக்கவும், "Add" தோன்றும், "Add" ஐ தேர்ந்தெடுத்து அளவுரு மதிப்புகளை நிரப்பவும்.

  பின்வரும் பதிலை நீங்கள் காண வேண்டும், அதாவது "add" கருவியிலிருந்து பெறப்பட்ட முடிவு:

  ![Result of running add](../../../../translated_images/ran-tool.a5a6ee878c1369ec1e379b81053395252a441799dbf23416c36ddf288faf8249.ta.png)

வாழ்த்துக்கள், நீங்கள் உங்கள் முதல் சர்வரை உருவாக்கி இயக்கியுள்ளீர்கள்!

#### Rust

MCP இன்ஸ்பெக்டர் CLI உடன் Rust சர்வரை இயக்க, பின்வரும் கட்டளையை பயன்படுத்தவும்:

```sh
npx @modelcontextprotocol/inspector cargo run --cli --method tools/call --tool-name add --tool-arg a=1 b=2
```

### அதிகாரப்பூர்வ SDKகள்

MCP பல மொழிகளுக்கான அதிகாரப்பூர்வ SDKகளை வழங்குகிறது:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoft உடன் இணைந்து பராமரிக்கப்படுகிறது
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI உடன் இணைந்து பராமரிக்கப்படுகிறது
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - அதிகாரப்பூர்வ TypeScript செயலாக்கம்
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - அதிகாரப்பூர்வ Python செயலாக்கம்
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - அதிகாரப்பூர்வ Kotlin செயலாக்கம்
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI உடன் இணைந்து பராமரிக்கப்படுகிறது
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - அதிகாரப்பூர்வ Rust செயலாக்கம்

## முக்கியக் குறிப்புகள்

- MCP மேம்பாட்டு சூழலை மொழி-சார்ந்த SDKகளுடன் எளிதாக அமைக்கலாம்
- MCP சர்வர்களை உருவாக்குவது தெளிவான திட்டங்களுடன் கருவிகளை உருவாக்கி பதிவு செய்வதைக் கொண்டுள்ளது
- சோதனை மற்றும் பிழைத்திருத்தம் நம்பகமான MCP செயலாக்கங்களுக்கு அவசியம்

## மாதிரிகள்

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## பணிகள்

உங்கள் விருப்பமான கருவியுடன் ஒரு எளிய MCP சர்வரை உருவாக்கவும்:

1. உங்கள் விருப்பமான மொழியில் கருவியை செயல்படுத்தவும் (.NET, Java, Python, TypeScript, அல்லது Rust).
2. உள்ளீட்டு அளவுருக்களையும் திருப்பி வழங்கும் மதிப்புகளையும் வரையறுக்கவும்.
3. சர்வர் எதிர்பார்த்தபடி இயங்குவதை உறுதிப்படுத்த இன்ஸ்பெக்டர் கருவியை இயக்கவும்.
4. பல்வேறு உள்ளீடுகளுடன் செயல்பாட்டை சோதிக்கவும்.

## தீர்வு

[Solution](./solution/README.md)

## கூடுதல் வளங்கள்

- [Azure இல் Model Context Protocol பயன்படுத்தி ஏஜென்ட்களை உருவாக்குதல்](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Azure Container Apps உடன் தொலை MCP (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP ஏஜென்ட்](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## அடுத்தது என்ன

அடுத்தது: [MCP கிளையண்ட்களுடன் தொடங்குதல்](../02-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**குறிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) மூலம் மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சித்தாலும், தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனிக்கவும். அசல் ஆவணம் அதன் சொந்த மொழியில் அதிகாரப்பூர்வ மூலமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பின் பயன்பாட்டால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பேற்கமாட்டோம்.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->