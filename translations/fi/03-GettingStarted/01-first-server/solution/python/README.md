# Tämän esimerkin suorittaminen

Suosittelemme asentamaan `uv`, mutta se ei ole pakollista. Katso [ohjeet](https://docs.astral.sh/uv/#highlights)

## -0- Luo virtuaalinen ympäristö

```bash
python -m venv venv
```

## -1- Aktivoi virtuaalinen ympäristö

```bash
venv\Scripts\activate
```

## -2- Asenna riippuvuudet

```bash
pip install "mcp[cli]"
```

## -3- Suorita esimerkki

```bash
mcp run server.py
```

## -4- Testaa esimerkkiä

Kun palvelin on käynnissä yhdessä terminaalissa, avaa toinen terminaali ja suorita seuraava komento:

```bash
mcp dev server.py
```

Tämän pitäisi käynnistää verkkopalvelin, jossa on visuaalinen käyttöliittymä, jonka avulla voit testata esimerkkiä.

Kun palvelin on yhdistetty:

- kokeile listata työkalut ja suorita `add` argumenteilla 2 ja 4. Tuloksena pitäisi näkyä 6.

- siirry resurssit ja resurssimalli -osioon ja kutsu get_greeting. Kirjoita nimi, ja sinun pitäisi nähdä tervehdys antamallasi nimellä.

### Testaus CLI-tilassa

Käynnistämäsi tarkastaja on itse asiassa Node.js-sovellus, ja `mcp dev` on sen ympärille rakennettu käynnistysohjelma.

Voit käynnistää sen suoraan CLI-tilassa suorittamalla seuraavan komennon:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/list
```

Tämä listaa kaikki palvelimessa saatavilla olevat työkalut. Sinun pitäisi nähdä seuraava tuloste:

```text
{
  "tools": [
    {
      "name": "add",
      "description": "Add two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "addArguments"
      }
    }
  ]
}
```

Työkalun kutsumiseksi kirjoita:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

Sinun pitäisi nähdä seuraava tuloste:

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> Tarkastajan suorittaminen CLI-tilassa on yleensä paljon nopeampaa kuin selaimessa.
> Lue lisää tarkastajasta [täältä](https://github.com/modelcontextprotocol/inspector).

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.