# സാമ്പിൾ പ്രവർത്തിപ്പിക്കുക

## ആശ്രിതത്വങ്ങൾ ഇൻസ്റ്റാൾ ചെയ്യുക

```sh
npm install
```

## നിർമ്മിക്കുക

```sh
npm run build
```

## ടോക്കണുകൾ സൃഷ്ടിക്കുക

```sh
npm run generate
```

ഇത് *.env* എന്ന ഫയലിൽ ഒരു ടോക്കൺ സൃഷ്ടിക്കുന്നു. ക്ലയന്റ് ഈ ഫയലിൽ നിന്ന് വായിക്കും.

## കോഡ് പ്രവർത്തിപ്പിക്കുക

സർവർ ആരംഭിക്കുക:

```sh
npm start
```

മറ്റൊരു ടെർമിനലിൽ ക്ലയന്റ് പ്രവർത്തിപ്പിക്കുക:

```sh
npm run client
```

സർവറിന്റെ ടെർമിനലിൽ, താഴെപോലുള്ള ഔട്ട്പുട്ട് കാണാം:

```text
User exists
User has required scopes
Middleware executed
```

ക്ലയന്റ് ടെർമിനലിൽ, താഴെപോലുള്ള ഔട്ട്പുട്ട് കാണാം:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### കാര്യങ്ങൾ മാറ്റുന്നു

സ്കോപ്പുകൾ നമുക്ക് മനസ്സിലാക്കാം. *server.ts* ഫയൽ കണ്ടെത്തുക, ഈ കോഡ് കാണുക:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

ഇത് പറഞ്ഞിരിക്കുന്നത് പാസ്സായ ടോക്കണിന് "User.Read" എന്ന സ്കോപ്പ് വേണം, ഇത് "User.Write" ആയി മാറ്റാം. ഇപ്പോൾ `npm run build` പ്രവർത്തിപ്പിച്ച് സർവർ `npm start` വീണ്ടും ആരംഭിക്കുക. ഈ സ്കോപ്പ് ഇല്ലാത്തതിനാൽ ഓതെന്റിക്കേഷൻ പരാജയപ്പെടും (നമുക്ക് User.Read ഉം Admin.Write ഉം ഉണ്ട്):

ക്ലയന്റ് ഇപ്പോൾ പറയുന്നു

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

സർവർ ടെർമിനലിൽ ഇത് പറയുന്നു:

```text
User exists
```

ഇതിനു മുകളിൽ ഇത് പോകുന്നില്ല.

ഈ സ്കോപ്പ് "User.Write" ചേർക്കുക, `npm run generate` പ്രവർത്തിപ്പിച്ച് ക്ലയന്റ് വീണ്ടും പ്രവർത്തിപ്പിക്കുക അല്ലെങ്കിൽ സർവർ കോഡ് പഴയ നിലയിലേക്ക് മാറ്റുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->