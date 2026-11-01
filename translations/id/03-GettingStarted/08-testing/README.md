## Pengujian dan Debugging

Sebelum Anda mulai menguji server MCP Anda, penting untuk memahami alat yang tersedia dan praktik terbaik untuk debugging. Pengujian yang efektif memastikan server Anda berperilaku sesuai harapan dan membantu Anda mengidentifikasi serta menyelesaikan masalah dengan cepat. Bagian berikut menguraikan pendekatan yang dianjurkan untuk memvalidasi implementasi MCP Anda.

## Ikhtisar

Pelajaran ini membahas cara memilih pendekatan pengujian yang tepat dan alat pengujian yang paling efektif.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Mendeskripsikan berbagai pendekatan untuk pengujian.
- Menggunakan berbagai alat untuk menguji kode Anda secara efektif.


## Menguji Server MCP

MCP menyediakan alat untuk membantu Anda menguji dan debugging server Anda:

- **MCP Inspector**: Alat baris perintah yang dapat dijalankan sebagai alat CLI maupun sebagai alat visual.
- **Pengujian manual**: Anda dapat menggunakan alat seperti curl untuk menjalankan permintaan web, tetapi alat apa pun yang dapat menjalankan HTTP juga bisa.
- **Pengujian unit**: Dimungkinkan menggunakan kerangka pengujian pilihan Anda untuk menguji fitur server dan klien.

### Menggunakan MCP Inspector

Kami telah menjelaskan penggunaan alat ini dalam pelajaran sebelumnya tetapi mari kita bahas sedikit secara garis besar. Ini adalah alat yang dibangun dengan Node.js dan Anda dapat menggunakannya dengan memanggil executable `npx` yang akan mengunduh dan memasang alat tersebut secara sementara dan membersihkan dirinya setelah menyelesaikan permintaan Anda.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) membantu Anda:

- **Menemukan Kemampuan Server**: Mendeteksi otomatis sumber daya, alat, dan prompt yang tersedia
- **Mengujicoba Eksekusi Alat**: Mencoba parameter yang berbeda dan melihat respons secara langsung
- **Melihat Metadata Server**: Memeriksa info server, skema, dan konfigurasi

Eksekusi alat secara tipikal terlihat seperti ini:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Perintah di atas memulai MCP dan antarmuka visualnya serta meluncurkan antarmuka web lokal di browser Anda. Anda dapat mengharapkan untuk melihat dashboard yang menampilkan server MCP terdaftar Anda, alat, sumber daya, dan prompt yang tersedia. Antarmuka ini memungkinkan Anda untuk menguji eksekusi alat secara interaktif, memeriksa metadata server, dan melihat respons secara realtime, sehingga memudahkan Anda memvalidasi dan debugging implementasi server MCP Anda.

Ini tampilannya: ![Inspector](../../../../translated_images/id/connect.141db0b2bd05f096.webp)

Anda juga dapat menjalankan alat ini dalam mode CLI dengan menambahkan atribut `--cli`. Berikut contoh menjalankan alat dalam mode "CLI" yang menampilkan semua alat di server:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Pengujian Manual

Selain menjalankan alat inspector untuk menguji kemampuan server, pendekatan lain yang serupa adalah menjalankan klien yang mampu menggunakan HTTP, misalnya curl.

Dengan curl, Anda dapat menguji server MCP secara langsung menggunakan permintaan HTTP:

```bash
# Example: Test server metadata
curl http://localhost:3000/v1/metadata

# Example: Execute a tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Seperti yang Anda lihat dari penggunaan curl di atas, Anda menggunakan permintaan POST untuk memanggil sebuah alat dengan muatan yang terdiri dari nama alat dan parameternya. Gunakan pendekatan yang paling sesuai dengan Anda. Alat CLI pada umumnya cenderung lebih cepat digunakan dan dapat diatur agar di-script yang bisa berguna dalam lingkungan CI/CD.

### Pengujian Unit

Buat pengujian unit untuk alat dan sumber daya Anda agar memastikan mereka bekerja sesuai harapan. Berikut adalah contoh kode pengujian.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Mark the whole module for async tests
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Create a couple of test tools
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Test without cursor parameter (omitted)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Test with cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Test with cursor as string
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Test with empty string cursor
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Kode sebelumnya melakukan hal berikut:

- Memanfaatkan kerangka pytest yang memungkinkan Anda membuat pengujian sebagai fungsi dan menggunakan pernyataan assert.
- Membuat Server MCP dengan dua alat berbeda.
- Menggunakan pernyataan `assert` untuk memeriksa bahwa kondisi tertentu terpenuhi.

Lihat [file lengkap di sini](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Dengan file di atas, Anda bisa menguji server Anda sendiri untuk memastikan kapabilitas dibuat seperti yang seharusnya.

Semua SDK utama memiliki bagian pengujian serupa sehingga Anda dapat menyesuaikan dengan runtime pilihan Anda.

## Contoh

- [Kalkulator Java](../samples/java/calculator/README.md)
- [Kalkulator .NET](../../../../03-GettingStarted/samples/csharp)
- [Kalkulator JavaScript](../samples/javascript/README.md)
- [Kalkulator TypeScript](../samples/typescript/README.md)
- [Kalkulator Python](../../../../03-GettingStarted/samples/python)

## Sumber Daya Tambahan

- [SDK Python](https://github.com/modelcontextprotocol/python-sdk)

## Apa Selanjutnya

- Selanjutnya: [Deploy](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->