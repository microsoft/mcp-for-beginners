# Mokymosi plano generatorius su Chainlit ir Microsoft Learn Docs MCP

## Reikalavimai

- Python 3.8 arba naujesnė versija
- pip (Python paketų tvarkyklė)
- Interneto prieiga, kad galėtumėte prisijungti prie Microsoft Learn Docs MCP serverio

## Diegimas

1. Nuklonuokite šį saugyklą arba atsisiųskite projekto failus.
2. Įdiekite reikalingas priklausomybes:

   ```bash
   pip install -r requirements.txt
   ```

## Naudojimas

### Scenarijus 1: Paprasta užklausa į Docs MCP
Komandinės eilutės klientas, kuris jungiasi prie Docs MCP serverio, siunčia užklausą ir pateikia rezultatą.

1. Paleiskite skriptą:
   ```bash
   python scenario1.py
   ```
2. Įveskite savo klausimą apie dokumentaciją, kai būsite paraginti.

### Scenarijus 2: Mokymosi plano generatorius (Chainlit internetinė programa)
Internetinė sąsaja (naudojant Chainlit), leidžianti vartotojams generuoti asmeninį, savaitė po savaitės mokymosi planą bet kuriai techninei temai.

1. Paleiskite Chainlit programą:
   ```bash
   chainlit run scenario2.py
   ```
2. Atidarykite terminale pateiktą vietinį URL (pvz., http://localhost:8000) savo naršyklėje.
3. Pokalbių lange įveskite savo mokymosi temą ir norimą mokymosi savaičių skaičių (pvz., „AI-900 sertifikatas, 8 savaitės“).
4. Programa atsakys su savaitės mokymosi planu, įskaitant nuorodas į atitinkamą Microsoft Learn dokumentaciją.

**Reikalingi aplinkos kintamieji:**

Norėdami naudoti 2 scenarijų (Chainlit internetinę programą su Azure OpenAI), turite nustatyti šiuos aplinkos kintamuosius `.env` faile, esančiame `python` kataloge:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Prieš paleisdami programą, užpildykite šias reikšmes savo Azure OpenAI ištekliaus duomenimis.

> [!TIP]
> Galite lengvai diegti savo modelius naudodami [Azure AI Foundry](https://ai.azure.com/).

### Scenarijus 3: Dokumentacija redaktoriuje su MCP serveriu VS Code

Vietoj naršyklės skirtukų perjungimo, norint ieškoti dokumentacijos, galite naudoti Microsoft Learn Docs tiesiogiai VS Code su MCP serveriu. Tai leidžia:
- Ieškoti ir skaityti dokumentaciją VS Code neišeinant iš kodavimo aplinkos.
- Įterpti nuorodas į dokumentaciją tiesiai į README ar kursų failus.
- Naudoti GitHub Copilot ir MCP kartu, kad sukurtumėte sklandų, AI pagrįstą dokumentacijos darbo procesą.

**Pavyzdžiai, kaip naudoti:**
- Greitai pridėti nuorodas į README rašant kursų ar projekto dokumentaciją.
- Naudoti Copilot kodui generuoti ir MCP, kad iš karto rastumėte ir cituotumėte atitinkamą dokumentaciją.
- Išlikti susikoncentravus redaktoriuje ir padidinti produktyvumą.

> [!IMPORTANT]
> Įsitikinkite, kad jūsų darbo aplinkoje yra galiojanti [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) konfigūracija (vietoje `.vscode/mcp.json`).

## Kodėl Chainlit tinkamas 2 scenarijui?

Chainlit yra modernus atvirojo kodo karkasas, skirtas kurti pokalbių internetines programas. Jis leidžia lengvai sukurti pokalbių vartotojo sąsajas, kurios jungiasi prie užpakalinių paslaugų, tokių kaip Microsoft Learn Docs MCP serveris. Šis projektas naudoja Chainlit, kad pateiktų paprastą, interaktyvų būdą realiuoju laiku generuoti asmeninius mokymosi planus. Naudodami Chainlit, galite greitai kurti ir diegti pokalbių įrankius, kurie pagerina produktyvumą ir mokymąsi.

## Ką ši programa daro

Ši programa leidžia vartotojams sukurti asmeninį mokymosi planą, tiesiog įvedant temą ir trukmę. Programa analizuoja jūsų įvestį, siunčia užklausą Microsoft Learn Docs MCP serveriui dėl atitinkamo turinio ir organizuoja rezultatus į struktūrizuotą, savaitės planą. Kiekvienos savaitės rekomendacijos pateikiamos pokalbyje, todėl jas lengva sekti ir stebėti savo pažangą. Integracija užtikrina, kad visada gausite naujausius ir aktualiausius mokymosi išteklius.

## Pavyzdinės užklausos

Išbandykite šias užklausas pokalbių lange, kad pamatytumėte, kaip programa reaguoja:

- `AI-900 sertifikatas, 8 savaitės`
- `Išmokti Azure Functions, 4 savaitės`
- `Azure DevOps, 6 savaitės`
- `Duomenų inžinerija Azure, 10 savaičių`
- `Microsoft saugumo pagrindai, 5 savaitės`
- `Power Platform, 7 savaitės`
- `Azure AI paslaugos, 12 savaičių`
- `Debesų architektūra, 9 savaitės`

Šie pavyzdžiai parodo programos lankstumą įvairiems mokymosi tikslams ir laikotarpiams.

## Nuorodos

- [Chainlit dokumentacija](https://docs.chainlit.io/)
- [MCP dokumentacija](https://github.com/MicrosoftDocs/mcp)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipiame dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojame kreiptis į profesionalius vertėjus. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, kylančius dėl šio vertimo naudojimo.