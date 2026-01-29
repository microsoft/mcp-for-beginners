# Kalkulaatori LLM klient

Java-rakendus, mis demonstreerib, kuidas kasutada LangChain4j, et ühendada MCP (Model Context Protocol) kalkulaatoriteenusega koos GitHub Models integratsiooniga.

## Eeltingimused

- Java 21 või uuem
- Maven 3.6+ (või kasutage kaasasolevat Maven wrapperit)
- GitHubi konto koos juurdepääsuga GitHub Modelsile
- MCP kalkulaatoriteenus, mis töötab aadressil `http://localhost:8080`

## GitHubi tokeni hankimine

See rakendus kasutab GitHub Modelsit, mis nõuab GitHubi isiklikku juurdepääsutokenit. Järgige neid samme, et saada oma token:

### 1. Juurdepääs GitHub Modelsile
1. Minge lehele [GitHub Models](https://github.com/marketplace/models)
2. Logige sisse oma GitHubi kontoga
3. Taotlege juurdepääsu GitHub Modelsile, kui te pole seda veel teinud

### 2. Looge isiklik juurdepääsutoken
1. Minge lehele [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Klõpsake "Generate new token" → "Generate new token (classic)"
3. Andke oma tokenile kirjeldav nimi (nt "MCP Calculator Client")
4. Määrake aegumistähtaeg vastavalt vajadusele
5. Valige järgmised õigused:
   - `repo` (kui pääsete ligi privaatsetele repositooriumidele)
   - `user:email`
6. Klõpsake "Generate token"
7. **Oluline**: Kopeerige token kohe - te ei saa seda hiljem uuesti näha!

### 3. Keskkonnamuutuja seadistamine

#### Windowsis (Command Prompt):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Windowsis (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### macOS/Linuxis:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Seadistamine ja paigaldamine

1. **Kloonige või liikuge projekti kataloogi**

2. **Paigaldage sõltuvused**:
   ```cmd
   mvnw clean install
   ```
   Või kui teil on Maven globaalselt paigaldatud:
   ```cmd
   mvn clean install
   ```

3. **Seadistage keskkonnamuutuja** (vt "GitHubi tokeni hankimine" sektsiooni eespool)

4. **Käivitage MCP kalkulaatoriteenus**:
   Veenduge, et teil on 1. peatüki MCP kalkulaatoriteenus käimas aadressil `http://localhost:8080/sse`. See peaks olema käimas enne kliendi käivitamist.

## Rakenduse käivitamine

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Mida rakendus teeb

Rakendus demonstreerib kolme peamist interaktsiooni kalkulaatoriteenusega:

1. **Liitmine**: Arvutab 24.5 ja 17.3 summa
2. **Ruutjuur**: Arvutab 144 ruutjuure
3. **Abi**: Kuvab saadaval olevad kalkulaatori funktsioonid

## Oodatav väljund

Eduka käivitamise korral peaksite nägema väljundit, mis on sarnane järgmisega:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Tõrkeotsing

### Levinud probleemid

1. **"GITHUB_TOKEN keskkonnamuutuja pole seadistatud"**
   - Veenduge, et olete seadistanud `GITHUB_TOKEN` keskkonnamuutuja
   - Taaskäivitage oma terminal/Command Prompt pärast muutuja seadistamist

2. **"Ühendus localhost:8080 keeldus"**
   - Veenduge, et MCP kalkulaatoriteenus töötab pordil 8080
   - Kontrollige, kas mõni teine teenus kasutab porti 8080

3. **"Autentimine ebaõnnestus"**
   - Kontrollige, kas teie GitHubi token on kehtiv ja omab õigeid õigusi
   - Kontrollige, kas teil on juurdepääs GitHub Modelsile

4. **Maveni ehitustõrked**
   - Veenduge, et kasutate Java 21 või uuemat: `java -version`
   - Proovige ehitust puhastada: `mvnw clean`

### Silumine

Silumise logimise lubamiseks lisage rakenduse käivitamisel järgmine JVM argument:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguratsioon

Rakendus on konfigureeritud:
- Kasutama GitHub Modelsit koos `gpt-4.1-nano` mudeliga
- Ühenduma MCP teenusega aadressil `http://localhost:8080/sse`
- Kasutama 60-sekundilist taimerit päringute jaoks
- Lubama päringu/vastuse logimist silumiseks

## Sõltuvused

Projekti peamised sõltuvused:
- **LangChain4j**: AI integratsiooni ja tööriistade haldamiseks
- **LangChain4j MCP**: Model Context Protocoli toetuseks
- **LangChain4j GitHub Models**: GitHub Models integratsiooniks
- **Spring Boot**: Rakenduse raamistik ja sõltuvuste süstimine

## Litsents

See projekt on litsentseeritud Apache License 2.0 alusel - vaadake [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) faili üksikasjade jaoks.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.