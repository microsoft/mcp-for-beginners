# Scenár 3: Dokumentácia priamo v editore s MCP serverom vo VS Code

## Prehľad

V tomto scenári sa naučíte, ako priniesť Microsoft Learn Docs priamo do vášho prostredia Visual Studio Code pomocou MCP servera. Namiesto neustáleho prepínania medzi záložkami prehliadača pri hľadaní dokumentácie môžete pristupovať, vyhľadávať a odkazovať na oficiálnu dokumentáciu priamo vo vašom editore. Tento prístup zjednodušuje váš pracovný tok, udržiava vás sústredených a umožňuje bezproblémovú integráciu s nástrojmi ako GitHub Copilot.

- Vyhľadávajte a čítajte dokumentáciu vo VS Code bez opustenia prostredia na písanie kódu.
- Odkazujte na dokumentáciu a vkladajte odkazy priamo do README alebo súborov kurzu.
- Používajte GitHub Copilot a MCP spoločne pre plynulý pracovný tok s podporou AI.

## Ciele učenia

Na konci tejto kapitoly budete vedieť, ako nastaviť a používať MCP server vo VS Code na zlepšenie vášho pracovného toku pri dokumentácii a vývoji. Budete schopní:

- Nakonfigurovať svoje pracovné prostredie na používanie MCP servera pre vyhľadávanie dokumentácie.
- Vyhľadávať a vkladať dokumentáciu priamo vo VS Code.
- Kombinovať silu GitHub Copilota a MCP pre produktívnejší pracovný tok s podporou AI.

Tieto zručnosti vám pomôžu zostať sústredení, zlepšiť kvalitu dokumentácie a zvýšiť vašu produktivitu ako vývojára alebo technického spisovateľa.

## Riešenie

Aby ste dosiahli prístup k dokumentácii priamo v editore, budete postupovať podľa série krokov, ktoré integrujú MCP server s VS Code a GitHub Copilot. Toto riešenie je ideálne pre autorov kurzov, dokumentačných spisovateľov a vývojárov, ktorí chcú zostať sústredení v editore pri práci s dokumentáciou a Copilotom.

- Rýchlo pridávajte referenčné odkazy do README počas písania dokumentácie ku kurzu alebo projektu.
- Používajte Copilota na generovanie kódu a MCP na okamžité vyhľadanie a citovanie relevantnej dokumentácie.
- Zostaňte sústredení vo vašom editore a zvýšte produktivitu.

### Podrobný návod

Pre začiatok postupujte podľa týchto krokov. Ku každému kroku môžete pridať snímku obrazovky z priečinka assets na vizuálne znázornenie postupu.

