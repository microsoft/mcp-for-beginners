# Weather MCP Server

Ini adalah contoh MCP Server dalam Python yang mengimplementasikan alat cuaca dengan respons tiruan. Ini dapat digunakan sebagai kerangka untuk MCP Server Anda sendiri. Fitur yang disertakan meliputi:

- **Weather Tool**: Alat yang menyediakan informasi cuaca tiruan berdasarkan lokasi yang diberikan.
- **Connect to Agent Builder**: Fitur yang memungkinkan Anda menghubungkan MCP server ke Agent Builder untuk pengujian dan debugging.
- **Debug in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Fitur yang memungkinkan Anda melakukan debugging MCP Server menggunakan MCP Inspector.

## Memulai dengan template Weather MCP Server

> **Prasyarat**
>
> Untuk menjalankan MCP Server di mesin pengembangan lokal Anda, Anda memerlukan:
>
> - [Python](https://www.python.org/)
> - (*Opsional - jika Anda lebih suka uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Persiapan lingkungan

Ada dua cara untuk menyiapkan lingkungan untuk proyek ini. Anda dapat memilih salah satu sesuai preferensi Anda.

> Catatan: Muat ulang VSCode atau terminal untuk memastikan python dari virtual environment digunakan setelah membuat virtual environment.

| Pendekatan | Langkah-langkah |
| -----------|-----------------|
| Menggunakan `uv` | 1. Buat virtual environment: `uv venv` <br>2. Jalankan perintah VSCode "***Python: Select Interpreter***" dan pilih python dari virtual environment yang dibuat <br>3. Instal dependensi (termasuk dependensi dev): `uv pip install -r pyproject.toml --extra dev` |
| Menggunakan `pip` | 1. Buat virtual environment: `python -m venv .venv` <br>2. Jalankan perintah VSCode "***Python: Select Interpreter***" dan pilih python dari virtual environment yang dibuat<br>3. Instal dependensi (termasuk dependensi dev): `pip install -e .[dev]` |

Setelah menyiapkan lingkungan, Anda dapat menjalankan server di mesin pengembangan lokal melalui Agent Builder sebagai MCP Client untuk memulai:
1. Buka panel Debug di VS Code. Pilih `Debug in Agent Builder` atau tekan `F5` untuk mulai melakukan debugging MCP server.
2. Gunakan AI Toolkit Agent Builder untuk menguji server dengan [prompt ini](../../../../../../../../../../open_prompt_builder). Server akan otomatis terhubung ke Agent Builder.
3. Klik `Run` untuk menguji server dengan prompt tersebut.

**Selamat!** Anda telah berhasil menjalankan Weather MCP Server di mesin pengembangan lokal melalui Agent Builder sebagai MCP Client.  
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Apa saja yang termasuk dalam template

| Folder / File | Isi                                      |
| ------------- | --------------------------------------- |
| `.vscode`     | File VSCode untuk debugging             |
| `.aitk`       | Konfigurasi untuk AI Toolkit            |
| `src`         | Kode sumber untuk weather mcp server   |

## Cara melakukan debugging Weather MCP Server

> Catatan:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) adalah alat visual untuk pengembang dalam pengujian dan debugging MCP server.
> - Semua mode debugging mendukung breakpoint, sehingga Anda dapat menambahkan breakpoint pada kode implementasi alat.

| Mode Debug | Deskripsi | Langkah debugging |
| ---------- | --------- | ----------------- |
| Agent Builder | Debug MCP server di Agent Builder melalui AI Toolkit. | 1. Buka panel Debug di VS Code. Pilih `Debug in Agent Builder` dan tekan `F5` untuk mulai debugging MCP server.<br>2. Gunakan AI Toolkit Agent Builder untuk menguji server dengan [prompt ini](../../../../../../../../../../open_prompt_builder). Server akan otomatis terhubung ke Agent Builder.<br>3. Klik `Run` untuk menguji server dengan prompt tersebut. |
| MCP Inspector | Debug MCP server menggunakan MCP Inspector. | 1. Instal [Node.js](https://nodejs.org/)<br>2. Siapkan Inspector: `cd inspector` && `npm install` <br>3. Buka panel Debug di VS Code. Pilih `Debug SSE in Inspector (Edge)` atau `Debug SSE in Inspector (Chrome)`. Tekan F5 untuk mulai debugging.<br>4. Saat MCP Inspector terbuka di browser, klik tombol `Connect` untuk menghubungkan MCP server ini.<br>5. Kemudian Anda dapat `List Tools`, pilih alat, masukkan parameter, dan `Run Tool` untuk debugging kode server Anda.<br> |

## Port Default dan kustomisasi

| Mode Debug | Port | Definisi | Kustomisasi | Catatan |
| ---------- | ---- | -------- | ----------- | ------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Edit [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) untuk mengubah port di atas. | N/A |
| MCP Inspector | 3001 (Server); 5173 dan 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Edit [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) untuk mengubah port di atas. | N/A |

## Masukan

Jika Anda memiliki masukan atau saran untuk template ini, silakan buka issue di [AI Toolkit GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.