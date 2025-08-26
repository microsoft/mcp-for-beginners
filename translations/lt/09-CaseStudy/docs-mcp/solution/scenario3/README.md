<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "db532b1ec386c9ce38c791653dc3c881",
  "translation_date": "2025-08-26T16:07:33+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/scenario3/README.md",
  "language_code": "lt"
}
-->
# Scenarijus 3: Dokumentacija redaktoriuje su MCP serveriu VS Code

## Apžvalga

Šiame scenarijuje sužinosite, kaip integruoti Microsoft Learn dokumentaciją tiesiai į savo Visual Studio Code aplinką naudojant MCP serverį. Vietoj nuolatinio naršyklės skirtukų perjungimo ieškant dokumentacijos, galėsite pasiekti, ieškoti ir naudoti oficialią dokumentaciją tiesiai redaktoriuje. Šis metodas supaprastina jūsų darbo eigą, leidžia išlikti susitelkus ir sklandžiai integruoti įrankius, tokius kaip GitHub Copilot.

- Ieškokite ir skaitykite dokumentaciją VS Code aplinkoje neišeidami iš kodo redaktoriaus.
- Naudokite dokumentaciją kaip nuorodas ir įterpkite jas tiesiai į README ar kursų failus.
- Naudokite GitHub Copilot ir MCP kartu, kad sukurtumėte sklandžią, dirbtiniu intelektu paremtą dokumentacijos darbo eigą.

## Mokymosi tikslai

Šio skyriaus pabaigoje suprasite, kaip nustatyti ir naudoti MCP serverį VS Code aplinkoje, kad pagerintumėte savo dokumentacijos ir kūrimo darbo eigą. Jūs galėsite:

- Suprasti, kaip sukonfigūruoti savo darbo aplinką MCP serverio dokumentacijos paieškai.
- Ieškoti ir įterpti dokumentaciją tiesiai iš VS Code.
- Derinti GitHub Copilot ir MCP galimybes, kad sukurtumėte produktyvesnę, dirbtiniu intelektu papildytą darbo eigą.

Šie įgūdžiai padės jums išlikti susitelkus, pagerinti dokumentacijos kokybę ir padidinti produktyvumą kaip kūrėjui ar techniniam rašytojui.

## Sprendimas

Norėdami pasiekti dokumentaciją tiesiai redaktoriuje, atliksite kelis veiksmus, kurie integruos MCP serverį su VS Code ir GitHub Copilot. Šis sprendimas puikiai tinka kursų autoriams, dokumentacijos rašytojams ir kūrėjams, kurie nori išlikti redaktoriuje dirbdami su dokumentacija ir Copilot.

- Greitai pridėkite nuorodas į README rašydami kursų ar projekto dokumentaciją.
- Naudokite Copilot kodui generuoti ir MCP, kad iš karto rastumėte ir cituotumėte atitinkamą dokumentaciją.
- Išlikite susitelkę redaktoriuje ir padidinkite produktyvumą.

### Žingsnis po žingsnio vadovas

Norėdami pradėti, atlikite šiuos veiksmus. Kiekvienam žingsniui galite pridėti ekrano nuotrauką iš assets aplanko, kad vizualiai iliustruotumėte procesą.

