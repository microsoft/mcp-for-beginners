# 🐙 Moduli 4: Maendeleo ya Vitendo ya MCP - Server ya Kigezo cha GitHub ya Kipekee

![Duration](https://img.shields.io/badge/Duration-30_minutes-blue?style=flat-square)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-orange?style=flat-square)
![MCP](https://img.shields.io/badge/MCP-Custom%20Server-purple?style=flat-square&logo=github)
![VS Code](https://img.shields.io/badge/VS%20Code-Integration-blue?style=flat-square&logo=visualstudiocode)
![GitHub Copilot](https://img.shields.io/badge/GitHub%20Copilot-Agent%20Mode-green?style=flat-square&logo=github)

> **⚡ Anza Haraka:** Tengeneza server ya MCP inayotumika moja kwa moja kwa uzalishaji ambayo inafanya kazi ya kunakili hifadhidata za GitHub na kuunganisha na VS Code kwa dakika 30 tu!

## 🎯 Malengo ya Kujifunza

Mwisho wa maabara hii, utaweza:

- ✅ Kuunda server ya MCP ya kipekee kwa mtiririko halisi wa maendeleo
- ✅ Kutekeleza kazi ya kunakili hifadhidata za GitHub kupitia MCP
- ✅ Kuunganisha server za MCP za kipekee na VS Code na Agent Builder
- ✅ Kutumia GitHub Copilot Agent Mode na zana za MCP za kipekee
- ✅ Kupima na kupeleka server za MCP za kipekee katika mazingira ya uzalishaji

## 📋 Mahitaji ya Awali

- Kumaliza Maabara 1-3 (Misingi ya MCP na maendeleo ya hali ya juu)
- Usajili wa GitHub Copilot ([usajili wa bure unapatikana](https://github.com/github-copilot/signup))
- VS Code yenye AI Toolkit na nyongeza za GitHub Copilot
- Git CLI imewekwa na kusanidiwa

## 🏗️ Muhtasari wa Mradi

### **Changamoto Halisi ya Maendeleo**
Kama watengenezaji, mara nyingi tunatumia GitHub kunakili hifadhidata na kuzifungua katika VS Code au VS Code Insiders. Mchakato huu wa mikono unahusisha:
1. Kufungua terminal/command prompt
2. Kuenda kwenye saraka inayotakiwa
3. Kutumia amri ya `git clone`
4. Kufungua VS Code katika saraka iliyonakiliwa

**Suluhisho letu la MCP linaboresha hili kuwa amri moja yenye akili!**

### **Utajenga Nini**
Server ya **GitHub Clone MCP** (`git_mcp_server`) inayotoa:

| Kipengele | Maelezo | Faida |
|---------|-------------|---------|
| 🔄 **Kunakili Hifadhidata kwa Akili** | Kunakili hifadhidata za GitHub kwa uhakiki | Ukaguzi wa makosa kiotomatiki |
| 📁 **Usimamizi wa Saraka kwa Akili** | Kagua na tengeneza saraka kwa usalama | Huzuia kufuta yaliyopo |
| 🚀 **Uunganishaji wa VS Code kwa Majukwaa Mbalimbali** | Fungua miradi katika VS Code/Insiders | Mtiririko wa kazi usio na mshono |
| 🛡️ **Udhibiti Imara wa Makosa** | Shughulikia matatizo ya mtandao, ruhusa, na njia | Uaminifu kwa mazingira ya uzalishaji |

---

## 📖 Utekelezaji Hatua kwa Hatua

### Hatua 1: Unda Agent wa GitHub katika Agent Builder

1. **Anzisha Agent Builder** kupitia nyongeza ya AI Toolkit
2. **Unda agent mpya** kwa usanidi ufuatao:
   ```
   Agent Name: GitHubAgent
   ```

3. **Anzisha server ya MCP ya kipekee:**
   - Nenda kwenye **Tools** → **Add Tool** → **MCP Server**
   - Chagua **"Create A new MCP Server"**
   - Chagua **kiolezo cha Python** kwa kubadilika zaidi
   - **Jina la Server:** `git_mcp_server`

### Hatua 2: Sanidi Agent Mode ya GitHub Copilot

1. **Fungua GitHub Copilot** katika VS Code (Ctrl/Cmd + Shift + P → "GitHub Copilot: Open")
2. **Chagua Modeli ya Agent** katika kiolesura cha Copilot
3. **Chagua modeli ya Claude 3.7** kwa uwezo bora wa kufikiri
4. **Washa uunganishaji wa MCP** kwa upatikanaji wa zana

> **💡 Ushauri wa Mtaalamu:** Claude 3.7 hutoa uelewa bora wa mtiririko wa maendeleo na mifumo ya kushughulikia makosa.

### Hatua 3: Tekeleza Kazi Kuu ya Server ya MCP

**Tumia maelekezo haya ya kina na GitHub Copilot Agent Mode:**

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

### Hatua 4: Jaribu Server Yako ya MCP

#### 4a. Jaribu katika Agent Builder

1. **Anzisha usanidi wa urekebishaji (debug) kwa Agent Builder**
2. **Sanidi agent yako kwa maelekezo haya ya mfumo:**

```
SYSTEM_PROMPT:
You are my intelligent coding repository assistant. You help developers efficiently clone GitHub repositories and set up their development environment. Always provide clear feedback about operations and handle errors gracefully.
```

3. **Jaribu kwa hali halisi za mtumiaji:**

```
USER_PROMPT EXAMPLES:

Scenario : Basic Clone and Open
"Clone {Your GitHub Repo link such as https://github.com/kinfey/GHCAgentWorkshop
 } and save to {The global path you specify}, then open it with VS Code Insiders"
```

![Agent Builder Testing](../../../../translated_images/sw/DebugAgent.81d152370c503241b3b39a251b8966f7f739286df19dd57f9147f6402214a012.png)

**Matokeo Yanayotarajiwa:**
- ✅ Kunakili kwa mafanikio na uthibitisho wa njia
- ✅ Kuzindua VS Code moja kwa moja
- ✅ Ujumbe wazi wa makosa kwa hali zisizo halali
- ✅ Kushughulikia vizuri kesi za pembezoni

#### 4b. Jaribu katika MCP Inspector

![MCP Inspector Testing](../../../../translated_images/sw/DebugInspector.eb5c95f94c69a8ba36944941b9a3588309a3a2fae101ace470ee09bde41d1667.png)

---

**🎉 Hongera!** Umefanikiwa kuunda server ya MCP ya vitendo, tayari kwa uzalishaji inayotatua changamoto halisi za mtiririko wa maendeleo. Server yako ya kunakili GitHub ya kipekee inaonyesha nguvu ya MCP katika kuendesha na kuboresha tija ya watengenezaji.

### 🏆 Mafanikio Uliyopata:
- ✅ **MCP Developer** - Umeunda server ya MCP ya kipekee
- ✅ **Workflow Automator** - Umeboresha michakato ya maendeleo  
- ✅ **Mtaalamu wa Uunganishaji** - Umeunganisha zana nyingi za maendeleo
- ✅ **Tayari kwa Uzalishaji** - Umetengeneza suluhisho zinazoweza kupelekwa

---

## 🎓 Kumaliza Warsha: Safari Yako na Model Context Protocol

**Mshiriki Mpendwa wa Warsha,**

Hongera kwa kumaliza moduli zote nne za warsha ya Model Context Protocol! Umefika mbali kutoka kuelewa misingi ya AI Toolkit hadi kujenga server za MCP zinazotumika moja kwa moja kwa uzalishaji zinazotatua changamoto halisi za maendeleo.

### 🚀 Muhtasari wa Njia Yako ya Kujifunza:

**[Moduli 1](../lab1/README.md)**: Umeanza kwa kuchunguza misingi ya AI Toolkit, upimaji wa modeli, na kuunda agent yako ya kwanza ya AI.

**[Moduli 2](../lab2/README.md)**: Umejifunza usanifu wa MCP, kuunganisha Playwright MCP, na kujenga agent wa otomatiki wa kivinjari.

**[Moduli 3](../lab3/README.md)**: Umeendelea na maendeleo ya server za MCP za kipekee kwa server ya Weather MCP na umemaster zana za urekebishaji.

**[Moduli 4](../lab4/README.md)**: Sasa umeweka yote pamoja kuunda zana ya otomatiki ya mtiririko wa kazi wa hifadhidata za GitHub.

### 🌟 Umejifunza Nini:

- ✅ **Ecosystem ya AI Toolkit**: Modeli, agent, na mifumo ya uunganishaji
- ✅ **Usanifu wa MCP**: Muundo wa mteja-server, itifaki za usafirishaji, na usalama
- ✅ **Zana za Mtaalamu**: Kutoka Playground hadi Inspector hadi uzalishaji
- ✅ **Maendeleo ya Kipekee**: Kujenga, kupima, na kupeleka server zako za MCP
- ✅ **Matumizi ya Vitendo**: Kutatua changamoto halisi za mtiririko wa kazi kwa AI

### 🔮 Hatua Zako Zifuatazo:

1. **Jenga Server Yako ya MCP**: Tumia ujuzi huu kuendesha mitiririko yako ya kipekee
2. **Jiunge na Jamii ya MCP**: Shiriki kazi zako na jifunze kutoka kwa wengine
3. **Chunguza Uunganishaji wa Juu**: Unganisha server za MCP na mifumo ya makampuni
4. **Changia Chanzo Huria**: Saidia kuboresha zana na nyaraka za MCP

Kumbuka, warsha hii ni mwanzo tu. Ecosystem ya Model Context Protocol inaendelea kukua kwa kasi, na sasa umewezeshwa kuwa mstari wa mbele wa zana za maendeleo zinazotumia AI.

**Asante kwa kushiriki na kujitolea kwako kwa kujifunza!**

Tunatumai warsha hii imezindua mawazo yatakayobadilisha jinsi unavyotengeneza na kuingiliana na zana za AI katika safari yako ya maendeleo.

**Furahia kuandika msimbo!**

---

**Kiarifu cha Msamaha**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatuna dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.