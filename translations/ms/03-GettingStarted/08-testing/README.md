## Ujian dan Penyahpepijatan

Sebelum anda mula menguji pelayan MCP anda, adalah penting untuk memahami alat yang tersedia dan amalan terbaik untuk penyahpepijatan. Ujian yang berkesan memastikan pelayan anda berfungsi seperti yang dijangka dan membantu anda mengenal pasti serta menyelesaikan isu dengan cepat. Bahagian berikut menggariskan pendekatan yang disyorkan untuk mengesahkan pelaksanaan MCP anda.

## Gambaran Keseluruhan

Pelajaran ini merangkumi bagaimana memilih pendekatan ujian yang betul dan alat ujian yang paling berkesan.

## Objektif Pembelajaran

Menjelang akhir pelajaran ini, anda akan dapat:

- Menghuraikan pelbagai pendekatan untuk ujian.
- Menggunakan pelbagai alat untuk menguji kod anda dengan berkesan.


## Menguji Pelayan MCP

MCP menyediakan alat untuk membantu anda menguji dan menyahpepijat pelayan anda:

- **MCP Inspector**: Alat baris arahan yang boleh dijalankan sama ada sebagai alat CLI dan alat visual.
- **Ujian manual**: Anda boleh menggunakan alat seperti curl untuk menjalankan permintaan web, tetapi mana-mana alat yang mampu menjalankan HTTP boleh digunakan.
- **Ujian unit**: Adalah mungkin untuk menggunakan rangka kerja ujian kegemaran anda untuk menguji ciri pelayan dan pelanggan.

### Menggunakan MCP Inspector

Kami telah menerangkan penggunaan alat ini dalam pelajaran sebelum ini tetapi mari kita bincangkan sedikit pada peringkat tinggi. Ia adalah alat yang dibina dalam Node.js dan anda boleh menggunakannya dengan memanggil boleh-laksana `npx` yang akan memuat turun dan memasang alat itu secara sementara dan akan membersihkan dirinya sendiri setelah selesai menjalankan permintaan anda.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) membantu anda:

- **Menemui Kebolehan Pelayan**: Mengesan sumber, alat, dan arahan yang tersedia secara automatik
- **Ujian Pelaksanaan Alat**: Cuba parameter yang berbeza dan lihat respons dalam masa nyata
- **Lihat Metadata Pelayan**: Memeriksa maklumat pelayan, skema, dan konfigurasi

Sebuah contoh biasa pelaksanaan alat kelihatan seperti ini:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Perintah di atas memulakan MCP dan antara muka visualnya serta melancarkan antara muka web tempatan dalam penyemak imbas anda. Anda boleh menjangkakan melihat papan pemuka yang memaparkan pelayan MCP yang didaftarkan, alat, sumber, dan arahan yang tersedia. Antara muka membolehkan anda menguji pelaksanaan alat secara interaktif, memeriksa metadata pelayan, dan melihat respons masa nyata, menjadikan ia lebih mudah untuk mengesahkan dan menyahpepijat pelaksanaan pelayan MCP anda.

Ini adalah bagaimana ia boleh kelihatan: ![Inspector](../../../../translated_images/ms/connect.141db0b2bd05f096.webp)

Anda juga boleh menjalankan alat ini dalam mod CLI di mana anda menambah atribut `--cli`. Berikut adalah contoh menjalankan alat dalam mod "CLI" yang menyenaraikan semua alat pada pelayan:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Ujian Manual

Selain menjalankan alat inspector untuk menguji kebolehan pelayan, satu pendekatan serupa adalah menjalankan klien yang mampu menggunakan HTTP seperti contoh curl.

Dengan curl, anda boleh menguji pelayan MCP secara langsung menggunakan permintaan HTTP:

```bash
# Example: Test server metadata
curl http://localhost:3000/v1/metadata

# Example: Execute a tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Seperti yang anda lihat daripada penggunaan curl di atas, anda menggunakan permintaan POST untuk memanggil alat menggunakan beban muatan yang terdiri daripada nama alat dan parameternya. Gunakan pendekatan yang paling sesuai untuk anda. Alat CLI secara umumnya cenderung lebih pantas digunakan dan sesuai untuk diskripkan yang boleh berguna dalam persekitaran CI/CD.

### Ujian Unit

Cipta ujian unit untuk alat dan sumber anda untuk memastikan ia berfungsi seperti yang dijangka. Berikut adalah contoh kod ujian.

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

Kod di atas melakukan perkara berikut:

- Memanfaatkan rangka kerja pytest yang membolehkan anda mencipta ujian sebagai fungsi dan menggunakan pernyataan assert.
- Mencipta Pelayan MCP dengan dua alat yang berbeza.
- Menggunakan pernyataan `assert` untuk memeriksa bahawa syarat tertentu dipenuhi.

Lihat [fail penuh di sini](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Berdasarkan fail di atas, anda boleh menguji pelayan anda sendiri untuk memastikan kebolehan dicipta seperti yang sepatutnya.

Semua SDK utama mempunyai seksyen ujian yang serupa supaya anda boleh menyesuaikan dengan masa jalan pilihan anda.

## Contoh 

- [Kalkulator Java](../samples/java/calculator/README.md)
- [Kalkulator .NET](../../../../03-GettingStarted/samples/csharp)
- [Kalkulator JavaScript](../samples/javascript/README.md)
- [Kalkulator TypeScript](../samples/typescript/README.md)
- [Kalkulator Python](../../../../03-GettingStarted/samples/python) 

## Sumber Tambahan

- [SDK Python](https://github.com/modelcontextprotocol/python-sdk)

## Apa Seterusnya

- Seterusnya: [Penghantaran](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->