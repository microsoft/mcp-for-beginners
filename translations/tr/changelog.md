# Değişiklik Kaydı: Yeni Başlayanlar için MCP Müfredatı

Bu belge, Model Context Protocol (MCP) Yeni Başlayanlar müfredatında yapılan tüm önemli değişikliklerin kaydıdır. Değişiklikler ters kronolojik sırayla (en yeni değişiklikler önce) belgelenmiştir.

## 9 Eylül 2026

### MCP 2026-07-28 Nihai Spesifikasyon Hizalaması

İngilizce müfredat, yayın adayı ve `2025-11-25`
temel rehberlikten nihai MCP `2026-07-28` spesifikasyonuna güncellendi.

- **Güncellendi**: Mevcut sürüm referansları, spesifikasyon bağlantıları, durum bilgisiz
  istek rehberliği, `server/discover`, Akışlanabilir HTTP başlıkları ve Görevler
  eklenti yaşam döngüsü dahil olmak üzere 38 İngilizce belge dosyası.
- **Düzeltildi**: Elicitation artık `elicitation/create` kullanıyor, Sampling
  `sampling/createMessage` kullanıyor ve `InputRequiredResult.resultType`
  `"input_required"` değerini kullanıyor.
- **Değiştirildi**: Yanlış olan Root Context konuşma durumu dersi, bilgi amaçlı dosya sistemi ipuçlarını,
  mevcut çok tur akışı, güvenlik sınırlarını ve göç seçeneklerini kapsayan protokole uygun Roots dersiyle değiştirildi.

- **Açıklandı**: Roots, Sampling, Logging ve Dynamic Client Registration `2026-07-28`'de kullanımdan 
  kaldırılmıştır; bunların önerilen yer değiştirmeleri ve erken kaldırma tarihleri belgelenmiştir.

- **Etiketlendi**: MCP `2025-11-25`, HTTP+SSE, başlangıç el sıkışmaları veya protokol oturumlarına
  halen bağlı olan örnekler güncel uygulamalar olarak değil, eski uyumluluk örnekleri olarak
  tutulmaktadır.
- **Güvenlik rehberi**: Bağımsız güvenlik rehberleri, kaldırılmış protokol oturum kimlikleri yerine
  istek başına yetkilendirme ve açık uygulama durumu tutamaçları kullanacak şekilde güncellendi.
  İstemci Kimliği Meta Verisi Belgeleri artık tercih edilen kayıt yolu olup, DCR uyumluluk amaçlıdır.

- **Destekleyici materyal**: Çalışma rehberi, katkıda bulunan kontrol listesi,
  Publora vaka çalışması ve APIM vaka çalışması güncellendi. APIM kılavuzu artık
  kullanımdan kaldırılmış `/sse` yerine mevcut Akışlanabilir HTTP `/mcp` uç noktasını öneriyor.
- **Kanonik bağlantılar**: İngilizce kaynak Markdown'daki emekliye ayrılmış ve taslak
  spesifikasyon URL'leri, sürümlü `2026-07-28` bağlantılarıyla değiştirilmiş, eski araçlara bağlı
  örnekler için açık bağlantılar korunmuştur.
- **Sabit dosya adları**: Nihai spesifikasyon rehberi ve iki güvenlik rehberi, yayın adayı ve yıl
  ekleri kaldırılarak yeniden adlandırıldı, tüm İngilizce bağlantılar sabit yollarına güncellendi.

- **Yeni yetkilendirme örneği**: Test edilmiş
  [TypeScript MCP `2026-07-28` kaynak sunucusu](./02-Security/samples/cimd-dcr-auth/README.md)
  eklendi; bu örnek tercih edilen İstemci Kimliği Meta Verisi Belgeleri ile kaldırılmış Dinamik
  İstemci Kaydı yedeklemesini karşılaştırıyor. Örnek RFC 9728 keşfi, JWKS doğrulaması,
  araç başına alanlar, on iki test ve Auth0 kurulum kılavuzu içeriyor.
- **Çeviri kapsamı**: Yalnızca İngilizce kaynak dosyalar düzenlendi; otomatik çevrilen
  çeviriler ve çevirilmiş görseller değişmeden bırakıldı.

## 29 Temmuz 2026

### Yeni Modül 08 Yardımcısı: Güvenilirlik Yardımcıları ve Güvenli Yeniden Denemeler

Gerçek dünya etkileri yaratan MCP araçları için satıcıdan bağımsız bir yardımcı ders eklendi,
nihai `2026-07-28` spesifikasyonuna uyumlu.


- **Yeni**: [güvenilirlik yan arabaşı dersi][reliability-sidecar]
  bir destek bileti hikayesi, iki Mermaid diyagramı ve bir yeniden deneme kararı
  akışı kullanarak kararlı işletim anahtarlarını, atomik tekrar kabulünü,
  uzlaştırmayı, delilleri ve Görevler uzantı sınırını açıklar.
- **Yeni**: Standart kütüphane Python ve SQLite hata enjeksiyonu egzersizi
  ayrı işlem ve bilet deposu kullanarak dışsal bir etkinlik işlendikten sonra
  kaybolan yanıtı gösterir. Altı deterministik test, saf çoğaltmayı,
  korumalı yeniden başlatma kurtarmasını, yük çakışmalarını, önbelleğe alınmış sonuçları,
  aktif talepleri ve eşzamanlı tekrar kabulü kapsar.
- **Güncellendi**: Modül 08 artık yan arabaşı dersine bağlantı verir, son 
  `2026-07-28` durumsuz istek modelini tanımlar, OpenTelemetry
  gözlemlenebilirliğini kullanımdan kaldırılan MCP günlük özelliğinden ayırır ve
  genel yeniden deneme örneğini salt-okuma işlemleri ile sınırlar.
- **İsteğe bağlı**: Ders taşınabilir kavramlarını etiketlenmiş bir topluluk
  uygulamasına eşler ancak barındırılan hizmeti veya bir ağ çağrısını
  egzersizin parçası yapmaz.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2 Temmuz 2026

### Yeni Ders: 2026-07-28 MCP Spesifikasyon Sürüm Adayı

21 Mayıs 2026'da duyurulan; 28 Temmuz 2026'da nihai sürümü planlanan `2026-07-28` MCP spesifikasyon sürüm adayının kapsamı eklendi, [resmi duyuru blog yazısından](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) özetlendi. Müfredat temel sürüm olarak yeni sürüm yayınlanana kadar **MCP Specification 2025-11-25** sürümünü korur, bu nedenle mevcut dersler yeniden yazılmak yerine geleceğe dönük rehberlik olarak sunulmaktadır.

- **Yeni**: [01-CoreConcepts/mcp-2026-07-28.md](./01-CoreConcepts/mcp-2026-07-28.md) — durumsuz protokol çekirdeğini ( `initialize` el sıkışma ve `Mcp-Session-Id` kaldırılması), yeni `Mcp-Method`/`Mcp-Name` yönlendirme başlıklarını, `ttlMs`/`cacheScope` önbellek meta verilerini, `_meta` içindeki W3C İzleme Bağlamını, resmi Uzantılar çerçevesini (MCP Uygulamaları ve yeni Görevler uzantısı), altı yetkilendirme sertleştirme SEP'sini, Roots/Sampling/Logging kullanımdan kaldırmayı ve JSON Schema 2020-12 araç şemalarına geçişi kapsayan tam bir ders.
- **Güncellendi**: yeni derse bağlantılar içeren geleceğe dönük bilgilendirme satırları:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): protokol sürüm notu, Sampling/Roots/Logging/Tasks bölümleri ve "Sırada ne var"
  - [02-Security/README.md](./02-Security/README.md): yetkilendirme sertleştirme bilgilendirmesi
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): durumsuz taşıma bilgilendirmesi
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Sampling kullanımdan kaldırma uyarısı

  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Günlük kaydı kullanımdan kaldırma ve Görevler genişletme çağrısı

  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): durumsuz/oturum-yönlendirme dikkat çekme
  - [README.md](./README.md): spesifikasyon bölümünde "İleriye Bakış" notu ve müfredat modülü tablosunda yeni bir `1.1` girişi
  - [study_guide.md](./study_guide.md): Temel Kavramlar genelinde ileriye dönük madde işareti ve tarihli ek not
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): durumsuz istek modeli öncesi `mcp-session-id` taşıma haritası üzerine dikkat çekme
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): Kök Bağlamlar/Örnekleme kullanımdan kaldırma ve Görevler uzantısı hakkında modül genel bakış notu
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): yetkilendirme güçlendirme dikkat çekme

## 24 Haziran 2026

### Yeni Ders: MCP'nin Copilot uygulamasında kullanımı

- [Araçlar bölümü](./12-tooling/README.md) Araçlar bölümü eklendi.
- [Copilot uygulamasında MCP](./12-tooling/01-copilot-app/README.md)

