# Senaryo 3: VS Code'da MCP Sunucusu ile Editör İçi Dokümantasyon

## Genel Bakış

Bu senaryoda, Microsoft Learn Dokümanlarını MCP sunucusu kullanarak doğrudan Visual Studio Code ortamınıza nasıl getireceğinizi öğreneceksiniz. Sürekli tarayıcı sekmeleri arasında geçiş yaparak dokümantasyon aramak yerine, resmi dokümanlara doğrudan editörünüzün içinden erişebilir, arama yapabilir ve referans verebilirsiniz. Bu yöntem iş akışınızı hızlandırır, odaklanmanızı sağlar ve GitHub Copilot gibi araçlarla sorunsuz entegrasyon imkanı sunar.

- Kodlama ortamınızdan çıkmadan VS Code içinde dokümanları arayın ve okuyun.
- Dokümantasyonlara referans verin ve bağlantıları doğrudan README veya kurs dosyalarınıza ekleyin.
- GitHub Copilot ve MCP’yi birlikte kullanarak yapay zekâ destekli kesintisiz bir dokümantasyon iş akışı oluşturun.

## Öğrenme Hedefleri

Bu bölümün sonunda, VS Code içinde MCP sunucusunu kurup kullanarak dokümantasyon ve geliştirme iş akışınızı nasıl geliştireceğinizi anlayacaksınız. Şunları yapabileceksiniz:

- Dokümantasyon araması için MCP sunucusunu kullanacak şekilde çalışma alanınızı yapılandırmak.
- VS Code içinden doğrudan dokümantasyon aramak ve eklemek.
- Daha verimli, yapay zekâ destekli bir iş akışı için GitHub Copilot ve MCP’nin gücünü birleştirmek.

Bu beceriler, odaklanmanızı artırmanıza, dokümantasyon kalitenizi iyileştirmenize ve geliştirici ya da teknik yazar olarak verimliliğinizi yükseltmenize yardımcı olacak.

## Çözüm

Editör içi dokümantasyon erişimi sağlamak için MCP sunucusunu VS Code ve GitHub Copilot ile entegre eden bir dizi adımı takip edeceksiniz. Bu çözüm, kurs yazarları, dokümantasyon yazarları ve dokümanlar ile Copilot arasında çalışırken odaklarını editörde tutmak isteyen geliştiriciler için idealdir.

- Kurs veya proje dokümantasyonu yazarken README dosyasına hızlıca referans bağlantıları ekleyin.
- Copilot’u kod üretmek için, MCP’yi ise ilgili dokümanları anında bulup alıntılamak için kullanın.
- Editörünüzde odaklanmaya devam edin ve verimliliğinizi artırın.

### Adım Adım Rehber

Başlamak için aşağıdaki adımları izleyin. Her adım için, süreci görsel olarak göstermek amacıyla assets klasöründen bir ekran görüntüsü ekleyebilirsiniz.