1. **Pridėkite MCP konfigūraciją:**
   Savo projekto šakniniame kataloge sukurkite `.vscode/mcp.json` failą ir pridėkite šią konfigūraciją:
   ```json
   {
     "servers": {
       "LearnDocsMCP": {
         "url": "https://learn.microsoft.com/api/mcp"
       }
     }
   }
   ```
   Ši konfigūracija nurodo VS Code, kaip prisijungti prie [`Microsoft Learn Docs MCP serverio`](https://github.com/MicrosoftDocs/mcp).
   
   ![1 žingsnis: Pridėkite mcp.json į .vscode aplanką](../../../../../../translated_images/step1-mcp-json.c06a007fccc3edfaf0598a31903c9ec71476d9fd3ae6c1b2b4321fd38688ca4b.lt.png)
    
2. **Atidarykite GitHub Copilot Chat panelę:**
   Jei dar neturite įdiegto GitHub Copilot plėtinio, eikite į VS Code plėtinių peržiūrą ir įdiekite jį. Galite jį atsisiųsti tiesiai iš [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat). Tada atidarykite Copilot Chat panelę iš šoninės juostos.

   ![2 žingsnis: Atidarykite Copilot Chat panelę](../../../../../../translated_images/step2-copilot-panel.f1cc86e9b9b8cd1a85e4df4923de8bafee4830541ab255e3c90c09777fed97db.lt.png)

3. **Įjunkite agento režimą ir patikrinkite įrankius:**
   Copilot Chat panelėje įjunkite agento režimą.

   ![3 žingsnis: Įjunkite agento režimą ir patikrinkite įrankius](../../../../../../translated_images/step3-agent-mode.cdc32520fd7dd1d149c3f5226763c1d85a06d3c041d4cc983447625bdbeff4d4.lt.png)

   Įjungę agento režimą, patikrinkite, ar MCP serveris yra įtrauktas į galimų įrankių sąrašą. Tai užtikrina, kad Copilot agentas galės pasiekti dokumentacijos serverį ir gauti reikiamą informaciją.
   
   ![3 žingsnis: Patikrinkite MCP serverio įrankį](../../../../../../translated_images/step3-verify-mcp-tool.76096a6329cbfecd42888780f322370a0d8c8fa003ed3eeb7ccd23f0fc50c1ad.lt.png)

4. **Pradėkite naują pokalbį ir pateikite užklausą agentui:**
   Atidarykite naują pokalbį Copilot Chat panelėje. Dabar galite pateikti agentui savo dokumentacijos užklausas. Agentas naudos MCP serverį, kad gautų ir parodytų atitinkamą Microsoft Learn dokumentaciją tiesiai jūsų redaktoriuje.

   - *"Bandau sudaryti mokymosi planą temai X. Planuoju mokytis 8 savaites, kiekvienai savaitei pasiūlykite turinį, kurį turėčiau peržiūrėti."*

   ![4 žingsnis: Pateikite užklausą agentui pokalbyje](../../../../../../translated_images/step4-prompt-chat.12187bb001605efc5077992b621f0fcd1df12023c5dce0464f8eb8f3d595218f.lt.png)

5. **Tiesioginė užklausa:**

   > Paimkime tiesioginę užklausą iš [#get-help](https://discord.gg/D6cRhjHWSC) skyriaus Azure AI Foundry Discord ([peržiūrėti originalią žinutę](https://discord.com/channels/1113626258182504448/1385498306720829572)):
   
   *"Ieškau atsakymų, kaip diegti kelių agentų sprendimą su AI agentais, sukurtais Azure AI Foundry. Nematau tiesioginio diegimo metodo, pvz., Copilot Studio kanalų. Taigi, kokie yra skirtingi būdai tai įgyvendinti, kad įmonės vartotojai galėtų sąveikauti ir atlikti darbą? Yra daugybė straipsnių/tinklaraščių, kurie teigia, kad tam galima naudoti Azure Bot paslaugą, kuri gali veikti kaip tiltas tarp MS Teams ir Azure AI Foundry agentų. Ar tai veiks, jei nustatysiu Azure botą, kuris jungiasi prie Orchestrator Agent Azure AI Foundry per Azure funkciją, kad atliktų orkestravimą, ar man reikia sukurti Azure funkciją kiekvienam AI agentui, kuris yra kelių agentų sprendimo dalis, kad atliktų orkestravimą Bot Framework? Bet kokie kiti pasiūlymai yra labai laukiami."*

   ![5 žingsnis: Tiesioginės užklausos](../../../../../../translated_images/step5-live-queries.49db3e4a50bea27327e3cb18c24d263b7d134930d78e7392f9515a1c00264a7f.lt.png)

   Agentas atsakys su atitinkamomis dokumentacijos nuorodomis ir santraukomis, kurias galėsite tiesiogiai įterpti į savo markdown failus arba naudoti kaip nuorodas savo kode.
   
### Pavyzdinės užklausos

Štai keletas pavyzdinių užklausų, kurias galite išbandyti. Šios užklausos parodys, kaip MCP serveris ir Copilot gali dirbti kartu, kad pateiktų momentinę, kontekstinę dokumentaciją ir nuorodas neišeinant iš VS Code:

- "Parodykite, kaip naudoti Azure Functions trigerius."
- "Įterpkite nuorodą į oficialią Azure Key Vault dokumentaciją."
- "Kokios yra geriausios praktikos Azure resursų saugumui užtikrinti?"
- "Raskite greitą pradžios vadovą Azure AI paslaugoms."

Šios užklausos parodys, kaip MCP serveris ir Copilot gali dirbti kartu, kad pateiktų momentinę, kontekstinę dokumentaciją ir nuorodas neišeinant iš VS Code.

---

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipiame dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, kylančius dėl šio vertimo naudojimo.