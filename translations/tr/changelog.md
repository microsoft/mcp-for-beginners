# Değişiklik Günlüğü: MCP Yeni Başlayanlar Müfredatı

Bu belge, Model Context Protocol (MCP) Yeni Başlayanlar müfredatında yapılan tüm önemli değişikliklerin kaydını tutar. Değişiklikler ters kronolojik sırayla (en yeni değişiklikler önce) belgelenmiştir.

## 29 Temmuz 2026

### Yeni Modül 08 Yardımcı Ders: Güvenilirlik Yan Arabirimleri ve Güvenli Tekrar Denemeler

Gerçek dünya etkileri yaratan MCP araçları için satıcıdan bağımsız bir yardımcı ders eklendi,
son `2026-07-28` spesifikasyonu ile uyumlu.

- **Yeni**: [güvenilirlik yan arabirim yardımcı dersi][reliability-sidecar]
  bir destek bileti hikayesi, iki Mermaid diyagramı ve bir tekrar deneme kararı
  akışı kullanarak stabil çalışma anahtarlarını, atomik tekrar kabulü,
  mutabakatı, kanıtları ve Görevler uzantısı sınırını açıklar.
- **Yeni**: Standart kütüphane Python ve SQLite arıza enjekte etme egzersizi,
  ayrı işlem ve bilet depoları kullanarak harici bir etkinin işlemi
  işlendikten sonra bir yanıt kaybını gösterir. Altı deterministik test, naif
  çoğaltmayı, korumalı yeniden başlatma kurtarmayı, yük çakışmalarını,
  önbelleğe alınan sonuçları, aktif iddiaları ve eş zamanlı tekrar kabulü kapsar.
- **Güncellendi**: Modül 08 artık yardımcı dersi bağlantılar, son
  `2026-07-28` durumsuz istek modelini tanımlar, OpenTelemetry
  gözlemlenebilirliğini kullanımdan kaldırılan MCP günlükleme özelliğinden ayırır
  ve genel tekrar deneme örneğini yalnızca salt okunur işlemlerle sınırlar.
- **İsteğe bağlı**: Ders, taşınabilir kavramlarını etiketlenmiş bir topluluk
  uygulamasına eşler ancak barındırılan hizmeti veya ağ çağrısını egzersizin
  bir parçası yapmaz.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2 Temmuz 2026

### Yeni Ders: 2026-07-28 MCP Spesifikasyon Sürüm Adayı

Yaklaşan `2026-07-28` MCP spesifikasyon sürüm adayının kapsamı eklendi (21 Mayıs 2026'da duyurulmuş; nihai sürüm 28 Temmuz 2026’da planlanmıştır), [resmi duyuru blog gönderisinden](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) özetlenmiştir. Müfredatın temel hali yeni sürüm gelene kadar **MCP Spesifikasyon 2025-11-25** olarak kalır, bu nedenle bu içerik mevcut derslerin yeniden yazımı değil, ileriye dönük rehberlik olarak sunulur.

- **Yeni**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — durumsuz protokol çekirdeğini tamamen kapsayan bir ders (`initialize` el sıkışması ve `Mcp-Session-Id` kaldırılması), yeni `Mcp-Method`/`Mcp-Name` yönlendirme başlıkları, `ttlMs`/`cacheScope` önbellekleme meta verisi, `_meta` içindeki W3C İzleme Bağlamı, resmi Uzantılar çerçevesi (MCP Uygulamaları ve yeni Görevler uzantısı), altı yetkilendirme sertleştirme SEP’si, Roots/Sampling/Logging'in kullanımdan kaldırılması ve araç şemaları için tam JSON Schema 2020-12 geçişi.
- **Güncellendi** ileriye dönük atıflarla yeni derse bağlantılar eklendi:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): protokol sürüm notu, Sampling/Roots/Logging/Görevler bölümleri ve "Sonraki Adımlar"
  - [02-Security/README.md](./02-Security/README.md): yetkilendirme sertleştirme notu
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): durumsuz taşıma notu
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Sampling kullanımdan kaldırma notu
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Günlükleme kullanımdan kaldırma ve Görevler uzantısı notu
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): durumsuz/oturum-yönlendirme notu
  - [README.md](./README.md): Spesifikasyon bölümünde "İleriye Bakış" notu ve müfredat modül tablosunda yeni `1.1` kaydı
  - [study_guide.md](./study_guide.md): Temel Kavramlar genel bakışında ileriye dönük madde ve tarihli ek not
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): durumsuz istek modelinin öncesinde `mcp-session-id` taşıma haritası notu
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): Modül genel bakışta Root Contexts/Sampling kullanımdan kaldırmaları ve Görevler uzantısı notu
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): yetkilendirme sertleştirme notu

## 24 Haziran 2026

### Yeni Ders: MCP'nin Copilot uygulamasında Kullanımı

- [Araçlar bölümü](./12-tooling/README.md) Araçlar bölümü eklendi.
- [Copilot uygulamasında MCP](./12-tooling/01-copilot-app/README.md)

## 16 Haziran 2026

### MCP Spesifikasyon Uyumu ve Örnek Doğrulama

Müfredat, mevcut **MCP Spesifikasyon 2025-11-25** ve en son resmi SDK’lar ile doğrulandı, ardından kalan eski spesifikasyon referansları düzeltildi ve temel örneklerin hâlâ derlenip çalıştırılabildiği teyit edildi.

#### Spesifikasyon Sürümü Düzeltmeleri (2025-06-18 / 2025-03-26 → 2025-11-25)

İngilizce içerik, hâlâ eski bir sürümün *geçerli/en son* standart olduğunu iddia eden yerlerde güncellendi ve bağlantılar kanonik `modelcontextprotocol.io` spesifikasyon yollarına yönlendirildi:
- **05-AdvancedTopics/mcp-security/README.md**: "Geçerli Standart" bandı, giriş, temel güvenlik ilkeleri başlığı, zorunlu gereksinimler başlığı, Microsoft Entra ID bölümü, Referanslar & Kaynaklar bağlantıları ve kapanış güvenlik uyarısı (8 referans) 2025-11-25 olarak güncellendi
- **05-AdvancedTopics/mcp-transport/README.md**: Ek Kaynaklar spesifikasyon bağlantısı ve "Geçerli Standart" bandı 2025-11-25 olarak güncellendi
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Güncel olmayan `2025-03-26` güvenlik ve güvenilirlik bağlantısı, mevcut 2025-11-25 güvenlik en iyi uygulamaları sayfası ile değiştirildi
- **03-GettingStarted/14-sampling/README.md**: Resmi sampling doküman bağlantısı 2025-11-25 olarak güncellendi

- **03-GettingStarted/05-stdio-server/README.md**: Güncel zaman “mevcut MCP spesifikasyonu” referansı ve Ek Kaynaklar spesifikasyon bağlantısı 2025-11-25 olarak güncellendi (doğruluk için tarihi SSE-kaldırma notları aynı bırakıldı)

