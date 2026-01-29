# Weather MCP Server

Ini adalah contoh MCP Server dalam Python yang melaksanakan alat cuaca dengan respons tiruan. Ia boleh digunakan sebagai rangka untuk MCP Server anda sendiri. Ia merangkumi ciri-ciri berikut:

- **Weather Tool**: Alat yang menyediakan maklumat cuaca tiruan berdasarkan lokasi yang diberikan.
- **Sambung ke Agent Builder**: Ciri yang membolehkan anda menyambungkan MCP server ke Agent Builder untuk ujian dan penyahpepijatan.
- **Debug dalam [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Ciri yang membolehkan anda menyahpepijat MCP Server menggunakan MCP Inspector.

## Mula dengan templat Weather MCP Server

> **Prasyarat**
>
> Untuk menjalankan MCP Server di mesin pembangunan tempatan anda, anda memerlukan:
>
> - [Python](https://www.python.org/)
> - (*Pilihan - jika anda lebih suka uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Sediakan persekitaran

Terdapat dua pendekatan untuk menyediakan persekitaran bagi projek ini. Anda boleh memilih salah satu mengikut kesukaan anda.

> Nota: Muat semula VSCode atau terminal untuk memastikan python persekitaran maya digunakan selepas mencipta persekitaran maya.

| Pendekatan | Langkah |
| -------- | ----- |
| Menggunakan `uv` | 1. Cipta persekitaran maya: `uv venv` <br>2. Jalankan Perintah VSCode "***Python: Select Interpreter***" dan pilih python dari persekitaran maya yang dicipta <br>3. Pasang kebergantungan (termasuk kebergantungan pembangunan): `uv pip install -r pyproject.toml --extra dev` |
| Menggunakan `pip` | 1. Cipta persekitaran maya: `python -m venv .venv` <br>2. Jalankan Perintah VSCode "***Python: Select Interpreter***" dan pilih python dari persekitaran maya yang dicipta<br>3. Pasang kebergantungan (termasuk kebergantungan pembangunan): `pip install -e .[dev]` |

Selepas menyediakan persekitaran, anda boleh menjalankan server di mesin pembangunan tempatan anda melalui Agent Builder sebagai MCP Client untuk memulakan:
1. Buka panel Debug VS Code. Pilih `Debug in Agent Builder` atau tekan `F5` untuk mula menyahpepijat MCP server.
2. Gunakan AI Toolkit Agent Builder untuk menguji server dengan [prompt ini](../../../../../../../../../../open_prompt_builder). Server akan disambungkan secara automatik ke Agent Builder.
3. Klik `Run` untuk menguji server dengan prompt tersebut.

**Tahniah**! Anda telah berjaya menjalankan Weather MCP Server di mesin pembangunan tempatan anda melalui Agent Builder sebagai MCP Client.  
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Apa yang termasuk dalam templat

| Folder / Fail | Kandungan                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | Fail VSCode untuk penyahpepijatan            |
| `.aitk`      | Konfigurasi untuk AI Toolkit                  |
| `src`        | Kod sumber untuk weather mcp server           |

## Cara menyahpepijat Weather MCP Server

> Nota:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) adalah alat visual untuk pembangun bagi menguji dan menyahpepijat MCP server.
> - Semua mod penyahpepijatan menyokong titik henti, jadi anda boleh menambah titik henti pada kod pelaksanaan alat.

| Mod Penyahpepijatan | Penerangan | Langkah untuk menyahpepijat |
| ---------- | ----------- | --------------- |
| Agent Builder | Menyahpepijat MCP server dalam Agent Builder melalui AI Toolkit. | 1. Buka panel Debug VS Code. Pilih `Debug in Agent Builder` dan tekan `F5` untuk mula menyahpepijat MCP server.<br>2. Gunakan AI Toolkit Agent Builder untuk menguji server dengan [prompt ini](../../../../../../../../../../open_prompt_builder). Server akan disambungkan secara automatik ke Agent Builder.<br>3. Klik `Run` untuk menguji server dengan prompt tersebut. |
| MCP Inspector | Menyahpepijat MCP server menggunakan MCP Inspector. | 1. Pasang [Node.js](https://nodejs.org/)<br> 2. Sediakan Inspector: `cd inspector` && `npm install` <br> 3. Buka panel Debug VS Code. Pilih `Debug SSE in Inspector (Edge)` atau `Debug SSE in Inspector (Chrome)`. Tekan F5 untuk mula menyahpepijat.<br> 4. Apabila MCP Inspector dilancarkan dalam pelayar, klik butang `Connect` untuk menyambungkan MCP server ini.<br> 5. Kemudian anda boleh `List Tools`, pilih alat, masukkan parameter, dan `Run Tool` untuk menyahpepijat kod server anda.<br> |

## Port Lalai dan pengubahsuaian

| Mod Penyahpepijatan | Port | Definisi | Pengubahsuaian | Nota |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Edit [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) untuk menukar port di atas. | N/A |
| MCP Inspector | 3001 (Server); 5173 dan 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Edit [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) untuk menukar port di atas.| N/A |

## Maklum balas

Jika anda mempunyai sebarang maklum balas atau cadangan untuk templat ini, sila buka isu di [repositori AI Toolkit GitHub](https://github.com/microsoft/vscode-ai-toolkit/issues)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.