# Menjalankan contoh ini

Ini adalah penyelesaian Rust untuk contoh klien LLM. Anda perlu memasang rantai alat Rust; lihat [panduan pemasangan rasmi](https://www.rust-lang.org/tools/install).

Klien memanggil model Microsoft Foundry yang diterapkan melalui OpenAI Azure
titik akhir v1.

> [!NOTE]
> Nilai yang dihantar sebagai `model` adalah nama pengeluaran Foundry anda, bukan semestinya
> nama model asas.

## -0- Konfigurasi Microsoft Foundry

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

## -1- Bina contoh

```bash
cargo build
```

## -2- Jalankan contoh

```bash
cargo run
```

Klien memulakan pelayan MCP kalkulator, mengambil senarai alatan, dan menggunakan
model yang diterapkan untuk memanggil alat `add`. Anda harus melihat output yang menunjukkan
panggilan alat (contoh, "Memanggil alat: add") dan keputusan panggilan tersebut.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->