#### Güncel SDK’lara Karşı Örnek Doğrulama

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` `@modelcontextprotocol/sdk@1.29.0` sürümünü çözdü; `tsc --noEmit` tür hatası olmadan geçti — mevcut `McpServer`/`StdioServerTransport` API’leri geçerliliğini koruyor
- **Python (03-GettingStarted/01-first-server/solution/python)**: İzole `.venv` içinde `mcp[cli]` (1.27.2) ile doğrulandı; `py_compile` başarılı oldu ve `FastMCP.list_tools()` doğru şekilde `add` ve `subtract` araçlarını döndürdü
- Tüm örnek `@modelcontextprotocol/sdk` sürüm aralıklarının (`>=1.26.0` / `^1.26.0` / `^1.27.0`) mevcut `1.29.0` sürümüne uyumlu ve API uyumsuzluğu olmadan çözüldüğü teyit edildi

#### Bağımlılık Sürüm Uyumlama (sürüm boşluklarını kapatma)

Güncel MCP sürümünü takip etmek için eski SDK sürümleri yükseltildi, depo genelindeki uygulama ile uyumlu hale getirildi:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: `@modelcontextprotocol/sdk` sürümü `^1.8.0` → `>=1.26.0` olarak yükseltildi ve eski `"updated for MCP 2025-06-18"` paket açıklaması `"aligned with MCP Specification 2025-11-25"` olarak güncellendi
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** ve **lab4/code/github_mcp_server/pyproject.toml**: `mcp==1.23.0` kesin sürümü `mcp>=1.26.0` olarak yükseltildi; her iki `uv.lock` dosyası (`uv lock`) yeniden üretildi, böylece kilit dosyaları mevcut `mcp 1.27.2` sürümüne uyumlu ve manifestlerle senkron kalıyor

#### Müfredat Boşluk Analizi — En Son Spesifikasyon Özellik Kapsamı

Müfredatın MCP 2025-11-25’te tanıtılan/genişletilen tüm temel özellikleri kapsadığı doğrulandı, dolayısıyla içerik boşluğu yok:
- **Sampling**: Ders 03-GettingStarted/14-sampling ve 05-AdvancedTopics/mcp-sampling
- **Elicitation (URL modu dahil)**: 01-CoreConcepts ve 05-AdvancedTopics/mcp-protocol-features içinde dokümante edildi
- **Roots**: 00-Introduction, 01-CoreConcepts ve 05-AdvancedTopics/mcp-root-contexts içinde dokümante edildi
- **Görevler (deneysel, uzun süreli işlemler)**: 01-CoreConcepts ve 05-AdvancedTopics/mcp-protocol-features içinde dokümante edildi
- **Araç Notasyonları** (`readOnlyHint` / `destructiveHint`): 01-CoreConcepts ve 05-AdvancedTopics/mcp-protocol-features içinde dokümante edildi

### Güvenlik Sertleştirme & Bağımlılık Güvenlik Açığı Giderimleri

Her bağımlılık manifesti ve örnek kaynak kodu üzerinde tam bir güvenlik taraması yapıldı, ardından raporlanan tüm npm uyarıları ve bir kod düzeyi bulgusu giderildi. Giderimler sonrası, `npm audit` her denetlenen dizinde **0 güvenlik açığı** rapor ediyor.

#### npm Bağımlılık Güvenlik Açıkları (dolaylı) — Giderildi

Tüm 15 taahhüt edilmiş `package-lock.json` dosyası denetlendi. Güvenlik açıkları yalnızca MCP Inspector geliştirme aracı, OpenAI istemcisi ve MCP SDK tarafından getirilen dolaylı bağımlılıklarda sınırlıydı; hepsi örnekleri bozmayacak şekilde çözüldü:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** ve **lab3/code/weather_mcp/inspector**: `@modelcontextprotocol/inspector` (sürümler `0.16.6` / `0.14.1` → `0.22.0`) yükseltildi; bu, beraberindeki `ajv`, `brace-expansion`, `diff`, `path-to-regexp` ve `ws` uyarılarını temizledi. `concurrently` tarafından taşınan kritik `shell-quote@1.8.4` uyarısını kaldırmak için npm `overrides` girdisi eklendi; her iki kilit dosyası yeniden üretildi (artık 0 güvenlik açığı)
- **03-GettingStarted/samples/typescript**: `npm audit fix` dolaylı `qs` (orta şiddetli) bağımlılığını yamalı sürüme güncelledi
- **03-GettingStarted/samples/javascript**: `npm audit fix` dolaylı `hono` (orta şiddetli) bağımlılığını yamalı sürüme güncelledi
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` dolaylı `form-data` (yüksek) bağımlılığını yamalı sürüme güncelledi
- **03-GettingStarted/11-simple-auth/solution/typescript**: Projenin yeniden üretilebilir ve denetlenebilir olması için eksik `package-lock.json` üretildi (0 güvenlik açığı)

#### Kod Seviyesi Güvenlik Düzeltmesi (OWASP A03: Enjeksiyon)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: `open_in_vscode` aracından `shell=True` kaldırıldı. Önceki `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` kodu, klasör yolundaki kabuk meta karakterlerinin `cmd.exe` tarafından yorumlanmasına izin veriyordu (komut enjeksiyonu riski). Artık kabuğu atlayarak doğrudan çözümlenmiş `Code.exe`yi klasör argümanı ile başlatıyor — fonksiyonel olarak eşdeğer ve güvenli

#### Python Bağımlılık Denetimi

- Tüm Python gereksinim setleri `pip-audit` ile denetlendi. `05-AdvancedTopics` ve `03-GettingStarted/samples/python` **bilinen güvenlik açığı olmadığını** raporladı (`mcp` / `httpx` / `pydantic` / `python-dotenv` aralıkları mevcut yamalı sürümlere çözülür)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` dolaylı **`werkzeug` 3.1.1** bağımlılığını üç adet `safe_join` Windows aygıt adı DoS uyarısı ile işaret etti — `CVE-2025-66221`, `CVE-2026-21860` ve `CVE-2026-27199` (tümü 3.1.6’da giderildi). Yamalanmış sürümün çözülmesi için açık güvenlik pini `werkzeug>=3.1.6` eklendi; kısıtlamanın `chainlit` / `mcp` / `semantic-kernel` yığını ile sorunsuz çözüldüğü doğrulandı

### Ürün İsmi Yeniden Markalaşması

Tüm müfredat içeriği Microsoft’un ürün yeniden markalaşmasını yansıtacak şekilde güncellendi:


#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Güncellenmiş Discord topluluk bağlantısı

- **AGENTS.md**: Güncellenmiş Discord sunucu referansı
- **README.md**: Güncellenmiş teknoloji ekosistemi referansları
- **study_guide.md**: Güncellenmiş vaka çalışması referansları
- **05-AdvancedTopics/README.md**: Güncellenmiş Modül 5.13 başlığı ve açıklaması
- **05-AdvancedTopics/mcp-integration/README.md**: Güncellenmiş bölüm başlığı ve açıklaması
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Tam modül başlığı ve içerik güncellemesi
- **05-AdvancedTopics/mcp-security-entra/README.md**: Güncellenmiş çapraz referans bağlantısı
- **07-LessonsfromEarlyAdoption/README.md**: Güncellenmiş vaka çalışması referansları
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Güncellenmiş Bölüm 9 başlığı, rozetler ve yetenekler
- **08-BestPractices/README.md**: Güncellenmiş Discord topluluk bağlantısı
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Güncellenmiş Discord kanal referansı
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Güncellenmiş model dağıtımı referansı
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Güncellenmiş AI Hizmetleri tablosu
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Güncellenmiş kaynak referansları

#### AI Toolkit / AITK → Microsoft Foundry Toolkit VS Code Uzantısı
- **README.md**: Güncellenmiş ana müfredat referansları
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Güncellenmiş modül başlığı, genel bakış ve tüm modül başlıkları
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Güncellenmiş başlık, öğrenme hedefleri, kurulum talimatları ve kaynaklar
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Güncellenmiş başlık, öğrenme hedefleri, MCP ana bilgisayarlar tablosu ve çapraz referanslar
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Güncellenmiş başlık, rozetler, önkoşullar ve kaynaklar
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Güncellenmiş Agent Builder referansları ve geri bildirim bağlantısı
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Güncellenmiş önkoşullar ve uzantı referansları

---

## 11 Nisan 2026

### Yeni Ders, Dokümantasyon Düzeltmeleri ve Bağımlılık Güncellemeleri

#### Yeni Müfredat İçeriği Eklendi

**Modül 05 - İleri Konular**
- **Ders 5.17: MCP ile Rekabetçi Çoklu Ajan Muhakemesi** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Çoklu ajan sistemleri için rekabetçi tartışma modelini kapsayan kapsamlı yeni rehber
  - Mermaid mimari diyagramı: iki ajan → paylaşılan MCP sunucusu → tartışma transkripti → yargıç → karar
  - Python ve TypeScript ile uygulanmış paylaşılan MCP araç sunucusu (`web_search` + `run_python`)
  - Açık araç kullanımı gereksinimleri içeren karşıt sistem istemleri (LEHİM / KARŞI / Yargıç)
  - Python, TypeScript ve C# ile tur yönetimi ve argüman yönlendirme yapan tartışma düzenleyici
  - Düzenleyici için MCP `ClientSession` gerçek araç çağrılarına bağlantısı
  - Kullanım senaryoları tablosu (halüsinasyon tespiti, tehdit modelleme, API tasarımı incelemesi, gerçeklik doğrulama, teknoloji seçimi)
  - Güvenlik önlemleri: izole çalışma, araç çağrısı doğrulaması, hız sınırlandırma, denetim kayıtları
  - Üç pratik senaryolu yapılandırılmış alıştırma (kod incelemesi, mimari karar, içerik denetimi)

#### Dokümantasyon Düzeltmeleri

**Modül 03 - Başlarken**
- **05-stdio-server/README.md**: Eksik TypeScript stdio sunucu örneği düzeltildi — Python ve .NET örnekleriyle uyumlu olması için eksik transport yaratımı (`new StdioServerTransport()`) ve `server.connect(transport)` çağrısı eklendi
- **14-sampling/README.md**: Yazım hatası düzeltildi — `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Müfredat Güncellemeleri

