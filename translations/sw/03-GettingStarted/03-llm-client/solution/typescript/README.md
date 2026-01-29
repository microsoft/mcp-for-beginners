# Kuendesha sampuli hii

Sampuli hii inahusisha kuwa na LLM upande wa mteja. LLM inahitaji uendeshe hii katika Codespaces au kuweka tokeni ya upatikanaji binafsi kwenye GitHub ili ifanye kazi.

## -1- Sakinisha utegemezi

```bash
npm install
```

## -3- Endesha seva

```bash
npm run build
```

## -4- Endesha mteja

```sh
npm run client
```

Unapaswa kuona matokeo yanayofanana na:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.