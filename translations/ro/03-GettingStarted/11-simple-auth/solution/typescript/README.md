# Rulează exemplul

## Instalează dependențele

```sh
npm install
```

## Construiește

```sh
npm run build
```

## Generează token-uri

```sh
npm run generate
```

Aceasta creează un token într-un fișier *.env*. Clientul va citi din acest fișier.

## Rulează codul

Pornește serverul cu:

```sh
npm start
```

Rulează clientul, într-un terminal separat, cu:

```sh
npm run client
```

În terminalul serverului, ar trebui să vezi un output similar cu:

```text
User exists
User has required scopes
Middleware executed
```

iar în terminalul clientului, ar trebui să vezi un output similar cu:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Modificarea lucrurilor

Să ne asigurăm că înțelegem scopurile. Găsește fișierul *server.ts* și acest cod:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Acesta indică faptul că token-ul transmis trebuie să aibă "User.Read". Să schimbăm asta în "User.Write". Acum rulează `npm run build` și repornește serverul cu `npm start`. Ar trebui să vezi acum că autentificarea eșuează, deoarece nu avem acest scop (avem User.Read și Admin.Write):

Clientul spune acum

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

și poți vedea în terminalul serverului că spune:

```text
User exists
```

și că nu trece mai departe de acest punct.

Fie adaugă acest scop "User.Write" și rulează `npm run generate` și rulează din nou clientul, fie schimbă codul serverului înapoi.

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.