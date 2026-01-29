# Executar exemplo

## Instalar dependências

```sh
npm install
```

## Compilar

```sh
npm run build
```

## Gerar tokens

```sh
npm run generate
```

Isso cria um token em um arquivo *.env*. O cliente irá ler a partir deste arquivo.

## Executar o código

Inicie o servidor com:

```sh
npm start
```

Execute o cliente, em um terminal separado, com:

```sh
npm run client
```

No terminal do servidor, você deve ver uma saída semelhante a:

```text
User exists
User has required scopes
Middleware executed
```

e no terminal do cliente, você deve ver uma saída semelhante a:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Alterando coisas

Vamos garantir que entendemos os escopos. Localize o arquivo *server.ts* e este código:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Isso indica que o token passado precisa ter "User.Read". Vamos alterar isso para "User.Write". Agora execute `npm run build` e reinicie o servidor com `npm start`. Você deve ver a autenticação falhar, pois não temos esse escopo (temos User.Read e Admin.Write):

O cliente agora diz

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

e você pode ver no terminal do servidor que ele diz:

```text
User exists
```

e que não avança além deste ponto.

Ou adicione este escopo "User.Write", execute `npm run generate` e execute novamente o cliente OU altere o código do servidor de volta.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.