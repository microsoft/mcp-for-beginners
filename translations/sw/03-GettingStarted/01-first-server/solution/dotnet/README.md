# Kuendesha sampuli hii

## -1- Sakinisha utegemezi

```bash
dotnet restore
```

## -3- Endesha sampuli

```bash
dotnet run
```

## -4- Jaribu sampuli

Ukiwa na seva inayoendesha kwenye terminal moja, fungua terminal nyingine na endesha amri ifuatayo:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Hii inapaswa kuanzisha seva ya wavuti yenye kiolesura cha kuona kinachokuruhusu kujaribu sampuli.

Mara seva inapounganishwa: 

- jaribu kuorodhesha zana na endesha `add`, ukiwa na hoja 2 na 4, unapaswa kuona 6 katika matokeo.
- nenda kwenye rasilimali na kiolezo cha rasilimali na uite "greeting", andika jina na unapaswa kuona salamu na jina ulilotoa.

### Kujaribu katika hali ya CLI

Unaweza kuizindua moja kwa moja katika hali ya CLI kwa kuendesha amri ifuatayo:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

Hii itaorodhesha zana zote zinazopatikana kwenye seva. Unapaswa kuona matokeo yafuatayo:

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

Kuendesha zana andika:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

Unapaswa kuona matokeo yafuatayo:

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
> Kwa kawaida ni haraka zaidi kuendesha inspector katika hali ya CLI kuliko kwenye kivinjari.
> Soma zaidi kuhusu inspector [hapa](https://github.com/modelcontextprotocol/inspector).

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.