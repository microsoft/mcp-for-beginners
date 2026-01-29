## Pengujian dan Debugging

Sebelum mulai menguji server MCP Anda, penting untuk memahami alat yang tersedia dan praktik terbaik dalam debugging. Pengujian yang efektif memastikan server Anda berfungsi sesuai harapan dan membantu Anda dengan cepat mengidentifikasi serta menyelesaikan masalah. Bagian berikut menjelaskan pendekatan yang direkomendasikan untuk memvalidasi implementasi MCP Anda.

## Gambaran Umum

Pelajaran ini membahas cara memilih pendekatan pengujian yang tepat dan alat pengujian yang paling efektif.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan dapat:

- Menjelaskan berbagai pendekatan untuk pengujian.
- Menggunakan berbagai alat untuk menguji kode Anda secara efektif.

## Pengujian Server MCP

MCP menyediakan alat untuk membantu Anda menguji dan debugging server Anda:

- **MCP Inspector**: Alat baris perintah yang dapat dijalankan sebagai CLI maupun alat visual.
- **Pengujian manual**: Anda dapat menggunakan alat seperti curl untuk menjalankan permintaan web, tapi alat apa pun yang mampu menjalankan HTTP juga bisa digunakan.
- **Unit testing**: Anda bisa menggunakan framework pengujian favorit untuk menguji fitur baik di server maupun klien.

### Menggunakan MCP Inspector

Kami telah menjelaskan penggunaan alat ini di pelajaran sebelumnya, tapi mari kita bahas secara singkat. Ini adalah alat yang dibuat dengan Node.js dan Anda dapat menggunakannya dengan menjalankan executable `npx` yang akan mengunduh dan menginstal alat ini secara sementara, lalu membersihkan dirinya sendiri setelah selesai menjalankan permintaan Anda.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) membantu Anda untuk:

- **Menemukan Kapabilitas Server**: Mendeteksi secara otomatis sumber daya, alat, dan prompt yang tersedia
- **Mengujicoba Eksekusi Alat**: Mencoba parameter berbeda dan melihat respons secara real-time
- **Melihat Metadata Server**: Memeriksa info server, skema, dan konfigurasi

Contoh penggunaan alat ini adalah sebagai berikut:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Perintah di atas menjalankan MCP dan antarmuka visualnya serta membuka antarmuka web lokal di browser Anda. Anda akan melihat dashboard yang menampilkan server MCP yang terdaftar, alat, sumber daya, dan prompt yang tersedia. Antarmuka ini memungkinkan Anda menguji eksekusi alat secara interaktif, memeriksa metadata server, dan melihat respons secara real-time, sehingga memudahkan validasi dan debugging implementasi server MCP Anda.

Berikut tampilannya: ![Inspector](../../../../translated_images/id/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.png)

Anda juga bisa menjalankan alat ini dalam mode CLI dengan menambahkan atribut `--cli`. Berikut contoh menjalankan alat dalam mode "CLI" yang menampilkan semua alat di server:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Pengujian Manual

Selain menjalankan alat inspector untuk menguji kapabilitas server, pendekatan lain yang serupa adalah menjalankan klien yang mampu menggunakan HTTP, misalnya curl.

Dengan curl, Anda dapat menguji server MCP secara langsung menggunakan permintaan HTTP:

```bash
# Example: Test server metadata
curl http://localhost:3000/v1/metadata

# Example: Execute a tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Seperti yang terlihat dari contoh penggunaan curl di atas, Anda menggunakan permintaan POST untuk memanggil sebuah alat dengan payload yang berisi nama alat dan parameternya. Gunakan pendekatan yang paling sesuai untuk Anda. Alat CLI umumnya lebih cepat digunakan dan mudah untuk diotomasi, yang berguna dalam lingkungan CI/CD.

### Unit Testing

Buat unit test untuk alat dan sumber daya Anda agar memastikan semuanya berjalan sesuai harapan. Berikut contoh kode pengujian.

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

Kode di atas melakukan hal berikut:

- Memanfaatkan framework pytest yang memungkinkan Anda membuat tes sebagai fungsi dan menggunakan pernyataan assert.
- Membuat MCP Server dengan dua alat berbeda.
- Menggunakan pernyataan `assert` untuk memeriksa bahwa kondisi tertentu terpenuhi.

Lihat [file lengkapnya di sini](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Dengan file tersebut, Anda dapat menguji server Anda sendiri untuk memastikan kapabilitas dibuat sesuai yang diharapkan.

Semua SDK utama memiliki bagian pengujian serupa sehingga Anda dapat menyesuaikannya dengan runtime pilihan Anda.

## Contoh

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Sumber Daya Tambahan

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Selanjutnya

- Selanjutnya: [Deployment](../09-deployment/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.