# Kuendesha sampuli hii

## -1- Sakinisha utegemezi

```bash
dotnet restore
```

## -2- Endesha sampuli

```bash
dotnet run
```

## -3- Jaribu sampuli

Fungua terminal tofauti kabla ya kuendesha amri zifuatazo (hakikisha seva bado inaendelea).

Ukiwa na seva inayoendelea kwenye terminal moja, fungua terminal nyingine na endesha amri ifuatayo:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

Hii itaanzisha seva ya wavuti yenye kiolesura cha kuona kinachokuruhusu kujaribu sampuli.

> Hakikisha kuwa **Streamable HTTP** imechaguliwa kama aina ya usafirishaji, na URL ni `http://localhost:3001/mcp`.

Mara seva inapounganishwa: 

- jaribu kuorodhesha zana na endesha `add`, ukiwa na hoja 2 na 4, unapaswa kuona 6 kama matokeo.
- nenda kwenye rasilimali na kiolezo cha rasilimali na uite "greeting", andika jina na unapaswa kuona salamu na jina ulilotoa.

### Kujaribu katika hali ya CLI

Unaweza kuizindua moja kwa moja katika hali ya CLI kwa kuendesha amri ifuatayo:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

Hii itaorodhesha zana zote zinazopatikana kwenye seva. Unapaswa kuona matokeo yafuatayo:

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

Ili kuitisha zana andika:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
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
> Kwa kawaida ni haraka zaidi kuendesha inspector katika hali ya CLI kuliko kwenye kivinjari.
> Soma zaidi kuhusu inspector [hapa](https://github.com/modelcontextprotocol/inspector).

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.