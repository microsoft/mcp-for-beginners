# Calculator LLM Client

O aplicație Java care demonstrează cum să folosești LangChain4j pentru a te conecta la un serviciu MCP (Model Context Protocol) calculator cu integrare GitHub Models.

## Cerințe preliminare

- Java 21 sau versiune superioară
- Maven 3.6+ (sau folosește Maven wrapper-ul inclus)
- Un cont GitHub cu acces la GitHub Models
- Un serviciu MCP calculator care rulează pe `http://localhost:8080`

## Obținerea token-ului GitHub

Această aplicație folosește GitHub Models, care necesită un token personal de acces GitHub. Urmează pașii de mai jos pentru a obține token-ul:

### 1. Accesează GitHub Models
1. Mergi la [GitHub Models](https://github.com/marketplace/models)
2. Autentifică-te cu contul tău GitHub
3. Solicită acces la GitHub Models dacă nu ai făcut-o deja

### 2. Creează un token personal de acces
1. Mergi la [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Apasă pe "Generate new token" → "Generate new token (classic)"
3. Dă token-ului un nume descriptiv (ex: "MCP Calculator Client")
4. Setează expirarea după cum dorești
5. Selectează următoarele permisiuni:
   - `repo` (dacă accesezi depozite private)
   - `user:email`
6. Apasă pe "Generate token"
7. **Important**: Copiază token-ul imediat - nu vei mai putea să-l vezi din nou!

### 3. Setează variabila de mediu

#### Pe Windows (Command Prompt):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Pe Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### Pe macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Configurare și instalare

1. **Clonează sau navighează în directorul proiectului**

2. **Instalează dependențele**:
   ```cmd
   mvnw clean install
   ```
   Sau dacă ai Maven instalat global:
   ```cmd
   mvn clean install
   ```

3. **Setează variabila de mediu** (vezi secțiunea „Obținerea token-ului GitHub” de mai sus)

4. **Pornește serviciul MCP Calculator**:
   Asigură-te că serviciul MCP calculator din capitolul 1 rulează pe `http://localhost:8080/sse`. Acesta trebuie să fie pornit înainte de a lansa clientul.

## Rularea aplicației

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Ce face aplicația

Aplicația demonstrează trei interacțiuni principale cu serviciul calculator:

1. **Adunare**: Calculează suma dintre 24.5 și 17.3
2. **Rădăcină pătrată**: Calculează rădăcina pătrată a lui 144
3. **Ajutor**: Afișează funcțiile disponibile ale calculatorului

## Rezultatul așteptat

La rulare cu succes, ar trebui să vezi un output similar cu:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Depanare

### Probleme comune

1. **"GITHUB_TOKEN environment variable not set"**
   - Asigură-te că ai setat variabila de mediu `GITHUB_TOKEN`
   - Repornește terminalul/command prompt-ul după setarea variabilei

2. **"Connection refused to localhost:8080"**
   - Verifică dacă serviciul MCP calculator rulează pe portul 8080
   - Verifică dacă alt serviciu nu folosește portul 8080

3. **"Authentication failed"**
   - Verifică dacă token-ul GitHub este valid și are permisiunile corecte
   - Asigură-te că ai acces la GitHub Models

4. **Erori la build cu Maven**
   - Verifică dacă folosești Java 21 sau o versiune superioară: `java -version`
   - Încearcă să cureți build-ul: `mvnw clean`

### Depanare avansată

Pentru a activa logarea de debug, adaugă următorul argument JVM la rulare:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Configurație

Aplicația este configurată să:
- Folosească GitHub Models cu modelul `gpt-4.1-nano`
- Se conecteze la serviciul MCP la `http://localhost:8080/sse`
- Folosească un timeout de 60 de secunde pentru cereri
- Activeze logarea cererilor și răspunsurilor pentru depanare

## Dependențe

Dependențele principale folosite în acest proiect:
- **LangChain4j**: pentru integrare AI și gestionarea uneltelor
- **LangChain4j MCP**: pentru suport Model Context Protocol
- **LangChain4j GitHub Models**: pentru integrarea GitHub Models
- **Spring Boot**: pentru framework-ul aplicației și injecția de dependențe

## Licență

Acest proiect este licențiat sub Apache License 2.0 - vezi fișierul [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) pentru detalii.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.