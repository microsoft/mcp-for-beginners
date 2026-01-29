# Bu örneği çalıştırma

Klasik HTTP akış sunucusu ve istemcisini, ayrıca MCP akış sunucusu ve istemcisini Python kullanarak nasıl çalıştıracağınızı öğrenin.

### Genel Bakış

- İşlem sırasında öğeleri işlerken istemciye ilerleme bildirimleri gönderen bir MCP sunucusu kuracaksınız.
- İstemci, her bildirimi gerçek zamanlı olarak gösterecek.
- Bu kılavuz, ön koşullar, kurulum, çalıştırma ve sorun giderme konularını kapsar.

### Ön Koşullar

- Python 3.9 veya daha yeni bir sürüm
- `mcp` Python paketi (şu komutla yükleyin: `pip install mcp`)

### Kurulum ve Ayarlar

1. Depoyu klonlayın veya çözüm dosyalarını indirin.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **Bir sanal ortam oluşturun ve etkinleştirin (önerilir):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **Gerekli bağımlılıkları yükleyin:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### Dosyalar

- **Sunucu:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **İstemci:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### Klasik HTTP Akış Sunucusunu Çalıştırma

1. Çözüm dizinine gidin:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. Klasik HTTP akış sunucusunu başlatın:

   ```pwsh
   python server.py
   ```

3. Sunucu başlayacak ve şu çıktıyı gösterecek:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### Klasik HTTP Akış İstemcisini Çalıştırma

1. Yeni bir terminal açın (aynı sanal ortamı ve dizini etkinleştirin):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. Akış mesajlarının sırasıyla yazdırıldığını göreceksiniz:

   ```text
   Running classic HTTP streaming client...
   Connecting to http://localhost:8000/stream with message: hello
   --- Streaming Progress ---
   Processing file 1/3...
   Processing file 2/3...
   Processing file 3/3...
   Here's the file content: hello
   --- Stream Ended ---
   ```

### MCP Akış Sunucusunu Çalıştırma

1. Çözüm dizinine gidin:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. MCP sunucusunu streamable-http taşıma yöntemiyle başlatın:
   ```pwsh
   python server.py mcp
   ```
3. Sunucu başlayacak ve şu çıktıyı gösterecek:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### MCP Akış İstemcisini Çalıştırma

1. Yeni bir terminal açın (aynı sanal ortamı ve dizini etkinleştirin):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. Sunucu her öğeyi işlerken bildirimlerin gerçek zamanlı olarak yazdırıldığını göreceksiniz:
   ```
   Running MCP client...
   Starting client...
   Session ID before init: None
   Session ID after init: a30ab7fca9c84f5fa8f5c54fe56c9612
   Session initialized, ready to call tools.
   Received message: root=LoggingMessageNotification(...)
   NOTIFICATION: root=LoggingMessageNotification(...)
   ...
   Tool result: meta=None content=[TextContent(type='text', text='Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello from client')]
   ```

### Temel Uygulama Adımları

1. **FastMCP kullanarak MCP sunucusunu oluşturun.**
2. **Bir listeyi işleyen ve `ctx.info()` veya `ctx.log()` kullanarak bildirim gönderen bir araç tanımlayın.**
3. **Sunucuyu `transport="streamable-http"` ile çalıştırın.**
4. **Bildirimleri geldikçe göstermek için bir mesaj işleyici içeren bir istemci uygulayın.**

### Kod İncelemesi
- Sunucu, ilerleme güncellemeleri göndermek için async fonksiyonlar ve MCP bağlamını kullanır.
- İstemci, bildirimleri ve nihai sonucu yazdırmak için bir async mesaj işleyici uygular.

### İpuçları ve Sorun Giderme

- Bloklamayan işlemler için `async/await` kullanın.
- Hem sunucuda hem de istemcide istisnaları ele alarak dayanıklılığı artırın.
- Gerçek zamanlı güncellemeleri gözlemlemek için birden fazla istemciyle test yapın.
- Hata alırsanız, Python sürümünüzü kontrol edin ve tüm bağımlılıkların yüklü olduğundan emin olun.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul etmiyoruz.