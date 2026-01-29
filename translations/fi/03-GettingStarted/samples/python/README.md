# MCP-laskinpalvelin (Python)

Yksinkertainen Model Context Protocol (MCP) -palvelimen toteutus Pythonilla, joka tarjoaa peruslaskinominaisuuksia.

## Asennus

Asenna tarvittavat riippuvuudet:

```bash
pip install -r requirements.txt
```

Tai asenna MCP Python SDK suoraan:

```bash
pip install mcp>=1.18.0
```

## Käyttö

### Palvelimen käynnistäminen

Palvelin on suunniteltu MCP-asiakkaiden (kuten Claude Desktop) käytettäväksi. Käynnistä palvelin:

```bash
python mcp_calculator_server.py
```

**Huom**: Kun suoritat palvelimen suoraan terminaalissa, näet JSON-RPC-validointivirheitä. Tämä on normaalia - palvelin odottaa oikein muotoiltuja MCP-asiakasviestejä.

### Toimintojen testaaminen

Testataksesi, että laskin toimii oikein:

```bash
python test_calculator.py
```

## Vianmääritys

### Tuontivirheet

Jos näet `ModuleNotFoundError: No module named 'mcp'`, asenna MCP Python SDK:

```bash
pip install mcp>=1.18.0
```

### JSON-RPC-virheet suoraan suoritettaessa

Virheet, kuten "Invalid JSON: EOF while parsing a value", kun suoritat palvelimen suoraan, ovat odotettavissa. Palvelin tarvitsee MCP-asiakasviestejä, ei suoraa terminaalisyötettä.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.