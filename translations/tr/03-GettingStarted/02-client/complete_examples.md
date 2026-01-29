# Tam MCP İstemci Örnekleri

Bu dizin, farklı programlama dillerinde tam ve çalışan MCP istemci örneklerini içerir. Her bir istemci, ana README.md eğitiminde açıklanan tüm işlevselliği göstermektedir.

## Mevcut İstemciler

### 1. Java İstemcisi (`client_example_java.java`)

- **Taşıma**: HTTP üzerinden SSE (Sunucu Gönderimli Olaylar)
- **Hedef Sunucu**: `http://localhost:8080`
- **Özellikler**:
  - Bağlantı kurulumu ve ping
  - Araç listeleme
  - Hesap makinesi işlemleri (toplama, çıkarma, çarpma, bölme, yardım)
  - Hata yönetimi ve sonuç çıkarımı

**Çalıştırmak için:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. C# İstemcisi (`client_example_csharp.cs`)

- **Taşıma**: Stdio (Standart Giriş/Çıkış)
- **Hedef Sunucu**: Yerel .NET MCP sunucusu üzerinden dotnet çalıştırma
- **Özellikler**:
  - Stdio taşıma ile otomatik sunucu başlatma
  - Araç ve kaynak listeleme
  - Hesap makinesi işlemleri
  - JSON sonuç ayrıştırma
  - Kapsamlı hata yönetimi

**Çalıştırmak için:**

```bash
dotnet run
```

### 3. TypeScript İstemcisi (`client_example_typescript.ts`)

- **Taşıma**: Stdio (Standart Giriş/Çıkış)
- **Hedef Sunucu**: Yerel Node.js MCP sunucusu
- **Özellikler**:
  - Tam MCP protokol desteği
  - Araç, kaynak ve istem işlemleri
  - Hesap makinesi işlemleri
  - Kaynak okuma ve istem yürütme
  - Güçlü hata yönetimi

**Çalıştırmak için:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Python İstemcisi (`client_example_python.py`)

- **Taşıma**: Stdio (Standart Giriş/Çıkış)  
- **Hedef Sunucu**: Yerel Python MCP sunucusu
- **Özellikler**:
  - İşlemler için async/await deseni
  - Araç ve kaynak keşfi
  - Hesap makinesi işlemleri testi
  - Kaynak içeriği okuma
  - Sınıf tabanlı organizasyon

**Çalıştırmak için:**

```bash
python client_example_python.py
```

## Tüm İstemcilerde Ortak Özellikler

Her bir istemci uygulaması aşağıdakileri göstermektedir:

1. **Bağlantı Yönetimi**
   - MCP sunucusuna bağlantı kurma
   - Bağlantı hatalarını yönetme
   - Uygun temizleme ve kaynak yönetimi

2. **Sunucu Keşfi**
   - Mevcut araçları listeleme
   - Mevcut kaynakları listeleme (destekleniyorsa)
   - Mevcut istemleri listeleme (destekleniyorsa)

3. **Araç Çağırma**
   - Temel hesap makinesi işlemleri (toplama, çıkarma, çarpma, bölme)
   - Sunucu bilgisi için yardım komutu
   - Uygun argüman geçişi ve sonuç yönetimi

4. **Hata Yönetimi**
   - Bağlantı hataları
   - Araç yürütme hataları
   - Zarif başarısızlık ve kullanıcı geri bildirimi

5. **Sonuç İşleme**
   - Yanıtlardan metin içeriği çıkarma
   - Okunabilirlik için çıktıyı biçimlendirme
   - Farklı yanıt formatlarını yönetme

## Ön Koşullar

Bu istemcileri çalıştırmadan önce, aşağıdakilere sahip olduğunuzdan emin olun:

1. **İlgili MCP sunucusu çalışıyor** (`../01-first-server/` dizininden)
2. **Seçtiğiniz dil için gerekli bağımlılıklar yüklü**
3. **Uygun ağ bağlantısı** (HTTP tabanlı taşımalar için)

## Uygulamalar Arasındaki Temel Farklar

| Dil        | Taşıma    | Sunucu Başlatma | Async Modeli | Temel Kütüphaneler  |
|------------|-----------|-----------------|--------------|---------------------|
| Java       | SSE/HTTP  | Harici          | Senkron      | WebFlux, MCP SDK    |
| C#         | Stdio     | Otomatik        | Async/Await  | .NET MCP SDK        |
| TypeScript | Stdio     | Otomatik        | Async/Await  | Node MCP SDK        |
| Python     | Stdio     | Otomatik        | AsyncIO      | Python MCP SDK      |
| Rust       | Stdio     | Otomatik        | Async/Await  | Rust MCP SDK, Tokio |

## Sonraki Adımlar

Bu istemci örneklerini inceledikten sonra:

1. **İstemcileri değiştirin** ve yeni özellikler veya işlemler ekleyin
2. **Kendi sunucunuzu oluşturun** ve bu istemcilerle test edin
3. **Farklı taşımaları deneyin** (SSE vs. Stdio)
4. **MCP işlevselliğini entegre eden daha karmaşık bir uygulama oluşturun**

## Sorun Giderme

### Yaygın Sorunlar

1. **Bağlantı reddedildi**: MCP sunucusunun beklenen port/yolda çalıştığından emin olun
2. **Modül bulunamadı**: Diliniz için gerekli MCP SDK'yı yükleyin
3. **İzin reddedildi**: Stdio taşıma için dosya izinlerini kontrol edin
4. **Araç bulunamadı**: Sunucunun beklenen araçları uyguladığını doğrulayın

### Hata Ayıklama İpuçları

1. **MCP SDK'nızda ayrıntılı günlüklemeyi etkinleştirin**
2. **Sunucu günlüklerini kontrol edin** ve hata mesajlarını inceleyin
3. **Araç adlarının ve imzalarının** istemci ve sunucu arasında eşleştiğini doğrulayın
4. **Önce MCP Inspector ile test yapın** ve sunucu işlevselliğini doğrulayın

## İlgili Belgeler

- [Ana İstemci Eğitimi](./README.md)
- [MCP Sunucu Örnekleri](../../../../03-GettingStarted/01-first-server)
- [MCP ile LLM Entegrasyonu](../../../../03-GettingStarted/03-llm-client)
- [Resmi MCP Belgeleri](https://modelcontextprotocol.io/)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul edilmez.