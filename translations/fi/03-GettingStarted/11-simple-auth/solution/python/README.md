# Suorita esimerkki

## Luo ympäristö

```sh
python -m venv venv
source ./venv/bin/activate
```

## Asenna riippuvuudet

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Luo tunnus

Sinun täytyy luoda tunnus, jota asiakas käyttää kommunikoidakseen palvelimen kanssa.

Kutsu:

```sh
python util.py
```

## Suorita koodi

Suorita koodi komennolla:

```sh
python server.py
```

Avaa erillinen pääte ja kirjoita:

```sh
python client.py
```

Palvelimen pääteikkunassa pitäisi näkyä jotain tällaista:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

Asiakkaan ikkunassa pitäisi näkyä tekstiä, joka muistuttaa seuraavaa:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

Tämä tarkoittaa, että kaikki toimii.

### Muuta tietoja, jotta näet virheen

Etsi tämä koodi tiedostosta *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Muuta se niin, että siinä lukee "User.Write". Nykyisellä tunnuksellasi ei ole tätä käyttöoikeustasoa, joten jos käynnistät palvelimen uudelleen ja yrität suorittaa asiakkaan uudelleen, palvelimen pääteikkunassa pitäisi näkyä virhe, joka muistuttaa seuraavaa:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Voit joko palauttaa palvelimen koodin alkuperäiseen tilaan tai luoda uuden tunnuksen, joka sisältää tämän lisäoikeuden, valinta on sinun.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.