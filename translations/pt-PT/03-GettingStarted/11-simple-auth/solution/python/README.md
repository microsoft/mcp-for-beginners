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

Será necessário gerar um token que o cliente usará para comunicar-se com o servidor.

Execute:

```sh
python util.py
```

## Executar código

Execute o código com:

```sh
python server.py
```

Num terminal separado, digite:

```sh
python client.py
```

No terminal do servidor, deverá aparecer algo como:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

Na janela do cliente, deverá aparecer texto semelhante a:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

Isso significa que está tudo a funcionar.

### Alterar a informação para verificar falhas

Localize este código em *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Altere-o para que diga "User.Write". O seu token atual não possui esse nível de permissão, então, se reiniciar o servidor e tentar executar o cliente novamente, deverá ver um erro semelhante ao seguinte no terminal do servidor:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Pode optar por voltar a alterar o código do servidor ou gerar um novo token que contenha este escopo adicional, a decisão é sua.

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.