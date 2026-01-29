# ఈ నమూనాను నడపడం

ఈ నమూనాలో క్లయింట్‌పై LLM ఉండటం అవసరం. LLM కోసం మీరు దీన్ని Codespacesలో నడపాలి లేదా GitHubలో వ్యక్తిగత యాక్సెస్ టోకెన్‌ను సెట్ చేయాలి.

## -1- డిపెండెన్సీలను ఇన్‌స్టాల్ చేయండి

```bash
npm install
```

## -3- సర్వర్‌ను నడపండి


```bash
npm run build
```

## -4- క్లయింట్‌ను నడపండి

```sh
npm run client
```

మీకు ఈ విధంగా ఫలితం కనిపించాలి:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారుల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->