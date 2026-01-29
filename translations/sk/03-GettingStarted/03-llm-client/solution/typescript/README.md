# Spustenie tohto príkladu

Tento príklad vyžaduje mať LLM na klientovi. LLM potrebuje, aby ste to buď spustili v Codespaces, alebo si nastavili osobný prístupový token v GitHub, aby to fungovalo.

## -1- Inštalácia závislostí

```bash
npm install
```

## -3- Spustenie servera

```bash
npm run build
```

## -4- Spustenie klienta

```sh
npm run client
```

Mali by ste vidieť výsledok podobný tomuto:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.