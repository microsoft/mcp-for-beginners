# Tämän esimerkin suorittaminen

## -1- Asenna riippuvuudet

```bash
dotnet restore
```

## -2- Suorita esimerkki

```bash
dotnet run
```

## -3- Testaa esimerkkiä

Avaa erillinen terminaali ennen kuin suoritat alla olevan (varmista, että palvelin on edelleen käynnissä).

Kun palvelin on käynnissä yhdessä terminaalissa, avaa toinen terminaali ja suorita seuraava komento:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

Tämän pitäisi käynnistää verkkopalvelin, jossa on visuaalinen käyttöliittymä, jonka avulla voit testata esimerkkiä.

> Varmista, että **Streamable HTTP** on valittu kuljetustyypiksi ja URL-osoite on `http://localhost:3001/mcp`.

Kun palvelin on yhdistetty: 

- kokeile listata työkalut ja suorittaa `add` argumenteilla 2 ja 4, tuloksena pitäisi näkyä 6.
- siirry resursseihin ja resurssipohjaan ja kutsu "greeting", kirjoita nimi ja sinun pitäisi nähdä tervehdys antamallasi nimellä.

### Testaus CLI-tilassa

Voit käynnistää sen suoraan CLI-tilassa suorittamalla seuraavan komennon:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

Tämä listaa kaikki palvelimessa saatavilla olevat työkalut. Sinun pitäisi nähdä seuraava tuloste:

```text
{
  "tools": [
    {
      "name": "AddNumbers",
      "description": "Add two numbers together.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "description": "The first number",
            "type": "integer"
          },
          "b": {
            "description": "The second number",
            "type": "integer"
          }
        },
        "title": "AddNumbers",
        "description": "Add two numbers together.",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

Työkalun kutsumiseksi kirjoita:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
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
> On yleensä paljon nopeampaa käyttää tarkastajaa CLI-tilassa kuin selaimessa.
> Lue lisää tarkastajasta [täältä](https://github.com/modelcontextprotocol/inspector).

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.