1. **Pridajte konfiguráciu MCP:**
   V koreňovom adresári projektu vytvorte súbor `.vscode/mcp.json` a pridajte nasledujúcu konfiguráciu:
   ```json
   {
     "servers": {
       "LearnDocsMCP": {
         "url": "https://learn.microsoft.com/api/mcp"
       }
     }
   }
   ```
   Táto konfigurácia hovorí VS Code, ako sa pripojiť k [`Microsoft Learn Docs MCP serveru`](https://github.com/MicrosoftDocs/mcp).
   
   ![Krok 1: Pridajte mcp.json do priečinka .vscode](../../../../../../translated_images/sk/step1-mcp-json.c06a007fccc3edfaf0598a31903c9ec71476d9fd3ae6c1b2b4321fd38688ca4b.png)
    
2. **Otvorte panel GitHub Copilot Chat:**
   Ak ešte nemáte nainštalované rozšírenie GitHub Copilot, prejdite do zobrazenia Rozšírenia vo VS Code a nainštalujte ho. Môžete si ho stiahnuť priamo z [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat). Potom otvorte panel Copilot Chat z bočného panela.

   ![Krok 2: Otvorte panel Copilot Chat](../../../../../../translated_images/sk/step2-copilot-panel.f1cc86e9b9b8cd1a85e4df4923de8bafee4830541ab255e3c90c09777fed97db.png)

3. **Povoľte agent mód a overte nástroje:**
   V paneli Copilot Chat povoľte agent mód.

   ![Krok 3: Povoľte agent mód a overte nástroje](../../../../../../translated_images/sk/step3-agent-mode.cdc32520fd7dd1d149c3f5226763c1d85a06d3c041d4cc983447625bdbeff4d4.png)

   Po povolení agent módu overte, či je MCP server uvedený medzi dostupnými nástrojmi. To zabezpečí, že agent Copilota má prístup k dokumentačnému serveru na získavanie relevantných informácií.
   
   ![Krok 3: Overenie nástroja MCP server](../../../../../../translated_images/sk/step3-verify-mcp-tool.76096a6329cbfecd42888780f322370a0d8c8fa003ed3eeb7ccd23f0fc50c1ad.png)
4. **Začnite nový chat a položte agentovi otázku:**
   Otvorte nový chat v paneli Copilot Chat. Teraz môžete agentovi klásť otázky týkajúce sa dokumentácie. Agent použije MCP server na získanie a zobrazenie relevantnej dokumentácie Microsoft Learn priamo vo vašom editore.

   - *„Snažím sa napísať študijný plán pre tému X. Budem sa jej venovať 8 týždňov, pre každý týždeň navrhni obsah, ktorý by som mal študovať.“*

   ![Krok 4: Položte agentovi otázku v chate](../../../../../../translated_images/sk/step4-prompt-chat.12187bb001605efc5077992b621f0fcd1df12023c5dce0464f8eb8f3d595218f.png)

5. **Živý dotaz:**

   > Pozrime sa na živý dotaz z [#get-help](https://discord.gg/D6cRhjHWSC) sekcie v Azure AI Foundry Discorde ([zobraziť pôvodnú správu](https://discord.com/channels/1113626258182504448/1385498306720829572)):
   
   *„Hľadám odpovede, ako nasadiť multi-agentné riešenie s AI agentmi vyvinutými na Azure AI Foundry. Vidím, že neexistuje priamy spôsob nasadenia, ako sú kanály Copilot Studio. Aké sú teda rôzne spôsoby, ako toto nasadenie realizovať, aby podnikový používateľ mohol interagovať a splniť úlohu?
Existuje množstvo článkov/blogov, ktoré tvrdia, že môžeme použiť Azure Bot službu ako most medzi MS Teams a Azure AI Foundry agentmi. Bude to fungovať, ak nastavím Azure bota, ktorý sa pripojí k Orchestrator Agentovi na Azure AI Foundry cez Azure funkciu na orchestráciu, alebo musím vytvoriť Azure funkciu pre každého AI agenta v multi-agentnom riešení, aby orchestrácia prebiehala na úrovni Bot frameworku? Akékoľvek ďalšie návrhy sú vítané.“*

   ![Krok 5: Živé dotazy](../../../../../../translated_images/sk/step5-live-queries.49db3e4a50bea27327e3cb18c24d263b7d134930d78e7392f9515a1c00264a7f.png)

   Agent odpovie relevantnými odkazmi na dokumentáciu a zhrnutiami, ktoré môžete priamo vložiť do svojich markdown súborov alebo použiť ako odkazy vo vašom kóde.
   
### Ukážkové dotazy

Tu je niekoľko príkladov dotazov, ktoré môžete vyskúšať. Tieto dotazy ukážu, ako MCP server a Copilot môžu spolupracovať na poskytovaní okamžitej, kontextovo relevantnej dokumentácie a odkazov bez opustenia VS Code:

- „Ukáž mi, ako používať Azure Functions triggery.“
- „Vlož odkaz na oficiálnu dokumentáciu pre Azure Key Vault.“
- „Aké sú najlepšie postupy na zabezpečenie Azure zdrojov?“
- „Nájdi rýchly štart pre Azure AI služby.“

Tieto dotazy demonštrujú, ako MCP server a Copilot môžu spolupracovať na poskytovaní okamžitej, kontextovo relevantnej dokumentácie a odkazov bez opustenia VS Code.

---

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.