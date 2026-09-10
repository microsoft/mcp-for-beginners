# MCP-laskinpalvelin (Python)



Yksinkertainen Model Context Protocol (MCP) -palvelimen toteutus Pythonilla, joka tarjoaa peruslaskin-toiminnallisuuden.


## Asennus

Asenna tarvittavat riippuvuudet:

```bash
pip install -r requirements.txt
```

Tai asenna MCP Python SDK suoraan:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Käyttö

### Palvelimen käynnistäminen

Palvelin on suunniteltu käytettäväksi MCP-asiakkaiden (kuten Claude Desktop) toimesta. Käynnistääksesi palvelimen:

```bash
python mcp_calculator_server.py
```

**Huom:** Kun suoritat suoraan komentorivillä, näet JSON-RPC-validointivirheitä. Tämä on normaalia käytöstä – palvelin odottaa MCP-asiakasviestejä, jotka on muotoiltu oikein.

### Funktioiden testaaminen

Testataksesi, että laskinfunktiot toimivat oikein:

```bash
python test_calculator.py
```

## Vianmääritys

### Tuontivirheet

Jos näet `ModuleNotFoundError: No module named 'mcp'`, asenna MCP Python SDK:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### JSON-RPC-virheet suoritettaessa suoraan

Virheet kuten "Invalid JSON: EOF while parsing a value" suoritettaessa palvelin suoraan ovat odotettavissa. Palvelin tarvitsee MCP-asiakasviestejä, ei suoraa komentorivisyöttöä.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->