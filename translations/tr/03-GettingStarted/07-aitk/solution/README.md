# 📘 Ödev Çözümü: Hesap Makinesi MCP Sunucunuzu Bir Karekök Aracıyla Genişletme

## Genel Bakış
Bu ödevde, hesap makinesi MCP sunucunuzu bir sayının karekökünü hesaplayan yeni bir araç ekleyerek geliştirdiniz. Bu ekleme, yapay zeka ajanınızın "16'nın karekökü nedir?" veya "√49'u hesapla" gibi doğal dil komutlarıyla daha gelişmiş matematiksel sorguları yanıtlamasını sağlar.

## 🛠️ Karekök Aracının Uygulanması
Bu işlevselliği eklemek için server.py dosyanızda yeni bir araç fonksiyonu tanımladınız. İşte uygulaması:

```python
"""
Sample MCP Calculator Server implementation in Python.

This module demonstrates how to create a simple MCP server with calculator tools
that can perform basic arithmetic operations (add, subtract, multiply, divide).
"""

from mcp.server.fastmcp import FastMCP
import math

server = FastMCP("calculator")

@server.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together and return the result."""
    return a + b

@server.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a and return the result."""
    return a - b

@server.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together and return the result."""
    return a * b

@server.tool()
def divide(a: float, b: float) -> float:
    """
    Divide a by b and return the result.
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@server.tool()
def sqrt(a: float) -> float:
    """
    Return the square root of a.

    Raises:
        ValueError: If a is negative.
    """
    if a < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    return math.sqrt(a)
```

## 🔍 Nasıl Çalışır

- **`math` modülünü içe aktarın**: Temel aritmetiğin ötesinde matematiksel işlemler yapmak için Python, yerleşik `math` modülünü sağlar. Bu modül çeşitli matematiksel fonksiyonlar ve sabitler içerir. `import math` ile içe aktararak, bir sayının karekökünü hesaplayan `math.sqrt()` gibi fonksiyonlara erişim sağlarsınız.
- **Fonksiyon Tanımı**: `@server.tool()` dekoratörü, `sqrt` fonksiyonunu yapay zeka ajanın tarafından erişilebilen bir araç olarak kaydeder.
- **Girdi Parametresi**: Fonksiyon, `float` türünde tek bir argüman `a` alır.
- **Hata Yönetimi**: Eğer `a` negatifse, fonksiyon `math.sqrt()` fonksiyonunun desteklemediği negatif sayıların karekökünü hesaplamayı önlemek için `ValueError` hatası fırlatır.
- **Dönüş Değeri**: Negatif olmayan girdiler için fonksiyon, Python’un yerleşik `math.sqrt()` yöntemiyle `a` sayısının karekökünü döndürür.

## 🔄 Sunucuyu Yeniden Başlatma
Yeni `sqrt` aracını ekledikten sonra, ajanın bu yeni işlevselliği tanıması ve kullanabilmesi için MCP sunucunuzu yeniden başlatmanız önemlidir.

## 💬 Yeni Aracı Test Etmek İçin Örnek Komutlar
Karekök işlevini test etmek için kullanabileceğiniz bazı doğal dil komutları şunlardır:

- "25'in karekökü nedir?"
- "81'in karekökünü hesapla."
- "0'ın karekökünü bul."
- "2.25'in karekökü nedir?"

Bu komutlar, ajanın `sqrt` aracını çağırmasını ve doğru sonuçları döndürmesini sağlamalıdır.

## ✅ Özet
Bu ödevi tamamlayarak:

- Hesap makinesi MCP sunucunuzu yeni bir `sqrt` aracıyla genişlettiniz.
- Yapay zeka ajanın doğal dil komutlarıyla karekök hesaplamalarını yapabilmesini sağladınız.
- Yeni araçlar ekleyip sunucuyu yeniden başlatarak ek işlevsellikleri entegre etme pratiği yaptınız.

Ajanınızın yeteneklerini geliştirmeye devam etmek için üs kuvveti veya logaritma gibi daha fazla matematiksel araç ekleyerek denemeler yapabilirsiniz!

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.