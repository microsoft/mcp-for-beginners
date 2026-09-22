# Aja esimerkki

> [!WARNING]
> Tämä esimerkki käyttää vanhentunutta Sampling-menetelmää ja perintö HTTP+SSE -päätepistettä. Se on
> säilytetty MCP `2025-11-25` -yhteensopivuuden vuoksi. Uusien toteutusten tulisi kutsua
> LLM-palveluntarjoajaa suoraan ja käyttää Streamable HTTP:tä etä-MCP-liikenteeseen.

## Luo virtuaaliympäristö

```sh
python -m venv venv
source ./venv/bin/activate
```

## Asenna riippuvuudet

```sh
pip install "mcp[cli]"
```

## Käynnistä palvelin

```sh
uvicorn server:app --port 8000
```

## Testaa palvelinta GitHub Copilotilla ja VS Codella

Lisää merkintä mcp.json-tiedostoon seuraavasti:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

Varmista, että napsautat "start" palvelimella.

Liitä GitHub Copilotiin seuraava kehotus:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

Ensimmäisellä kerralla sinulta kysytään, haluatko hyväksyä Sampling-toiminnon, sitten sinua pyydetään hyväksymään työkalu "create_blog" suoritettavaksi. Sinun tulisi nähdä vastaus, joka on samanlainen kuin:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->