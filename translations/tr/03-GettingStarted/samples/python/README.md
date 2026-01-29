# MCP Hesap Makinesi Sunucusu (Python)

Python'da basit bir Model Context Protocol (MCP) sunucu uygulaması, temel hesap makinesi işlevselliği sağlar.

## Kurulum

Gerekli bağımlılıkları yükleyin:

```bash
pip install -r requirements.txt
```

Ya da MCP Python SDK'sını doğrudan yükleyin:

```bash
pip install mcp>=1.18.0
```

## Kullanım

### Sunucuyu Çalıştırma

Sunucu, MCP istemcileri (örneğin Claude Desktop) tarafından kullanılmak üzere tasarlanmıştır. Sunucuyu başlatmak için:

```bash
python mcp_calculator_server.py
```

**Not**: Terminalde doğrudan çalıştırıldığında JSON-RPC doğrulama hataları göreceksiniz. Bu normal bir davranıştır - sunucu, doğru biçimlendirilmiş MCP istemci mesajlarını bekliyor.

### Fonksiyonları Test Etme

Hesap makinesi fonksiyonlarının doğru çalıştığını test etmek için:

```bash
python test_calculator.py
```

## Sorun Giderme

### İçe Aktarma Hataları

Eğer `ModuleNotFoundError: No module named 'mcp'` hatası alırsanız, MCP Python SDK'sını yükleyin:

```bash
pip install mcp>=1.18.0
```

### JSON-RPC Hataları Doğrudan Çalıştırıldığında

Sunucuyu doğrudan çalıştırırken "Geçersiz JSON: EOF bir değeri ayrıştırırken" gibi hatalar almanız beklenir. Sunucu, terminal girdisi yerine MCP istemci mesajlarına ihtiyaç duyar.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.