## 16 Haziran 2026

### MCP Spesifikasyon Hizalaması ve Örnek Doğrulama

Müfredat, mevcut **MCP Spesifikasyonu 2025-11-25** ve en son resmi SDK'lar ile doğrulandı, ardından kalan eski spesifikasyon referansları düzeltildi ve temel örneklerin hâlâ derlenip çalıştığı teyit edildi.

#### Spesifikasyon Sürümü Düzeltmeleri (2025-06-18 / 2025-03-26 → 2025-11-25)

İngilizce içerik, daha eski bir spec revizyonunun *mevcut/en güncel* standart olduğunu iddia eden yerler güncellendi ve bağlantılar canonical `modelcontextprotocol.io` spec yollarına yönlendirildi:
- **05-AdvancedTopics/mcp-security/README.md**: "Mevcut Standart" bayrağı, giriş, temel güvenlik ilkeleri başlığı, zorunlu gereksinimler başlığı, Microsoft Entra ID bölümü, Referanslar & Kaynaklar bağlantıları ve kapanış güvenlik bildirimi (8 referans) 2025-11-25 olarak güncellendi
- **05-AdvancedTopics/mcp-transport/README.md**: Ek Kaynaklar spesifikasyon linki ve "Mevcut Standart" bayrağı 2025-11-25 olarak güncellendi
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Eski `2025-03-26` güvenlik-ve-güven bağlantısı güncel 2025-11-25 güvenlik en iyi uygulamaları sayfası ile değiştirildi
- **03-GettingStarted/14-sampling/README.md**: Resmi örnekleme dokümanları linki 2025-11-25 olarak güncellendi
- **03-GettingStarted/05-stdio-server/README.md**: Şimdiki zaman kipli "mevcut MCP spesifikasyonu" referansı ve Ek Kaynaklar spesifikasyon linki 2025-11-25 olarak güncellendi (tarihsel SSE-kaldırma notları doğruluk için olduğu gibi bırakıldı)

#### Mevcut SDK'lara Karşı Örnek Doğrulama

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` `@modelcontextprotocol/sdk@1.29.0` paketini çözdü; `tsc --noEmit` tipi hatası olmadan geçti — mevcut `McpServer`/`StdioServerTransport` API'leri geçerliliğini koruyor
- **Python (03-GettingStarted/01-first-server/solution/python)**: İzole bir `.venv` içinde `mcp[cli]` (1.27.2) ile doğrulandı; `py_compile` geçti ve `FastMCP.list_tools()` `add` ve `subtract` araçlarını doğru şekilde döndürdü
- Tüm örnek `@modelcontextprotocol/sdk` sürüm aralıklarının (`>=1.26.0` / `^1.26.0` / `^1.27.0`) mevcut `1.29.0` sürümüne sorunsuz ve API uyumsuzluğu olmadan çözüldüğü teyit edildi

#### Bağımlılık Sabitleme Uyumu (sürüm boşluklarını kapatma)

Eski SDK sabitlemeleri, her örneğin mevcut MCP sürümünü takip etmesi için yükseltildi; depo genelindeki uygulama ile eşleşiyor:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: `@modelcontextprotocol/sdk` `^1.8.0`'den `>=1.26.0`'a yükseltildi ve modül açıklaması `"updated for MCP 2025-06-18"` `"aligned with MCP Specification 2025-11-25"` olarak güncellendi
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** ve **lab4/code/github_mcp_server/pyproject.toml**: Kesin sabit `mcp==1.23.0` `mcp>=1.26.0` olarak yükseltildi; her iki `uv.lock` dosyası (`uv lock`) yeniden oluşturuldu böylece kilit dosyalar mevcut `mcp 1.27.2` sürümüne çözülüyor ve manifestlerle senkron kalıyor

#### Müfredat Boşluğu Analizi — En Son Spec Özellik Kapsamı

Müfredatın MCP 2025-11-25 içinde tanıtılan/genişletilen tüm ilkel tipleri zaten kapsadığı doğrulandı, bu nedenle içerik boşluğu yok:
- **Örnekleme**: Ders 03-GettingStarted/14-sampling ve 05-AdvancedTopics/mcp-sampling
- **Belirtme (URL modu dahil)**: 01-CoreConcepts ve 05-AdvancedTopics/mcp-protocol-features içinde belgelenmiş
- **Kökler**: 00-Introduction, 01-CoreConcepts ve 05-AdvancedTopics/mcp-root-contexts içinde belgelenmiş
- **Görevler (deneysel, uzun süreli işlemler)**: 01-CoreConcepts ve 05-AdvancedTopics/mcp-protocol-features içinde belgelenmiş
- **Araç Açıklamaları** (`readOnlyHint` / `destructiveHint`): 01-CoreConcepts ve 05-AdvancedTopics/mcp-protocol-features içinde belgelenmiş

### Güvenlik Güçlendirme & Bağımlılık Güvenlik Açıkları Düzeltmeleri

Tüm bağımlılık manifestoları ve örnek kaynak kodda tam bir güvenlik taraması yapıldı, ardından bildirilen tüm npm uyarıları ve bir kod seviyesi bulgu giderildi. Düzenlemeler sonrası her denetlenen dizinde `npm audit` **0 açık** raporladı.

#### npm Bağımlılık Güvenlik Açıkları (geçişli) — Düzeltildi

Tüm 15 taahhüt edilmiş `package-lock.json` dosyası denetlendi. Güvenlik açıkları MCP Inspector dev aracının, OpenAI istemcisinin ve MCP SDK'nın dolaylı bağımlılıklarında sınırlıydı; hepsi örnekleri kırmadan şimdi çözüldü:

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** ve **lab3/code/weather_mcp/inspector**: Paketli `ajv`, `brace-expansion`, `diff`, `path-to-regexp` ve `ws` uyarılarını temizleyen `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`) sürümü yükseltildi. `concurrently` tarafından taşınan kritik uyarıyı ortadan kaldırmak için yamalanmış `shell-quote@1.8.4` sürümünü zorlayan bir npm `overrides` girdisi eklendi; her iki kilit dosyası yeniden oluşturuldu (şimdi 0 güvenlik açığı)
- **03-GettingStarted/samples/typescript**: `npm audit fix` ile geçişli `qs` (orta düzey) yamalı bir sürüme güncellendi
- **03-GettingStarted/samples/javascript**: `npm audit fix` ile geçişli `hono` (orta düzey) yamalı bir sürüme güncellendi
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` ile geçişli `form-data` (yüksek) yamalı bir sürüme güncellendi
- **03-GettingStarted/11-simple-auth/solution/typescript**: Projenin tekrarlanabilir ve denetlenebilir olması için eksik `package-lock.json` oluşturuldu (0 güvenlik açığı)

#### Kod Düzeyinde Güvenlik Düzeltmesi (OWASP A03: Enjeksiyon)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: `open_in_vscode` aracından `shell=True` kaldırıldı. Önceki `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` komutu, klasör yolundaki kabuk meta karakterlerinin `cmd.exe` tarafından yorumlanmasına izin veriyordu (komut enjeksiyon vektörü). Artık `Code.exe` doğrudan klasör argümanı ile kabuk olmadan başlatılıyor — işlevsel olarak eşdeğer ve güvenli.

#### Python Bağımlılık Denetimi

