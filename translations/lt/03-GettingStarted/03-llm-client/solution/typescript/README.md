# Paleisti šį pavyzdį

Šis pavyzdys reikalauja, kad klientas turėtų LLM. LLM reikia, kad paleistumėte tai Codespaces aplinkoje arba nustatytumėte asmeninį prieigos raktą GitHub, kad viskas veiktų.

## -1- Įdiekite priklausomybes

```bash
npm install
```

## -3- Paleiskite serverį

```bash
npm run build
```

## -4- Paleiskite klientą

```sh
npm run client
```

Turėtumėte matyti rezultatą, panašų į:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.