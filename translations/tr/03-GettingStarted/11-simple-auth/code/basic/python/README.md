# Örnek Çalıştırma

Bu örnek, geçerli bir Authorization başlığını kontrol eden bir ara yazılım ile bir MCP Sunucusu başlatır.

## Bağımlılıkları Yükle

```bash
pip install "mcp[cli]" 
```

## Sunucuyu Başlat

```bash
python server.py
```

Başka bir terminalde istemciyi başlatın

```bash
python client.py
```

Şuna benzer bir sonuç görmelisiniz:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

Bu, gönderilen kimlik bilgilerinin kabul edildiği anlamına gelir.

`client.py` dosyasındaki kimlik bilgilerini "secret-token2" olarak değiştirin, ardından yanıtın bir parçası olarak şu metni görmelisiniz:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

Bu, kimlik doğrulamanızın yapıldığı (bir kimlik bilginiz vardı), ancak geçersiz olduğu anlamına gelir.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmemektedir.