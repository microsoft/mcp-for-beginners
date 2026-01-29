# నమూనా నడపండి

## ఆధారాలు ఇన్‌స్టాల్ చేయండి

```sh
npm install
```

## నిర్మించండి

```sh
npm run build
```

## టోకెన్లు సృష్టించండి

```sh
npm run generate
```

ఇది *.env* ఫైల్‌లో ఒక టోకెన్‌ను సృష్టిస్తుంది. క్లయింట్ ఈ ఫైల్ నుండి చదువుతుంది.

## కోడ్ నడపండి

సర్వర్‌ను ప్రారంభించండి:

```sh
npm start
```

వేరే టెర్మినల్‌లో క్లయింట్‌ను నడపండి:

```sh
npm run client
```

సర్వర్ టెర్మినల్‌లో, మీరు ఈ విధమైన అవుట్పుట్‌ను చూడగలరు:

```text
User exists
User has required scopes
Middleware executed
```

మరియు క్లయింట్ టెర్మినల్ నుండి, మీరు ఈ విధమైన అవుట్పుట్‌ను చూడగలరు:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### మార్పులు చేయడం

మనం స్కోపులను అర్థం చేసుకున్నామో లేదో చూసుకుందాం. *server.ts* ఫైల్‌ను కనుగొని ఈ కోడ్‌ను చూడండి:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

ఇది చెప్పేది ఇచ్చిన టోకెన్ "User.Read" స్కోప్ కలిగి ఉండాలి, దీన్ని "User.Write" గా మార్చండి. ఇప్పుడు `npm run build` నడపండి మరియు సర్వర్‌ను `npm start` తో మళ్లీ ప్రారంభించండి. ఇప్పుడు మీరు auth విఫలమవుతుందని చూడగలరు ఎందుకంటే మనకు ఈ స్కోప్ లేదు (మన దగ్గర User.Read మరియు Admin.Write ఉన్నాయి):

క్లయింట్ ఇప్పుడు ఇలా చెబుతుంది

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

మరియు సర్వర్ టెర్మినల్‌లో ఇది ఇలా చెబుతుంది:

```text
User exists
```

మరియు ఇది ఈ పాయింట్ దాటి వెళ్లదు.

ఈ స్కోప్ "User.Write" ను జోడించి `npm run generate` నడపండి మరియు క్లయింట్‌ను మళ్లీ నడపండి లేదా సర్వర్ కోడ్‌ను తిరిగి మార్చండి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ డాక్యుమెంట్‌ను AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పులు ఉండవచ్చు. మూల డాక్యుమెంట్ దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->