<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6d6315e03f591fb5a39be91da88585dc",
  "translation_date": "2025-08-26T16:47:43+00:00",
  "source_file": "03-GettingStarted/03-llm-client/solution/typescript/README.md",
  "language_code": "lt"
}
-->
# Paleisti šį pavyzdį

Šis pavyzdys reikalauja, kad klientas turėtų LLM. Norint naudoti LLM, reikia arba paleisti šį pavyzdį Codespaces aplinkoje, arba nustatyti asmeninį prieigos raktą GitHub platformoje.

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
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.