**Ana README.md**
- Yeni ders 5.17 (MCP ile Rekabetçi Çoklu Ajan Muhakemesi) müfredat tablosuna ve yeni derse doğrudan link eklendi

**05-AdvancedTopics/README.md**
- Ders 5.17 satırı dersler tablosuna eklendi

**study_guide.md**
- İleri Konular zihin haritası ve metin açıklamasına Rekabetçi Çoklu Ajan Muhakemesi başlığı eklendi

#### Kod ve Güvenlik Düzeltmeleri

**Modül 05 - Rekabetçi Ajanlar (`mcp-adversarial-agents`)**
- **Güvenlik düzeltmesi — komut enjeksiyonu**: TypeScript `run_python` aracındaki kabuk interpolasyonu `execSync`, komut enjeksiyonu yüzeyini ortadan kaldırmak için `execFile` + `promisify` ile değiştirildi (LLM kontrollü kod artık kabuk kullanılmadan doğrudan argv olarak geçiriliyor)
- **MCP araç döngüsü bağlantısı**: Python tartışma düzenleyicisi, engelleyen senkron `Anthropic` yerine asenkron `AsyncAnthropic` istemcisini kullanacak şekilde, her ajan turuna canlı `ClientSession` iletilecek şekilde ve model son yanıt çıkana kadar `session.list_tools()` ile araç tanımlarını alarak `session.call_tool()` aracılığıyla `tool_use` bloklarını yöneten döngü ile güncellendi

#### Bağımlılık Güncellemeleri

- Birden fazla pakette (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows) `hono` sürümü 4.12.12'ye yükseltildi
- TypeScript paketlerinde `@hono/node-server` sürümü 1.19.11'den 1.19.13'e yükseltildi
- Python paketlerinde (10-StreamliningAIWorkflows lab 3 ve 4) `cryptography` sürümü 46.0.5'ten 46.0.7'ye yükseltildi
- 10-StreamliningAIWorkflows denetleyicisinde `lodash` sürümü 4.17.23'ten 4.18.1'e yükseltildi

#### Çeviriler

- 48+ dil için çeviriler en son kaynak değişiklikleriyle senkronize edildi (i18n güncellemesi)

---

## 5 Şubat 2026

### Depo Genelinde Doğrulama ve Navigasyon İyileştirmeleri

#### Yeni Müfredat İçeriği Eklendi

**Modül 03 - Başlarken**
- **12-mcp-hosts/README.md**: MCP ana bilgisayarlarının kurulumu için kapsamlı yeni rehber
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf yapılandırma örnekleri
  - Tüm ana bilgisayarlar için JSON yapılandırma şablonları
  - Transport türleri karşılaştırma tablosu (stdio, SSE/HTTP, WebSocket)
  - Yaygın bağlantı sorunlarının giderilmesi
  - Ana bilgisayar yapılandırması için güvenlik en iyi uygulamaları

- **13-mcp-inspector/README.md**: MCP Denetleyicisi için yeni hata ayıklama rehberi
  - Kurulum yöntemleri (npx, global npm, kaynaktan)
  - Stdio ve HTTP/SSE üzerinden sunucu bağlantısı
  - Araçlar, kaynaklar ve istem iş akışlarını test etme
  - VS Code entegrasyonu ile MCP Denetleyicisi
  - Yaygın hata ayıklama senaryoları ve çözümleri

**Modül 04 - Pratik Uygulama**
- **pagination/README.md**: Yeni sayfalama uygulama rehberi
  - Python, TypeScript, Java'da imleç tabanlı sayfalama desenleri
  - İstemci tarafı sayfalama yönetimi
  - İmleç tasarım stratejileri (opak vs. yapılandırılmış)
  - Performans optimizasyon önerileri

**Modül 05 - İleri Konular**
- **mcp-protocol-features/README.md**: Yeni protokol özellikleri derinlemesine inceleme
  - İlerleme bildirimleri uygulaması
  - İstek iptali desenleri
  - URI desenli kaynak şablonları
  - Sunucu yaşam döngüsü yönetimi
  - Günlük seviyesi kontrolü
  - JSON-RPC kodları ile hata yönetimi desenleri

#### Navigasyon Düzeltmeleri (24+ dosya güncellendi)

**Ana Modül README'leri**
 Artık hem ilk derse hem de sonraki modüle bağlantı içeriyor

**02-Security Alt dosyaları**
- Tüm 5 ek güvenlik dokümanı artık "Sonraki Ne?" navigasyonu içeriyor:

**09-CaseStudy Dosyaları**
- Tüm vaka çalışması dosyaları artık sıralı navigasyon içeriyor:

**10-StreamliningAI Laboratuvarları**
Modül 10 genel görünümüne ve Modül 11'e Sonraki Ne? bölümü eklendi

#### Kod ve İçerik Düzeltmeleri

**SDK ve Bağımlılık Güncellemeleri**
Boş openai sürümü `^4.95.0` olarak düzeltildi
SDK `^1.8.0`'den `>=1.26.0`'a güncellendi
MCP sürüm pinleri `>=1.26.0` olarak güncellendi

**Kod Düzeltmeleri**
Geçersiz model `gpt-4o-mini`, `gpt-4.1-mini` ile değiştirildi

**İçerik Düzeltmeleri**
Bozuk link `READMEmd` → `README.md` olarak düzeltildi, müfredat başlığı `Module 1-3` → `Module 0-3` olarak düzeltildi, büyük-küçük harf duyarlı yol düzeltilmesi yapıldı
Bozuk çoğaltılmış Case Study 5 içeriği kaldırıldı

**Yeni Başlayanlar İçin Rehberlik İyileştirmeleri**
Yeni başlayanlar için uygun giriş, öğrenme hedefleri ve önkoşullar eklendi

#### Müfredat Güncellemeleri

**Ana README.md**
- Müfredat tablosuna 3.12 (MCP Ana Bilgisayarlar), 3.13 (MCP Denetleyicisi), 4.1 (Sayfalama), 5.16 (Protokol Özellikleri) girişleri eklendi

**Modül README'leri**
Ders listesine 12 ve 13 eklendi
Sayfalama bağlantılı Pratik Kılavuzlar bölümü eklendi
Derslere 5.15 (Özel Transport) ve 5.16 (Protokol Özellikleri) eklendi

**study_guide.md**
- Yeni konularla güncellenmiş zihin haritası: MCP Ana Bilgisayar Kurulumu, MCP Denetleyicisi, Sayfalama Stratejileri, Protokol Özellikleri Derin İnceleme

## 28 Ocak 2026

### MCP Spesifikasyonu 2025-11-25 Uyum Gözden Geçirmesi

#### Temel Kavramlar Geliştirmesi (01-CoreConcepts/)
- **Yeni İstemci Primitifi - Roots**: Sunucuların dosya sistemi sınırlarını ve erişim izinlerini anlamasını sağlayan kapsamlı Roots istemci primitifi dokümantasyonu eklendi
- **Araç Anotasyonları**: Araç yürütme kararlarını iyileştirmek için araç davranış anotasyonları (`readOnlyHint`, `destructiveHint`) üzerine dokümantasyon eklendi
- **Sampling'de Araç Çağrısı**: Sampling dokümantasyonu, örnek alma isteklerinde model tabanlı araç çağırma için `tools` ve `toolChoice` parametrelerini içerecek şekilde güncellendi
- **URL Modu Tetiklemesi**: Sunucu kaynaklı dış web etkileşimleri için URL tabanlı tetikleme dokümantasyonu eklendi
- **Tasks (Deneysel)**: Dayanıklı yürütme sarmalayıcıları ve ertelenmiş sonuç alma için deneysel Tasks özelliğini belgeleyen yeni bölüm eklendi
- **Simgeler Desteği**: Araçlar, kaynaklar, kaynak şablonları ve istemlerin artık ek meta veri olarak simgeler içerebileceği belirtilmiştir

