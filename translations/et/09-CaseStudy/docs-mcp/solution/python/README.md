# Õppeplaani generaator Chainlitiga ja Microsoft Learn Docs MCP-ga

## Eeltingimused

- Python 3.8 või uuem
- pip (Python pakettide haldur)
- Internetiühendus, et ühendada Microsoft Learn Docs MCP serveriga

## Paigaldamine

1. Klooni see repositoorium või laadi alla projekti failid.
2. Paigalda vajalikud sõltuvused:

   ```bash
   pip install -r requirements.txt
   ```

## Kasutamine

### Stsenaarium 1: Lihtne päring Docs MCP-le
Käsurea klient, mis ühendub Docs MCP serveriga, saadab päringu ja kuvab tulemuse.

1. Käivita skript:
   ```bash
   python scenario1.py
   ```
2. Sisesta oma dokumentatsiooni küsimus käsurea viipas.

### Stsenaarium 2: Õppeplaani generaator (Chainlit veebirakendus)
Veebipõhine liides (kasutades Chainlitit), mis võimaldab kasutajatel luua isikupärastatud, nädalate kaupa jaotatud õppeplaani mis tahes tehnilise teema jaoks.

1. Käivita Chainlit rakendus:
   ```bash
   chainlit run scenario2.py
   ```
2. Ava terminalis antud kohalik URL (nt http://localhost:8000) oma brauseris.
3. Vestlusaknas sisesta oma õppe teema ja nädalate arv, mille jooksul soovid õppida (nt "AI-900 sertifikaat, 8 nädalat").
4. Rakendus vastab nädalate kaupa jaotatud õppeplaaniga, mis sisaldab linke asjakohasele Microsoft Learn dokumentatsioonile.

**Vajalikud keskkonnamuutujad:**

Et kasutada stsenaariumi 2 (Chainlit veebirakendus Azure OpenAI-ga), tuleb `.env` failis `python` kataloogis määrata järgmised keskkonnamuutujad:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Täida need väärtused oma Azure OpenAI ressursi andmetega enne rakenduse käivitamist.

> [!TIP]
> Oma mudelite juurutamine on lihtne, kasutades [Azure AI Foundry](https://ai.azure.com/).

### Stsenaarium 3: Dokumentatsioon otse VS Code'is MCP serveriga

Selle asemel, et vahetada brauseri vahelehti dokumentatsiooni otsimiseks, saad tuua Microsoft Learn Docs otse VS Code'i. See võimaldab:
- Otsida ja lugeda dokumentatsiooni otse VS Code'is, ilma et peaksid oma koodikeskkonnast lahkuma.
- Viidata dokumentatsioonile ja lisada linke otse oma README-sse või kursuse failidesse.
- Kasutada GitHub Copilotit ja MCP-d koos, et luua sujuv, AI-põhine dokumentatsiooni töövoog.

**Näited kasutusjuhtudest:**
- Lisa kiiresti viitelinke README-sse, kui kirjutad kursust või projekti dokumentatsiooni.
- Kasuta Copilotit koodi genereerimiseks ja MCP-d, et koheselt leida ja viidata asjakohasele dokumentatsioonile.
- Püsi keskendunud oma redaktoris ja suurenda produktiivsust.

> [!IMPORTANT]
> Veendu, et sul oleks kehtiv [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) konfiguratsioon oma tööruumis (asukoht on `.vscode/mcp.json`).

## Miks kasutada Chainlitit stsenaariumis 2?

Chainlit on kaasaegne avatud lähtekoodiga raamistik vestluspõhiste veebirakenduste loomiseks. See muudab lihtsaks vestlusliideste loomise, mis ühenduvad taustateenustega, nagu Microsoft Learn Docs MCP server. See projekt kasutab Chainlitit, et pakkuda lihtsat ja interaktiivset viisi isikupärastatud õppeplaanide reaalajas genereerimiseks. Chainlitit kasutades saad kiiresti luua ja juurutada vestluspõhiseid tööriistu, mis suurendavad produktiivsust ja õppimist.

## Mida see rakendus teeb

See rakendus võimaldab kasutajatel luua isikupärastatud õppeplaani, sisestades lihtsalt teema ja kestuse. Rakendus analüüsib sinu sisestust, pärib Microsoft Learn Docs MCP serverist asjakohast sisu ja korraldab tulemused struktureeritud, nädalate kaupa jaotatud plaaniks. Iga nädala soovitused kuvatakse vestluses, muutes nende järgimise ja edusammude jälgimise lihtsaks. Integreerimine tagab, et saad alati kõige värskema ja asjakohasema õppematerjali.

## Näidispäringud

Proovi neid päringuid vestlusaknas, et näha, kuidas rakendus vastab:

- `AI-900 sertifikaat, 8 nädalat`
- `Õpi Azure Functions, 4 nädalat`
- `Azure DevOps, 6 nädalat`
- `Andmeinseneeria Azure'is, 10 nädalat`
- `Microsofti turvalisuse alused, 5 nädalat`
- `Power Platform, 7 nädalat`
- `Azure AI teenused, 12 nädalat`
- `Pilvearhitektuur, 9 nädalat`

Need näited näitavad rakenduse paindlikkust erinevate õppeeesmärkide ja ajaraamide jaoks.

## Viited

- [Chainlit dokumentatsioon](https://docs.chainlit.io/)
- [MCP dokumentatsioon](https://github.com/MicrosoftDocs/mcp)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.