- `pip-audit` ile tüm Python gereksinim setleri denetlendi. `05-AdvancedTopics` ve `03-GettingStarted/samples/python` **bilinen bir güvenlik açığı olmadığını** bildirdi (`mcp` / `httpx` / `pydantic` / `python-dotenv` sürümleri güncel yamalı sürümleri çözüyor)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit`, üç `safe_join` Windows cihaz-adı DoS uyarısı olan geçişli bağımlılık **`werkzeug` 3.1.1**'i işaret etti — `CVE-2025-66221`, `CVE-2026-21860` ve `CVE-2026-27199` (tümü 3.1.6'da düzeltildi). Yamalanmış sürümün çözülmesi için açık bir güvenlik sabitlemesi `werkzeug>=3.1.6` eklendi; kısıtlamaların `chainlit` / `mcp` / `semantic-kernel` yığınıyla temiz çözüldüğü doğrulandı

### Ürün İsmi Yeniden Markalaşması

Microsoft'un ürün yeniden markalaşmasını yansıtmak için tüm müfredat içerikleri güncellendi:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Discord topluluk bağlantısı güncellendi
- **AGENTS.md**: Discord sunucu referansı güncellendi
- **README.md**: Teknoloji ekosistemi referansları güncellendi
- **study_guide.md**: Vaka çalışması referansları güncellendi
- **05-AdvancedTopics/README.md**: Modül 5.13 başlık ve açıklaması güncellendi
- **05-AdvancedTopics/mcp-integration/README.md**: Bölüm başlığı ve açıklaması güncellendi
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Tam modül başlığı ve içerik güncellemesi
- **05-AdvancedTopics/mcp-security-entra/README.md**: Çapraz referans bağlantısı güncellendi
- **07-LessonsfromEarlyAdoption/README.md**: Vaka çalışması referansları güncellendi
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Bölüm 9 başlığı, rozetler ve yetenekler güncellendi
- **08-BestPractices/README.md**: Discord topluluk bağlantısı güncellendi
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Discord kanal referansı güncellendi
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Model dağıtım referansı güncellendi
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: AI Hizmetleri tablosu güncellendi
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Kaynak referansları güncellendi

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension for VS Code
- **README.md**: Ana müfredat referansları güncellendi
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Modül başlığı, genel bakış ve tüm modül başlıkları güncellendi
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Başlık, öğrenme hedefleri, kurulum talimatları ve kaynaklar güncellendi
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Başlık, öğrenme hedefleri, MCP ana bilgisayarlar tablosu ve çapraz referanslar güncellendi
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Başlık, rozetler, önkoşullar ve kaynaklar güncellendi
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Agent Builder referansları ve geri bildirim bağlantısı güncellendi
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Önkoşullar ve eklenti referansları güncellendi

---

## 11 Nisan 2026

### Yeni Ders, Dokümantasyon Düzeltmeleri ve Bağımlılık Güncellemeleri

#### Yeni Müfredat İçeriği Eklendi

**Modül 05 - Gelişmiş Konular**
- **Ders 5.17: MCP ile Rekabetçi Çoklu Ajan Muhakemesi** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Çoklu ajan sistemleri için rekabetçi tartışma modelini kapsayan yeni kapsamlı kılavuz
  - Mermaid mimari diyagramı: iki ajan → paylaşılan MCP sunucusu → tartışma transkripti → hakem → karar
  - Python ve TypeScript'te uygulanmış paylaşılan MCP araç sunucusu (`web_search` + `run_python`)
  - Karşıt sistem istemleri (LEHTE / ALEYHTE / Hakem) açık araç kullanımı gereksinimleri ile
  - Tur ve argüman yönlendirmesini yöneten Python, TypeScript ve C# tartışma yöneticisi
  - Orkestratör için MCP `ClientSession` kablolaması gerçek araç çağrılarına
  - Kullanım durumu tablosu (halüsinasyon tespiti, tehdit modelleme, API tasarım incelemesi, gerçek doğrulama, teknoloji seçimi)
  - Güvenlik önlemleri: izole yürütme, araç çağrısı doğrulama, oran sınırlama, denetim kaydı
  - Üç pratik senaryo içeren yapılandırılmış egzersiz (kod incelemesi, mimari karar, içerik denetimi)

#### Dokümantasyon Düzeltmeleri

**Modül 03 - Başlarken**
- **05-stdio-server/README.md**: Eksik olan TypeScript stdio sunucu örneği düzeltildi — Python ve .NET örneklerine uyması için eksik taşıma oluştumu (`new StdioServerTransport()`) ve `server.connect(transport)` çağrısı eklendi
- **14-sampling/README.md**: Yazım hatası düzeltildi — `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Müfredat Güncellemeleri

**Ana README.md**
- Yeni ders bağlantısı ile müfredat tablosuna giriş 5.17 (MCP ile Rekabetçi Çoklu Ajan Muhakemesi) eklendi

**05-AdvancedTopics/README.md**
- Dersler tablosuna Ders 5.17 satırı eklendi

**study_guide.md**
- Gelişmiş Konuların zihin haritasına ve metin açıklamasına Rekabetçi Çoklu Ajan Muhakemesi konusu eklendi

#### Kod ve Güvenlik Düzeltmeleri

**Modül 05 - Rekabetçi Ajanlar (`mcp-adversarial-agents`)**
- **Güvenlik düzeltmesi — komut enjeksiyonu**: TypeScript `run_python` aracında `execSync` kabuk içeriği `execFile` + `promisify` ile değiştirildi, komut enjeksiyonu yüzeyi ortadan kaldırıldı (LLM kontrollü kod artık kabuksuz literal argv öğesi olarak geçiyor)
- **MCP araç döngüsü kablolaması**: Python tartışma yöneticisi, engelleyen senkron `Anthropic` yerine `AsyncAnthropic` kullanacak, canlı `ClientSession` her ajan dönüşüne doğrudan geçecek, her tur `session.list_tools()` ile araç tanımları alacak ve model son metin yanıtı verene kadar `tool_use` bloklarını `session.call_tool()` aracılığıyla döngüyle yönetecek şekilde güncellendi

#### Bağımlılık Güncellemeleri

- `hono`, (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows) dahil birçok pakette 4.12.12 sürümüne yükseltildi
- TypeScript paketlerinde `@hono/node-server` 1.19.11'den 1.19.13'e yükseltildi
- Python paketlerinde (10-StreamliningAIWorkflows lab 3 ve 4) `cryptography` 46.0.5'ten 46.0.7'ye yükseltildi
- 10-StreamliningAIWorkflows inspector'da `lodash` 4.17.23'ten 4.18.1'e yükseltildi

#### Çeviriler

- 48+ dil için çeviriler, en son kaynak değişiklikleri ile senkronize edildi (i18n güncellemesi)

---

## 5 Şubat 2026

### Depo Genelinde Doğrulama ve Gezinme İyileştirmeleri

#### Yeni Müfredat İçeriği Eklendi

**Modül 03 - Başlarken**
- **12-mcp-hosts/README.md**: MCP ana bilgisayar kurulumları için yeni kapsamlı kılavuz
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf yapılandırma örnekleri
  - Tüm önemli ana bilgisayarlar için JSON yapılandırma şablonları
  - Taşıma türleri karşılaştırma tablosu (stdio, SSE/HTTP, WebSocket)
  - Yaygın bağlantı sorunlarının giderilmesi
  - Ana bilgisayar yapılandırması için güvenlik en iyi uygulamaları

- **13-mcp-inspector/README.md**: MCP Inspector için yeni hata ayıklama kılavuzu
  - Kurulum yöntemleri (npx, npm global, kaynaktan)
  - stdio ve HTTP/SSE üzerinden sunucuya bağlanma
  - Test araçları, kaynaklar ve istem iş akışları
  - MCP Inspector ile VS Code entegrasyonu
  - Yaygın hata ayıklama senaryoları ve çözümleri

**Modül 04 - Pratik Uygulama**
- **pagination/README.md**: Yeni sayfalama uygulama kılavuzu
  - Python, TypeScript, Java'da imleç tabanlı sayfalama desenleri
  - İstemci tarafı sayfalama işlemi
  - İmleç tasarım stratejileri (opak ve yapısal)
  - Performans optimizasyon önerileri

**Modül 05 - Gelişmiş Konular**
- **mcp-protocol-features/README.md**: Yeni protokol özellikleri derinlemesine inceleme
  - İlerleme bildirimleri uygulaması
  - İstek iptali desenleri
  - URI desenleri ile kaynak şablonları
  - Sunucu yaşam döngüsü yönetimi
  - Günlük (logging) seviyesi kontrolü
  - JSON-RPC kodları ile hata işleme desenleri

#### Gezinme Düzeltmeleri (24+ dosya güncellendi)

**Ana Modüller README dosyaları**
 Artık hem ilk derse hem de sonraki modüle bağlantı veriyor

**02-Güvenlik Alt Dosyaları**
- Tüm 5 ek güvenlik dokümanına artık "Sonraki Ne" navigasyonu eklendi:

**09-VakaÇalışması Dosyaları**
- Tüm vaka çalışması dosyalarına ardışık gezinme eklendi:

**10-StreamliningAI Labları**
Modül 10 genel bakış ve Modül 11'e Sonraki Ne bölümü eklendi

#### Kod ve İçerik Düzeltmeleri

**SDK ve Bağımlılık Güncellemeleri**
Boşopenai sürümü `^4.95.0` olarak düzeltildi
SDK `^1.8.0`'den `>=1.26.0`'a güncellendi
mcp sürüm sabitlemeleri `>=1.26.0` olarak güncellendi

**Kod Düzeltmeleri**
Geçersiz model `gpt-4o-mini` `gpt-4.1-mini` olarak düzeltildi

**İçerik Düzeltmeleri**
Bozuk bağlantı `READMEmd` → `README.md` düzeltildi, müfredat başlığı `Module 1-3` → `Module 0-3` olarak değiştirildi, büyük/küçük harf duyarlı yol düzeltildi
Bozuk çoğaltılmış Case Study 5 içeriği kaldırıldı

**Başlangıç Rehberliği İyileştirmeleri**
Yeni başlayanlar için uygun tanıtım, öğrenme hedefleri ve önkoşullar eklendi

