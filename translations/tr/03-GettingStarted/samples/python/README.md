# MCP Hesaplayıcı Sunucusu (Python)



Basit bir Python Model Context Protocol (MCP) sunucu uygulaması, temel hesap makinesi işlevselliği sağlar.


## Kurulum

Gerekli bağımlılıkları yükleyin:

```bash
pip install -r requirements.txt
```

Veya MCP Python SDK'yı doğrudan yükleyin:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Kullanım

### Sunucuyu Çalıştırma

Sunucu MCP istemcileri (Claude Desktop gibi) tarafından kullanmak üzere tasarlanmıştır. Sunucuyu başlatmak için:

```bash
python mcp_calculator_server.py
```

**Not**: Terminalde doğrudan çalıştırıldığında JSON-RPC doğrulama hataları göreceksiniz. Bu normal davranıştır - sunucu, düzgün biçimlendirilmiş MCP istemci mesajlarını beklemektedir.

### Fonksiyonları Test Etme

Hesaplayıcı fonksiyonlarının doğru çalıştığını test etmek için:

```bash
python test_calculator.py
```

## Sorun Giderme

### İçe Aktarma Hataları

`ModuleNotFoundError: No module named 'mcp'` hatası alırsanız, MCP Python SDK'yı yükleyin:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### Doğrudan Çalıştırıldığında JSON-RPC Hataları

Sunucuyu doğrudan çalıştırırken "Invalid JSON: EOF while parsing a value" gibi hatalar beklenir. Sunucu, doğrudan terminal girişi değil MCP istemci mesajları gerektirir.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->