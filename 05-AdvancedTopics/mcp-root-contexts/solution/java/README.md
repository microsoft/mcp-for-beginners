# Java Root Context Example

This example demonstrates how to implement MCP root contexts in a Java application for financial analysis scenarios.

## Prerequisites

- Java 21 or later
- Maven 3.8+ or Gradle 8+
- IDE (IntelliJ IDEA, Eclipse, or VS Code with Java extensions)

## Setup with Maven

1. **Create a new Maven project:**
   ```bash
   mvn archetype:generate -DgroupId=com.example.mcp \
     -DartifactId=root-context-example \
     -DarchetypeArtifactId=maven-archetype-quickstart \
     -DinteractiveMode=false
   cd root-context-example
   ```

2. **Update `pom.xml`:**
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <project xmlns="http://maven.apache.org/POM/4.0.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
            http://maven.apache.org/xsd/maven-4.0.0.xsd">
     <modelVersion>4.0.0</modelVersion>
     
     <groupId>com.example.mcp</groupId>
     <artifactId>root-context-example</artifactId>
     <version>1.0.0</version>
     <packaging>jar</packaging>
     
     <properties>
       <maven.compiler.source>21</maven.compiler.source>
       <maven.compiler.target>21</maven.compiler.target>
       <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
     </properties>
     
     <dependencies>
       <dependency>
         <groupId>com.mcp</groupId>
         <artifactId>mcp-client</artifactId>
         <version>1.0.0</version>
       </dependency>
     </dependencies>
     
     <build>
       <plugins>
         <plugin>
           <groupId>org.apache.maven.plugins</groupId>
           <artifactId>maven-compiler-plugin</artifactId>
           <version>3.11.0</version>
         </plugin>
       </plugins>
     </build>
   </project>
   ```

3. **Copy the example code:**
   - Place `FinancialAnalysisContext.java` in `src/main/java/com/example/mcp/contexts/`

## Setup with Gradle

1. **Create a new Gradle project:**
   ```bash
   gradle init --type java-application --dsl groovy
   ```

2. **Update `build.gradle`:**
   ```groovy
   plugins {
       id 'application'
   }
   
   repositories {
       mavenCentral()
   }
   
   dependencies {
       implementation 'com.mcp:mcp-client:1.0.0'
   }
   
   java {
       toolchain {
           languageVersion = JavaLanguageVersion.of(21)
       }
   }
   
   application {
       mainClass = 'com.example.mcp.contexts.FinancialAnalysisContext'
   }
   ```

## Configuration

Update the MCP server URL in the constructor:
```java
FinancialAnalysisContext example = new FinancialAnalysisContext("YOUR_MCP_SERVER_URL");
```

## Running the Example

### With Maven:
```bash
# Compile the project
mvn compile

# Run the application
mvn exec:java -Dexec.mainClass="com.example.mcp.contexts.FinancialAnalysisContext"
```

### With Gradle:
```bash
# Build the project
./gradlew build

# Run the application
./gradlew run
```

### With IDE:
- Open the project in your IDE
- Run the `main` method in `FinancialAnalysisContext.java`

## What the Example Demonstrates

- 📊 **Analysis Session Creation**: Setting up a context for financial analysis
- 📈 **Progressive Analysis**: Building insights through multiple questions
- 🔍 **Deep Dive Investigations**: Following up on discovered trends
- 📋 **Executive Summaries**: Synthesizing findings for leadership
- 🗄️ **Context Archival**: Properly preserving analysis results

## Expected Output

```
📊 Created financial analysis context: [context-id]
📈 Initial Analysis:
[AI analysis of Q1 trends and cost drivers]
🔍 Deep Dive Analysis:
[AI analysis of cloud infrastructure costs]
📋 Executive Summary:
[AI-generated executive summary with recommendations]

📊 Final Context Information:
├─ Created: [timestamp]
├─ Last Updated: [timestamp]
└─ Status: Analysis Complete

🗄️ Financial analysis context archived successfully
✅ Financial analysis demonstration completed!
```

## Key Features

- **Enterprise Java patterns**: Builder pattern, dependency injection ready
- **Exception handling**: Comprehensive error management
- **Business intelligence**: Financial analysis workflow
- **Metadata tracking**: Progressive context enrichment

## Project Structure

```
src/
├── main/
│   └── java/
│       └── com/
│           └── example/
│               └── mcp/
│                   └── contexts/
│                       └── FinancialAnalysisContext.java
└── test/
    └── java/
        └── com/
            └── example/
                └── mcp/
                    └── contexts/
                        └── FinancialAnalysisContextTest.java
```

## Next Steps

- Add unit tests with JUnit 5
- Implement Spring Boot integration
- Add logging with SLF4J and Logback
- Create REST API endpoints
- Integrate with existing enterprise systems