# Temel Hesap Makinesi MCP Servisi

Bu servis, Model Context Protocol (MCP) üzerinden temel hesap makinesi işlemleri sağlar. MCP uygulamalarını öğrenen yeni başlayanlar için basit bir örnek olarak tasarlanmıştır.

Daha fazla bilgi için bkz. [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Özellikler

Bu hesap makinesi servisi aşağıdaki yetenekleri sunar:

1. **Temel Aritmetik İşlemler**:
   - İki sayının toplanması
   - Bir sayının diğerinden çıkarılması
   - İki sayının çarpılması
   - Bir sayının diğerine bölünmesi (sıfıra bölme kontrolü ile)

## `stdio` Türünü Kullanma

## Yapılandırma

1. **MCP Sunucularını Yapılandırma**:
   - Çalışma alanınızı VS Code’da açın.
   - MCP sunucularını yapılandırmak için çalışma alanı klasörünüzde `.vscode/mcp.json` dosyası oluşturun. Örnek yapılandırma:

     ```jsonc
     {
       "inputs": [
         {
           "type": "promptString",
           "id": "repository-root",
           "description": "The absolute path to the repository root"
         }
       ],
       "servers": {
         "calculator-mcp-dotnet": {
           "type": "stdio",
           "command": "dotnet",
           "args": [
             "run",
             "--project",
             "${input:repository-root}/03-GettingStarted/samples/csharp/src/calculator.csproj"
           ]
         }
       }
     }
     ```

   - GitHub depo kökünü girmeniz istenecek, bu bilgi `git rev-parse --show-toplevel` komutuyla alınabilir.

## Servisi Kullanma

Servis, MCP protokolü üzerinden aşağıdaki API uç noktalarını sunar:

- `add(a, b)`: İki sayıyı toplar
- `subtract(a, b)`: İkinci sayıyı birinciden çıkarır
- `multiply(a, b)`: İki sayıyı çarpar
- `divide(a, b)`: Birinci sayıyı ikinciye böler (sıfır kontrolü ile)
- isPrime(n): Bir sayının asal olup olmadığını kontrol eder

## VS Code’da Github Copilot Chat ile Test Etme

1. MCP protokolünü kullanarak servise istek yapmayı deneyin. Örneğin, şunları sorabilirsiniz:
   - "5 ve 3'ü topla"
   - "4'ten 10 çıkar"
   - "6 ve 7'yi çarp"
   - "8'i 2'ye böl"
   - "37854 asal mı?"
   - "4242’den önce ve sonra gelen 3 asal sayı nedir?"
2. Araçların kullanıldığından emin olmak için isteme #MyCalculator ekleyin. Örneğin:
   - "5 ve 3'ü topla #MyCalculator"
   - "4'ten 10 çıkar #MyCalculator"

## Konteynerize Edilmiş Versiyon

Önceki çözüm, .NET SDK yüklü ve tüm bağımlılıklar hazır olduğunda harikadır. Ancak, çözümü paylaşmak veya farklı bir ortamda çalıştırmak isterseniz, konteynerize edilmiş versiyonu kullanabilirsiniz.

1. Docker’ı başlatın ve çalıştığından emin olun.
1. Bir terminalden `03-GettingStarted\samples\csharp\src` klasörüne gidin.
1. Hesap makinesi servisi için Docker imajını oluşturmak için aşağıdaki komutu çalıştırın ( `<YOUR-DOCKER-USERNAME>` kısmını Docker Hub kullanıcı adınızla değiştirin):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ```
1. İmaj oluşturulduktan sonra, Docker Hub’a yükleyelim. Aşağıdaki komutu çalıştırın:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Dockerize Edilmiş Versiyonu Kullanma

1. `.vscode/mcp.json` dosyasında sunucu yapılandırmasını aşağıdaki ile değiştirin:
   ```json
    "mcp-calc": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calc"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   Yapılandırmaya baktığınızda, komutun `docker` ve argümanların `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc` olduğunu göreceksiniz. `--rm` bayrağı konteyner durduktan sonra silinmesini sağlar, `-i` bayrağı ise konteynerin standart girdisiyle etkileşim kurmanıza izin verir. Son argüman ise az önce oluşturup Docker Hub’a yüklediğimiz imajın adıdır.

## Dockerize Edilmiş Versiyonu Test Etme

`"mcp-calc": {` satırının üstündeki küçük Başlat düğmesine tıklayarak MCP Sunucusunu başlatın ve tıpkı önceki gibi hesap makinesi servisine matematik işlemleri yaptırabilirsiniz.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.