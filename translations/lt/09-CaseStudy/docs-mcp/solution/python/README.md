<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-08-26T16:08:00+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "lt"
}
-->
# Studijų plano generatorius su Chainlit ir Microsoft Learn Docs MCP

## Reikalavimai

- Python 3.8 ar naujesnė versija
- pip (Python paketų tvarkyklė)
- Interneto prieiga, kad galėtumėte prisijungti prie Microsoft Learn Docs MCP serverio

## Įdiegimas

1. Nukopijuokite šį repozitoriją arba atsisiųskite projekto failus.
2. Įdiekite reikalingas priklausomybes:

   ```bash
   pip install -r requirements.txt
   ```

## Naudojimas

### Scenarijus 1: Paprastas užklausimas į Docs MCP
Komandinės eilutės klientas, kuris prisijungia prie Docs MCP serverio, siunčia užklausą ir pateikia rezultatą.

1. Paleiskite skriptą:
   ```bash
   python scenario1.py
   ```
2. Įveskite savo dokumentacijos klausimą, kai būsite paraginti.

### Scenarijus 2: Studijų plano generatorius (Chainlit internetinė aplikacija)
Internetinė sąsaja (naudojant Chainlit), leidžianti vartotojams sukurti asmeninį, savaitėmis suskirstytą studijų planą bet kuriai techninei temai.

1. Paleiskite Chainlit aplikaciją:
   ```bash
   chainlit run scenario2.py
   ```
2. Atidarykite vietinį URL, pateiktą jūsų terminale (pvz., http://localhost:8000), naršyklėje.
3. Pokalbio lange įveskite savo studijų temą ir norimą studijų trukmę (pvz., „AI-900 sertifikatas, 8 savaitės“).
4. Aplikacija atsakys su savaitėmis suskirstytu studijų planu, įskaitant nuorodas į atitinkamą Microsoft Learn dokumentaciją.

**Reikalingi aplinkos kintamieji:**

Norėdami naudoti 2 scenarijų (Chainlit internetinę aplikaciją su Azure OpenAI), turite nustatyti šiuos aplinkos kintamuosius `.env` faile, esančiame `python` kataloge:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Prieš paleisdami aplikaciją, užpildykite šias reikšmes savo Azure OpenAI resurso duomenimis.

> **Patarimas:** Savo modelius galite lengvai diegti naudodami [Azure AI Foundry](https://ai.azure.com/).

### Scenarijus 3: Dokumentacija redaktoriuje su MCP serveriu VS Code

Užuot perjungę naršyklės skirtukus ieškodami dokumentacijos, galite Microsoft Learn Docs integruoti tiesiai į VS Code naudodami MCP serverį. Tai leidžia:
- Ieškoti ir skaityti dokumentaciją VS Code aplinkoje, neišeinant iš kodavimo aplinkos.
- Įterpti nuorodas į dokumentaciją tiesiai į README ar kursų failus.
- Naudoti GitHub Copilot ir MCP kartu, kad sukurtumėte sklandų, AI pagrįstą dokumentacijos darbo procesą.

**Pavyzdiniai naudojimo atvejai:**
- Greitai pridėti nuorodas į README rašant kursą ar projekto dokumentaciją.
- Naudoti Copilot kodui generuoti ir MCP, kad iškart rastumėte ir cituotumėte atitinkamą dokumentaciją.
- Išlikti susikoncentravus redaktoriuje ir padidinti produktyvumą.

> [!IMPORTANT]
> Įsitikinkite, kad jūsų darbo aplinkoje yra galiojanti [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) konfigūracija (vietoje `.vscode/mcp.json`).

## Kodėl Chainlit 2 scenarijui?

Chainlit yra modernus atvirojo kodo karkasas, skirtas kurti pokalbių internetines aplikacijas. Jis leidžia lengvai sukurti pokalbių pagrindu veikiančias vartotojo sąsajas, kurios jungiasi prie galinių paslaugų, tokių kaip Microsoft Learn Docs MCP serveris. Šis projektas naudoja Chainlit, kad pateiktų paprastą, interaktyvų būdą realiu laiku generuoti asmeninius studijų planus. Naudodami Chainlit, galite greitai kurti ir diegti pokalbių pagrindu veikiančius įrankius, kurie didina produktyvumą ir mokymąsi.

## Ką ši aplikacija daro

Ši aplikacija leidžia vartotojams sukurti asmeninį studijų planą tiesiog įvedant temą ir trukmę. Aplikacija analizuoja jūsų įvestį, užklausia Microsoft Learn Docs MCP serverį dėl atitinkamo turinio ir organizuoja rezultatus į struktūrizuotą, savaitėmis suskirstytą planą. Kiekvienos savaitės rekomendacijos pateikiamos pokalbio lange, todėl lengva sekti ir stebėti savo pažangą. Integracija užtikrina, kad visada gausite naujausius ir aktualiausius mokymosi išteklius.

## Pavyzdinės užklausos

Išbandykite šias užklausas pokalbio lange, kad pamatytumėte, kaip aplikacija reaguoja:

- `AI-900 sertifikatas, 8 savaitės`
- `Sužinoti apie Azure Functions, 4 savaitės`
- `Azure DevOps, 6 savaitės`
- `Duomenų inžinerija Azure platformoje, 10 savaičių`
- `Microsoft saugumo pagrindai, 5 savaitės`
- `Power Platform, 7 savaitės`
- `Azure AI paslaugos, 12 savaičių`
- `Debesų architektūra, 9 savaitės`

Šie pavyzdžiai demonstruoja aplikacijos lankstumą skirtingiems mokymosi tikslams ir laikotarpiams.

## Nuorodos

- [Chainlit dokumentacija](https://docs.chainlit.io/)
- [MCP dokumentacija](https://github.com/MicrosoftDocs/mcp)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.