#### Dokümantasyon Güncellemeleri
- **README.md**: MCP Spesifikasyonu 2025-11-25 sürüm referansı ve tarih tabanlı sürüm açıklaması eklendi
- **study_guide.md**: Temel Kavramlar bölümüne Tasks ve Araç Anotasyonları eklendi; belge zaman damgası güncellendi

#### Spesifikasyon Uyum Doğrulaması
- **Protokol Sürümü**: Tüm dokümantasyonun güncel MCP Spesifikasyonu 2025-11-25 ile uyumlu olduğu doğrulandı
- **Mimari Uyum**: İki katmanlı mimari (Veri Katmanı + Taşıma Katmanı) belgelerinin doğruluğu onaylandı
- **Primitifler Dokümantasyonu**: Sunucu primitifleri (Kaynaklar, İstemler, Araçlar) ve istemci primitifleri (Sampling, Tetikleme, Günlükleme, Roots) doğrulandı
- **Taşıma Mekanizmaları**: STDIO ve Akışkan HTTP taşıma dokümantasyonının doğruluğu onaylandı
- **Güvenlik Rehberliği**: Güncel MCP Güvenlik En İyi Uygulamaları dokümantasyonu ile uyumluluk doğrulandı

#### Temel MCP 2025-11-25 Özellikleri Dokümante Edildi
- **OpenID Connect Keşfi**: Yetki sunucusu keşfi için OIDC
- **OAuth İstemci Kimliği Meta Veri Belgeleri**: Önerilen istemci kayıt mekanizması
- **JSON Şeması 2020-12**: MCP şema tanımları için varsayılan lehçe
- **SDK Katman Sistemi**: SDK özellik desteği ve bakımı için resmi gereksinimler
- **Yönetim Yapısı**: MCP yönetiminde Çalışma Grupları ve İlgi Gruplarının resmi yapısı

### Güvenlik Dokümantasyonu Büyük Güncellemesi (02-Security/)

