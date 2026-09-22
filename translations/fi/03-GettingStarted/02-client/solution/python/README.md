# Tämän esimerkin suorittaminen

Suositellaan asentamaan `uv`, mutta se ei ole pakollista, katso [ohjeet](https://docs.astral.sh/uv/#highlights)

## -0- Luo virtuaaliympäristö

```bash
python -m venv venv
```

## -1- Aktivoi virtuaaliympäristö

```bash
venv\Scripts\activate
```

## -2- Asenna riippuvuudet

```bash
pip install "mcp[cli]"
```

## -3- Suorita esimerkki

```bash
python client.py
```

Näet tulosteen, joka on samankaltainen kuin:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
INFO Processing request of type ListToolsRequest server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
INFO Processing request of type ReadResourceRequest server.py:534
CALL TOOL
INFO Processing request of type CallToolRequest server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->