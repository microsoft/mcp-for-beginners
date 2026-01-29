# Käynnistä esimerkki

Tämä esimerkki käynnistää MCP-palvelimen, jossa on välimuisti, joka tarkistaa, että Authorization-otsikko on kelvollinen.

## Asenna riippuvuudet

```bash
pip install "mcp[cli]" 
```

## Käynnistä palvelin

```bash
python server.py
```

käynnistä asiakas toisessa terminaalissa

```bash
python client.py
```

Sinun pitäisi nähdä tulos, joka näyttää tältä:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

tämä tarkoittaa, että lähetetty tunniste hyväksytään.

Kokeile vaihtaa tunniste `client.py`-tiedostossa "secret-token2":ksi, jolloin sinun pitäisi nähdä tämä teksti osana vastausta:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

tämä tarkoittaa, että sinut tunnistettiin (sinulla oli tunniste), mutta se oli virheellinen.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.