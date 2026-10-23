# Menjalankan contoh ini

Ini adalah solusi Rust untuk contoh klien LLM. Anda perlu menginstal Rust toolchain; lihat [panduan instal resmi](https://www.rust-lang.org/tools/install).

Klien memanggil model Microsoft Foundry yang dideploy melalui endpoint Azure OpenAI
v1.

> [!NOTE]
> Nilai yang diteruskan sebagai `model` adalah nama deployment Foundry Anda, tidak harus
> nama model yang mendasarinya.

## -0- Konfigurasikan Microsoft Foundry

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<api-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<resource-name>.openai.azure.com"
$env:AZURE_OPENAI_API_KEY = "<api-key>"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5.1"
```

## -1- Bangun contoh

```bash
cargo build
```

## -2- Jalankan contoh

```bash
cargo run
```

Klien memulai server MCP kalkulator, mengambil daftar alatnya, dan menggunakan
model yang dideploy untuk memanggil alat `add`. Anda harus melihat keluaran yang menunjukkan
pemanggilan alat (misalnya, "Calling tool: add") dan hasil dari pemanggilan tersebut.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->