# Pokretanje ovog primjera

## -1- Instalirajte ovisnosti

```bash
dotnet restore
```

## -2- Pokrenite primjer

```bash
dotnet run
```

## -3- Testirajte primjer

Pokrenite zaseban terminal prije nego što izvršite naredbu ispod (provjerite je li poslužitelj još uvijek pokrenut).

Dok je poslužitelj pokrenut u jednom terminalu, otvorite drugi terminal i izvršite sljedeću naredbu:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

Ovo bi trebalo pokrenuti web poslužitelj s vizualnim sučeljem koje vam omogućuje testiranje primjera.

> Provjerite da je **Streamable HTTP** odabran kao vrsta prijenosa, a URL je `http://localhost:3001/mcp`.

Kada se poslužitelj poveže:

- pokušajte popisati alate i pokrenuti `add`, s argumentima 2 i 4, trebali biste vidjeti rezultat 6.
- idite na resurse i predložak resursa te pozovite "greeting", unesite ime i trebali biste vidjeti pozdrav s imenom koje ste unijeli.

### Testiranje u CLI načinu

Možete ga pokrenuti izravno u CLI načinu izvršavanjem sljedeće naredbe:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

Ovo će prikazati popis svih dostupnih alata na poslužitelju. Trebali biste vidjeti sljedeći izlaz:

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

Za pozivanje alata unesite:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
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
> Obično je puno brže pokrenuti inspektor u CLI načinu nego u pregledniku.
> Više o inspektoru pročitajte [ovdje](https://github.com/modelcontextprotocol/inspector).

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za bilo kakva pogrešna tumačenja ili nesporazume koji mogu proizaći iz korištenja ovog prijevoda.