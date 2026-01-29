# Spuštění tohoto příkladu

Tento příklad zahrnuje použití LLM na klientovi. LLM vyžaduje, abyste to buď spustili v Codespaces, nebo si nastavili osobní přístupový token na GitHubu.

## -1- Nainstalujte závislosti

```bash
npm install
```

## -3- Spusťte server

```bash
npm run build
```

## -4- Spusťte klienta

```sh
npm run client
```

Měli byste vidět výsledek podobný tomuto:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.