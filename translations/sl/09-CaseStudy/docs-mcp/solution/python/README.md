# Generator načrta učenja z Chainlit in Microsoft Learn Docs MCP

## Predpogoji

- Python 3.8 ali novejši
- pip (upravitelj paketov za Python)
- Dostop do interneta za povezavo s strežnikom Microsoft Learn Docs MCP

## Namestitev

1. Klonirajte to repozitorij ali prenesite projektne datoteke.
2. Namestite potrebne odvisnosti:

   ```bash
   pip install -r requirements.txt
   ```

## Uporaba

### Scenarij 1: Preprosto poizvedovanje v Docs MCP
Odjemalec ukazne vrstice, ki se poveže s strežnikom Docs MCP, pošlje poizvedbo in prikaže rezultat.

1. Zaženite skripto:
   ```bash
   python scenario1.py
   ```
2. Na poziv vnesite svoje vprašanje o dokumentaciji.

### Scenarij 2: Generator načrta učenja (Chainlit spletna aplikacija)
Spletni vmesnik (z uporabo Chainlit), ki uporabnikom omogoča ustvarjanje personaliziranega, tedenskega načrta učenja za katerokoli tehnično temo.

1. Zaženite aplikacijo Chainlit:
   ```bash
   chainlit run scenario2.py
   ```
2. Odprite lokalni URL, ki se prikaže v vašem terminalu (npr. http://localhost:8000), v brskalniku.
3. V pogovornem oknu vnesite svojo temo učenja in število tednov, ki jih želite posvetiti učenju (npr. "AI-900 certifikacija, 8 tednov").
4. Aplikacija bo odgovorila s tedenskim načrtom učenja, ki vključuje povezave do ustrezne dokumentacije Microsoft Learn.

**Potrebne okoljske spremenljivke:**

Za uporabo scenarija 2 (Chainlit spletna aplikacija z Azure OpenAI) morate nastaviti naslednje okoljske spremenljivke v datoteki `.env` v imeniku `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Pred zagonom aplikacije izpolnite te vrednosti s podrobnostmi o vašem Azure OpenAI viru.

> [!TIP]
> Svoje modele lahko preprosto uvedete z uporabo [Azure AI Foundry](https://ai.azure.com/).

### Scenarij 3: Dokumentacija v urejevalniku z MCP strežnikom v VS Code

Namesto preklapljanja med zavihki brskalnika za iskanje dokumentacije lahko Microsoft Learn Docs pripeljete neposredno v svoj VS Code z uporabo MCP strežnika. To vam omogoča:
- Iskanje in branje dokumentacije znotraj VS Code brez zapuščanja programskega okolja.
- Sklicevanje na dokumentacijo in vstavljanje povezav neposredno v README ali datoteke tečajev.
- Uporabo GitHub Copilot in MCP skupaj za brezhiben, z umetno inteligenco podprt delovni tok dokumentacije.

**Primeri uporabe:**
- Hitro dodajanje referenčnih povezav v README med pisanjem tečaja ali projektne dokumentacije.
- Uporaba Copilota za generiranje kode in MCP za takojšnje iskanje ter navajanje ustrezne dokumentacije.
- Osredotočenost v urejevalniku in povečanje produktivnosti.

> [!IMPORTANT]
> Prepričajte se, da imate veljavno konfiguracijo [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) v svojem delovnem prostoru (lokacija je `.vscode/mcp.json`).

## Zakaj Chainlit za scenarij 2?

Chainlit je sodoben odprtokodni okvir za gradnjo pogovornih spletnih aplikacij. Omogoča enostavno ustvarjanje klepetalnih uporabniških vmesnikov, ki se povezujejo z zalednimi storitvami, kot je Microsoft Learn Docs MCP strežnik. Ta projekt uporablja Chainlit za zagotavljanje preprostega, interaktivnega načina za ustvarjanje personaliziranih načrtov učenja v realnem času. Z uporabo Chainlit lahko hitro zgradite in uvedete klepetalne orodja, ki izboljšujejo produktivnost in učenje.

## Kaj omogoča ta aplikacija

Ta aplikacija uporabnikom omogoča ustvarjanje personaliziranega načrta učenja z enostavnim vnosom teme in trajanja. Aplikacija obdela vaš vnos, pošlje poizvedbo strežniku Microsoft Learn Docs MCP za ustrezno vsebino in organizira rezultate v strukturiran, tedenski načrt. Priporočila za vsak teden so prikazana v klepetu, kar omogoča enostavno sledenje in spremljanje napredka. Integracija zagotavlja, da vedno prejmete najnovejše in najbolj relevantne vire za učenje.

## Primeri poizvedb

Preizkusite te poizvedbe v klepetalnem oknu, da vidite, kako aplikacija odgovarja:

- `AI-900 certifikacija, 8 tednov`
- `Nauči se Azure Functions, 4 tedne`
- `Azure DevOps, 6 tednov`
- `Podatkovno inženirstvo na Azure, 10 tednov`
- `Microsoft varnostni temelji, 5 tednov`
- `Power Platform, 7 tednov`
- `Azure AI storitve, 12 tednov`
- `Oblačna arhitektura, 9 tednov`

Ti primeri prikazujejo prilagodljivost aplikacije za različne učne cilje in časovne okvire.

## Reference

- [Chainlit Dokumentacija](https://docs.chainlit.io/)
- [MCP Dokumentacija](https://github.com/MicrosoftDocs/mcp)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.