1. **MCP yapılandırmasını ekleyin:**  
   Proje kök dizininizde `.vscode/mcp.json` dosyası oluşturun ve aşağıdaki yapılandırmayı ekleyin:  
   ```json
   {
     "servers": {
       "LearnDocsMCP": {
         "url": "https://learn.microsoft.com/api/mcp"
       }
     }
   }
   ```  
   Bu yapılandırma, VS Code’a [`Microsoft Learn Docs MCP server`](https://github.com/MicrosoftDocs/mcp) ile nasıl bağlantı kurulacağını söyler.

   ![Adım 1: mcp.json dosyasını .vscode klasörüne ekleyin](../../../../../../translated_images/tr/step1-mcp-json.c06a007fccc3edfaf0598a31903c9ec71476d9fd3ae6c1b2b4321fd38688ca4b.png)
    
2. **GitHub Copilot Chat panelini açın:**  
   Eğer GitHub Copilot eklentisi yüklü değilse, VS Code’daki Extensions görünümüne gidip yükleyin. Doğrudan [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) üzerinden de indirebilirsiniz. Ardından, yan panelden Copilot Chat panelini açın.

   ![Adım 2: Copilot Chat panelini açın](../../../../../../translated_images/tr/step2-copilot-panel.f1cc86e9b9b8cd1a85e4df4923de8bafee4830541ab255e3c90c09777fed97db.png)

3. **Agent modunu etkinleştirin ve araçları doğrulayın:**  
   Copilot Chat panelinde agent modunu etkinleştirin.

   ![Adım 3: Agent modunu etkinleştirin ve araçları doğrulayın](../../../../../../translated_images/tr/step3-agent-mode.cdc32520fd7dd1d149c3f5226763c1d85a06d3c041d4cc983447625bdbeff4d4.png)

   Agent modunu açtıktan sonra, MCP sunucusunun kullanılabilir araçlar arasında listelendiğinden emin olun. Bu, Copilot agent’ın ilgili bilgileri almak için dokümantasyon sunucusuna erişebilmesini sağlar.

   ![Adım 3: MCP sunucu aracını doğrulayın](../../../../../../translated_images/tr/step3-verify-mcp-tool.76096a6329cbfecd42888780f322370a0d8c8fa003ed3eeb7ccd23f0fc50c1ad.png)

4. **Yeni bir sohbet başlatın ve agent’a komut verin:**  
   Copilot Chat panelinde yeni bir sohbet açın. Artık agent’a dokümantasyon sorgularınızı iletebilirsiniz. Agent, MCP sunucusunu kullanarak ilgili Microsoft Learn dokümanlarını doğrudan editörünüzde getirecek ve gösterecektir.

   - *"X konusu için bir çalışma planı hazırlamaya çalışıyorum. 8 hafta boyunca çalışacağım, her hafta için hangi içerikleri almam gerektiğini öner."*

   ![Adım 4: Agent’a sohbet içinde komut verin](../../../../../../translated_images/tr/step4-prompt-chat.12187bb001605efc5077992b621f0fcd1df12023c5dce0464f8eb8f3d595218f.png)

5. **Canlı Sorgu:**

   > Azure AI Foundry Discord’daki [#get-help](https://discord.gg/D6cRhjHWSC) bölümünden canlı bir sorgu alalım ([orijinal mesajı görüntüle](https://discord.com/channels/1113626258182504448/1385498306720829572)):  
   
   *"Azure AI Foundry üzerinde geliştirilen AI ajanlarıyla çoklu ajan çözümünü nasıl dağıtacağım konusunda cevap arıyorum. Copilot Studio kanalları gibi doğrudan bir dağıtım yöntemi olmadığını görüyorum. Peki, kurumsal kullanıcıların etkileşimde bulunup işi halletmesi için bu dağıtımı yapmanın farklı yolları nelerdir?  
   MS Teams ile Azure AI Foundry Ajanları arasında köprü görevi görecek Azure Bot servisini kullanabileceğimizi söyleyen birçok makale/blog var, peki Azure fonksiyonu aracılığıyla Orchestrator Agent’a bağlanan bir Azure bot kurarsam bu işe yarar mı yoksa çoklu ajan çözümündeki her AI ajanı için Bot framework’te orkestrasyon yapmak üzere ayrı Azure fonksiyonları mı oluşturmam gerekir? Başka önerilere de açığım."*

   ![Adım 5: Canlı sorgular](../../../../../../translated_images/tr/step5-live-queries.49db3e4a50bea27327e3cb18c24d263b7d134930d78e7392f9515a1c00264a7f.png)

   Agent, ilgili dokümantasyon bağlantıları ve özetlerle yanıt verecek; bunları markdown dosyalarınıza doğrudan ekleyebilir veya kodunuzda referans olarak kullanabilirsiniz.

### Örnek Sorgular

Deneyebileceğiniz bazı örnek sorgular şunlardır. Bu sorgular, MCP sunucusu ve Copilot’un VS Code’dan çıkmadan anında, bağlama duyarlı dokümantasyon ve referanslar sunmak için nasıl birlikte çalıştığını gösterecektir:

- "Azure Functions tetikleyicilerini nasıl kullanırım göster."
- "Azure Key Vault için resmi dokümantasyon bağlantısı ekle."
- "Azure kaynaklarını güvence altına almak için en iyi uygulamalar nelerdir?"
- "Azure AI servisleri için hızlı başlangıç rehberi bul."

Bu sorgular, MCP sunucusu ve Copilot’un VS Code’dan çıkmadan anında, bağlama duyarlı dokümantasyon ve referanslar sağlamak için nasıl birlikte çalıştığını gösterecektir.

---

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.