#### Müfredat Güncellemeleri

**Ana README.md**
- Müfredat tablosuna 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Sayfalama), 5.16 (Protokol Özellikleri) girişleri eklendi

**Modül README dosyaları**
Ders listesine 12 ve 13 eklendi
Sayfalama bağlantısı ile Pratik Kılavuzlar bölümü eklendi
Dersler 5.15 (Özel Taşıma) ve 5.16 (Protokol Özellikleri) eklendi

**study_guide.md**
- Zihin haritası tüm yeni konularla güncellendi: MCP Hosts Kurulumu, MCP Inspector, Sayfalama Stratejileri, Protokol Özellikleri Derinlemesine

## 28 Ocak 2026

### MCP Spesifikasyonu 2025-11-25 Uyumluluk İncelemesi

#### Temel Kavramlar Geliştirmesi (01-CoreConcepts/)
- **Yeni İstemci İlkel - Roots**: Sunucuların dosya sistemi sınırlarını ve erişim izinlerini anlamasını sağlayan Roots istemci ilkeline dair kapsamlı dökümantasyon eklendi
- **Araç Açıklamaları**: Araç yürütme kararlarını geliştirmek için araç davranış açıklamaları (`readOnlyHint`, `destructiveHint`) dokümantasyonu eklendi
- **Örnekleme'de Araç Çağrısı**: Örnekleme belgeleri, örnekleme istekleri sırasında model odaklı araç çağrısı için `tools` ve `toolChoice` parametrelerini içerir şekilde güncellendi
- **URL Mod Elicitasyonu**: Sunucu kaynaklı dış web etkileşimleri için URL tabanlı tetikleme dokümantasyonu eklendi
- **Görevler (Deneysel)**: Kalıcı yürütme sarmalayıcıları ve ertelenmiş sonuç alma için deneysel Görevler özelliğini belgeleyen yeni bölüm eklendi

- **Simge Desteği**: Araçlar, kaynaklar, kaynak şablonları ve istemlerin artık ek meta veri olarak simgeler içerebileceği not edildi

#### Dokümantasyon Güncellemeleri
- **README.md**: MCP Spesifikasyonu 2025-11-25 sürüm referansı ve tarih tabanlı sürüm açıklaması eklendi
- **study_guide.md**: Müfredat haritası, Temel Kavramlar bölümünde Görevler ve Araç Açıklamaları eklenerek güncellendi; belge zaman damgası güncellendi

#### Spesifikasyon Uyum Doğrulaması
- **Protokol Sürümü**: Tüm dokümantasyonun güncel MCP Spesifikasyonu 2025-11-25'i referans verdiği doğrulandı
- **Mimari Hizalaması**: İki katmanlı mimari (Veri Katmanı + Taşıma Katmanı) dokümantasyon doğruluğu onaylandı
- **Primitifler Dokümantasyonu**: Sunucu primitifleri (Kaynaklar, İstemler, Araçlar) ve istemci primitifleri (Örnekleme, Teşhis, Kayıt, Kökler) doğrulandı
- **Taşıma Mekanizmaları**: STDIO ve Streamable HTTP taşıma dokümantasyonunun doğruluğu kontrol edildi
- **Güvenlik Rehberliği**: Güncel MCP Güvenlik En İyi Uygulamaları dokümantasyonuyla uyum teyit edildi

#### Belgelendi MCP 2025-11-25 Ana Özellikleri
- **OpenID Connect Discovery**: OIDC aracılığıyla kimlik doğrulama sunucusu keşfi
- **OAuth İstemci Kimliği Meta Veri Belgeleri**: Önerilen istemci kayıt mekanizması
- **JSON Şeması 2020-12**: MCP şema tanımları için varsayılan lehçe
- **SDK Katmanlama Sistemi**: SDK özellik desteği ve bakım için resmiyet kazandırılan gereksinimler
- **Yönetim Yapısı**: MCP yönetiminde Çalışma Grupları ve İlgi Grupları'nın resmi yapısı

### Güvenlik Dokümantasyonu Büyük Güncelleme (02-Security/)

