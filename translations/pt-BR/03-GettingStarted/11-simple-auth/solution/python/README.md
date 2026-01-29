# Executar exemplo

## Criar ambiente

```sh
python -m venv venv
source ./venv/bin/activate
```

## Instalar dependências

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Gerar token

Você precisará gerar um token que o cliente usará para se comunicar com o servidor.

Execute:

```sh
python util.py
```

## Executar código

Execute o código com:

```sh
python server.py
```

Em um terminal separado, digite:

```sh
python client.py
```

No terminal do servidor, você deve ver algo como:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

Na janela do cliente, você deve ver um texto semelhante a:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

Isso significa que está tudo funcionando.

### Alterar as informações para ver falhas

Localize este código em *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Altere para que diga "User.Write". Seu token atual não possui esse nível de permissão, então, se você reiniciar o servidor e tentar executar o cliente novamente, deverá ver um erro semelhante ao seguinte no terminal do servidor:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Você pode voltar ao código original do servidor ou gerar um novo token que contenha esse escopo adicional, a escolha é sua.

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.