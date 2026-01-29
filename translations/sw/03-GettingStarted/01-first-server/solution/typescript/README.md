# Kuendesha sampuli hii

Inapendekezwa usakinishe `uv` lakini si lazima, angalia [maelekezo](https://docs.astral.sh/uv/#highlights)

## -1- Sakinisha utegemezi

```bash
npm install
```

## -3- Endesha sampuli

```bash
npm run build
```

## -4- Jaribu sampuli

Ukiwa na seva inayoendesha kwenye terminal moja, fungua terminal nyingine na endesha amri ifuatayo:

```bash
npm run inspector
```

Hii itaanzisha seva ya wavuti yenye kiolesura cha kuona kinachokuruhusu kujaribu sampuli.

Mara seva inapounganishwa: 

- jaribu kuorodhesha zana na endesha `add`, ukiwa na hoja 2 na 4, unapaswa kuona 6 katika matokeo.
- nenda kwenye rasilimali na kiolezo cha rasilimali na uite "greeting", andika jina na unapaswa kuona salamu na jina ulilotoa.

### Kujaribu katika hali ya CLI

Kikagua ulichokimbia ni programu ya Node.js na `mcp dev` ni kifuniko kinachozunguka programu hiyo.

Unaweza kuianzisha moja kwa moja katika hali ya CLI kwa kuendesha amri ifuatayo:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

Hii itaorodhesha zana zote zinazopatikana kwenye seva. Unapaswa kuona matokeo yafuatayo:

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

Kuendesha zana andika:

```bash
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

Unapaswa kuona matokeo yafuatayo:

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
> Kwa kawaida ni haraka zaidi kuendesha kikagua katika hali ya CLI kuliko kwenye kivinjari.
> Soma zaidi kuhusu kikagua [hapa](https://github.com/modelcontextprotocol/inspector).

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asilia katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.