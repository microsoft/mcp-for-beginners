# Executar exemplo

## Instalar dependências

```sh
npm install
```

## Construir

```sh
npm run build
```

## Gerar tokens

```sh
npm run generate
```

Isto cria um token num ficheiro *.env*. O cliente irá ler a partir deste ficheiro.

## Executar código

Inicie o servidor com:

```sh
npm start
```

Execute o cliente, num terminal separado, com:

```sh
npm run client
```

No terminal do servidor, deverá ver um output semelhante a:

```text
User exists
User has required scopes
Middleware executed
```

e no terminal do cliente, deverá ver um output semelhante a:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Alterar coisas

Vamos garantir que entendemos os escopos. Localize o ficheiro *server.ts* e este código:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Isto indica que o token passado precisa de ter "User.Read". Vamos alterar isso para "User.Write". Agora execute `npm run build` e reinicie o servidor com `npm start`. Deverá agora ver que a autenticação falha, pois não temos este escopo (temos User.Read e Admin.Write):

O cliente agora diz

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

e pode ver no terminal do servidor que diz:

```text
User exists
```

e que não avança além deste ponto.

Ou adicione este escopo "User.Write", execute `npm run generate` e volte a executar o cliente OU altere o código do servidor de volta.

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.