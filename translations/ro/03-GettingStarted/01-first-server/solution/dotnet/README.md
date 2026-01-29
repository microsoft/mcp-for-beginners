# Rularea acestui exemplu

## -1- Instalează dependențele

```bash
dotnet restore
```

## -3- Rulează exemplul

```bash
dotnet run
```

## -4- Testează exemplul

Cu serverul pornit într-un terminal, deschide un alt terminal și rulează următoarea comandă:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Aceasta ar trebui să pornească un server web cu o interfață vizuală care îți permite să testezi exemplul.

Odată ce serverul este conectat:

- încearcă să listezi uneltele și rulează `add`, cu argumentele 2 și 4; ar trebui să vezi 6 în rezultat.
- mergi la resurse și șablonul de resurse și apelează "greeting", introdu un nume și ar trebui să vezi un mesaj de salut cu numele pe care l-ai furnizat.

### Testarea în modul CLI

Poți să-l lansezi direct în modul CLI rulând următoarea comandă:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

Aceasta va lista toate uneltele disponibile pe server. Ar trebui să vezi următorul output:

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

Pentru a apela o unealtă, tastează:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

Ar trebui să vezi următorul output:

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
> De obicei, este mult mai rapid să rulezi inspectorul în modul CLI decât în browser.
> Citește mai multe despre inspector [aici](https://github.com/modelcontextprotocol/inspector).

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.