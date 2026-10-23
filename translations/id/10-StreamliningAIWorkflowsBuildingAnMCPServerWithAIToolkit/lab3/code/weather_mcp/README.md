# Server MCP Cuaca

Ini adalah contoh Server MCP dalam Python yang mengimplementasikan alat cuaca dengan respons tiruan. Ini dapat digunakan sebagai kerangka untuk Server MCP Anda sendiri. Ini mencakup fitur-fitur berikut:

- **Alat Cuaca**: Sebuah alat yang menyediakan informasi cuaca tiruan berdasarkan lokasi yang diberikan.
- **Terhubung ke Agent Builder**: Fitur yang memungkinkan Anda menghubungkan server MCP ke Agent Builder untuk pengujian dan debugging.
- **Debug di [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Fitur yang memungkinkan Anda melakukan debug Server MCP menggunakan MCP Inspector.

## Mulai dengan template Server MCP Cuaca

> **Prasyarat**
>
> Untuk menjalankan Server MCP di mesin pengembangan lokal Anda, Anda memerlukan:
>
> - [Python](https://www.python.org/)
> - (*Opsional - jika Anda lebih suka uv*) [uv](https://github.com/astral-sh/uv)
> - [Ekstensi Debugger Python](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Siapkan lingkungan

Ada dua pendekatan untuk menyiapkan lingkungan untuk proyek ini. Anda dapat memilih salah satu berdasarkan preferensi Anda.

> Catatan: Muat ulang VSCode atau terminal untuk memastikan python lingkungan virtual digunakan setelah membuat lingkungan virtual.

| Pendekatan | Langkah-langkah |
| -------- | ----- |
| Menggunakan `uv` | 1. Buat lingkungan virtual: `uv venv` <br>2. Jalankan Perintah VSCode "***Python: Select Interpreter***" dan pilih python dari lingkungan virtual yang dibuat <br>3. Instal dependensi (termasuk dependensi pengembangan): `uv pip install -r pyproject.toml --extra dev` |
| Menggunakan `pip` | 1. Buat lingkungan virtual: `python -m venv .venv` <br>2. Jalankan Perintah VSCode "***Python: Select Interpreter***" dan pilih python dari lingkungan virtual yang dibuat<br>3. Instal dependensi (termasuk dependensi pengembangan): `pip install -e .[dev]` |

Setelah menyiapkan lingkungan, Anda dapat menjalankan server di mesin pengembangan lokal Anda melalui Agent Builder sebagai Klien MCP untuk memulai:
1. Buka panel Debug VS Code. Pilih `Debug in Agent Builder` atau tekan `F5` untuk mulai melakukan debug server MCP.
2. Dalam Microsoft Foundry Toolkit Agent Builder, pilih deployment Foundry aktif seperti `gpt-5.1`, lalu masukkan: `What is the weather in Shanghai?` Server akan tersambung secara otomatis.
3. Klik `Run` untuk menguji server dengan prompt.

**Selamat**! Anda telah berhasil menjalankan Server MCP Cuaca di mesin pengembangan lokal Anda melalui Agent Builder sebagai Klien MCP.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Apa saja yang termasuk dalam template

| Folder / Berkas | Isi                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | Berkas-berkas VSCode untuk debugging       |
| `.aitk`      | Konfigurasi untuk Microsoft Foundry Toolkit                |
| `src`        | Kode sumber untuk server MCP cuaca           |

## Cara melakukan debug Server MCP Cuaca

> Catatan:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) adalah alat pengembang visual untuk pengujian dan debugging server MCP.
> - Semua mode debugging mendukung breakpoint, sehingga Anda dapat menambahkan breakpoint ke kode implementasi alat.

| Mode Debug | Deskripsi | Langkah untuk debug |
| ---------- | ----------- | --------------- |
| Agent Builder | Debug server MCP di Agent Builder melalui Microsoft Foundry Toolkit. | 1. Buka panel Debug VS Code. Pilih `Debug in Agent Builder` dan tekan `F5` untuk mulai melakukan debug server MCP.<br>2. Pilih deployment Foundry aktif seperti `gpt-5.1`, lalu masukkan `What is the weather in Shanghai?`. Server akan tersambung secara otomatis.<br>3. Klik `Run` untuk menguji server dengan prompt. |
| MCP Inspector | Debug server MCP menggunakan MCP Inspector. | 1. Instal [Node.js](https://nodejs.org/)<br> 2. Siapkan Inspector: `cd inspector` && `npm install` <br> 3. Buka panel Debug VS Code. Pilih `Debug SSE in Inspector (Edge)` atau `Debug SSE in Inspector (Chrome)`. Tekan F5 untuk mulai melakukan debug.<br> 4. Ketika MCP Inspector terbuka di browser, klik tombol `Connect` untuk menghubungkan server MCP ini.<br> 5. Kemudian Anda dapat `List Tools`, pilih alat, masukkan parameter, dan `Run Tool` untuk melakukan debug kode server Anda.<br> |

## Port Default dan kustomisasi

| Mode Debug | Port | Definisi | Kustomisasi | Catatan |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Sunting [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) untuk mengubah port di atas. | N/A |
| MCP Inspector | 3001 (Server); 5173 dan 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Sunting [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) untuk mengubah port di atas.| N/A |

## Umpan balik

Jika Anda memiliki umpan balik atau saran untuk template ini, silakan buka isu di [repositori Microsoft Foundry Toolkit GitHub](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->