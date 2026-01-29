# Pokretanje ovog primjera

Preporučuje se instalirati `uv`, ali nije obavezno, pogledajte [upute](https://docs.astral.sh/uv/#highlights)

## -1- Instalirajte ovisnosti

```bash
npm install
```

## -3- Pokrenite primjer

```bash
npm run build
```

## -4- Testirajte primjer

Dok je server pokrenut u jednom terminalu, otvorite drugi terminal i pokrenite sljedeću naredbu:

```bash
npm run inspector
```

Ovo bi trebalo pokrenuti web server s vizualnim sučeljem koje vam omogućuje testiranje primjera.

Kada se server poveže:

- pokušajte popisati alate i pokrenuti `add`, s argumentima 2 i 4, trebali biste vidjeti rezultat 6.
- idite na resurse i predložak resursa te pozovite "greeting", unesite ime i trebali biste vidjeti pozdrav s imenom koje ste unijeli.

### Testiranje u CLI načinu rada

Inspektor koji ste pokrenuli zapravo je Node.js aplikacija, a `mcp dev` je omotač oko nje.

Možete ga pokrenuti izravno u CLI načinu rada pokretanjem sljedeće naredbe:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

Ovo će prikazati sve alate dostupne na serveru. Trebali biste vidjeti sljedeći izlaz:

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

Za pozivanje alata upišite:

```bash
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

Trebali biste vidjeti sljedeći izlaz:

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
> Obično je puno brže pokrenuti inspektor u CLI načinu rada nego u pregledniku.
> Više o inspektoru pročitajte [ovdje](https://github.com/modelcontextprotocol/inspector).

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.