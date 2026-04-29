## Тестирање и отклањање грешака

Пре него што почнете да тестирате свој MCP сервер, важно је разумети расположиве алате и најбоље праксе за отклањање грешака. Ефективно тестирање осигурава да ваш сервер ради као што се очекује и помаже вам да брзо идентификујете и решите проблеме. Следећи одељак описује препоручене приступе за валидацију ваше MCP имплементације.

## Преглед

Овај час описује како да изаберете прави приступ тестирању и најефикаснији алат за тестирање.

## Циљеви учења

До краја овог часа моћи ћете да:

- Опишете различите приступе тестирању.
- Користите различите алате за ефективно тестирање свог кода.

## Тестирање MCP сервера

MCP пружа алате који вам помажу да тестирате и отклоните грешке на серверима:

- **MCP Inspector**: Алатка командне линије која се може користити као CLI алатка и као визуелни алат.
- **Ручно тестирање**: Можете користити алат као што је curl да извршите веб захтеве, али сваки алат који може да покреће HTTP захтеве ће урадити посао.
- **Јединично тестирање**: Могуће је користити ваш омиљени тестни фрејмворк за тестирање функционалности и сервера и клијента.

### Коришћење MCP Inspectora

Описали смо коришћење овог алата у претходним часовима, али хајде да га укратко представимо. Ради се о алату направљеном у Node.js и можете га користити позивајући извршну датотеку `npx`, која ће привремено преузети и инсталирати сам алат, а потом очистити након што обради ваш захтев.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) вам помаже да:

- **Откријете могућности сервера**: Аутоматски детектује расположиве ресурсе, алате и упите
- **Тестирате извршење алата**: Испробајте различите параметре и видите одговоре у реалном времену
- **Прегледате метаподатке сервера**: Испитајте податке о серверу, шеме и конфигурације

Типичан покретачки команд изгледа овако:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Горња команда покреће MCP и његов визуелни интерфејс и лансира локални веб интерфејс у вашем прегледачу. Можете очекивати да видите таблу која приказује ваше регистроване MCP сервере, њихове расположиве алате, ресурсе и упите. Интерфејс вам омогућава интерактивно тестирање извршења алата, испитивање метаподатака сервера и преглед одговора у реалном времену, што олакшава валидацију и отклањање грешака у вашим MCP имплементацијама.

Ево како то може изгледати: ![Inspector](../../../../translated_images/sr/connect.141db0b2bd05f096.webp)

Можете такође покренути овај алат у CLI режиму додавањем атрибута `--cli`. Ево примера покретања алата у "CLI" режиму који листа све алате на серверу:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Ручно тестирање

Поред покретања Inspector алата за тестирање могућности сервера, други сличан приступ је покретање клијента који може користити HTTP, као што је на пример curl.

Са curl-ом можете директно тестирати MCP сервере користећи HTTP захтеве:

```bash
# Пример: Мета-подаци тест сервера
curl http://localhost:3000/v1/metadata

# Пример: Покрени алатку
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Као што видите из горе наведеног примера коришћења curl-а, користите POST захтев да позовете алат помоћу корисног оптерећења које садржи име алата и његове параметре. Користите приступ који вам највише одговара. CLI алати обично су бржи за коришћење и лако се могу скриптовати, што може бити корисно у CI/CD окружењу.

### Јединично тестирање

Креирајте јединичне тестове за своје алате и ресурсе како бисте били сигурни да раде како се очекује. Ево примера тест кода.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Обележите цео модул за аsync тестове
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Направите пар алата за тестирање
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Тест без параметра курсор (искључено)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Тест са курсором=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Тест са курсором као стринг
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Тест са празним стринг курсором
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Горњи код ради следеће:

- Користи pytest фрејмворк који вам омогућава да креирате тестове као функције и користите assert изјаве.
- Креира MCP сервер са два различита алата.
- Користи `assert` изјаву да провери да су одређени услови испуњени.

Погледајте [целу датотеку овде](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Уз горе наведени фајл, можете тестирати свој сопствени сервер како бисте били сигурни да су могућности креиране како треба.

Сви значајније SDK имају сличне секције за тестирање па можете прилагодити вашем изабраном окружењу.

## Примери

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Додатни ресурси

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Шта следи

- Следеће: [Deploy](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање**:
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, имајте на уму да аутоматски преводи могу садржати грешке или нетачности. Изворни документ на његовом матерњем језику треба сматрати ауторитетом. За критичне информације препоручује се професионални људски превод. Не сносимо одговорност за било какве неспоразуме или погрешне тумачења настала коришћењем овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->