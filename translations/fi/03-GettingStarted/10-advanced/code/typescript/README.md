# Aja esimerkki

## Asenna riippuvuudet

```sh
npm install
```

## Rakenna se

```sh
npm run build
```

## Käynnistä se

```sh
npm start
```

Näet tekstin:

```text
Registering tools...
Starting server...
```

Hienoa, tämä tarkoittaa, että se käynnistyy oikein.

## Testaa palvelinta

Testaa ominaisuuksia seuraavalla komennolla:

```sh
npx @modelcontextprotocol/inspector node build/app.js
```

Tämän pitäisi käynnistää tarkastustyökalun verkkokäyttöliittymä.

### Testaa CLI-tilassa

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/list
```

Näet seuraavan tulosteen:

```json
{
  "tools": [
    {
      "name": "add",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "number"
          },
          "b": {
            "type": "number"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "additionalProperties": false,
        "$schema": "http://json-schema.org/draft-07/schema#"
      },
      "rawSchema": {
        "_def": {
          "unknownKeys": "strip",
          "catchall": {
            "_def": {
              "typeName": "ZodNever"
            },
            "~standard": {
              "version": 1,
              "vendor": "zod"
            }
          },
          "typeName": "ZodObject"
        },
        "~standard": {
          "version": 1,
          "vendor": "zod"
        },
        "_cached": null
      }
    },
    {
      "name": "subtract",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "number"
          },
          "b": {
            "type": "number"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "additionalProperties": false,
        "$schema": "http://json-schema.org/draft-07/schema#"
      },
      "rawSchema": {
        "_def": {
          "unknownKeys": "strip",
          "catchall": {
            "_def": {
              "typeName": "ZodNever"
            },
            "~standard": {
              "version": 1,
              "vendor": "zod"
            }
          },
          "typeName": "ZodObject"
        },
        "~standard": {
          "version": 1,
          "vendor": "zod"
        },
        "_cached": null
      }
    }
  ]
}
```

Aja työkalu:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

Näet vastauksen, joka on samankaltainen kuin:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Tool add called with arguments: {\"a\":1,\"b\":2}, result: {\"content\":[{\"type\":\"text\",\"text\":\"3\"}]}"
    }
  ]
```

Kokeile testata työkalua, jota ei ole olemassa, kuten "add2", tällä komennolla:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add2 --tool-arg a=1 --tool-arg b=2
```

Näet nyt tämän viestin, joka osoittaa, että validointi toimii:

```text
{
  "content": [],
  "error": {
    "code": "tool_not_found",
    "message": "Tool add2 not found."
  }
```

Kokeile myös lähettää parametri `c`, joka pitäisi hylätä skeeman perusteella, näin:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg c=2
```

Näet nyt "virheelliset argumentit" -virheen:

```text
{
  "content": [],
  "error": {
    "code": "invalid_arguments",
    "message": "Invalid arguments for tool add: [\n  {\n    \"code\": \"invalid_type\",\n    \"expected\": \"number\",\n    \"received\": \"undefined\",\n    \"path\": [\n      \"b\"\n    ],\n    \"message\": \"Required\"\n  }\n]"
  }
}
```

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.