#### MCP Güvenlik Zirvesi Atölyesi (Sherpa) Entegrasyonu
- **Yeni Pratik Eğitim Kaynağı**: [MCP Güvenlik Zirvesi Atölyesi (Sherpa)](https://azure-samples.github.io/sherpa/) ile tüm güvenlik dokümantasyonunda kapsamlı entegrasyon eklendi
- **Sefer Rotası Kapsamı**: Base Camp'ten Zirve'ye kamp-kamp ilerleme tam olarak belgelendi
- **OWASP Uyumu**: Tüm güvenlik rehberliği artık OWASP MCP Azure Güvenlik Kılavuzu risklerine karşılık geliyor

#### OWASP MCP Top 10 Entegrasyonu
- **Yeni Bölüm**: Güvenlik ana README'sine Azure hafifletmeleriyle OWASP MCP Top 10 Güvenlik Riskleri tablosu eklendi
- **Risk Bazlı Dokümantasyon**: mcp-security-controls-2025.md, her güvenlik alanı için OWASP MCP risk referansları ile güncellendi
- **Referans Mimari**: OWASP MCP Azure Güvenlik Kılavuzu referans mimarisi ve uygulama desenlerine bağlantı eklendi

#### Güncellenen Güvenlik Dosyaları
- **README.md**: Sherpa Atölyesi genel bakışı, sefer rota tablosu, OWASP MCP Top 10 risk özetleri ve pratik eğitim bölümü eklendi
- **mcp-security-controls-2025.md**: Başlık Şubat 2026 olarak güncellendi, OWASP risk referansları (MCP01-MCP08) eklendi, sürüm uyumsuzluğu giderildi
- **mcp-security-best-practices-2025.md**: Sherpa ve OWASP kaynakları bölümü eklendi, zaman damgası güncellendi
- **mcp-best-practices.md**: Sherpa ve OWASP bağlantıları ile uygulamalı eğitim bölümü eklendi
- **azure-content-safety-implementation.md**: OWASP MCP06 referansı, Sherpa Kamp 3 uyumu ve ek kaynaklar bölümü eklendi

#### Yeni Kaynak Bağlantıları Eklendi
- [MCP Güvenlik Zirvesi Atölyesi (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Güvenlik Kılavuzu](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Bireysel OWASP MCP risk sayfaları (MCP01-MCP10)

### Müfredat Geneli MCP Spesifikasyonu 2025-11-25 Uyumu

#### Modül 03 - Başlarken
- **SDK Dokümantasyonu**: Go SDK resmi SDK listesine eklendi; tüm SDK referansları MCP Spesifikasyonu 2025-11-25 uyumlu olarak güncellendi
- **Taşıma Açıklaması**: STDIO ve HTTP Akışlı taşıma açıklamaları açık spesifikasyon referanslarıyla güncellendi

#### Modül 04 - Pratik Uygulama
- **SDK Güncellemeleri**: Go SDK eklendi; SDK listesi spesifikasyon sürüm referansıyla güncellendi
- **Yetkilendirme Spesifikasyonu**: MCP Yetkilendirme spesifikasyon bağlantısı 2025-11-25 sürümüne güncellendi

#### Modül 05 - İleri Konular
- **Yeni Özellikler**: MCP Spesifikasyonu 2025-11-25 yeni özellikleri (Görevler, Araç Açıklamaları, URL Modu Teşhisi, Kökler) hakkında not eklendi
- **Güvenlik Kaynakları**: OWASP MCP Top 10 ve Sherpa atölyesi bağlantıları ek referanslara eklendi

#### Modül 06 - Topluluk Katkıları
- **SDK Listesi**: Swift ve Rust SDK’ları eklendi; spesifikasyon bağlantısı 2025-11-25 sürümüne güncellendi
- **Spesifikasyon Referansı**: MCP Spesifikasyon bağlantısı doğrudan spesifikasyon URL’sine güncellendi

#### Modül 07 - Erken Benimsemeden Dersler
- **Kaynak Güncellemeleri**: MCP Spesifikasyonu 2025-11-25 bağlantısı ve OWASP MCP Top 10 ek kaynaklara eklendi

#### Modül 08 - En İyi Uygulamalar
- **Spesifikasyon Sürümü**: MCP Spesifikasyonu referansı 2025-11-25 olarak güncellendi
- **Güvenlik Kaynakları**: OWASP MCP Top 10 ve Sherpa atölyesi ek referanslara eklendi

#### Modül 10 - AI İş Akışlarını Hızlandırma
- **Rozet Güncellemesi**: MCP sürüm rozeti SDK sürümünden (1.9.3) spesifikasyon sürümüne (2025-11-25) değiştirildi
- **Kaynak Bağlantıları**: MCP Spesifikasyon bağlantısı güncellendi; OWASP MCP Top 10 eklendi

#### Modül 11 - MCP Sunucu Uygulamalı Laboratuvarlar
- **Spesifikasyon Referansı**: MCP Spesifikasyon bağlantısı 2025-11-25 sürümüne güncellendi
- **Güvenlik Kaynakları**: Resmi kaynaklara OWASP MCP Top 10 eklendi

## 18 Aralık 2025

### Güvenlik Dokümantasyonu Güncellemesi - MCP Spesifikasyonu 2025-11-25

#### MCP Güvenlik En İyi Uygulamaları (02-Security/mcp-best-practices.md) - Spesifikasyon Sürüm Güncellemesi
- **Protokol Sürümü Güncellemesi**: En güncel MCP Spesifikasyonu 2025-11-25 (25 Kasım 2025 yayınlandı) referansı eklendi
  - Tüm spesifikasyon sürüm referansları 2025-06-18’den 2025-11-25’e güncellendi
  - Belge tarih referansları 18 Ağustos 2025’den 18 Aralık 2025’e değiştirildi
  - Tüm spesifikasyon URL’lerinin güncel dokümantasyona işaret ettiği doğrulandı
- **İçerik Doğrulaması**: Güvenlik en iyi uygulamalarının en güncel standartlara tam uyumu doğrulandı
  - **Microsoft Güvenlik Çözümleri**: Prompt Shields (önceden "Jailbreak risk tespiti"), Azure İçerik Güvenliği, Microsoft Entra ID ve Azure Key Vault güncel terminoloji ve bağlantıları doğrulandı
  - **OAuth 2.1 Güvenliği**: En güncel OAuth güvenlik en iyi uygulamaları ile uyum teyit edildi
  - **OWASP Standartları**: LLM’ler için OWASP Top 10 referanslarının güncel olduğu doğrulandı
  - **Azure Servisleri**: Tüm Microsoft Azure dokümantasyon bağlantıları ve en iyi uygulamalar teyit edildi
- **Standartlar Uyumu**: Referans verilen tüm güvenlik standartlarının güncel olduğu doğrulandı
  - NIST AI Risk Yönetim Çerçevesi
  - ISO 27001:2022
  - OAuth 2.1 Güvenlik En İyi Uygulamaları
  - Azure güvenlik ve uygunluk çerçeveleri
- **Uygulama Kaynakları**: Tüm uygulama kılavuzu bağlantıları ve kaynaklar doğrulandı
  - Azure API Yönetimi kimlik doğrulama desenleri
  - Microsoft Entra ID entegrasyon kılavuzları
  - Azure Key Vault gizli yönetimi
  - DevSecOps boru hatları ve izleme çözümleri

### Dokümantasyon Kalite Güvencesi
- **Spesifikasyon Uyumu**: Tüm zorunlu MCP güvenlik gereksinimlerinin (GEREKİR/GEREKMEZ) en güncel spesifikasyonla uyumu sağlandı
- **Kaynak Güncelliği**: Microsoft dokümantasyon, güvenlik standartları ve uygulama kılavuzlarına dış bağlantılar doğrulandı
- **En İyi Uygulamalar Kapsamı**: Kimlik doğrulama, yetkilendirme, AI’ye özgü tehditler, tedarik zinciri güvenliği ve kurumsal desenler tam olarak kapsandı

## 6 Ekim 2025

### Başlarken Bölüm Genişletmesi – Gelişmiş Sunucu Kullanımı & Basit Kimlik Doğrulama

#### Gelişmiş Sunucu Kullanımı (03-GettingStarted/10-advanced)
- **Yeni Bölüm Eklendi**: Hem düzenli hem de düşük seviye sunucu mimarilerini kapsayan kapsamlı MCP sunucu kullanım kılavuzu tanıtıldı.
  - **Düzenli vs Düşük Seviye Sunucu**: Her iki yaklaşım için Python ve TypeScript örnek kodları ile detaylı karşılaştırma.
  - **İşleyici Tabanlı Tasarım**: Ölçeklenebilir, esnek sunucu uygulamaları için araç/kaynak/istemci yönetiminde işleyici bazlı tasarım açıklaması.
  - **Pratik Desenler**: İleri düzey özellikler ve mimari için düşük seviye sunucu desenlerinin gerçek dünya senaryoları.

#### Basit Kimlik Doğrulama (03-GettingStarted/11-simple-auth)
- **Yeni Bölüm Eklendi**: MCP sunucularında basit kimlik doğrulama uygulamasına adım adım rehber.
  - **Kimlik Doğrulama Kavramları**: Kimlik doğrulama ve yetkilendirme; kimlik bilgisi yönetiminin net açıklaması.
  - **Temel Kimlik Doğrulama Uygulaması**: Python (Starlette) ve TypeScript (Express) ile ara katman (middleware) kimlik doğrulama desenleri, kod örnekleriyle.
  - **Gelişmiş Güvenliğe Geçiş**: Basit kimlik doğrulama ile başlayıp OAuth 2.1 ve RBAC’a geçiş için rehberlik; ileri güvenlik modüllerine referanslar.

Bu eklemeler, temel kavramlardan ileri üretim desenlerine köprü kurarak daha sağlam, güvenli ve esnek MCP sunucu uygulamaları geliştirmek için pratik, uygulamalı rehberlik sağlar.

## 29 Eylül 2025

### MCP Sunucu Veritabanı Entegrasyon Laboratuvarları - Kapsamlı Uygulamalı Öğrenme Yolu

#### 11-MCPServerHandsOnLabs - Yeni Tam Veritabanı Entegrasyon Müfredatı
- **Tamamlanmış 13-Lab Öğrenme Yolu**: PostgreSQL veritabanı entegrasyonlu üretime hazır MCP sunucuları için kapsamlı uygulamalı müfredat eklendi
  - **Gerçek Dünya Uygulaması**: Zava Retail analitik kullanım senaryosu, kurumsal düzey desenler sergileniyor
  - **Yapılandırılmış Öğrenme İlerlemesi**:
    - **Laboratuvarlar 00-03: Temeller** - Giriş, Temel Mimari, Güvenlik & Çoklu Kiracı, Ortam Kurulumu
    - **Laboratuvarlar 04-06: MCP Sunucu İnşası** - Veritabanı Tasarımı & Şema, MCP Sunucu Uygulaması, Araç Geliştirme  
    - **Laboratuvarlar 07-09: İleri Özellikler** - Anlamsal Arama Entegrasyonu, Test & Hata Ayıklama, VS Code Entegrasyonu
    - **Laboratuvarlar 10-12: Üretim & En İyi Uygulamalar** - Dağıtım Stratejileri, İzleme & Gözlemlenebilirlik, En İyi Uygulamalar & Optimizasyon
  - **Kurumsal Teknolojiler**: FastMCP framework, pgvector ile PostgreSQL, Azure OpenAI gömüleri, Azure Container Apps, Application Insights
  - **İleri Özellikler**: Satır Düzeyi Güvenlik (RLS), anlamsal arama, çoklu kiracı veri erişimi, vektör gömüleri, gerçek zamanlı izleme

#### Terminoloji Standardizasyonu - Modülden Laboratuvara Dönüşüm
- **Kapsamlı Dokümantasyon Güncellemesi**: 11-MCPServerHandsOnLabs’taki tüm README dosyaları “Laboratuvar” terimi kullanacak şekilde sistematik olarak güncellendi
  - **Bölüm Başlıkları**: Tüm 13 laboratuvarda “Bu Modül Neleri Kapsar” yerine “Bu Laboratuvar Neleri Kapsar” güncellemesi yapıldı
  - **İçerik Açıklaması**: Dokümantasyon genelinde “Bu modül sağlar...” ifadesi “Bu laboratuvar sağlar...” olarak değiştirildi
  - **Öğrenme Hedefleri**: “Bu modülün sonunda...” ifadesi “Bu laboratuvarın sonunda...” olarak güncellendi
  - **Gezinme Bağlantıları**: Tüm “Modül XX:” referansları çapraz referanslarda ve navigasyonda “Laboratuvar XX:” olarak dönüştürüldü
  - **Tamamlama Takibi**: “Bu modülün tamamlanmasından sonra...” ifadesi “Bu laboratuvarın tamamlanmasından sonra...” olarak güncellendi
  - **Teknik Referanslar Korundu**: Yapılandırma dosyalarındaki Python modül referansları olduğu gibi bırakıldı (örneğin, `"module": "mcp_server.main"`)

#### Çalışma Rehberi İyileştirmesi (study_guide.md)
- **Görsel Müfredat Haritası**: Yeni “11. Veritabanı Entegrasyon Laboratuvarları” bölümü ve kapsamlı laboratuvar yapısı görselleştirmesi eklendi
- **Depo Yapısı**: On olan ana bölüm sayısı on bir’e çıkarılarak 11-MCPServerHandsOnLabs detaylı şekilde tanıtıldı
- **Öğrenme Yolu Rehberi**: 00-11 bölümlerini kapsayacak şekilde navigasyon talimatları geliştirildi
- **Teknoloji Kapsamı**: FastMCP, PostgreSQL, Azure servis entegrasyon detayları eklendi
- **Öğrenme Çıktıları**: Üretime hazır sunucu geliştirme, veritabanı entegrasyon desenleri ve kurumsal güvenlik vurgulandı

#### Ana README Yapılandırma İyileştirmesi
- **Laboratuvar Tabanlı Terminoloji**: 11-MCPServerHandsOnLabs ana README.md dosyasında “Laboratuvar” yapısı tutarlı şekilde kullanıldı
- **Öğrenme Yolu Organizasyonu**: Temel kavramlardan ileri uygulamalara ve üretim dağıtımına açık gelişim sağlandı
- **Gerçek Dünya Odaklı**: Kurumsal düzey desenler ve teknolojilerle pratik, uygulamalı öğrenim vurgulandı

### Dokümantasyon Kalite & Tutarlılık İyileştirmeleri
- **Uygulamaya Dayalı Öğrenme Vurgusu**: Dokümantasyon genelinde uygulamalı, laboratuvar temelli yaklaşım pekiştirildi
- **Kurumsal Desenlere Odaklanma**: Üretime hazır uygulamalar ve kurumsal güvenlik hususları öne çıkarıldı
- **Teknoloji Entegrasyonu**: Modern Azure servisleri ve AI entegrasyon desenleri kapsamlı şekilde işlendi
- **Öğrenme İlerlemesi**: Temel kavramlardan üretim dağıtımına açık, yapılandırılmış yol haritası sunuldu

## 26 Eylül 2025

### Vaka Çalışmaları İyileştirmesi - GitHub MCP Kaydı Entegrasyonu

#### Vaka Çalışmaları (09-CaseStudy/) - Ekosistem Gelişimi Odaklı
- **README.md**: Kapsamlı GitHub MCP Kaydı vaka çalışması ile büyük genişleme
  - **GitHub MCP Kaydı Vaka Çalışması**: Eylül 2025'te GitHub MCP Kaydı lansmanını inceleyen yeni kapsamlı vaka çalışması
    - **Sorun Analizi**: Parçalanmış MCP sunucu keşfi ve dağıtım zorluklarının detaylı incelemesi
    - **Çözüm Mimarisi**: GitHub’un merkezi kayıt çözümü ve tek tıklamayla VS Code kurulumu
    - **İş Etkisi**: Geliştirici onboarding ve verimlilikte ölçülebilir iyileşmeler
    - **Stratejik Değer**: Modüler ajan dağıtımı ve araçlar arası birlikte çalışabilirlik odaklı
    - **Ekosistem Gelişimi**: Agentik entegrasyon için temel platform olarak konumlandırma
  - **Gelişmiş Vaka Çalışması Yapısı**: Yedi vaka çalışmasının tümü tutarlı biçimlendirme ve kapsamlı tanımlarla güncellendi
    - Azure AI Seyahat Acenteleri: Çoklu ajan orkestrasyonuna vurgu
    - Azure DevOps Entegrasyonu: İş akışı otomasyonuna odaklanma
    - Gerçek Zamanlı Dokümantasyon Getirme: Python konsol istemcisi uygulaması
    - Etkileşimli Çalışma Planı Oluşturucu: Chainlit konuşma tabanlı web uygulaması

    - Editör İçi Dokümantasyon: VS Code ve GitHub Copilot entegrasyonu
    - Azure API Yönetimi: Kurumsal API entegrasyon desenleri
    - GitHub MCP Kaydı: Ekosistem geliştirme ve topluluk platformu
  - **Kapsamlı Sonuç**: Birden çok MCP uygulama boyutunu kapsayan yedi vaka çalışmasını vurgulayan yeniden yazılmış sonuç bölümü
    - Kurumsal Entegrasyon, Çoklu Ajan Orkestrasyonu, Geliştirici Verimliliği
    - Ekosistem Geliştirme, Eğitimsel Uygulamalar sınıflandırması
    - Mimari desenler, uygulama stratejileri ve en iyi uygulamalar hakkında geliştirilmiş içgörüler
    - MCP'nin olgun, üretime hazır protokol olarak vurgulanması

#### Çalışma Kılavuzu Güncellemeleri (study_guide.md)
- **Görsel Müfredat Haritası**: Vaka Çalışmaları bölümünde GitHub MCP Kaydını içerecek şekilde güncellenmiş zihin haritası
- **Vaka Çalışmaları Tanımı**: Genel tanımlardan yedi kapsamlı vaka çalışmasının detaylı dökümüne yükseltildi
- **Depo Yapısı**: Bölüm 10, spesifik uygulama detaylarıyla kapsamlı vaka çalışması kapsamını yansıtacak şekilde güncellendi
- **Değişiklik Günlüğü Entegrasyonu**: GitHub MCP Kaydı eklenmesi ve vaka çalışması geliştirmelerini belgeleyen 26 Eylül 2025 girdisi eklendi
- **Tarih Güncellemeleri**: En son revizyonu (26 Eylül 2025) yansıtacak şekilde alt bilgi zaman damgası güncellendi

### Dokümantasyon Kalitesi İyileştirmeleri
- **Tutarlılık Artırma**: Tüm yedi örnek için vaka çalışması formatı ve yapısı standartlaştırıldı
- **Kapsamlı Kapsama**: Vaka çalışmaları artık kurumsal, geliştirici verimliliği ve ekosistem geliştirme senaryolarını kapsıyor
- **Stratejik Konumlandırma**: MCP'nin ajans sistem dağıtımı için temel platform olarak vurgusu geliştirildi
- **Kaynak Entegrasyonu**: Ek kaynaklar güncellenerek GitHub MCP Kaydı bağlantısı dahil edildi

## 15 Eylül 2025

### İleri Konular Genişletmesi - Özel Taşıyıcılar & Bağlam Mühendisliği

#### MCP Özel Taşıyıcılar (05-AdvancedTopics/mcp-transport/) - Yeni İleri Uygulama Kılavuzu
- **README.md**: MCP özel taşıyıcı mekanizmaları için kapsamlı uygulama rehberi
  - **Azure Event Grid Taşıyıcısı**: Kapsamlı sunucusuz olay tabanlı taşıyıcı uygulaması
    - Azure Functions entegrasyonlu C#, TypeScript ve Python örnekleri
    - Ölçeklenebilir MCP çözümleri için olay tabanlı mimari desenleri
    - Webhook alıcıları ve push tabanlı mesaj yönetimi
  - **Azure Event Hubs Taşıyıcısı**: Yüksek veri akışlı streaming taşıyıcı uygulaması
    - Düşük gecikmeli senaryolar için gerçek zamanlı streaming yetenekleri
    - Bölümlendirme stratejileri ve kontrol noktası yönetimi
    - Mesaj toplu işleme ve performans optimizasyonu
  - **Kurumsal Entegrasyon Desenleri**: Üretime hazır mimari örnekler
    - Birden fazla Azure Function üzerinde dağıtılmış MCP işleme
    - Çoklu taşıyıcı tiplerini birleştiren hibrit taşıyıcı mimarileri
    - Mesaj dayanıklılığı, güvenilirliği ve hata yönetimi stratejileri
  - **Güvenlik & İzleme**: Azure Key Vault entegrasyonu ve gözlemlenebilirlik desenleri
    - Yönetilen kimlik doğrulama ve minimum yetki erişimi
    - Application Insights telemetri ve performans izleme
    - Devre kesiciler ve hata tolerans desenleri
  - **Test Çerçeveleri**: Özel taşıyıcılar için kapsamlı test stratejileri
    - Test çiftleri ve mocking çerçeveleriyle birim testi
    - Azure Test Containers ile entegrasyon testi
    - Performans ve yük testi değerlendirmeleri

#### Bağlam Mühendisliği (05-AdvancedTopics/mcp-contextengineering/) - Gelişmekte Olan AI Disiplini
- **README.md**: Gelişmekte olan alan olarak bağlam mühendisliğinin kapsamlı keşfi
  - **Temel İlkeler**: Tam bağlam paylaşımı, eylem karar farkındalığı ve bağlam penceresi yönetimi
  - **MCP Protokol Uyumu**: MCP tasarımının bağlam mühendisliği zorluklarını nasıl ele aldığı
    - Bağlam penceresi sınırlamaları ve ilerleyici yükleme stratejileri
    - Alaka belirleme ve dinamik bağlam geri getirme
    - Çok modlu bağlam yönetimi ve güvenlik değerlendirmeleri
  - **Uygulama Yaklaşımları**: Tek iş parçacıklı vs. çoklu ajan mimarileri
    - Bağlam bölümlendirme ve önceliklendirme teknikleri
    - İlerleyici bağlam yükleme ve sıkıştırma stratejileri
    - Katmanlı bağlam yaklaşımları ve geri getirme optimizasyonu
  - **Ölçüm Çerçevesi**: Bağlam etkinliğini değerlendirmek için gelişmekte olan metrikler
    - Girdi verimliliği, performans, kalite ve kullanıcı deneyimi değerlendirmeleri
    - Bağlam optimizasyonuna deneysel yaklaşımlar
    - Hata analizi ve iyileştirme metodolojileri

#### Müfredat Navigasyon Güncellemeleri (README.md)
- **Gelişmiş Modül Yapısı**: Yeni ileri konuları içerecek şekilde müfredat tablosu güncellendi
  - Bağlam Mühendisliği (5.14) ve Özel Taşıyıcı (5.15) girdileri eklendi
  - Tüm modüllerde tutarlı biçimlendirme ve gezinme bağlantıları
  - Mevcut içerik kapsamını yansıtacak şekilde açıklamalar güncellendi

### Dizin Yapısı İyileştirmeleri
- **Adlandırma Standardizasyonu**: "mcp transport" klasörü "mcp-transport" olarak diğer ileri konu klasörleriyle tutarlılık için yeniden adlandırıldı
- **İçerik Organizasyonu**: Tüm 05-AdvancedTopics klasörleri artık tutarlı isimlendirme desenini takip ediyor (mcp-[konu])

### Dokümantasyon Kalitesi Geliştirmeleri
- **MCP Spesifikasyon Uyumu**: Tüm yeni içerikler 2025-06-18 MCP Spesifikasyonunu referans alıyor
- **Çok Dilli Örnekler**: C#, TypeScript ve Python dillerinde kapsamlı kod örnekleri
- **Kurumsal Odak**: Üretime hazır desenler ve Azure bulut entegrasyonu genelinde
- **Görsel Dokümantasyon**: Mimari ve akış görselleştirmeleri için Mermaid diyagramları

## 18 Ağustos 2025

### Dokümantasyon Kapsamlı Güncellemesi - MCP 2025-06-18 Standartları

#### MCP Güvenlik En İyi Uygulamaları (02-Security/) - Tam Modernizasyon
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: MCP Spesifikasyonu 2025-06-18 ile uyumlu tam yeniden yazım
  - **Zorunlu Gereksinimler**: Resmi spesifikasyondaki açık MUST/MUST NOT gereksinimleri açık görsel göstergelerle eklendi
  - **12 Temel Güvenlik Uygulaması**: 15 maddelik listeden kapsamlı güvenlik alanlarına yeniden yapılandırıldı
    - Dış kimlik sağlayıcı entegrasyonu ile Token Güvenliği & Doğrulama
    - Kriptografik gereksinimlerle Oturum Yönetimi & Taşıma Güvenliği
    - Microsoft Prompt Shields entegrasyonlu AI-Özel Tehdit Koruması
    - En az ayrıcalık ilkesi ile Erişim Kontrolü & İzinler
    - Azure Content Safety entegrasyonlu İçerik Güvenliği & İzleme
    - Kapsamlı bileşen doğrulaması ile Tedarik Zinciri Güvenliği
    - PKCE uygulaması ile OAuth Güvenliği & Confused Deputy Önleme
    - Otomatik yeteneklerle Olay Müdahalesi & Kurtarma
    - Düzenleyici uyum ile Uyumluluk & Yönetişim
    - Sıfır güven mimarisi ile Gelişmiş Güvenlik Kontrolleri
    - Kapsamlı çözümlerle Microsoft Güvenlik Ekosistemi Entegrasyonu
    - Uyarlanabilir uygulamalarla Sürekli Güvenlik Evrimi
  - **Microsoft Güvenlik Çözümleri**: Prompt Shields, Azure Content Safety, Entra ID ve GitHub Gelişmiş Güvenlik için geliştirilmiş entegrasyon rehberliği
  - **Uygulama Kaynakları**: Resmi MCP Dokümantasyonu, Microsoft Güvenlik Çözümleri, Güvenlik Standartları ve Uygulama Kılavuzları şeklinde kapsamlı kaynak bağlantıları kategorize edildi

#### Gelişmiş Güvenlik Kontrolleri (02-Security/) - Kurumsal Uygulama
- **MCP-SECURITY-CONTROLS-2025.md**: Kurumsal sınıf güvenlik çerçevesi ile tam yenilenme
  - **9 Kapsamlı Güvenlik Alanı**: Temel kontrollerden ayrıntılı kurumsal çerçeveye genişletildi
    - Microsoft Entra ID entegrasyonlu Gelişmiş Kimlik Doğrulama & Yetkilendirme
    - Kapsamlı doğrulama ile Token Güvenliği & Anti-Passthrough Kontrolleri
    - Kaçırma önleme ile Oturum Güvenlik Kontrolleri
    - Prompt enjeksiyonu ve araç zehirlenmesi önlemeli AI-Özel Güvenlik Kontrolleri
    - OAuth proxy güvenliği ile Confused Deputy Saldırısı Önleme
    - Sandboxing ve izolasyon ile Araç Çalıştırma Güvenliği
    - Bağımlılık doğrulaması ile Tedarik Zinciri Güvenlik Kontrolleri
    - SIEM entegrasyonlu İzleme & Tespit Kontrolleri
    - Otomatik yeteneklerle Olay Müdahalesi & Kurtarma
  - **Uygulama Örnekleri**: Ayrıntılı YAML yapılandırma blokları ve kod örnekleri eklendi
  - **Microsoft Çözümleri Entegrasyonu**: Azure güvenlik servisleri, GitHub Gelişmiş Güvenlik ve kurumsal kimlik yönetimini kapsamlı biçimde kapsar

#### Gelişmiş Konular Güvenliği (05-AdvancedTopics/mcp-security/) - Üretime Hazır Uygulama
- **README.md**: Kurumsal güvenlik uygulaması için tam yeniden yazım
  - **Mevcut Spesifikasyon Uyumu**: MCP Spesifikasyonu 2025-06-18 ve zorunlu güvenlik gereksinimleriyle güncellendi
  - **Geliştirilmiş Kimlik Doğrulama**: Microsoft Entra ID entegrasyonu, kapsamlı .NET ve Java Spring Security örnekleriyle
  - **AI Güvenliği Entegrasyonu**: Microsoft Prompt Shields ve Azure Content Safety ayrıntılı Python örnekleriyle uygulandı
  - **Gelişmiş Tehdit Azaltma**: Aşağıdakiler için kapsamlı uygulama örnekleri
    - PKCE ve kullanıcı onayı doğrulamasıyla Confused Deputy Saldırı Önleme
    - Hedef doğrulama ve güvenli token yönetimi ile Token Passthrough Önleme
    - Kriptografik bağlama ve davranış analizi ile Oturum Kaçırma Önleme
  - **Kurumsal Güvenlik Entegrasyonu**: Azure Application Insights izleme, tehdit tespiti hatları ve tedarik zinciri güvenliği
  - **Uygulama Kontrol Listesi**: Microsoft güvenlik ekosistemi avantajlarıyla zorunlu ve önerilen güvenlik kontrollerinin net ayrımı

### Dokümantasyon Kalitesi & Standart Uyumu
- **Spesifikasyon Referansları**: Tüm referanslar güncellenerek mevcut MCP Spesifikasyonu 2025-06-18'e uyumludur
- **Microsoft Güvenlik Ekosistemi**: Tüm güvenlik dokümantasyonları boyunca geliştirilmiş entegrasyon rehberliği
- **Pratik Uygulama**: Kurumsal desenlerle .NET, Java ve Python'da ayrıntılı kod örnekleri eklendi
- **Kaynak Organizasyonu**: Resmi dokümantasyon, güvenlik standartları ve uygulama kılavuzlarının kapsamlı kategorilendirmesi
- **Görsel Gösterge**: Zorunlu gereksinimler ve önerilen uygulamalar net şekilde işaretlendi


#### Temel Kavramlar (01-CoreConcepts/) - Tam Modernizasyon
- **Protokol Versiyon Güncellemesi**: Güncel MCP Spesifikasyonu 2025-06-18 referans alınarak tarih bazlı sürümleme (YYYY-AA-GG formatı)
- **Mimari İyileştirme**: MCP mimari desenlerini yansıtacak şekilde Hosts, Clients ve Servers açıklamaları geliştirildi
  - Hosts artık birden fazla MCP istemci bağlantısını koordine eden AI uygulamaları olarak net tanımlandı
  - Clients, bir-bir sunucu ilişkisini sürdüren protokol bağlantı noktaları olarak tanımlandı
  - Servers, yerel ve uzak dağıtım senaryoları ile geliştirildi
- **Primitive Yeniden Yapılandırma**: Sunucu ve istemci primitive'lerinin tam yenilenmesi
  - Sunucu Primitive'leri: Kaynaklar (veri kaynakları), İstekler (şablonlar), Araçlar (çalıştırılabilir fonksiyonlar) detaylı açıklamalar ve örneklerle
  - İstemci Primitive'leri: Örnekleme (LLM tamamlama), Elicitation (kullanıcı girdisi), Logging (hata ayıklama/izleme)
  - Mevcut keşif (`*/list`), alma (`*/get`) ve çağrı (`*/call`) yöntem kalıpları ile güncellendi
- **Protokol Mimarisi**: İki katmanlı mimari modeli tanıtıldı
  - Veri Katmanı: Yaşam döngüsü yönetimi ve primitive'lerle JSON-RPC 2.0 temeli
  - Taşıma Katmanı: STDIO (yerel) ve SSE destekli Streamable HTTP (uzak) taşıma mekanizmaları
- **Güvenlik Çerçevesi**: Açık kullanıcı onayı, veri gizliliği koruması, araç çalıştırma güvenliği ve taşıma katmanı güvenliği dahil kapsamlı güvenlik ilkeleri
- **İletişim Desenleri**: Başlatma, keşif, yürütme ve bildirim akışlarını gösteren güncellenmiş protokol mesajları
- **Kod Örnekleri**: Güncel MCP SDK desenlerini yansıtacak şekilde çok dilli (.NET, Java, Python, JavaScript) örnekler yenilendi

#### Güvenlik (02-Security/) - Kapsamlı Güvenlik Yenilemesi  
- **Standart Uyumu**: MCP Spesifikasyonu 2025-06-18 güvenlik gereksinimleriyle tam uyum
- **Kimlik Doğrulama Evrimi**: Özel OAuth sunucularından dış kimlik sağlayıcı devrine (Microsoft Entra ID) geçiş belgelendi
- **AI-Özel Tehdit Analizi**: Modern AI saldırı vektörlerine genişletilmiş kapsam
  - Gerçek dünyadan örneklerle detaylı prompt enjeksiyonu saldırı senaryoları
  - Araç zehirlenmesi mekanizmaları ve "halı çekme" saldırı kalıpları
  - Bağlam penceresi zehirlenmesi ve model karışıklığı saldırıları
- **Microsoft AI Güvenlik Çözümleri**: Microsoft güvenlik ekosisteminin kapsamlı tanıtımı
  - Gelişmiş tespit, vurgulama ve sınırlayıcı tekniklerle AI Prompt Shields
  - Azure Content Safety entegrasyon desenleri
  - Tedarik zinciri koruması için GitHub Gelişmiş Güvenlik
- **Gelişmiş Tehdit Azaltma**: Aşağıdakiler için detaylı güvenlik kontrolleri
  - MCP-özgü oturum kaçırma saldırı senaryoları ve kriptografik oturum ID gereksinimleri ile oturum kaçırma
  - Açık onay gereksinimleri ile MCP proxy senaryolarında Confused Deputy sorunları
  - Zorunlu doğrulama kontrolleri ile token passthrough açıkları
- **Tedarik Zinciri Güvenliği**: Temel modeller, gömme servisleri, bağlam sağlayıcılar ve üçüncü taraf API'leri içeren genişletilmiş AI tedarik zinciri kapsamı
- **Temel Güvenlik**: Sıfır güven mimarisi ve Microsoft güvenlik ekosistemi dahil kurumsal güvenlik desenleriyle geliştirilmiş entegrasyon
- **Kaynak Organizasyonu**: Türlerine göre kategorize edilmiş kapsamlı kaynak bağlantıları (Resmi Dokümanlar, Standartlar, Araştırma, Microsoft Çözümleri, Uygulama Kılavuzları)

### Dokümantasyon Kalitesi İyileştirmeleri
- **Yapılandırılmış Öğrenme Hedefleri**: Özel, uygulanabilir sonuçlarla geliştirilmiş öğrenme hedefleri 
- **Çapraz Referanslar**: İlgili güvenlik ve temel kavram konuları arasında bağlantılar eklendi
- **Güncel Bilgi**: Tüm tarih referansları ve spesifikasyon bağlantıları mevcut standartlara göre güncellendi
- **Uygulama Rehberliği**: Her iki bölümde de özel, uygulanabilir uygulama yönergeleri eklendi

## 16 Temmuz 2025

### README ve Navigasyon İyileştirmeleri
- README.md'deki müfredat navigasyonu tamamen yeniden tasarlandı
- `<details>` etiketleri daha erişilebilir tablo tabanlı format ile değiştirildi
- Yeni "alternative_layouts" klasöründe alternatif düzen seçenekleri oluşturuldu
- Kart tabanlı, sekmeli ve akordeon-stil gezinme örnekleri eklendi
- Depo yapısı bölümü en son dosyalarla güncellendi
- "Bu Müfredatı Nasıl Kullanılır" bölümü net önerilerle geliştirildi
- MCP spesifikasyon bağlantıları doğru URL'lere işaret edecek şekilde güncellendi
- Müfredat yapısına Bağlam Mühendisliği bölümü (5.14) eklendi

### Çalışma Kılavuzu Güncellemeleri
- Mevcut depo yapısına uyacak şekilde çalışma kılavuzu tamamen gözden geçirildi
- MCP İstemcileri ve Araçları ile Popüler MCP Sunucuları için yeni bölümler eklendi
- Görsel Müfredat Haritası tüm konuları doğru yansıtacak şekilde güncellendi
- İleri Konular tanımları tüm uzmanlaşmış alanları kapsayacak şekilde geliştirildi
- Vaka Çalışmaları bölümü gerçek örnekleri yansıtacak şekilde güncellendi
- Bu kapsamlı değişiklik günlüğü eklendi

### Topluluk Katkıları (06-CommunityContributions/)
- Görüntü oluşturma için MCP sunucuları hakkında detaylı bilgi eklendi
- VSCode'da Claude kullanımı üzerine kapsamlı bölüm eklendi
- Cline terminal istemcisi kurulumu ve kullanım talimatları eklendi
- MCP istemci bölümü tüm popüler istemci seçenekleriyle güncellendi
- Katkı örnekleri daha doğru kod örnekleriyle geliştirildi

### İleri Konular (05-AdvancedTopics/)
- Tüm uzmanlaşmış konu klasörleri tutarlı adlandırma ile düzenlendi
- Bağlam mühendisliği materyalleri ve örnekleri eklendi
- Foundry ajan entegrasyon dokümantasyonu eklendi
- Entra ID güvenlik entegrasyon dokümantasyonu geliştirildi

## 11 Haziran 2025

### İlk Oluşturma
- MCP for Beginners müfredatının ilk versiyonu yayınlandı

- Tüm 10 ana bölüm için temel yapı oluşturuldu
- Navigasyon için Görsel Müfredat Haritası uygulandı
- Birden çok programlama dilinde başlangıç örnek projeler eklendi

### Başlarken (03-GettingStarted/)
- İlk sunucu uygulama örnekleri oluşturuldu
- İstemci geliştirme rehberi eklendi
- LLM istemci entegrasyon talimatları dahil edildi
- VS Code entegrasyon dokümantasyonu eklendi
- Sunucu Gönderimli Olaylar (SSE) sunucu örnekleri uygulandı

### Temel Kavramlar (01-CoreConcepts/)
- İstemci-sunucu mimarisinin detaylı açıklaması eklendi
- Ana protokol bileşenleri üzerine dokümantasyon oluşturuldu
- MCP’de mesajlaşma desenleri belgelenmiştir

## 23 Mayıs 2025

### Depo Yapısı
- Depo temel klasör yapısıyla başlatıldı
- Her ana bölüm için README dosyaları oluşturuldu
- Çeviri altyapısı kuruldu
- Görsel varlıklar ve diyagramlar eklendi

### Dokümantasyon
- Müfredat genel bakışlı başlangıç README.md oluşturuldu
- CODE_OF_CONDUCT.md ve SECURITY.md eklendi
- Yardım alma rehberli SUPPORT.md ayarlandı
- Ön çalışma rehberi yapısı oluşturuldu

## 15 Nisan 2025

### Planlama ve Çerçeve
- MCP Başlangıç Müfredatı için ilk planlama yapıldı
- Öğrenme hedefleri ve hedef kitle tanımlandı
- Müfredatın 10 bölümlük yapısı taslağı hazırlandı
- Örnekler ve vaka çalışmaları için kavramsal çerçeve geliştirildi
- Temel kavramlar için ilk prototip örnekler oluşturuldu

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->