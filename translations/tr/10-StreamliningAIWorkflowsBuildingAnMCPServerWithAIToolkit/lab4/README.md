# 🐙 Modül 4: Pratik MCP Geliştirme - Özel GitHub Klon Sunucusu

![Duration](https://img.shields.io/badge/Duration-30_minutes-blue?style=flat-square)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-orange?style=flat-square)
![MCP](https://img.shields.io/badge/MCP-Custom%20Server-purple?style=flat-square&logo=github)
![VS Code](https://img.shields.io/badge/VS%20Code-Integration-blue?style=flat-square&logo=visualstudiocode)
![GitHub Copilot](https://img.shields.io/badge/GitHub%20Copilot-Agent%20Mode-green?style=flat-square&logo=github)

> **⚡ Hızlı Başlangıç:** Sadece 30 dakikada GitHub depo klonlama ve VS Code entegrasyonunu otomatikleştiren üretime hazır bir MCP sunucusu oluşturun!

## 🎯 Öğrenme Hedefleri

Bu laboratuvarın sonunda şunları yapabileceksiniz:

- ✅ Gerçek dünya geliştirme iş akışları için özel bir MCP sunucusu oluşturmak
- ✅ MCP üzerinden GitHub depo klonlama işlevselliğini uygulamak
- ✅ Özel MCP sunucularını VS Code ve Agent Builder ile entegre etmek
- ✅ GitHub Copilot Agent Mode’u özel MCP araçlarıyla kullanmak
- ✅ Özel MCP sunucularını üretim ortamlarında test etmek ve dağıtmak

## 📋 Ön Koşullar

- Laboratuvar 1-3’ün tamamlanması (MCP temelleri ve ileri geliştirme)
- GitHub Copilot aboneliği ([ücretsiz kayıt mevcut](https://github.com/github-copilot/signup))
- AI Toolkit ve GitHub Copilot eklentileri yüklü VS Code
- Kurulu ve yapılandırılmış Git CLI

## 🏗️ Proje Genel Bakışı

### **Gerçek Dünya Geliştirme Zorluğu**
Geliştiriciler olarak sık sık GitHub’dan depoları klonlayıp VS Code veya VS Code Insiders’da açıyoruz. Bu manuel süreç şunları içerir:
1. Terminal/komut istemcisini açmak
2. İstenen dizine gitmek
3. `git clone` komutunu çalıştırmak
4. Klonlanan dizinde VS Code’u açmak

**Bizim MCP çözümümüz bunu tek bir akıllı komuta indiriyor!**

### **Ne İnşa Edeceksiniz**
Bir **GitHub Klon MCP Sunucusu** (`git_mcp_server`) oluşturacaksınız, bu sunucu şunları sağlar:

| Özellik | Açıklama | Faydası |
|---------|----------|---------|
| 🔄 **Akıllı Depo Klonlama** | GitHub depolarını doğrulama ile klonlar | Otomatik hata kontrolü |
| 📁 **Akıllı Dizin Yönetimi** | Dizinleri güvenli şekilde kontrol eder ve oluşturur | Üzerine yazmayı önler |
| 🚀 **Çapraz Platform VS Code Entegrasyonu** | Projeleri VS Code/Insiders’da açar | Kesintisiz iş akışı geçişi |
| 🛡️ **Güçlü Hata Yönetimi** | Ağ, izin ve yol sorunlarını ele alır | Üretime hazır güvenilirlik |

---

## 📖 Adım Adım Uygulama

### Adım 1: Agent Builder’da GitHub Agent Oluşturma

1. AI Toolkit eklentisi üzerinden **Agent Builder’ı başlatın**
2. Aşağıdaki yapılandırmayla **yeni bir agent oluşturun:**
   ```
   Agent Name: GitHubAgent
   ```

3. **Özel MCP sunucusunu başlatın:**
   - **Tools** → **Add Tool** → **MCP Server** yolunu izleyin
   - **"Create A new MCP Server"** seçeneğini seçin
   - Maksimum esneklik için **Python şablonunu** tercih edin
   - **Sunucu Adı:** `git_mcp_server`

### Adım 2: GitHub Copilot Agent Mode’u Yapılandırma

1. VS Code’da **GitHub Copilot’u açın** (Ctrl/Cmd + Shift + P → "GitHub Copilot: Open")
2. Copilot arayüzünde **Agent Model’i seçin**
3. Gelişmiş akıl yürütme için **Claude 3.7 modelini seçin**
4. Araç erişimi için **MCP entegrasyonunu etkinleştirin**

> **💡 İpucu:** Claude 3.7, geliştirme iş akışları ve hata yönetimi kalıplarını daha iyi anlar.

### Adım 3: Temel MCP Sunucu İşlevselliğini Uygulama

**GitHub Copilot Agent Mode ile aşağıdaki detaylı prompt’u kullanın:**

```
Create two MCP tools with the following comprehensive requirements:

🔧 TOOL A: clone_repository
Requirements:
- Clone any GitHub repository to a specified local folder
- Return the absolute path of the successfully cloned project
- Implement comprehensive validation:
  ✓ Check if target directory already exists (return error if exists)
  ✓ Validate GitHub URL format (https://github.com/user/repo)
  ✓ Verify git command availability (prompt installation if missing)
  ✓ Handle network connectivity issues
  ✓ Provide clear error messages for all failure scenarios

🚀 TOOL B: open_in_vscode
Requirements:
- Open specified folder in VS Code or VS Code Insiders
- Cross-platform compatibility (Windows/Linux/macOS)
- Use direct application launch (not terminal commands)
- Auto-detect available VS Code installations
- Handle cases where VS Code is not installed
- Provide user-friendly error messages

Additional Requirements:
- Follow MCP 1.9.3 best practices
- Include proper type hints and documentation
- Implement logging for debugging purposes
- Add input validation for all parameters
- Include comprehensive error handling
```

### Adım 4: MCP Sunucunuzu Test Edin

#### 4a. Agent Builder’da Test

1. Agent Builder için **debug yapılandırmasını başlatın**
2. Agent’ınızı aşağıdaki sistem prompt’u ile yapılandırın:

```
SYSTEM_PROMPT:
You are my intelligent coding repository assistant. You help developers efficiently clone GitHub repositories and set up their development environment. Always provide clear feedback about operations and handle errors gracefully.
```

3. Gerçekçi kullanıcı senaryolarıyla test edin:

```
USER_PROMPT EXAMPLES:

Scenario : Basic Clone and Open
"Clone {Your GitHub Repo link such as https://github.com/kinfey/GHCAgentWorkshop
 } and save to {The global path you specify}, then open it with VS Code Insiders"
```

![Agent Builder Testing](../../../../translated_images/tr/DebugAgent.81d152370c503241b3b39a251b8966f7f739286df19dd57f9147f6402214a012.png)

**Beklenen Sonuçlar:**
- ✅ Yol doğrulaması ile başarılı klonlama
- ✅ Otomatik VS Code açılışı
- ✅ Geçersiz durumlar için net hata mesajları
- ✅ Kenar durumların doğru yönetimi

#### 4b. MCP Inspector’da Test


![MCP Inspector Testing](../../../../translated_images/tr/DebugInspector.eb5c95f94c69a8ba36944941b9a3588309a3a2fae101ace470ee09bde41d1667.png)

---



**🎉 Tebrikler!** Gerçek geliştirme iş akışı sorunlarını çözen pratik ve üretime hazır bir MCP sunucusu oluşturmayı başardınız. Özel GitHub klon sunucunuz, geliştirici verimliliğini otomatikleştirip artırmada MCP’nin gücünü gösteriyor.

### 🏆 Kazanılan Başarılar:
- ✅ **MCP Geliştiricisi** - Özel MCP sunucusu oluşturdu
- ✅ **İş Akışı Otomatörü** - Geliştirme süreçlerini kolaylaştırdı  
- ✅ **Entegrasyon Uzmanı** - Birden fazla geliştirme aracını bağladı
- ✅ **Üretime Hazır** - Dağıtıma uygun çözümler geliştirdi

---

## 🎓 Atölye Tamamlama: Model Context Protocol Yolculuğunuz

**Değerli Atölye Katılımcısı,**

Model Context Protocol atölyesinin dört modülünü tamamladığınız için tebrikler! Temel AI Toolkit kavramlarından başlayarak gerçek dünya geliştirme zorluklarını çözen üretime hazır MCP sunucuları oluşturma noktasına geldiniz.

### 🚀 Öğrenme Yolculuğunuzun Özeti:

**[Modül 1](../lab1/README.md)**: AI Toolkit temellerini, model testlerini ve ilk AI agent’ınızı oluşturmayı keşfettiniz.

**[Modül 2](../lab2/README.md)**: MCP mimarisini öğrendiniz, Playwright MCP’yi entegre ettiniz ve ilk tarayıcı otomasyon agent’ınızı geliştirdiniz.

**[Modül 3](../lab3/README.md)**: Hava durumu MCP sunucusu ile özel MCP sunucu geliştirmede ilerlediniz ve hata ayıklama araçlarını ustalıkla kullandınız.

**[Modül 4](../lab4/README.md)**: Şimdi her şeyi kullanarak pratik bir GitHub depo iş akışı otomasyon aracı oluşturdunuz.

### 🌟 Ustalaştığınız Konular:

- ✅ **AI Toolkit Ekosistemi**: Modeller, agent’lar ve entegrasyon kalıpları
- ✅ **MCP Mimarisi**: İstemci-sunucu tasarımı, taşıma protokolleri ve güvenlik
- ✅ **Geliştirici Araçları**: Playground’dan Inspector’a ve üretim dağıtımına kadar
- ✅ **Özel Geliştirme**: Kendi MCP sunucularınızı oluşturma, test etme ve dağıtma
- ✅ **Pratik Uygulamalar**: AI ile gerçek dünya iş akışı sorunlarını çözme

### 🔮 Sonraki Adımlarınız:

1. **Kendi MCP Sunucunuzu İnşa Edin**: Bu becerileri kullanarak benzersiz iş akışlarınızı otomatikleştirin
2. **MCP Topluluğuna Katılın**: Yaptıklarınızı paylaşın ve başkalarından öğrenin
3. **İleri Entegrasyonu Keşfedin**: MCP sunucularını kurumsal sistemlere bağlayın
4. **Açık Kaynağa Katkıda Bulunun**: MCP araçları ve dokümantasyonunu geliştirin

Unutmayın, bu atölye sadece bir başlangıç. Model Context Protocol ekosistemi hızla gelişiyor ve siz artık AI destekli geliştirme araçlarının ön saflarında yer almaya hazırsınız.

**Katılımınız ve öğrenmeye olan bağlılığınız için teşekkür ederiz!**

Umarız bu atölye, geliştirme yolculuğunuzda AI araçlarıyla nasıl çalışacağınız konusunda size ilham verir.

**İyi kodlamalar!**

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.