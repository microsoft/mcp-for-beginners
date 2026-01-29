# ಮಾದರಿ ಚಾಲನೆ

## ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ

```sh
npm install
```

## ನಿರ್ಮಿಸಿ

```sh
npm run build
```

## ಟೋಕನ್‌ಗಳನ್ನು ರಚಿಸಿ

```sh
npm run generate
```

ಇದು *.env* ಫೈಲ್‌ನಲ್ಲಿ ಟೋಕನ್ ಅನ್ನು ರಚಿಸುತ್ತದೆ. ಕ್ಲೈಂಟ್ ಈ ಫೈಲ್‌ನಿಂದ ಓದುತ್ತದೆ.

## ಕೋಡ್ ಚಾಲನೆ

ಸರ್ವರ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ:

```sh
npm start
```

ವಿಭಿನ್ನ ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಕ್ಲೈಂಟ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡಿ:

```sh
npm run client
```

ಸರ್ವರ್ ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ, ನೀವು ಹೀಗೊಂದು ಔಟ್‌ಪುಟ್ ನೋಡಬಹುದು:

```text
User exists
User has required scopes
Middleware executed
```

ಮತ್ತು ಕ್ಲೈಂಟ್ ಟರ್ಮಿನಲ್‌ನಿಂದ, ನೀವು ಹೀಗೊಂದು ಔಟ್‌ಪುಟ್ ನೋಡಬಹುದು:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### ಬದಲಾವಣೆಗಳು

ನಾವು ಸ್ಕೋಪ್‌ಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳೋಣ. *server.ts* ಫೈಲ್ ಅನ್ನು ಹುಡುಕಿ ಮತ್ತು ಈ ಕೋಡ್ ನೋಡಿ:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

ಇದು ಪಾಸಾದ ಟೋಕನ್‌ಗೆ "User.Read" ಸ್ಕೋಪ್ ಬೇಕೆಂದು ಹೇಳುತ್ತದೆ, ಅದನ್ನು "User.Write" ಗೆ ಬದಲಾಯಿಸೋಣ. ಈಗ `npm run build` ಅನ್ನು ರನ್ ಮಾಡಿ ಮತ್ತು ಸರ್ವರ್ ಅನ್ನು `npm start` ಮೂಲಕ ಮರುಪ್ರಾರಂಭಿಸಿ. ಈಗ ನೀವು auth ವಿಫಲವಾಗಿರುವುದನ್ನು ನೋಡಬಹುದು ಏಕೆಂದರೆ ನಮಗೆ ಈ ಸ್ಕೋಪ್ ಇಲ್ಲ (ನಮಗೆ User.Read ಮತ್ತು Admin.Write ಇದೆ):

ಕ್ಲೈಂಟ್ ಈಗ ಹೇಳುತ್ತದೆ

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

ಮತ್ತು ಸರ್ವರ್ ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ನೀವು ನೋಡಬಹುದು:

```text
User exists
```

ಮತ್ತು ಇದು ಈ ಬಿಂದುವಿನ ನಂತರ ಮುಂದುವರಿಯುವುದಿಲ್ಲ.

ಈ ಸ್ಕೋಪ್ "User.Write" ಅನ್ನು ಸೇರಿಸಿ ಮತ್ತು `npm run generate` ಅನ್ನು ರನ್ ಮಾಡಿ ಮತ್ತು ಕ್ಲೈಂಟ್ ಅನ್ನು ಮರುಚಾಲನೆ ಮಾಡಿ ಅಥವಾ ಸರ್ವರ್ ಕೋಡ್ ಅನ್ನು ಹಿಂದಕ್ಕೆ ಬದಲಾಯಿಸಿ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->