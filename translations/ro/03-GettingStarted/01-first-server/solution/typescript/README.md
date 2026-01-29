# Rularea acestui exemplu

Se recomandă instalarea `uv`, dar nu este obligatoriu, vezi [instrucțiuni](https://docs.astral.sh/uv/#highlights)

## -1- Instalează dependențele

```bash
npm install
```

## -3- Rulează exemplul

```bash
npm run build
```

## -4- Testează exemplul

Cu serverul pornit într-un terminal, deschide un alt terminal și rulează următoarea comandă:

```bash
npm run inspector
```

Aceasta ar trebui să pornească un server web cu o interfață vizuală care îți permite să testezi exemplul.

Odată ce serverul este conectat:

- încearcă să listezi uneltele și să rulezi `add`, cu argumentele 2 și 4, ar trebui să vezi 6 în rezultat.
- mergi la resurse și șablonul de resurse și apelează "greeting", introdu un nume și ar trebui să vezi un mesaj de salut cu numele pe care l-ai furnizat.

### Testarea în modul CLI

Inspectorul pe care l-ai rulat este de fapt o aplicație Node.js, iar `mcp dev` este un wrapper în jurul acesteia.

Poți să-l lansezi direct în modul CLI rulând următoarea comandă:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

Aceasta va lista toate uneltele disponibile pe server. Ar trebui să vezi următorul output:

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

Pentru a apela o unealtă, tastează:

```bash
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

Ar trebui să vezi următorul output:

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
> De obicei, este mult mai rapid să rulezi inspectorul în modul CLI decât în browser.
> Citește mai multe despre inspector [aici](https://github.com/modelcontextprotocol/inspector).

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.