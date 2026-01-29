# Server MCP Cuaca

Ini adalah contoh Server MCP dalam Python yang mengimplementasikan alat cuaca dengan respons tiruan. Server ini dapat digunakan sebagai kerangka untuk Server MCP Anda sendiri. Fitur yang disertakan adalah:

- **Alat Cuaca**: Alat yang menyediakan informasi cuaca tiruan berdasarkan lokasi yang diberikan.
- **Alat Clone Git**: Alat yang mengkloning repositori git ke folder yang ditentukan.
- **Alat Buka VS Code**: Alat yang membuka folder di VS Code atau VS Code Insiders.
- **Terhubung ke Agent Builder**: Fitur yang memungkinkan Anda menghubungkan server MCP ke Agent Builder untuk pengujian dan debugging.
- **Debug di [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Fitur yang memungkinkan Anda melakukan debugging Server MCP menggunakan MCP Inspector.

## Memulai dengan template Server MCP Cuaca

> **Prasyarat**
>
> Untuk menjalankan Server MCP di mesin pengembangan lokal Anda, Anda memerlukan:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Diperlukan untuk alat git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) atau [VS Code Insiders](https://code.visualstudio.com/insiders/) (Diperlukan untuk alat open_in_vscode)
> - (*Opsional - jika Anda lebih suka uv*) [uv](https://github.com/astral-sh/uv)
> - [Ekstensi Debugger Python](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Persiapkan lingkungan

Ada dua pendekatan untuk menyiapkan lingkungan proyek ini. Anda dapat memilih salah satu berdasarkan preferensi Anda.

> Catatan: Muat ulang VSCode atau terminal untuk memastikan Python dari lingkungan virtual digunakan setelah membuat lingkungan virtual.

| Pendekatan | Langkah |
| ---------- | ------- |
| Menggunakan `uv` | 1. Buat lingkungan virtual: `uv venv` <br>2. Jalankan Perintah VSCode "***Python: Select Interpreter***" dan pilih Python dari lingkungan virtual yang dibuat <br>3. Instal dependensi (termasuk dependensi pengembangan): `uv pip install -r pyproject.toml --extra dev` |
| Menggunakan `pip` | 1. Buat lingkungan virtual: `python -m venv .venv` <br>2. Jalankan Perintah VSCode "***Python: Select Interpreter***" dan pilih Python dari lingkungan virtual yang dibuat<br>3. Instal dependensi (termasuk dependensi pengembangan): `pip install -e .[dev]` | 

Setelah menyiapkan lingkungan, Anda dapat menjalankan server di mesin pengembangan lokal Anda melalui Agent Builder sebagai MCP Client untuk memulai:
1. Buka panel Debug VS Code. Pilih `Debug in Agent Builder` atau tekan `F5` untuk memulai debugging server MCP.
2. Gunakan AI Toolkit Agent Builder untuk menguji server dengan [prompt ini](../../../../../../../../../../../open_prompt_builder). Server akan terhubung secara otomatis ke Agent Builder.
3. Klik `Run` untuk menguji server dengan prompt.

**Selamat**! Anda telah berhasil menjalankan Server MCP Cuaca di mesin pengembangan lokal Anda melalui Agent Builder sebagai MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Apa yang termasuk dalam template

| Folder / File | Isi                                         |
| ------------- | ------------------------------------------ |
| `.vscode`     | File VSCode untuk debugging                |
| `.aitk`       | Konfigurasi untuk AI Toolkit               |
| `src`         | Kode sumber untuk server MCP cuaca         |

## Cara debugging Server MCP Cuaca

> Catatan:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) adalah alat pengembang visual untuk pengujian dan debugging server MCP.
> - Semua mode debugging mendukung breakpoint, sehingga Anda dapat menambahkan breakpoint ke kode implementasi alat.

## Alat yang Tersedia

### Alat Cuaca
Alat `get_weather` menyediakan informasi cuaca tiruan untuk lokasi tertentu.

| Parameter  | Tipe   | Deskripsi                                   |
| ---------- | ------ | ------------------------------------------- |
| `location` | string | Lokasi untuk mendapatkan informasi cuaca (misalnya, nama kota, negara bagian, atau koordinat) |

### Alat Clone Git
Alat `git_clone_repo` mengkloning repositori git ke folder yang ditentukan.

| Parameter       | Tipe   | Deskripsi                                         |
| --------------- | ------ | ------------------------------------------------- |
| `repo_url`      | string | URL repositori git yang akan dikloning            |
| `target_folder` | string | Path ke folder tempat repositori akan dikloning   |

Alat ini mengembalikan objek JSON dengan:
- `success`: Boolean yang menunjukkan apakah operasi berhasil
- `target_folder` atau `error`: Path repositori yang dikloning atau pesan error

### Alat Buka VS Code
Alat `open_in_vscode` membuka folder di aplikasi VS Code atau VS Code Insiders.

| Parameter      | Tipe   | Deskripsi                                         |
| -------------- | ------ | ------------------------------------------------- |
| `folder_path`  | string | Path ke folder yang akan dibuka                   |
| `use_insiders` | boolean (opsional) | Apakah menggunakan VS Code Insiders daripada VS Code biasa |

Alat ini mengembalikan objek JSON dengan:
- `success`: Boolean yang menunjukkan apakah operasi berhasil
- `message` atau `error`: Pesan konfirmasi atau pesan error

| Mode Debug | Deskripsi | Langkah untuk debugging |
| ---------- | --------- | ----------------------- |
| Agent Builder | Debug server MCP di Agent Builder melalui AI Toolkit. | 1. Buka panel Debug VS Code. Pilih `Debug in Agent Builder` dan tekan `F5` untuk memulai debugging server MCP.<br>2. Gunakan AI Toolkit Agent Builder untuk menguji server dengan [prompt ini](../../../../../../../../../../../open_prompt_builder). Server akan terhubung secara otomatis ke Agent Builder.<br>3. Klik `Run` untuk menguji server dengan prompt. |
| MCP Inspector | Debug server MCP menggunakan MCP Inspector. | 1. Instal [Node.js](https://nodejs.org/)<br> 2. Siapkan Inspector: `cd inspector` && `npm install` <br> 3. Buka panel Debug VS Code. Pilih `Debug SSE in Inspector (Edge)` atau `Debug SSE in Inspector (Chrome)`. Tekan F5 untuk memulai debugging.<br> 4. Ketika MCP Inspector diluncurkan di browser, klik tombol `Connect` untuk menghubungkan server MCP ini.<br> 5. Kemudian Anda dapat `List Tools`, memilih alat, memasukkan parameter, dan `Run Tool` untuk debugging kode server Anda.<br> |

## Port Default dan Kustomisasi

| Mode Debug     | Port  | Definisi                          | Kustomisasi                          | Catatan       |
| -------------- | ----- | --------------------------------- | ------------------------------------ |-------------- |
| Agent Builder  | 3001  | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Edit [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) untuk mengubah port di atas. | N/A |
| MCP Inspector  | 3001 (Server); 5173 dan 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Edit [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) untuk mengubah port di atas.| N/A |

## Umpan Balik

Jika Anda memiliki umpan balik atau saran untuk template ini, silakan buka masalah di [repositori GitHub AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.