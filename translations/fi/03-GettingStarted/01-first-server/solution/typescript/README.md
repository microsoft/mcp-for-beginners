# Tämän esimerkin suorittaminen

Suositellaan asentamaan `uv`, mutta se ei ole pakollista. Katso [ohjeet](https://docs.astral.sh/uv/#highlights)

## -1- Asenna riippuvuudet

```bash
npm install
```

## -3- Suorita esimerkki

```bash
npm run build
```

## -4- Testaa esimerkkiä

Kun palvelin on käynnissä yhdessä terminaalissa, avaa toinen terminaali ja suorita seuraava komento:

```bash
npm run inspector
```

Tämän pitäisi käynnistää verkkopalvelin, jossa on visuaalinen käyttöliittymä, jonka avulla voit testata esimerkkiä.

Kun palvelin on yhdistetty:

- kokeile listata työkaluja ja suorita `add` argumenteilla 2 ja 4, sinun pitäisi nähdä tuloksena 6.
- siirry resursseihin ja resurssipohjaan ja kutsu "greeting", kirjoita nimi, ja sinun pitäisi nähdä tervehdys antamallasi nimellä.

### Testaaminen CLI-tilassa

Käyttämäsi tarkastustyökalu on itse asiassa Node.js-sovellus, ja `mcp dev` on sen ympärille rakennettu käynnistysskripti.

Voit käynnistää sen suoraan CLI-tilassa suorittamalla seuraavan komennon:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
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
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
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
> Tarkastustyökalun suorittaminen CLI-tilassa on yleensä paljon nopeampaa kuin selaimessa.
> Lue lisää tarkastustyökalusta [täältä](https://github.com/modelcontextprotocol/inspector).

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.