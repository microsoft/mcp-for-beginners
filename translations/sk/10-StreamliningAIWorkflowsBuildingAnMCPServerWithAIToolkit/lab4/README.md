# 🐙 Modul 4: Praktický vývoj MCP – Vlastný server na klonovanie GitHub repozitárov

![Duration](https://img.shields.io/badge/Duration-30_minutes-blue?style=flat-square)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-orange?style=flat-square)
![MCP](https://img.shields.io/badge/MCP-Custom%20Server-purple?style=flat-square&logo=github)
![VS Code](https://img.shields.io/badge/VS%20Code-Integration-blue?style=flat-square&logo=visualstudiocode)
![GitHub Copilot](https://img.shields.io/badge/GitHub%20Copilot-Agent%20Mode-green?style=flat-square&logo=github)

> **⚡ Rýchly štart:** Vytvorte produkčne pripravený MCP server, ktorý automatizuje klonovanie GitHub repozitárov a integráciu s VS Code za pouhých 30 minút!

## 🎯 Ciele učenia

Na konci tohto labu budete vedieť:

- ✅ Vytvoriť vlastný MCP server pre reálne vývojové workflow
- ✅ Implementovať funkciu klonovania GitHub repozitárov cez MCP
- ✅ Integrovať vlastné MCP servery s VS Code a Agent Builderom
- ✅ Používať GitHub Copilot Agent Mode s vlastnými MCP nástrojmi
- ✅ Testovať a nasadzovať vlastné MCP servery v produkčnom prostredí

## 📋 Predpoklady

- Dokončenie labov 1-3 (základy MCP a pokročilý vývoj)
- Predplatné GitHub Copilot ([dostupná bezplatná registrácia](https://github.com/github-copilot/signup))
- VS Code s rozšíreniami AI Toolkit a GitHub Copilot
- Nainštalovaný a nakonfigurovaný Git CLI

## 🏗️ Prehľad projektu

### **Reálny vývojový problém**
Ako vývojári často používame GitHub na klonovanie repozitárov a ich otvorenie vo VS Code alebo VS Code Insiders. Tento manuálny proces zahŕňa:
1. Otvorenie terminálu/príkazového riadku
2. Navigáciu do požadovaného adresára
3. Spustenie príkazu `git clone`
4. Otvorenie VS Code v naklonovanom adresári

**Naše MCP riešenie to zjednodušuje na jeden inteligentný príkaz!**

### **Čo vytvoríte**
**GitHub Clone MCP Server** (`git_mcp_server`), ktorý ponúka:

| Funkcia | Popis | Výhoda |
|---------|-------------|---------|
| 🔄 **Inteligentné klonovanie repozitárov** | Klonovanie GitHub repozitárov s validáciou | Automatická kontrola chýb |
| 📁 **Inteligentná správa adresárov** | Bezpečná kontrola a vytváranie adresárov | Zabránenie prepísaniu |
| 🚀 **Multiplatformová integrácia VS Code** | Otváranie projektov vo VS Code/Insiders | Plynulý prechod vo workflow |
| 🛡️ **Robustné spracovanie chýb** | Riešenie problémov s sieťou, oprávneniami a cestami | Spoľahlivosť pre produkciu |

---

## 📖 Krok za krokom implementácia

### Krok 1: Vytvorte GitHub agenta v Agent Builderi

1. **Spustite Agent Builder** cez rozšírenie AI Toolkit
2. **Vytvorte nového agenta** s nasledujúcou konfiguráciou:
   ```
   Agent Name: GitHubAgent
   ```

3. **Inicializujte vlastný MCP server:**
   - Prejdite do **Tools** → **Add Tool** → **MCP Server**
   - Vyberte **"Create A new MCP Server"**
   - Zvoľte **Python šablónu** pre maximálnu flexibilitu
   - **Názov servera:** `git_mcp_server`

### Krok 2: Nastavte GitHub Copilot Agent Mode

1. **Otvorte GitHub Copilot** vo VS Code (Ctrl/Cmd + Shift + P → "GitHub Copilot: Open")
2. **Vyberte Agent Model** v rozhraní Copilota
3. **Zvoľte model Claude 3.7** pre lepšie schopnosti uvažovania
4. **Povoľte MCP integráciu** pre prístup k nástrojom

> **💡 Tip:** Claude 3.7 poskytuje lepšie porozumenie vývojovým workflow a vzorom spracovania chýb.

### Krok 3: Implementujte základnú funkcionalitu MCP servera

**Použite nasledujúci detailný prompt s GitHub Copilot Agent Mode:**

```
Create two MCP tools with the following comprehensive requirements:

🔧 TOOL A: clone_repository
Requirements:
- Clone any GitHub repository to a specified local folder
- Return the absolute path of the successfully cloned project
- Implement comprehensive validation:
  ✓ Check if target directory already exists (return error if exists)
  ✓ Validate GitHub URL format (https://github.com/user/repo)
  ✓ Verify git command availability (prompt installation if missing)
  ✓ Handle network connectivity issues
  ✓ Provide clear error messages for all failure scenarios

🚀 TOOL B: open_in_vscode
Requirements:
- Open specified folder in VS Code or VS Code Insiders
- Cross-platform compatibility (Windows/Linux/macOS)
- Use direct application launch (not terminal commands)
- Auto-detect available VS Code installations
- Handle cases where VS Code is not installed
- Provide user-friendly error messages

Additional Requirements:
- Follow MCP 1.9.3 best practices
- Include proper type hints and documentation
- Implement logging for debugging purposes
- Add input validation for all parameters
- Include comprehensive error handling
```

### Krok 4: Otestujte svoj MCP server

#### 4a. Testovanie v Agent Builderi

1. **Spustite debug konfiguráciu** v Agent Builderi
2. **Nakonfigurujte svojho agenta s týmto systémovým promptom:**

```
SYSTEM_PROMPT:
You are my intelligent coding repository assistant. You help developers efficiently clone GitHub repositories and set up their development environment. Always provide clear feedback about operations and handle errors gracefully.
```

3. **Testujte realistické používateľské scenáre:**

```
USER_PROMPT EXAMPLES:

Scenario : Basic Clone and Open
"Clone {Your GitHub Repo link such as https://github.com/kinfey/GHCAgentWorkshop
 } and save to {The global path you specify}, then open it with VS Code Insiders"
```

![Agent Builder Testing](../../../../translated_images/sk/DebugAgent.81d152370c503241b3b39a251b8966f7f739286df19dd57f9147f6402214a012.png)

**Očakávané výsledky:**
- ✅ Úspešné klonovanie s potvrdením cesty
- ✅ Automatické spustenie VS Code
- ✅ Jasné chybové hlásenia pri neplatných scenároch
- ✅ Správne riešenie okrajových prípadov

#### 4b. Testovanie v MCP Inspectore

![MCP Inspector Testing](../../../../translated_images/sk/DebugInspector.eb5c95f94c69a8ba36944941b9a3588309a3a2fae101ace470ee09bde41d1667.png)

---

**🎉 Gratulujeme!** Úspešne ste vytvorili praktický, produkčne pripravený MCP server, ktorý rieši reálne vývojové workflow výzvy. Váš vlastný GitHub clone server ukazuje silu MCP pri automatizácii a zvyšovaní produktivity vývojárov.

### 🏆 Dosiahnuté úspechy:
- ✅ **MCP Developer** – Vytvoril vlastný MCP server
- ✅ **Workflow Automator** – Zjednodušil vývojové procesy  
- ✅ **Integration Expert** – Prepojil viacero vývojových nástrojov
- ✅ **Production Ready** – Vytvoril riešenia pripravené na nasadenie

---

## 🎓 Ukončenie workshopu: Vaša cesta s Model Context Protocol

**Vážený účastník workshopu,**

Gratulujeme k úspešnému dokončeniu všetkých štyroch modulov workshopu Model Context Protocol! Prešli ste dlhú cestu od pochopenia základov AI Toolkit až po tvorbu produkčne pripravených MCP serverov, ktoré riešia reálne vývojové výzvy.

### 🚀 Rekapitulácia vašej učebnej cesty:

**[Modul 1](../lab1/README.md)**: Začali ste skúmaním základov AI Toolkit, testovaním modelov a vytvorením prvého AI agenta.

**[Modul 2](../lab2/README.md)**: Naučili ste sa architektúru MCP, integrovali Playwright MCP a vytvorili prvého agenta pre automatizáciu prehliadača.

**[Modul 3](../lab3/README.md)**: Pokročili ste vo vývoji vlastných MCP serverov s Weather MCP serverom a zvládli ste nástroje na ladenie.

**[Modul 4](../lab4/README.md)**: Teraz ste všetko aplikovali na vytvorenie praktického nástroja na automatizáciu workflow GitHub repozitárov.

### 🌟 Čo ste zvládli:

- ✅ **Ekosystém AI Toolkit**: Modely, agenti a integračné vzory
- ✅ **Architektúra MCP**: Klient-server dizajn, transportné protokoly a bezpečnosť
- ✅ **Vývojárske nástroje**: Od Playground cez Inspector až po produkčné nasadenie
- ✅ **Vlastný vývoj**: Tvorba, testovanie a nasadzovanie vlastných MCP serverov
- ✅ **Praktické aplikácie**: Riešenie reálnych workflow výziev pomocou AI

### 🔮 Vaše ďalšie kroky:

1. **Vytvorte si vlastný MCP server**: Uplatnite tieto zručnosti na automatizáciu svojich jedinečných workflow
2. **Pridajte sa ku komunite MCP**: Zdieľajte svoje projekty a učte sa od ostatných
3. **Preskúmajte pokročilú integráciu**: Prepojte MCP servery s podnikových systémami
4. **Prispievajte do open source**: Pomáhajte zlepšovať MCP nástroje a dokumentáciu

Pamätajte, že tento workshop je len začiatok. Ekosystém Model Context Protocol sa rýchlo vyvíja a vy ste teraz pripravení byť na čele vývoja AI nástrojov.

**Ďakujeme za vašu účasť a odhodlanie učiť sa!**

Dúfame, že vám tento workshop priniesol inšpiráciu, ktorá zmení spôsob, akým vytvárate a používate AI nástroje vo vašej vývojovej práci.

**Prajeme veľa úspechov pri kódovaní!**

---

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.