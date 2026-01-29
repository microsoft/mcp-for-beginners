# Opintosuunnitelman luontityökalu Chainlitillä ja Microsoft Learn Docs MCP:llä

## Esivaatimukset

- Python 3.8 tai uudempi
- pip (Pythonin pakettienhallinta)
- Internet-yhteys Microsoft Learn Docs MCP -palvelimeen yhdistämistä varten

## Asennus

1. Kloonaa tämä repositorio tai lataa projektitiedostot.
2. Asenna tarvittavat riippuvuudet:

   ```bash
   pip install -r requirements.txt
   ```

## Käyttö

### Skenaario 1: Yksinkertainen kysely Docs MCP:lle
Komentoriviohjelma, joka yhdistyy Docs MCP -palvelimeen, lähettää kyselyn ja tulostaa tuloksen.

1. Suorita skripti:
   ```bash
   python scenario1.py
   ```
2. Syötä dokumentaatiokysymyksesi kehotteeseen.

### Skenaario 2: Opintosuunnitelman luontityökalu (Chainlit-verkkosovellus)
Verkkopohjainen käyttöliittymä (Chainlitin avulla), jonka avulla käyttäjät voivat luoda henkilökohtaisen, viikko viikolta etenevän opintosuunnitelman mihin tahansa tekniseen aiheeseen.

1. Käynnistä Chainlit-sovellus:
   ```bash
   chainlit run scenario2.py
   ```
2. Avaa terminaalissa annettu paikallinen URL-osoite (esim. http://localhost:8000) selaimessasi.
3. Chat-ikkunassa syötä opiskeltava aihe ja viikkojen määrä, jonka haluat käyttää (esim. "AI-900-sertifikaatti, 8 viikkoa").
4. Sovellus vastaa viikko viikolta etenevällä opintosuunnitelmalla, joka sisältää linkkejä asiaankuuluvaan Microsoft Learn -dokumentaatioon.

**Vaadittavat ympäristömuuttujat:**

Jotta voit käyttää skenaariota 2 (Chainlit-verkkosovellus Azure OpenAI:n kanssa), sinun on asetettava seuraavat ympäristömuuttujat `.env`-tiedostoon `python`-hakemistossa:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Täytä nämä arvot Azure OpenAI -resurssisi tiedoilla ennen sovelluksen suorittamista.

> [!TIP]
> Voit helposti ottaa käyttöön omia malleja [Azure AI Foundryn](https://ai.azure.com/) avulla.

### Skenaario 3: Dokumentaatio suoraan editorissa MCP-palvelimen avulla VS Codessa

Sen sijaan, että vaihtaisit selaimen välilehtiä etsiäksesi dokumentaatiota, voit tuoda Microsoft Learn Docs -sisällön suoraan VS Codeen MCP-palvelimen avulla. Tämä mahdollistaa:
- Dokumentaation etsimisen ja lukemisen suoraan VS Codessa ilman, että poistut koodausympäristöstä.
- Dokumentaatioviitteiden lisäämisen ja linkkien upottamisen suoraan README- tai kurssitiedostoihin.
- GitHub Copilotin ja MCP:n käytön yhdessä saumattoman, tekoälypohjaisen dokumentaatiotyönkulun luomiseksi.

**Esimerkkikäyttötapaukset:**
- Lisää nopeasti viitelinkkejä README-tiedostoon kirjoittaessasi kurssi- tai projektidokumentaatiota.
- Käytä Copilotia koodin luomiseen ja MCP:tä löytääksesi ja viitataksesi asiaankuuluvaan dokumentaatioon välittömästi.
- Pysy keskittyneenä editorissa ja paranna tuottavuutta.

> [!IMPORTANT]
> Varmista, että sinulla on kelvollinen [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) -konfiguraatio työtilassasi (sijainti on `.vscode/mcp.json`).

## Miksi Chainlit skenaariossa 2?

Chainlit on moderni avoimen lähdekoodin kehys keskustelupohjaisten verkkosovellusten rakentamiseen. Sen avulla on helppo luoda chat-pohjaisia käyttöliittymiä, jotka yhdistyvät taustapalveluihin, kuten Microsoft Learn Docs MCP -palvelimeen. Tämä projekti käyttää Chainlitiä tarjotakseen yksinkertaisen, interaktiivisen tavan luoda henkilökohtaisia opintosuunnitelmia reaaliajassa. Chainlitin avulla voit nopeasti rakentaa ja ottaa käyttöön chat-pohjaisia työkaluja, jotka parantavat tuottavuutta ja oppimista.

## Mitä tämä tekee

Tämä sovellus mahdollistaa käyttäjien henkilökohtaisen opintosuunnitelman luomisen yksinkertaisesti syöttämällä aiheen ja keston. Sovellus jäsentää syötteen, tekee kyselyn Microsoft Learn Docs MCP -palvelimelle asiaankuuluvasta sisällöstä ja järjestää tulokset rakenteelliseksi, viikko viikolta eteneväksi suunnitelmaksi. Jokaisen viikon suositukset näytetään chatissa, mikä tekee niiden seuraamisesta ja edistymisen seuraamisesta helppoa. Integraatio varmistaa, että saat aina uusimmat ja asiaankuuluvimmat oppimisresurssit.

## Esimerkkikyselyt

Kokeile näitä kyselyitä chat-ikkunassa nähdäksesi, miten sovellus vastaa:

- `AI-900-sertifikaatti, 8 viikkoa`
- `Opi Azure Functions, 4 viikkoa`
- `Azure DevOps, 6 viikkoa`
- `Data engineering Azurella, 10 viikkoa`
- `Microsoftin tietoturvan perusteet, 5 viikkoa`
- `Power Platform, 7 viikkoa`
- `Azure AI -palvelut, 12 viikkoa`
- `Pilviarkkitehtuuri, 9 viikkoa`

Nämä esimerkit osoittavat sovelluksen joustavuuden eri oppimistavoitteiden ja aikataulujen suhteen.

## Viitteet

- [Chainlit-dokumentaatio](https://docs.chainlit.io/)
- [MCP-dokumentaatio](https://github.com/MicrosoftDocs/mcp)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.