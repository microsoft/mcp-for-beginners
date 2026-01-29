# Pokretanje ovog primjera

## -1- Instalirajte ovisnosti

```bash
dotnet restore
```

## -3- Pokrenite primjer

```bash
dotnet run
```

## -4- Testirajte primjer

Dok server radi u jednom terminalu, otvorite drugi terminal i pokrenite sljedeću naredbu:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Ovo bi trebalo pokrenuti web server s vizualnim sučeljem koje vam omogućuje testiranje primjera.

Kada se server poveže:

- pokušajte popisati alate i pokrenuti `add` s argumentima 2 i 4, trebali biste vidjeti 6 kao rezultat.
- idite na resurse i predložak resursa te pozovite "greeting", unesite ime i trebali biste vidjeti pozdrav s imenom koje ste unijeli.

### Testiranje u CLI načinu

Možete ga pokrenuti izravno u CLI načinu pokretanjem sljedeće naredbe:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

Ovo će prikazati popis svih alata dostupnih na serveru. Trebali biste vidjeti sljedeći izlaz:

```text
{
  "tools": [
    {
      "name": "Add",
      "description": "Adds two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "integer"
          },
          "b": {
            "type": "integer"
          }
        },
        "title": "Add",
        "description": "Adds two numbers",
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
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

Trebali biste vidjeti sljedeći izlaz:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Sum 3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> Obično je puno brže pokrenuti inspektor u CLI načinu nego u pregledniku.
> Pročitajte više o inspektoru [ovdje](https://github.com/modelcontextprotocol/inspector).

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.