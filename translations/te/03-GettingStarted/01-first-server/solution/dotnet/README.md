# ఈ నమూనాను నడపడం

## -1- ఆధారాలను ఇన్‌స్టాల్ చేయండి

```bash
dotnet restore
```

## -3- నమూనాను నడపండి


```bash
dotnet run
```

## -4- నమూనాను పరీక్షించండి

ఒక టెర్మినల్‌లో సర్వర్ నడుస్తున్నప్పుడు, మరో టెర్మినల్ తెరవండి మరియు క్రింది కమాండ్‌ను నడపండి:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

ఇది ఒక విజువల్ ఇంటర్‌ఫేస్‌తో కూడిన వెబ్ సర్వర్‌ను ప్రారంభించి, మీరు నమూనాను పరీక్షించడానికి అనుమతిస్తుంది.

సర్వర్ కనెక్ట్ అయిన తర్వాత:

- టూల్స్ జాబితా చేయడానికి ప్రయత్నించండి మరియు `add` ను ఆర్గ్స్ 2 మరియు 4 తో నడపండి, ఫలితంలో 6 కనిపించాలి.
- resources మరియు resource template కి వెళ్లి "greeting" ను పిలవండి, ఒక పేరు టైప్ చేయండి మరియు మీరు అందించిన పేరుతో ఒక అభివాదం కనిపిస్తుంది.

### CLI మోడ్‌లో పరీక్షించడం

క్రింది కమాండ్‌ను నడిపించి మీరు దీన్ని నేరుగా CLI మోడ్‌లో ప్రారంభించవచ్చు:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

ఇది సర్వర్‌లో అందుబాటులో ఉన్న అన్ని టూల్స్‌ను జాబితా చేస్తుంది. మీరు క్రింది అవుట్పుట్‌ను చూడాలి:

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

ఒక టూల్‌ను పిలవడానికి టైప్ చేయండి:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

మీరు క్రింది అవుట్పుట్‌ను చూడాలి:

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
> బ్రౌజర్ కంటే CLI మోడ్‌లో ఇన్స్పెక్టర్ నడపడం సాధారణంగా చాలా వేగంగా ఉంటుంది.
> ఇన్స్పెక్టర్ గురించి మరింత చదవండి [ఇక్కడ](https://github.com/modelcontextprotocol/inspector).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->