#### MCP Güvenlik Zirvesi Atölyesi (Sherpa) Entegrasyonu
- **Yeni Uygulamalı Eğitim Kaynağı**: Tüm güvenlik dokümantasyonunda [MCP Güvenlik Zirvesi Atölyesi (Sherpa)](https://azure-samples.github.io/sherpa/) ile kapsamlı entegrasyon eklendi
- **Sefer Rotası Kapsamı**: Ana Kamp'tan Zirve'ye tam kamp-kamp ilerleyişi belgelendi
- **OWASP Uyumu**: Tüm güvenlik rehberliği artık OWASP MCP Azure Güvenlik Kılavuzu risklerine uyumlu

#### OWASP MCP En Çok 10 Entegrasyonu
- **Yeni Bölüm**: Ana Güvenlik README'sine Azure etkileriyle OWASP MCP En Çok 10 Güvenlik Riski tablosu eklendi
- **Risk Tabanlı Dokümantasyon**: Her güvenlik alanı için OWASP MCP risk referanslarıyla `mcp-security-controls-2025.md` güncellendi
- **Referans Mimari**: OWASP MCP Azure Güvenlik Kılavuzu referans mimarisi ve uygulama desenlerine bağlantı verildi

#### Güncellenmiş Güvenlik Dosyaları
- **README.md**: Sherpa Atölyesi genel görünümü, sefer rota tablosu, OWASP MCP En Çok 10 risk özeti ve uygulamalı eğitim bölümü eklendi
- **mcp-security-controls-2025.md**: Başlık Şubat 2026 olarak güncellendi, OWASP risk referansları (MCP01-MCP08) eklendi, spesifikasyon sürüm tutarsızlığı giderildi
- **mcp-security-best-practices-2025.md**: Sherpa ve OWASP kaynakları bölümü eklendi, zaman damgası güncellendi
- **mcp-best-practices.md**: Sherpa ve OWASP bağlantıları içeren uygulamalı eğitim bölümü eklendi
- **azure-content-safety-implementation.md**: OWASP MCP06 referansı, Sherpa Kamp 3 uyumu ve ek kaynaklar bölümü eklendi

#### Yeni Kaynak Bağlantıları Eklendi
- [MCP Güvenlik Zirvesi Atölyesi (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure Güvenlik Rehberi](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP İlk 10](https://owasp.org/www-project-mcp-top-10/)
- Bireysel OWASP MCP risk sayfaları (MCP01-MCP10)

### Müfredat Genelinde MCP Spesifikasyonu 2025-11-25 Uyumu

#### Modül 03 - Başlarken
- **SDK Dokümantasyonu**: Resmi SDK listesine Go SDK eklendi; tüm SDK referansları MCP Spesifikasyonu 2025-11-25 ile uyumlu şekilde güncellendi
- **Taşıma Açıklaması**: STDIO ve HTTP Streaming taşıma açıklamaları açık spesifikasyon referanslarıyla güncellendi

#### Modül 04 - Pratik Uygulama
- **SDK Güncellemeleri**: Go SDK eklendi; SDK listesi spesifikasyon versiyon referansıyla güncellendi
- **Yetkilendirme Spesifikasyonu**: MCP Yetkilendirme spesifikasyon bağlantısı güncel 2025-11-25 sürümüne güncellendi

#### Modül 05 - İleri Konular
- **Yeni Özellikler**: MCP Spesifikasyonu 2025-11-25'in yeni özelliklerine (Görevler, Araç Açıklamaları, URL Modu Tespiti, Kökler) dair not eklendi
- **Güvenlik Kaynakları**: Ek referanslara OWASP MCP İlk 10 ve Sherpa atölye bağlantıları eklendi

#### Modül 06 - Topluluk Katkıları
- **SDK Listesi**: Swift ve Rust SDK'ları eklendi; spesifikasyon bağlantısı 2025-11-25 olarak güncellendi
- **Spesifikasyon Referansı**: MCP Spesifikasyon bağlantısı doğrudan spesifikasyon URL'si olarak güncellendi

#### Modül 07 - Erken Benimsemeden Dersler
- **Kaynak Güncellemeleri**: MCP Spesifikasyonu 2025-11-25 bağlantısı ve OWASP MCP İlk 10 ek kaynaklara eklendi

#### Modül 08 - En İyi Uygulamalar
- **Spes Versiyonu**: MCP Spesifikasyon referansı 2025-11-25 olarak güncellendi
- **Güvenlik Kaynakları**: Ek referanslara OWASP MCP İlk 10 ve Sherpa atölye eklendi

#### Modül 10 - AI İş Akışlarını Kolaylaştırma
- **Rozet Güncellemesi**: MCP versiyon rozeti SDK versiyonundan (1.9.3) spesifikasyon versiyonuna (2025-11-25) değiştirildi
- **Kaynak Bağlantıları**: MCP Spesifikasyon bağlantısı güncellendi; OWASP MCP İlk 10 eklendi

#### Modül 11 - MCP Sunucu Uygulamalı Laboratuvarlar
- **Spesifikasyon Referansı**: MCP Spesifikasyon bağlantısı 2025-11-25 sürümüne güncellendi
- **Güvenlik Kaynakları**: Resmi kaynaklara OWASP MCP İlk 10 eklendi

## 18 Aralık 2025

### Güvenlik Dokümantasyonu Güncellemesi - MCP Spesifikasyonu 2025-11-25

#### MCP Güvenlik En İyi Uygulamaları (02-Security/mcp-best-practices.md) - Spesifikasyon Versiyonu Güncellemesi
- **Protokol Versiyonu Güncellemesi**: En son MCP Spesifikasyonu 2025-11-25 (25 Kasım 2025'te yayımlandı) referanslarıyla güncellendi
  - Tüm spesifikasyon versiyon referansları 2025-06-18'den 2025-11-25'e güncellendi
  - Doküman tarih referansları 18 Ağustos 2025'ten 18 Aralık 2025'e değiştirildi
  - Tüm spesifikasyon URL'lerinin mevcut dokümantasyona işaret ettiği doğrulandı
- **İçerik Doğrulama**: En son standartlara göre güvenlik en iyi uygulamalarının kapsamlı doğrulaması yapıldı
  - **Microsoft Güvenlik Çözümleri**: Prompt Shields (önceki adıyla "Jailbreak risk tespiti"), Azure Content Safety, Microsoft Entra ID ve Azure Key Vault için güncel terminoloji ve bağlantılar doğrulandı
  - **OAuth 2.1 Güvenliği**: En son OAuth güvenlik en iyi uygulamalarıyla uyum sağlandı
  - **OWASP Standartları**: LLM'ler için OWASP İlk 10 referanslarının güncel olduğu doğrulandı
  - **Azure Hizmetleri**: Tüm Microsoft Azure dokümantasyon linkleri ve en iyi uygulamalar doğrulandı
- **Standartlara Uyum**: Referans verilen tüm güvenlik standartları güncel olarak onaylandı
  - NIST AI Risk Yönetimi Çerçevesi
  - ISO 27001:2022
  - OAuth 2.1 Güvenlik En İyi Uygulamaları
  - Azure güvenlik ve uyumluluk çerçeveleri
- **Uygulama Kaynakları**: Tüm uygulama rehberi bağlantıları ve kaynakları doğrulandı
  - Azure API Yönetimi kimlik doğrulama desenleri
  - Microsoft Entra ID entegrasyon rehberleri
  - Azure Key Vault gizli yönetimi
  - DevSecOps pipeline'ları ve izleme çözümleri

### Dokümantasyon Kalite Güvencesi
- **Spesifikasyon Uygunluğu**: Tüm zorunlu MCP güvenlik gereksinimlerinin (MUST/MUST NOT) en son spesifikasyonla uyum sağladığı teyit edildi
- **Kaynak Güncelliği**: Microsoft dokümantasyonu, güvenlik standartları ve uygulama rehberlerine dış bağlantıların tümü doğrulandı
- **En İyi Uygulamalar Kapsamı**: Kimlik doğrulama, yetkilendirme, AI'ya özgü tehditler, tedarik zinciri güvenliği ve kurumsal desenlerin kapsamlı şekilde ele alındığı teyit edildi

## 6 Ekim 2025

### Başlarken Bölümü Genişletme – İleri Sunucu Kullanımı & Basit Kimlik Doğrulama

#### İleri Sunucu Kullanımı (03-GettingStarted/10-advanced)
- **Yeni Bölüm Eklendi**: Düzenli ve düşük seviye sunucu mimarilerini kapsayan kapsamlı ileri MCP sunucu kullanımı rehberi tanıtıldı.
  - **Düzenli ve Düşük Seviye Sunucu**: Her iki yaklaşım için Python ve TypeScript kod örnekleriyle ayrıntılı karşılaştırma.
  - **Handler Tabanlı Tasarım**: Ölçeklenebilir, esnek sunucu uygulamaları için handler tabanlı araç/kaynak/tetik yönetimi açıklaması.
  - **Pratik Desenler**: Düşük seviye sunucu desenlerinin ileri özellikler ve mimaride yararlı olduğu gerçek dünya senaryoları.

#### Basit Kimlik Doğrulama (03-GettingStarted/11-simple-auth)
- **Yeni Bölüm Eklendi**: MCP sunucularında basit kimlik doğrulama uygulamasına adım adım rehber.
  - **Kimlik Doğrulama Kavramları**: Kimlik doğrulama ve yetkilendirme ayrımı ile kimlik bilgileri yönetiminin açık açıklaması.
  - **Temel Kimlik Doğrulama Uygulaması**: Python (Starlette) ve TypeScript (Express) için ara yazılım tabanlı kimlik doğrulama desenleri ve kod örnekleri.
  - **İleri Güvenliğe Geçiş**: Basit kimlik doğrulamayla başlayıp OAuth 2.1 ve RBAC'a ilerleme rehberi; ileri güvenlik modüllerine referanslar.

Bu eklemeler, temel kavramlarla ileri üretim desenleri arasında köprü kurarak, daha sağlam, güvenli ve esnek MCP sunucu uygulamaları geliştirmek için pratik, uygulamalı rehberlik sağlar.

## 29 Eylül 2025

### MCP Sunucu Veritabanı Entegrasyon Laboratuvarları - Kapsamlı Uygulamalı Öğrenme Yolu

#### 11-MCPServerHandsOnLabs - Yeni Tam Veritabanı Entegrasyon Müfredatı
- **Tam 13-Lab Öğrenme Yolu**: Üretime hazır MCP sunucular inşa etmek için PostgreSQL veritabanı entegrasyonlu kapsamlı uygulamalı müfredat eklendi
  - **Gerçek Dünya Uygulaması**: Zava Retail analitik kullanım durumu, kurumsal düzey desenler sunar
  - **Yapılandırılmış Öğrenme İlerlemesi**:
    - **Lab 00-03: Temeller** - Giriş, Temel Mimari, Güvenlik & Çoklu Kiracı, Ortam Kurulumu
    - **Lab 04-06: MCP Sunucu İnşası** - Veritabanı Tasarımı & Şeması, MCP Sunucu Uygulaması, Araç Geliştirme  
    - **Lab 07-09: İleri Özellikler** - Anlamsal Arama Entegrasyonu, Test & Hata Ayıklama, VS Code Entegrasyonu
    - **Lab 10-12: Üretim & En İyi Uygulamalar** - Dağıtım Stratejileri, İzleme & Gözlemlenebilirlik, En İyi Uygulamalar & Optimizasyon
  - **Kurumsal Teknolojiler**: FastMCP çerçevesi, PostgreSQL ve pgvector, Azure OpenAI gömme sistemler, Azure Container Apps, Application Insights
  - **İleri Özellikler**: Satır Düzeyi Güvenlik (RLS), anlamsal arama, çoklu kiracı veri erişimi, vektör gömme, gerçek zamanlı izleme

#### Terminoloji Standardizasyonu - Modülden Laba Dönüşüm
- **Kapsamlı Dokümantasyon Güncellemesi**: 11-MCPServerHandsOnLabs içindeki tüm README dosyaları "Modül" yerine "Lab" terimi kullanacak şekilde sistematik olarak güncellendi
  - **Bölüm Başlıkları**: 13 laboratuvarın tamamında "Bu Modül Ne Kapsar" başlığı "Bu Lab Ne Kapsar" şeklinde güncellendi
  - **İçerik Açıklaması**: Dokümantasyon boyunca "Bu modül sağlar..." ifadesi "Bu lab sağlar..." olarak değiştirildi
  - **Öğrenme Hedefleri**: "Bu modülün sonunda..." ifadeleri "Bu labın sonunda..." olarak güncellendi
  - **Yönlendirme Bağlantıları**: Tüm "Modül XX:" referansları çapraz referanslarda ve navigasyonda "Lab XX:" olarak dönüştürüldü
  - **Tamamlama Takibi**: "Bu modülü tamamladıktan sonra..." ifadeleri "Bu labı tamamladıktan sonra..." olarak güncellendi
  - **Teknik Referanslar Korundu**: Konfigürasyon dosyalarında Python modül referansları (örneğin, `"module": "mcp_server.main"`) korundu

#### Çalışma Rehberi Geliştirmesi (study_guide.md)
- **Görsel Müfredat Haritası**: Yeni "11. Veritabanı Entegrasyon Laboratuvarları" bölümü ile kapsamlı lab yapısı görselleştirildi
- **Depo Yapısı**: On bölümden on bir ana bölüme ve detaylı 11-MCPServerHandsOnLabs açıklamasına güncellendi
- **Öğrenme Yolu Rehberi**: 00-11 bölümlerini kapsayacak şekilde navigasyon talimatları geliştirildi
- **Teknoloji Kapsamı**: FastMCP, PostgreSQL, Azure servis entegrasyon detayları eklendi
- **Öğrenme Sonuçları**: Üretime hazır sunucu geliştirme, veritabanı entegrasyon desenleri ve kurumsal güvenlik vurgulandı

#### Ana README Yapısı Geliştirmesi
- **Lab Tabanlı Terminoloji**: 11-MCPServerHandsOnLabs içindeki ana README.md dosyasında "Lab" yapısı tutarlı şekilde kullanıldı
- **Öğrenme Yolu Organizasyonu**: Temel kavramlardan ileri uygulama ve üretim dağıtımına net ilerleme
- **Gerçek Dünya Odaklılık**: Kurumsal seviyede desen ve teknolojilerle pratik, uygulamalı öğrenme vurgusu

### Dokümantasyon Kalite ve Tutarlılık İyileştirmeleri
- **Uygulamalı Öğrenme Vurgusu**: Dokümantasyonda uygulamalı, lab tabanlı yaklaşım güçlendirildi
- **Kurumsal Desenlere Odaklanma**: Üretime hazır uygulamalar ve kurumsal güvenlik dikkate alındı
- **Teknoloji Entegrasyonu**: Modern Azure servisleri ve AI entegrasyon desenleri kapsamlı şekilde ele alındı
- **Öğrenme İlerlemesi**: Temel kavramlardan üretim dağıtımına kadar net, yapısal yol haritası

## 26 Eylül 2025

### Vaka Çalışmaları Genişletmesi - GitHub MCP Registry Entegrasyonu

#### Vaka Çalışmaları (09-CaseStudy/) - Ekosistem Geliştirme Odaklı
- **README.md**: Kapsamlı GitHub MCP Registry vaka çalışması ile büyük genişletme
  - **GitHub MCP Registry Vaka Çalışması**: Eylül 2025'te GitHub'ın MCP Registry lansmanını detaylı inceleyen yeni vaka çalışması
    - **Sorun Analizi**: Parçalanmış MCP sunucu keşfi ve dağıtım zorluklarının ayrıntılı incelemesi
    - **Çözüm Mimari**: GitHub'ın merkezi kayıt yaklaşımı ve tek tıkla VS Code kurulumu
    - **İş Etkisi**: Geliştirici onboarding ve verimlilikte ölçülebilir gelişmeler
    - **Stratejik Değer**: Modüler ajan dağıtımı ve araçlar arası birlikte çalışabilirliğe odaklanma
    - **Ekosistem Geliştirme**: Ajan bazlı entegrasyon için temel platform olarak konumlandırma
  - **Geliştirilmiş Vaka Çalışması Yapısı**: Yedi vaka çalışmasının tümü tutarlı format ve kapsamlı açıklamalarla güncellendi
    - Azure AI Seyahat Ajanları: Çoklu ajan orkestrasyon vurgusu
    - Azure DevOps Entegrasyonu: İş akışı otomasyonu odaklı
    - Gerçek Zamanlı Dokümantasyon Getirme: Python konsol istemcisi uygulaması
    - Etkileşimli Çalışma Planı Üreticisi: Chainlit sohbet tabanlı web uygulaması
    - Editör İçi Dokümantasyon: VS Code ve GitHub Copilot entegrasyonu
    - Azure API Yönetimi: Kurumsal API entegrasyon desenleri
    - GitHub MCP Registry: Ekosistem geliştirme ve topluluk platformu
  - **Kapsamlı Sonuç**: Yedi vaka çalışmasını kapsayan, çeşitli MCP uygulama boyutlarını vurgulayan yeniden yazılmış sonuç bölümü
    - Kurumsal Entegrasyon, Çoklu Ajan Orkestrasyonu, Geliştirici Verimliliği
    - Ekosistem Geliştirme, Eğitimsel Uygulamalar kategorileri
    - Mimari desenler, uygulama stratejileri ve en iyi uygulamalar hakkında derinlemesine içgörüler
    - MCP'nin olgun, üretime hazır protokol olarak önemi

#### Çalışma Rehberi Güncellemeleri (study_guide.md)
- **Görsel Müfredat Haritası**: GitHub MCP Registry'nin Vaka Çalışması bölümüne dahil edilmesiyle mindmap güncellendi
- **Vaka Çalışması Açıklamaları**: Genel açıklamalardan yedi kapsamlı vaka çalışmasının detaylı dökümüne yükseltildi
- **Depo Yapısı**: 10. bölüm kapsamlı vaka çalışması detaylarıyla güncellendi
- **Değişiklik Günlüğü Entegrasyonu**: 26 Eylül 2025 girişi, GitHub MCP Registry eklemesi ve vaka çalışması geliştirilmeleri belgeledi
- **Tarih Güncellemeleri**: En son revizyonu (26 Eylül 2025) yansıtacak şekilde alt bilgi zaman damgası güncellendi

### Dokümantasyon Kalite İyileştirmeleri
- **Tutarlılık Artırımı**: Tüm yedi örnekte vaka çalışması format ve yapısı standart hale getirildi
- **Kapsamlı Kapsama**: Vaka çalışmaları artık kurumsal, geliştirici verimliliği ve ekosistem geliştirme senaryolarını kapsıyor
- **Stratejik Konumlandırma**: MCP’nin ajan tabanlı sistem dağıtımı için temel platform olarak önemi güçlendirildi
- **Kaynak Entegrasyonu**: Ek kaynaklara GitHub MCP Registry bağlantısı eklendi

## 15 Eylül 2025

### İleri Konular Genişletmesi - Özel Taşıma Mekanizmaları & Bağlam Mühendisliği

#### MCP Özel Taşıma Mekanizmaları (05-AdvancedTopics/mcp-transport/) - Yeni İleri Düzey Uygulama Rehberi
- **README.md**: Özel MCP taşıma mekanizmaları için kapsamlı uygulama rehberi
  - **Azure Event Grid Taşıması**: Kapsamlı sunucusuz olay tabanlı taşıma uygulaması
    - C#, TypeScript ve Python örnekleri ile Azure Functions entegrasyonu
    - Ölçeklenebilir MCP çözümleri için olay odaklı mimari desenleri
    - Webhook alıcıları ve itmeli mesaj yönetimi
  - **Azure Event Hubs Taşıması**: Yüksek verimli akış taşıma uygulaması
    - Düşük gecikmeli senaryolar için gerçek zamanlı akış yetenekleri
    - Bölümleme stratejileri ve kontrol noktası yönetimi
    - Mesaj paketleme ve performans optimizasyonu
  - **Kurumsal Entegrasyon Desenleri**: Üretime hazır mimari örnekler
    - Çoklu Azure Functions üzerinde dağıtılmış MCP işleme
    - Birden çok taşıma türünü birleştiren hibrit taşıma mimarileri
    - Mesaj dayanıklılığı, güvenilirliği ve hata yönetimi stratejileri
  - **Güvenlik & İzleme**: Azure Key Vault entegrasyonu ve gözlemlenebilirlik desenleri
    - Yönetilen kimlik doğrulama ve en az ayrıcalık erişimi
    - Application Insights telemetri ve performans izleme
    - Devre kesiciler ve hata tolerans desenleri
  - **Test Çerçeveleri**: Özel taşıma mekanizmaları için kapsamlı test stratejileri
    - Test çiftleri ve taklit çerçeveleri ile birim testi
    - Azure Test Containers ile entegrasyon testi
    - Performans ve yük testi düşünceleri

#### Bağlam Mühendisliği (05-AdvancedTopics/mcp-contextengineering/) - Yükselen AI Disiplini
- **README.md**: Bağlam mühendisliği alanının kapsamlı incelemesi olarak ortaya çıkan bir alan
  - **Temel İlkeler**: Tam bağlam paylaşımı, eylem karar farkındalığı ve bağlam pencere yönetimi

  - **MCP Protokol Hizalaması**: MCP tasarımının bağlam mühendisliği zorluklarını nasıl ele aldığı
    - Bağlam penceresi sınırlamaları ve aşamalı yükleme stratejileri
    - Alaka belirleme ve dinamik bağlam getirme
    - Çok modlu bağlam işleme ve güvenlik hususları
  - **Uygulama Yaklaşımları**: Tek iş parçacıklı vs. çoklu ajan mimarileri
    - Bağlam parçalara ayırma ve önceliklendirme teknikleri
    - Aşamalı bağlam yükleme ve sıkıştırma stratejileri
    - Katmanlı bağlam yaklaşımları ve getirme optimizasyonu
  - **Ölçüm Çerçevesi**: Bağlam etkinliği değerlendirmesi için ortaya çıkan metrikler
    - Girdi verimliliği, performans, kalite ve kullanıcı deneyimi hususları
    - Bağlam optimizasyonuna yönelik deneysel yaklaşımlar
    - Hata analizi ve iyileştirme metodolojileri

#### Müfredat Navigasyon Güncellemeleri (README.md)
- **Geliştirilmiş Modül Yapısı**: Yeni gelişmiş konuları içerecek şekilde müfredat tablosu güncellendi
  - Bağlam Mühendisliği (5.14) ve Özel Taşıma (5.15) maddeleri eklendi
  - Tüm modüller arasında tutarlı biçimlendirme ve gezinme bağlantıları
  - Güncel içerik kapsamını yansıtacak şekilde açıklamalar güncellendi

### Dizin Yapısı İyileştirmeleri
- **İsimlendirme Standartlaştırması**: "mcp transport" tutarlılık için "mcp-transport" olarak yeniden adlandırıldı
- **İçerik Organizasyonu**: Tüm 05-GelişmişKonular klasörleri şimdi tutarlı isimlendirme desenini takip ediyor (mcp-[konu])

### Dokümantasyon Kalitesi Geliştirmeleri
- **MCP Spesifikasyon Hizalaması**: Tüm yeni içerikler mevcut MCP Spesifikasyonu 2025-06-18 referans alınarak hazırlandı
- **Çok Dilli Örnekler**: C#, TypeScript ve Python’da kapsamlı kod örnekleri
- **Kurumsal Odak**: Üretime hazır kalıplar ve Azure bulut entegrasyonu genelinde
- **Görsel Dokümantasyon**: Mimari ve akış görselleştirmeleri için Mermaid diyagramları

## 18 Ağustos 2025

### Dokümantasyon Kapsamlı Güncelleme - MCP 2025-06-18 Standartları

#### MCP Güvenlik En İyi Uygulamaları (02-Security/) - Tam Modernizasyon
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: MCP Spesifikasyonu 2025-06-18 ile tam uyumlu yeniden yazım
  - **Zorunlu Gereksinimler**: Resmi spesifikasyondan açıkça belirtilmiş MUST/MUST NOT gereksinimleri eklendi, net görsel göstergelerle
  - **12 Temel Güvenlik Uygulaması**: 15 maddelik listeden kapsamlı güvenlik alanlarına yeniden yapılandırıldı
    - Dış kimlik sağlayıcı entegrasyonlu Token Güvenliği & Kimlik Doğrulama
    - Kriptografik gereksinimlerle Oturum Yönetimi & Taşıma Güvenliği
    - Microsoft Prompt Shields entegrasyonlu AI’ye özgü Tehdit Koruması
    - En aza indirgenmiş ayrıcalık ilkesi ile Erişim Kontrolü & İzinler
    - Azure Content Safety entegrasyonlu İçerik Güvenliği & İzleme
    - Kapsamlı bileşen doğrulamasıyla Tedarik Zinciri Güvenliği
    - PKCE uygulaması ile OAuth Güvenliği & “Confused Deputy” engelleme
    - Otomatik yeteneklerle Olay Müdahalesi & Kurtarma
    - Düzenleyici uyum ile Uyumluluk & Yönetişim
    - Sıfır güven mimarisi ile Gelişmiş Güvenlik Kontrolleri
    - Kapsamlı çözümlerle Microsoft Güvenlik Ekosistemi Entegrasyonu
    - Uyarlanabilir uygulamalarla Sürekli Güvenlik Evrimi
  - **Microsoft Güvenlik Çözümleri**: Prompt Shields, Azure Content Safety, Entra ID ve GitHub Gelişmiş Güvenliği için geliştirilmiş entegrasyon rehberi
  - **Uygulama Kaynakları**: Resmi MCP Dokümantasyonu, Microsoft Güvenlik Çözümleri, Güvenlik Standartları ve Uygulama Kılavuzları kategorilerinde kapsamlı kaynak bağlantıları

#### Gelişmiş Güvenlik Kontrolleri (02-Security/) - Kurumsal Uygulama
- **MCP-SECURITY-CONTROLS-2025.md**: Kurumsal seviyede güvenlik çerçevesi ile tamamen yenilendi
  - **9 Kapsamlı Güvenlik Alanı**: Temel kontrollerden detaylı kurumsal çerçeveye genişletildi
    - Microsoft Entra ID entegrasyonlu Gelişmiş Kimlik Doğrulama & Yetkilendirme
    - Kapsamlı doğrulamayla Token Güvenliği & Anti-Passthrough Kontrolleri
    - Kaçırma önleyici Oturum Güvenliği Kontrolleri
    - Prompt enjeksiyonu ve araç zehirlenmesini engelleyen AI'ya Özgü Güvenlik Kontrolleri
    - OAuth proxy güvenliği ile Confused Deputy Saldırı Önleme
    - Sandboxing ve izolasyonlu Araç Çalıştırma Güvenliği
    - Bağımlılık doğrulamasıyla Tedarik Zinciri Güvenlik Kontrolleri
    - SIEM entegrasyonlu İzleme & Algılama Kontrolleri
    - Otomatik yeteneklerle Olay Müdahalesi & Kurtarma
  - **Uygulama Örnekleri**: Detaylı YAML yapılandırma blokları ve kod örnekleri eklendi
  - **Microsoft Çözümleri Entegrasyonu**: Azure güvenlik servisleri, GitHub Gelişmiş Güvenlik ve kurumsal kimlik yönetimi tam kapsamlı

#### Gelişmiş Konular Güvenliği (05-AdvancedTopics/mcp-security/) - Üretime Hazır Uygulama
- **README.md**: Kurumsal güvenlik uygulaması için tamamen yenilendi
  - **Mevcut Spesifikasyon Uyumu**: MCP Spesifikasyonu 2025-06-18 ile güncellendi ve zorunlu güvenlik gereksinimleri eklendi
  - **Gelişmiş Kimlik Doğrulama**: Microsoft Entra ID entegrasyonlu kapsamlı .NET ve Java Spring Security örnekleri
  - **AI Güvenlik Entegrasyonu**: Microsoft Prompt Shields ve Azure Content Safety Python örnekleriyle uygulandı
  - **Gelişmiş Tehdit Azaltma**: Kapsamlı uygulama örnekleri
    - PKCE ve kullanıcı onayı doğrulaması ile Confused Deputy Saldırı Önleme
    - Hedef kitle doğrulaması ve güvenli token yönetimiyle Token Passthrough Engelleme
    - Kriptografik bağlama ve davranış analizi ile Oturum Kaçırma Önleme
  - **Kurumsal Güvenlik Entegrasyonu**: Azure Application Insights izleme, tehdit tespit boru hatları ve tedarik zinciri güvenliği
  - **Uygulama Kontrol Listesi**: Zorunlu ve önerilen güvenlik kontrolleri açıkça belirtildi; Microsoft güvenlik ekosistemi faydaları

### Dokümantasyon Kalitesi ve Standartlara Uyum
- **Spesifikasyon Referansları**: Tüm referanslar mevcut MCP Spesifikasyonu 2025-06-18 olarak güncellendi
- **Microsoft Güvenlik Ekosistemi**: Tüm güvenlik dokümantasyonunda entegrasyon rehberliği geliştirildi
- **Pratik Uygulama**: .NET, Java ve Python’da ayrıntılı kod örnekleri ve kurumsal kalıplar eklendi
- **Kaynak Organizasyonu**: Resmi dokümantasyon, güvenlik standartları ve uygulama kılavuzları kapsamlı şekilde kategorize edildi
- **Görsel Göstergeler**: Zorunlu gereksinimler ile önerilen uygulamalar net olarak işaretlendi


#### Temel Kavramlar (01-CoreConcepts/) - Tam Modernizasyon
- **Protokol Versiyon Güncellemesi**: Tarih tabanlı versiyonlama ile MCP Spesifikasyonu 2025-06-18 referans alındı (YYYY-AA-GG formatı)
- **Mimari İyileştirmeler**: Ana bilgisayarlar, istemciler ve sunucuların açıklamaları MCP mimari kalıplarına göre geliştirildi
  - Hostlar artık birden çok MCP istemci bağlantısını koordine eden yapay zeka uygulamaları olarak net tanımlandı
  - İstemciler protokol bağlayıcıları olarak, bire bir sunucu ilişkileri sürdürme olarak tanımlandı
  - Sunucular yerel ve uzak dağıtım senaryoları ile geliştirildi
- **İlkel Yapıların Yeniden Düzeni**: Sunucu ve istemci ilkel yapılar tamamen yenilendi
  - Sunucu İlkel Yapıları: Kaynaklar (veri kaynakları), İstemler (şablonlar), Araçlar (çalıştırılabilir fonksiyonlar) detaylı açıklama ve örneklerle
  - İstemci İlkel Yapıları: Örnekleme (LLM tamamlamaları), Elde Etme (kullanıcı girdisi), Günlük Kaydı (hata ayıklama/izleme)
  - Mevcut keşif (`*/list`), çağırma (`*/get`) ve yürütme (`*/call`) yöntem kalıplarıyla güncellendi
- **Protokol Mimarisi**: İki katmanlı mimari modeli tanıtıldı
  - Veri Katmanı: Yaşam döngüsü yönetimi ve ilkel yapılarla JSON-RPC 2.0 temeli
  - Taşıma Katmanı: STDIO (yerel) ve Streamable HTTP ile SSE (uzak) taşıma mekanizmaları
- **Güvenlik Çerçevesi**: Açık kullanıcı rızası, veri gizliliği koruması, araç yürütme güvenliği ve taşıma katmanı güvenliği dahil kapsamlı güvenlik prensipleri
- **İletişim Kalıpları**: Protokol mesajları başlatma, keşif, yürütme ve bildirim akışlarını gösterecek şekilde güncellendi
- **Kod Örnekleri**: Mevcut MCP SDK kalıplarını yansıtacak şekilde çok dilli örnekler (.NET, Java, Python, JavaScript) yenilendi

#### Güvenlik (02-Security/) - Kapsamlı Güvenlik Yenileme  
- **Standartlara Uyum**: MCP Spesifikasyonu 2025-06-18 güvenlik gereksinimleri ile tam uyum
- **Kimlik Doğrulama Evrimi**: Özel OAuth sunucularından dış kimlik sağlayıcı delege (Microsoft Entra ID) evrimi belgelendi
- **AI’ye Özgü Tehdit Analizi**: Modern yapay zeka saldırı vektörlerinin kapsamı genişletildi
  - Gerçek dünya örnekleriyle detaylı prompt enjeksiyonu saldırı senaryoları
  - Araç zehirlenme mekanizmaları ve “kilit çekme” saldırı kalıpları
  - Bağlam pencere zehirlenmesi ve model karışıklığı saldırıları
- **Microsoft AI Güvenlik Çözümleri**: Microsoft güvenlik ekosisteminin kapsamlı ele alınması
  - Gelişmiş algılama, odaklama ve ayırıcı tekniklerle AI Prompt Shields
  - Azure Content Safety entegrasyon kalıpları
  - Tedarik zinciri koruması için GitHub Gelişmiş Güvenlik
- **Gelişmiş Tehdit Azaltma**: Ayrıntılı güvenlik kontrolleri
  - MCP’ye özgü oturum kaçırma saldırı senaryoları ve kriptografik oturum ID gereksinimleriyle Oturum kaçırma
  - Açık onay gereksinimleriyle MCP proxy senaryolarındaki Confused Deputy sorunları
  - Zorunlu doğrulama kontrolleriyle Token geçirme açıkları
- **Tedarik Zinciri Güvenliği**: Temel modeller, gömme hizmetleri, bağlam sağlayıcıları ve üçüncü taraf API’ler dahil AI tedarik zinciri kapsam genişletildi
- **Temel Güvenlik**: Sıfır güven mimarisi ve Microsoft güvenlik ekosistemi dahil kurumsal güvenlik kalıplarıyla geliştirilmiş entegrasyon
- **Kaynak Organizasyonu**: Türlere göre kategorize edilmiş kapsamlı kaynak bağlantıları (Resmi Dokümanlar, Standartlar, Araştırma, Microsoft Çözümleri, Uygulama Kılavuzları)

### Dokümantasyon Kalite İyileştirmeleri
- **Yapılandırılmış Öğrenme Hedefleri**: Spesifik, uygulanabilir sonuçlar ile öğrenme hedefleri geliştirilmiştir  
- **Çapraz Referanslar**: İlgili güvenlik ve temel kavram konuları arasında bağlantılar eklendi
- **Güncel Bilgi**: Tüm tarih referansları ve spesifikasyon bağlantıları mevcut standartlara göre güncellendi
- **Uygulama Rehberi**: Her iki bölümde de spesifik, uygulanabilir uygulama rehberliği eklendi

## 16 Temmuz 2025

### README ve Navigasyon İyileştirmeleri
- README.md'deki müfredat navigasyonu tamamen yeniden tasarlandı
- `<details>` etiketleri daha erişilebilir tablo tabanlı formata dönüştürüldü
- Yeni "alternative_layouts" klasöründe alternatif düzen seçenekleri oluşturuldu
- Kart tabanlı, sekmeli ve akordeon stilli gezinme örnekleri eklendi
- Depo yapısı bölümü en güncel dosyaları içerecek şekilde güncellendi
- "Bu Müfredat Nasıl Kullanılır" bölümü net önerilerle geliştirildi
- MCP spesifikasyon bağlantıları doğru URL’lere işaret edecek şekilde güncellendi
- Müfredat yapısına Bağlam Mühendisliği bölümü (5.14) eklendi

### Çalışma Rehberi Güncellemeleri
- Depo yapısına tam uyumlu olacak şekilde çalışma rehberi tamamen yeniden düzenlendi
- MCP İstemcileri ve Araçları ile Popüler MCP Sunucuları hakkında yeni bölümler eklendi
- Görsel Müfredat Haritası tüm konuları doğru şekilde yansıtacak şekilde güncellendi
- Tüm uzmanlık alanlarını kapsayacak şekilde Gelişmiş Konular açıklamaları geliştirildi
- Gerçek örnekleri yansıtacak şekilde Vaka Çalışmaları bölümü güncellendi
- Bu kapsamlı değişiklik günlüğü eklendi

### Topluluk Katkıları (06-CommunityContributions/)
- Görüntü oluşturma için MCP sunucuları hakkında ayrıntılı bilgi eklendi
- VSCode'da Claude kullanımı üzerine kapsamlı bölüm eklendi
- Cline terminal istemcisi kurulumu ve kullanım talimatları eklendi
- Tüm popüler istemci seçeneklerini içerecek şekilde MCP istemci bölümü güncellendi
- Katkı örnekleri daha doğru kod örnekleriyle geliştirildi

### Gelişmiş Konular (05-AdvancedTopics/)
- Tüm uzman konu klasörleri tutarlı isimlendirme ile organize edildi
- Bağlam mühendisliği materyalleri ve örnekleri eklendi
- Foundry ajan entegrasyon dokümantasyonu eklendi
- Entra ID güvenlik entegrasyon dokümantasyonu geliştirildi

## 11 Haziran 2025

### İlk Oluşturma
- MCP for Beginners müfredatının ilk sürümü yayımlandı
- Tüm 10 ana bölüm için temel yapı oluşturuldu
- Navigasyon için Görsel Müfredat Haritası uygulandı
- Çoklu programlama dillerinde başlangıç örnek projeler eklendi

### Başlarken (03-GettingStarted/)
- İlk sunucu uygulama örnekleri oluşturuldu
- İstemci geliştirme rehberi eklendi
- LLM istemci entegrasyon talimatları dahil edildi
- VS Code entegrasyon dokümantasyonu eklendi
- Server-Sent Events (SSE) sunucu örnekleri uygulandı

### Temel Kavramlar (01-CoreConcepts/)
- İstemci-sunucu mimarisinin ayrıntılı açıklaması eklendi
- Ana protokol bileşenleri üzerine dokümantasyon oluşturuldu
- MCP’de mesajlaşma kalıpları belgelendi

## 23 Mayıs 2025

### Depo Yapısı
- Depo temel klasör yapısıyla başlatıldı
- Her ana bölüm için README dosyaları oluşturuldu
- Çeviri altyapısı kuruldu
- Görsel varlıklar ve diyagramlar eklendi

### Dokümantasyon
- Müfredat genel bakışlı ilk README.md oluşturuldu
- CODE_OF_CONDUCT.md ve SECURITY.md eklendi
- Yardım alma rehberi içeren SUPPORT.md dosyası kuruldu
- Ön çalışma rehberi yapısı oluşturuldu

## 15 Nisan 2025

### Planlama ve Çerçeve
- MCP for Beginners müfredatı için ilk planlama yapıldı
- Öğrenme hedefleri ve hedef kitle tanımlandı
- Müfredatın 10 bölümlük yapısı ortaya kondu
- Örnekler ve vaka çalışmaları için kavramsal çerçeve geliştirildi
- Anahtar kavramlar için ilk prototip örnekler oluşturuldu

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->