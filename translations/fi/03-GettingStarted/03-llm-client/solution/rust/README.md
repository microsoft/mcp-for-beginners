# Tämän esimerkin suorittaminen

Tämä on Rust-ratkaisu LLM-asiakasnäytteelle. Sinulla tulee olla asennettuna Rust-työkaluketju; katso [virallinen asennusopas](https://www.rust-lang.org/tools/install).

Asiakas kutsuu käyttöön otettua Microsoft Foundry -mallia Azure OpenAI
v1-päätepisteen kautta.

> [!NOTE]
> Arvo, joka välitetään `model`, on Foundry-käyttöönottosi nimi, ei välttämättä
> varsinaisen mallin nimi.

## -0- Määritä Microsoft Foundry

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<api-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<resource-name>.openai.azure.com"
$env:AZURE_OPENAI_API_KEY = "<api-key>"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5.1"
```

## -1- Rakenna esimerkki

```bash
cargo build
```

## -2- Suorita esimerkki

```bash
cargo run
```

Asiakas käynnistää laskin-MCP-palvelimen, hakee sen työkaluluettelon ja käyttää
käyttöön otettua mallia kutsuakseen `add`-työkalua. Näet tulostuksen, joka ilmaisee
työkalukutsun (esimerkiksi "Calling tool: add") ja kutsun tuloksen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->