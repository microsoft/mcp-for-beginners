# Tämän esimerkin suorittaminen

Näin suoritat klassisen HTTP-suoratoistopalvelimen ja -asiakkaan sekä MCP-suoratoistopalvelimen ja -asiakkaan Pythonilla.

### Yleiskatsaus

- Asetat MCP-palvelimen, joka lähettää etenemisilmoituksia asiakkaalle käsitellessään kohteita.
- Asiakas näyttää jokaisen ilmoituksen reaaliajassa.
- Tämä opas kattaa vaatimukset, asennuksen, suorittamisen ja vianmäärityksen.

### Vaatimukset

- Python 3.9 tai uudempi
- `mcp` Python-paketti (asenna komennolla `pip install mcp`)

### Asennus ja käyttöönotto

1. Kloonaa arkisto tai lataa ratkaisun tiedostot.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Luo ja aktivoi virtuaaliympäristö (suositeltavaa):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Asenna tarvittavat riippuvuudet:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Tiedostot

- **Palvelin:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **Asiakas:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Klassisen HTTP-suoratoistopalvelimen suorittaminen

1. Siirry ratkaisun hakemistoon:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Käynnistä klassinen HTTP-suoratoistopalvelin:

   ```pwsh
   python server.py
   ```

3. Palvelin käynnistyy ja näyttää:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Klassisen HTTP-suoratoistoasiakkaan suorittaminen

1. Avaa uusi pääte (aktivoi sama virtuaaliympäristö ja hakemisto):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Näet suoratoistetut viestit tulostettuna peräkkäin:

   ```text
   Running classic HTTP streaming client...
   Connecting to http://localhost:8000/stream with message: hello
   --- Streaming Progress ---
   Processing file 1/3...
   Processing file 2/3...
   Processing file 3/3...
   Here's the file content: hello
   --- Stream Ended ---
   ```

### MCP-suoratoistopalvelimen suorittaminen

1. Siirry ratkaisun hakemistoon:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. Käynnistä MCP-palvelin streamable-http-kuljetuksella:
   ```pwsh
   python server.py mcp
   ```
3. Palvelin käynnistyy ja näyttää:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### MCP-suoratoistoasiakkaan suorittaminen

1. Avaa uusi pääte (aktivoi sama virtuaaliympäristö ja hakemisto):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Näet ilmoitukset tulostettuna reaaliajassa, kun palvelin käsittelee kutakin kohdetta:
   ```
   Running MCP client...
   Starting client...
   Session ID before init: None
   Session ID after init: a30ab7fca9c84f5fa8f5c54fe56c9612
   Session initialized, ready to call tools.
   Received message: root=LoggingMessageNotification(...)
   NOTIFICATION: root=LoggingMessageNotification(...)
   ...
   Tool result: meta=None content=[TextContent(type='text', text='Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello from client')]
   ```

### Keskeiset toteutusvaiheet

1. **Luo MCP-palvelin FastMCP:llä.**
2. **Määritä työkalu, joka käsittelee listan ja lähettää ilmoituksia käyttämällä `ctx.info()` tai `ctx.log()`.**
3. **Suorita palvelin komennolla `transport="streamable-http"`.**
4. **Toteuta asiakas, jossa on viestinkäsittelijä ilmoitusten näyttämiseksi niiden saapuessa.**

### Koodin läpikäynti
- Palvelin käyttää asynkronisia funktioita ja MCP-kontekstia etenemispäivitysten lähettämiseen.
- Asiakas toteuttaa asynkronisen viestinkäsittelijän ilmoitusten ja lopputuloksen tulostamiseen.

### Vinkkejä ja vianmääritys

- Käytä `async/await` ei-estävissä operaatioissa.
- Käsittele aina poikkeukset sekä palvelimessa että asiakkaassa varmistaaksesi luotettavuuden.
- Testaa useilla asiakkailla nähdäksesi reaaliaikaiset päivitykset.
- Jos kohtaat virheitä, tarkista Python-versiosi ja varmista, että kaikki riippuvuudet on asennettu.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.