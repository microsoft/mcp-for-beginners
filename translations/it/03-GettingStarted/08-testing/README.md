## Testing e Debugging

Prima di iniziare a testare il tuo server MCP, è importante comprendere gli strumenti disponibili e le migliori pratiche per il debugging. Un testing efficace assicura che il tuo server si comporti come previsto e ti aiuta a identificare e risolvere rapidamente i problemi. La sezione seguente delinea gli approcci consigliati per la convalida della tua implementazione MCP.

## Panoramica

Questa lezione copre come selezionare l'approccio di testing giusto e lo strumento di testing più efficace.

## Obiettivi di Apprendimento

Al termine di questa lezione, sarai in grado di:

- Descrivere vari approcci per il testing.
- Usare diversi strumenti per testare efficacemente il tuo codice.


## Testing dei Server MCP

MCP fornisce strumenti per aiutarti a testare e fare il debug dei tuoi server:

- **MCP Inspector**: Uno strumento da linea di comando che può essere eseguito sia come strumento CLI che come strumento visivo.
- **Testing manuale**: Puoi utilizzare uno strumento come curl per eseguire richieste web, ma qualsiasi strumento in grado di eseguire HTTP andrà bene.
- **Unit testing**: È possibile utilizzare il framework di testing preferito per testare le funzionalità sia del server che del client.

### Utilizzo di MCP Inspector

Abbiamo descritto l'uso di questo strumento in lezioni precedenti, ma parliamone un po' a livello generale. È uno strumento costruito in Node.js e puoi usarlo chiamando l'eseguibile `npx` che scaricherà e installerà temporaneamente lo strumento stesso e si pulirà una volta terminata l'esecuzione della tua richiesta.

Il [MCP Inspector](https://github.com/modelcontextprotocol/inspector) ti aiuta a:

- **Scoprire le Capacità del Server**: Rilevare automaticamente risorse, strumenti e prompt disponibili
- **Testare l'Esecuzione degli Strumenti**: Provare diversi parametri e vedere le risposte in tempo reale
- **Visualizzare i Metadata del Server**: Esaminare informazioni sul server, schemi e configurazioni

Una tipica esecuzione dello strumento appare così:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Il comando sopra avvia un MCP e la sua interfaccia visiva e lancia un'interfaccia web locale nel tuo browser. Puoi aspettarti di vedere una dashboard che mostra i tuoi server MCP registrati, i loro strumenti, risorse e prompt disponibili. L'interfaccia ti consente di testare interattivamente l'esecuzione degli strumenti, ispezionare i metadata del server e visualizzare le risposte in tempo reale, facilitando la convalida e il debug delle implementazioni del tuo server MCP.

Ecco come può apparire: ![Inspector](../../../../translated_images/it/connect.141db0b2bd05f096.webp)

Puoi anche eseguire questo strumento in modalità CLI, in tal caso aggiungi l'attributo `--cli`. Ecco un esempio di esecuzione dello strumento in modalità "CLI" che elenca tutti gli strumenti presenti sul server:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Testing Manuale

Oltre a eseguire lo strumento inspector per testare le capacità del server, un altro approccio simile è eseguire un client in grado di usare HTTP come ad esempio curl.

Con curl, puoi testare direttamente i server MCP utilizzando richieste HTTP:

```bash
# Esempio: Metadati del server di test
curl http://localhost:3000/v1/metadata

# Esempio: Eseguire uno strumento
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Come puoi vedere dall'uso di curl sopra, utilizzi una richiesta POST per invocare uno strumento usando un payload composto dal nome dello strumento e dai suoi parametri. Usa l'approccio che più ti si addice. Gli strumenti CLI in generale tendono a essere più veloci da usare e si prestano ad essere orchestrati tramite script, il che può essere utile in un ambiente CI/CD.

### Unit Testing

Crea test unitari per i tuoi strumenti e risorse per assicurarti che funzionino come previsto. Ecco un esempio di codice di testing.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Segna l'intero modulo per i test asincroni
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Crea un paio di strumenti di test
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Test senza parametro cursor (omesso)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Test con cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Test con cursor come stringa
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Test con cursor stringa vuota
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Il codice precedente fa quanto segue:

- Sfrutta il framework pytest che ti permette di creare test come funzioni e usare dichiarazioni assert.
- Crea un Server MCP con due strumenti differenti.
- Usa l'istruzione `assert` per verificare che determinate condizioni siano soddisfatte.

Dai un'occhiata al [file completo qui](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Dato il file sopra, puoi testare il tuo server per assicurarti che le capacità vengano create come dovrebbero.

Tutti i principali SDK hanno sezioni di testing simili, così puoi adattarti al runtime scelto.

## Esempi 

- [Calcolatrice Java](../samples/java/calculator/README.md)
- [Calcolatrice .Net](../../../../03-GettingStarted/samples/csharp)
- [Calcolatrice JavaScript](../samples/javascript/README.md)
- [Calcolatrice TypeScript](../samples/typescript/README.md)
- [Calcolatrice Python](../../../../03-GettingStarted/samples/python) 

## Risorse Aggiuntive

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Cosa c'è Dopo

- Successivo: [Deployment](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire la massima accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->