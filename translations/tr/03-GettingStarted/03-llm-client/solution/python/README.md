# Bu örneği çalıştırmak

`uv` kurmanız önerilir ancak zorunlu değildir, detaylar için [talimatlara](https://docs.astral.sh/uv/#highlights) bakabilirsiniz.

## -0- Sanal ortam oluşturun

```bash
python -m venv venv
```

## -1- Sanal ortamı etkinleştirin

```bash
venv\Scrips\activate
```

## -2- Bağımlılıkları yükleyin

```bash
pip install "mcp[cli]"
pip install openai
pip install azure-ai-inference
```

## -3- Örneği çalıştırın

```bash
python client.py
```

Aşağıdakine benzer bir çıktı görmelisiniz:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
                    INFO     Processing request of type ListToolsRequest                                                                               server.py:534
LISTING TOOLS
Tool:  add
Tool {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}
CALLING LLM
TOOL:  {'function': {'arguments': '{"a":2,"b":20}', 'name': 'add'}, 'id': 'call_BCbyoCcMgq0jDwR8AuAF9QY3', 'type': 'function'}
[05/08/25 21:04:55] INFO     Processing request of type CallToolRequest                                                                                server.py:534
TOOLS result:  [TextContent(type='text', text='22', annotations=None)]
```

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.