# Run sample

## Install dependencies

```sh
npm install
```

## Build

```sh
npm run build
```

## Generate tokens

```sh
npm run generate
```

Dis one go create token for one file *.env*. Di client go dey read from dis file.

## Run code

Start di server wit:

```sh
npm start
```

Run di client, for another terminal wit:

```sh
npm run client
```

For di server terminal, you go see output wey resemble dis:

```text
User exists
User has required scopes
Middleware executed
```

and for di client terminal, you go see output wey resemble dis:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Changing things

Make we make sure say we sabi di scopes. Find di file *server.ts* and dis code:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Dis one dey talk say di token wey dem pass need get "User.Read", make we change am to "User.Write". Now run `npm run build` and restart di server `npm start`. You go see say auth go fail because we no get dis scope (we get User.Read and Admin.Write):

Di client go talk say

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

and you go see for di server terminal say e talk:

```text
User exists
```

and e no go pass dis point.

Either add dis scope "User.Write" and run `npm run generate` and rerun di client OR change di server code back.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis docu wey you dey see don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) take translate am. Even though we dey try make sure say e correct, abeg no forget say machine translation fit get mistake or no too accurate. Di original docu for di language wey dem first write am na di main correct one. If na important matter, e go better make you use professional human translation. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->