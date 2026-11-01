# Pelayan MCP Cuaca

Ini ialah contoh Pelayan MCP dalam Python yang melaksanakan alat cuaca dengan tindak balas tiruan. Ia boleh digunakan sebagai rangka kerja untuk Pelayan MCP anda sendiri. Ia merangkumi ciri-ciri berikut:

- **Alat Cuaca**: Alat yang menyediakan maklumat cuaca tiruan berdasarkan lokasi yang diberikan.
- **Sambung ke Pembina Ejen**: Ciri yang membolehkan anda menyambungkan pelayan MCP ke Pembina Ejen untuk ujian dan penyahpepijatan.
- **Penyahpepijatan dalam [Pemeriksa MCP](https://github.com/modelcontextprotocol/inspector)**: Ciri yang membolehkan anda menyahpepijat Pelayan MCP menggunakan Pemeriksa MCP.

## Mulakan dengan templat Pelayan MCP Cuaca

> **Keperluan Prasyarat**
>
> Untuk menjalankan Pelayan MCP di mesin pembangunan tempatan anda, anda memerlukan:
>
> - [Python](https://www.python.org/)
> - (*Pilihan - jika anda memilih uv*) [uv](https://github.com/astral-sh/uv)
> - [Sambungan Penyahpepijat Python](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Sediakan persekitaran

Terdapat dua pendekatan untuk menyediakan persekitaran bagi projek ini. Anda boleh memilih salah satu berdasarkan pilihan anda.

> Nota: Muat semula VSCode atau terminal untuk memastikan python persekitaran maya digunakan selepas mencipta persekitaran maya.

| Pendekatan | Langkah |
| -------- | ----- |
| Menggunakan `uv` | 1. Cipta persekitaran maya: `uv venv` <br>2. Jalankan Perintah VSCode "***Python: Select Interpreter***" dan pilih python daripada persekitaran maya yang dicipta <br>3. Pasang kebergantungan (termasuk kebergantungan pembangunan): `uv pip install -r pyproject.toml --extra dev` |
| Menggunakan `pip` | 1. Cipta persekitaran maya: `python -m venv .venv` <br>2. Jalankan Perintah VSCode "***Python: Select Interpreter***" dan pilih python daripada persekitaran maya yang dicipta<br>3. Pasang kebergantungan (termasuk kebergantungan pembangunan): `pip install -e .[dev]` |

Selepas menyediakan persekitaran, anda boleh menjalankan pelayan di mesin pembangunan tempatan anda melalui Pembina Ejen sebagai Klien MCP untuk memulakan:
1. Buka panel Penyahpepijatan VS Code. Pilih `Debug in Agent Builder` atau tekan `F5` untuk mula menyahpepijat pelayan MCP.
2. Dalam Pembina Ejen Alat Microsoft Foundry, pilih penempatan Foundry yang aktif seperti `gpt-5.1`, kemudian masukkan: `What is the weather in Shanghai?` Pelayan akan disambungkan secara automatik.
3. Klik `Run` untuk menguji pelayan dengan arahan.

**Tahniah**! Anda telah berjaya menjalankan Pelayan MCP Cuaca di mesin pembangunan tempatan anda melalui Pembina Ejen sebagai Klien MCP.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Apa yang disertakan dalam templat

| Folder / Fail | Kandungan                                  |
| ------------ | ----------------------------------------- |
| `.vscode`    | Fail VSCode untuk penyahpepijatan          |
| `.aitk`      | Konfigurasi untuk Microsoft Foundry Toolkit               |
| `src`        | Kod sumber untuk pelayan mcp cuaca            |

## Cara menyahpepijat Pelayan MCP Cuaca

> Nota:
> - [Pemeriksa MCP](https://github.com/modelcontextprotocol/inspector) adalah alat pembangun visual untuk ujian dan penyahpepijatan pelayan MCP.
> - Semua mod penyahpepijatan menyokong titik henti, jadi anda boleh menambah titik henti pada kod pelaksanaan alat.

| Mod Penyahpepijatan | Penerangan | Langkah penyahpepijatan |
| ------------------ | ---------- | ------------------------- |
| Pembina Ejen | Nyahpepijat pelayan MCP dalam Pembina Ejen melalui Microsoft Foundry Toolkit. | 1. Buka panel Penyahpepijatan VS Code. Pilih `Debug in Agent Builder` dan tekan `F5` untuk mula menyahpepijat pelayan MCP.<br>2. Pilih penempatan Foundry yang aktif seperti `gpt-5.1`, kemudian masukkan `What is the weather in Shanghai?`. Pelayan akan disambungkan secara automatik.<br>3. Klik `Run` untuk menguji pelayan dengan arahan. |
| Pemeriksa MCP | Nyahpepijat pelayan MCP menggunakan Pemeriksa MCP. | 1. Pasang [Node.js](https://nodejs.org/)<br> 2. Sediakan Pemeriksa: `cd inspector` && `npm install` <br> 3. Buka panel Penyahpepijatan VS Code. Pilih `Debug SSE in Inspector (Edge)` atau `Debug SSE in Inspector (Chrome)`. Tekan F5 untuk mula menyahpepijat.<br> 4. Apabila Pemeriksa MCP dilancarkan dalam pelayar, klik butang `Connect` untuk menyambung pelayan MCP ini.<br> 5. Kemudian anda boleh `List Tools`, pilih alat, masukkan parameter, dan `Run Tool` untuk menyahpepijat kod pelayan anda.<br> |

## Port Lalai dan pengubahsuaian

| Mod Penyahpepijatan | Port | Definisi | Pengubahsuaian | Nota |
| ------------------ | ---- | -------- | ------------- | -----|
| Pembina Ejen | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Edit [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) untuk menukar port di atas. | Tiada |
| Pemeriksa MCP | 3001 (Pelayan); 5173 dan 3000 (Pemeriksa) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Edit [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) untuk menukar port di atas.| Tiada |

## Maklum balas

Jika anda mempunyai sebarang maklum balas atau cadangan untuk templat ini, sila buka isu di [Repositori Microsoft Foundry Toolkit GitHub](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->