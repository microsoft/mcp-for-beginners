# ఈ నమూనాను నడపడం

## -1- ఆధారాలను ఇన్‌స్టాల్ చేయండి

```bash
dotnet restore
```

## -2- నమూనాను నడపండి

```bash
dotnet run
```

## -3- నమూనాను పరీక్షించండి

క్రింద ఇచ్చినది నడిపే ముందు వేరే టెర్మినల్ ప్రారంభించండి (సర్వర్ ఇంకా నడుస్తున్నదని నిర్ధారించుకోండి).

ఒక టెర్మినల్‌లో సర్వర్ నడుస్తున్నప్పుడు, మరో టెర్మినల్ తెరవండి మరియు క్రింది కమాండ్ నడపండి:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

ఇది ఒక విజువల్ ఇంటర్‌ఫేస్‌తో కూడిన వెబ్ సర్వర్‌ను ప్రారంభించి, మీరు నమూనాను పరీక్షించడానికి అనుమతిస్తుంది.

> **Streamable HTTP** ట్రాన్స్‌పోర్ట్ రకం గా ఎంచుకున్నదని మరియు URL `http://localhost:3001/mcp` అని నిర్ధారించుకోండి.

సర్వర్ కనెక్ట్ అయిన తర్వాత:

- టూల్స్ జాబితా చేయడానికి ప్రయత్నించండి మరియు `add` ను ఆర్గ్స్ 2 మరియు 4 తో నడపండి, ఫలితంగా 6 కనిపించాలి.
- resources మరియు resource template కి వెళ్లి "greeting" ను పిలవండి, ఒక పేరు టైప్ చేయండి, మీరు ఇచ్చిన పేరుతో గ్రీటింగ్ కనిపిస్తుంది.

### CLI మోడ్‌లో పరీక్షించడం

క్రింది కమాండ్ నడిపి మీరు దీన్ని నేరుగా CLI మోడ్‌లో ప్రారంభించవచ్చు:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

ఇది సర్వర్‌లో అందుబాటులో ఉన్న అన్ని టూల్స్‌ను జాబితా చేస్తుంది. మీరు క్రింది అవుట్పుట్ చూడాలి:

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

ఒక టూల్‌ను పిలవడానికి టైప్ చేయండి:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

మీరు క్రింది అవుట్పుట్ చూడాలి:

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
> బ్రౌజర్ కంటే CLI మోడ్‌లో ఇన్స్పెక్టర్ నడపడం సాధారణంగా చాలా వేగంగా ఉంటుంది.
> ఇన్స్పెక్టర్ గురించి మరింత చదవండి [ఇక్కడ](https://github.com/modelcontextprotocol/inspector).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలోనే అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారుల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->