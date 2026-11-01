# Pelayan MCP Cuaca

Ini adalah contoh Pelayan MCP dalam Python yang melaksanakan alat cuaca dengan respons tiruan. Ia boleh digunakan sebagai rangka untuk Pelayan MCP anda sendiri. Ia merangkumi ciri-ciri berikut:

- **Alat Cuaca**: Alat yang menyediakan maklumat cuaca tiruan berdasarkan lokasi yang diberikan.
- **Alat Klon Git**: Alat yang mengklon repositori git ke folder yang ditetapkan.
- **Alat Buka VS Code**: Alat yang membuka folder dalam VS Code atau VS Code Insiders.
- **Sambung ke Pembina Ejen**: Ciri yang membolehkan anda menyambungkan pelayan MCP ke Pembina Ejen untuk ujian dan penyahpepijatan.
- **Nyahpepijat dalam [Pemeriksa MCP](https://github.com/modelcontextprotocol/inspector)**: Ciri yang membolehkan anda nyahpepijat Pelayan MCP menggunakan Pemeriksa MCP.

## Mula dengan templat Pelayan MCP Cuaca

> **Prasyarat**
>
> Untuk menjalankan Pelayan MCP di mesin pembangunan tempatan anda, anda memerlukan:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Diperlukan untuk alat git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) atau [VS Code Insiders](https://code.visualstudio.com/insiders/) (Diperlukan untuk alat open_in_vscode)
> - (*Pilihan - jika anda lebih suka uv*) [uv](https://github.com/astral-sh/uv)
> - [Sambungan Nyahpepijat Python](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Sediakan persekitaran

Terdapat dua pendekatan untuk menyediakan persekitaran untuk projek ini. Anda boleh memilih mana-mana satu berdasarkan keutamaan anda.

> Nota: Muat semula VSCode atau terminal untuk memastikan python persekitaran maya digunakan selepas membuat persekitaran maya.

| Pendekatan | Langkah |
| -------- | ----- |
| Menggunakan `uv` | 1. Buat persekitaran maya: `uv venv` <br>2. Jalankan Perintah VSCode "***Python: Select Interpreter***" dan pilih python dari persekitaran maya yang dibuat <br>3. Pasang kebergantungan (termasuk kebergantungan pembangunan): `uv pip install -r pyproject.toml --extra dev` |
| Menggunakan `pip` | 1. Buat persekitaran maya: `python -m venv .venv` <br>2. Jalankan Perintah VSCode "***Python: Select Interpreter***" dan pilih python dari persekitaran maya yang dibuat<br>3. Pasang kebergantungan (termasuk kebergantungan pembangunan): `pip install -e .[dev]` | 

Selepas menyediakan persekitaran, anda boleh menjalankan pelayan di mesin pembangunan tempatan anda melalui Pembina Ejen sebagai Klien MCP untuk memulakan:
1. Buka panel Nyahpepijat VS Code. Pilih `Debug in Agent Builder` atau tekan `F5` untuk mula nyahpepijat pelayan MCP.
2. Dalam Microsoft Foundry Toolkit untuk Visual Studio Code Pembina Ejen, pilih penempatan Foundry aktif seperti `gpt-5.1`, kemudian masukkan: `What is the weather in Shanghai?` Pelayan akan disambungkan secara automatik.
3. Klik `Run` untuk menguji pelayan dengan arahan.

**Tahniah**! Anda telah berjaya menjalankan Pelayan MCP Cuaca di mesin pembangunan tempatan anda melalui Pembina Ejen sebagai Klien MCP.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Apa yang termasuk dalam templat

| Folder / Fail| Kandungan                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | Fail VSCode untuk nyahpepijat                   |
| `.aitk`      | Konfigurasi Microsoft Foundry Toolkit            |
| `src`        | Kod sumber untuk pelayan mcp cuaca               |

## Cara untuk nyahpepijat Pelayan MCP Cuaca

> Nota:
> - [Pemeriksa MCP](https://github.com/modelcontextprotocol/inspector) adalah alat visual pembangun untuk menguji dan nyahpepijat pelayan MCP.
> - Semua mod nyahpepijat menyokong titik henti, jadi anda boleh menambah titik henti pada kod pelaksanaan alat.

## Alat yang tersedia

### Alat Cuaca
Alat `get_weather` menyediakan maklumat cuaca tiruan untuk lokasi tertentu.

| Parameter | Jenis | Penerangan |
| --------- | ---- | ----------- |
| `location` | string | Lokasi untuk mendapatkan cuaca (contohnya, nama bandar, negeri, atau koordinat) |

### Alat Klon Git
Alat `git_clone_repo` mengklon repositori git ke folder yang ditentukan.

| Parameter | Jenis | Penerangan |
| --------- | ---- | ----------- |
| `repo_url` | string | URL repositori git untuk diklon |
| `target_folder` | string | Laluan ke folder di mana repositori hendak diklon |

Alat ini mengembalikan objek JSON dengan:
- `success`: Boolean yang menunjukkan jika operasi berjaya
- `target_folder` atau `error`: Laluan repositori yang diklon atau mesej ralat

### Alat Buka VS Code
Alat `open_in_vscode` membuka folder dalam aplikasi VS Code atau VS Code Insiders.

| Parameter | Jenis | Penerangan |
| --------- | ---- | ----------- |
| `folder_path` | string | Laluan ke folder yang hendak dibuka |
| `use_insiders` | boolean (pilihan) | Sama ada menggunakan VS Code Insiders berbanding VS Code biasa |

Alat ini mengembalikan objek JSON dengan:
- `success`: Boolean yang menunjukkan jika operasi berjaya
- `message` atau `error`: Mesej pengesahan atau mesej ralat

| Mod Nyahpepijat | Penerangan | Langkah untuk nyahpepijat |
| ---------- | ----------- | --------------- |
| Pembina Ejen | Nyahpepijat pelayan MCP dalam Pembina Ejen melalui Microsoft Foundry Toolkit untuk Visual Studio Code. | 1. Buka panel Nyahpepijat VS Code. Pilih `Debug in Agent Builder` dan tekan `F5` untuk mula nyahpepijat pelayan MCP.<br>2. Pilih penempatan Foundry aktif seperti `gpt-5.1`, kemudian masukkan `What is the weather in Shanghai?`. Pelayan akan disambungkan secara automatik.<br>3. Klik `Run` untuk menguji pelayan dengan arahan. |
| Pemeriksa MCP | Nyahpepijat pelayan MCP menggunakan Pemeriksa MCP. | 1. Pasang [Node.js](https://nodejs.org/)<br> 2. Sediakan Pemeriksa: `cd inspector` && `npm install` <br> 3. Buka panel Nyahpepijat VS Code. Pilih `Debug SSE in Inspector (Edge)` atau `Debug SSE in Inspector (Chrome)`. Tekan F5 untuk mula nyahpepijat.<br> 4. Apabila Pemeriksa MCP dilancarkan dalam pelayar, klik butang `Connect` untuk menyambungkan pelayan MCP ini.<br> 5. Kemudian anda boleh `List Tools`, pilih alat, masukkan parameter, dan `Run Tool` untuk nyahpepijat kod pelayan anda.<br> |

## Pelabuhan lalai dan pengubahsuaian

| Mod Nyahpepijat | Pelabuhan | Definisi | Pengubahsuaian | Nota |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Pembina Ejen | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Edit [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) untuk menukar pelabuhan di atas. | N/A |
| Pemeriksa MCP | 3001 (Pelayan); 5173 dan 3000 (Pemeriksa) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Edit [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) untuk menukar pelabuhan di atas.| N/A |

## Maklum balas

Jika anda mempunyai sebarang maklum balas atau cadangan untuk templat ini, sila buka isu di [Repositori Microsoft Foundry Toolkit untuk Visual Studio Code GitHub](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->