## Ujian dan Penjejakan Ralat

Sebelum anda mula menguji pelayan MCP anda, adalah penting untuk memahami alat yang tersedia dan amalan terbaik untuk penjejakan ralat. Ujian yang berkesan memastikan pelayan anda berfungsi seperti yang diharapkan dan membantu anda mengenal pasti serta menyelesaikan masalah dengan cepat. Bahagian berikut menggariskan pendekatan yang disyorkan untuk mengesahkan pelaksanaan MCP anda.

## Gambaran Keseluruhan

Pelajaran ini merangkumi cara memilih pendekatan ujian yang sesuai dan alat ujian yang paling berkesan.

## Objektif Pembelajaran

Menjelang akhir pelajaran ini, anda akan dapat:

- Menerangkan pelbagai pendekatan untuk ujian.
- Menggunakan pelbagai alat untuk menguji kod anda dengan berkesan.

## Ujian Pelayan MCP

MCP menyediakan alat untuk membantu anda menguji dan menjejaki ralat pelayan anda:

- **Pemeriksa MCP**: Alat baris arahan yang boleh dijalankan sebagai alat CLI dan juga sebagai alat visual.
- **Ujian manual**: Anda boleh menggunakan alat seperti curl untuk menjalankan permintaan web, tetapi mana-mana alat yang boleh menjalankan HTTP juga boleh digunakan.
- **Ujian unit**: Anda boleh menggunakan rangka kerja ujian pilihan anda untuk menguji ciri-ciri pelayan dan klien.

### Menggunakan Pemeriksa MCP

Kami telah menerangkan penggunaan alat ini dalam pelajaran sebelum ini tetapi mari kita bincangkan sedikit pada tahap tinggi. Ia adalah alat yang dibina dalam Node.js dan anda boleh menggunakannya dengan memanggil boleh laku `npx` yang akan memuat turun dan memasang alat itu buat sementara waktu dan akan membersihkan dirinya sendiri apabila selesai menjalankan permintaan anda.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) membantu anda:

- **Mengesan Keupayaan Pelayan**: Mengesan sumber, alat, dan arahan yang tersedia secara automatik
- **Uji Pelaksanaan Alat**: Cuba parameter berlainan dan lihat respons secara masa nyata
- **Lihat Metadata Pelayan**: Periksa maklumat pelayan, skema, dan konfigurasi

Larian tipikal alat ini kelihatan seperti berikut:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Arahan di atas memulakan MC dan antara muka visualnya serta melancarkan antara muka web tempatan dalam pelayar anda. Anda boleh menjangkakan untuk melihat papan pemuka yang memaparkan pelayan MCP yang didaftarkan, alat, sumber, dan arahan mereka yang tersedia. Antaramuka membolehkan anda menguji pelaksanaan alat secara interaktif, memeriksa metadata pelayan, dan melihat respons masa nyata, menjadikannya lebih mudah untuk mengesahkan dan menjejaki ralat pelaksanaan server MCP anda.

Ini adalah bagaimana ia boleh kelihatan: ![Inspector](../../../../translated_images/ms/connect.141db0b2bd05f096.webp)

Anda juga boleh menjalankan alat ini dalam mod CLI di mana anda menambah atribut `--cli`. Berikut adalah contoh menjalankan alat dalam mod "CLI" yang menyenaraikan semua alat pada pelayan:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Ujian Manual

Selain menjalankan alat pemeriksa untuk menguji keupayaan pelayan, pendekatan serupa lain adalah menjalankan klien yang boleh menggunakan HTTP seperti contoh curl.

Dengan curl, anda boleh menguji pelayan MCP secara langsung menggunakan permintaan HTTP:

```bash
# Contoh: Metadata pelayan ujian
curl http://localhost:3000/v1/metadata

# Contoh: Jalankan alat
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Seperti yang anda lihat daripada penggunaan curl di atas, anda menggunakan permintaan POST untuk memanggil alat menggunakan beban data yang terdiri daripada nama alat dan parameternya. Gunakan pendekatan yang paling sesuai dengan anda. Alat CLI secara umum cenderung lebih pantas digunakan dan memudahkan untuk diskriptkan yang boleh berguna dalam persekitaran CI/CD.

### Ujian Unit

Cipta ujian unit untuk alat dan sumber anda untuk memastikan mereka berfungsi seperti yang diharapkan. Berikut adalah sebahagian contoh kod ujian.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Tandakan seluruh modul untuk ujian async
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Cipta beberapa alat ujian
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Uji tanpa parameter kursor (dilangkau)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Uji dengan kursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Uji dengan kursor sebagai string
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Uji dengan kursor string kosong
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

Kod di atas melakukan perkara berikut:

- Menggunakan rangka kerja pytest yang membolehkan anda mencipta ujian sebagai fungsi dan menggunakan pernyataan assert.
- Mencipta Pelayan MCP dengan dua alat yang berbeza.
- Menggunakan pernyataan `assert` untuk memeriksa bahawa keadaan tertentu dipenuhi.

Lihat fail penuh di [sini](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Berdasarkan fail di atas, anda boleh menguji pelayan anda sendiri untuk memastikan keupayaan dicipta seperti sepatutnya.

Semua SDK utama mempunyai bahagian ujian yang serupa supaya anda boleh sesuaikan dengan runtime pilihan anda.

## Contoh

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Sumber Tambahan

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Apa Seterusnya

- Seterusnya: [Deployment](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk tepat, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi ralat atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->