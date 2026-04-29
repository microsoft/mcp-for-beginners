## Ujian dan Pengaturcaraan

Sebelum anda mula menguji pelayan MCP anda, adalah penting untuk memahami alat yang tersedia dan amalan terbaik untuk pengaturcaraan. Ujian yang berkesan memastikan pelayan anda berfungsi seperti yang diharapkan dan membantu anda mengenal pasti serta menyelesaikan isu dengan cepat. Bahagian berikut menggariskan pendekatan yang disyorkan untuk mengesahkan pelaksanaan MCP anda.

## Gambaran Keseluruhan

Pengajaran ini merangkumi bagaimana memilih pendekatan ujian yang tepat dan alat ujian yang paling berkesan.

## Objektif Pembelajaran

Menjelang akhir pengajaran ini, anda akan dapat:

- Menerangkan pelbagai pendekatan untuk ujian.
- Menggunakan pelbagai alat untuk menguji kod anda dengan berkesan.

## Ujian Pelayan MCP

MCP menyediakan alat untuk membantu anda menguji dan mengatur cara pelayan anda:

- **MCP Inspector**: Alat baris perintah yang boleh dijalankan sebagai alat CLI dan juga sebagai alat visual.
- **Ujian manual**: Anda boleh menggunakan alat seperti curl untuk menjalankan permintaan web, tetapi mana-mana alat yang mampu menjalankan HTTP juga boleh digunakan.
- **Ujian unit**: Adalah mungkin menggunakan rangka kerja ujian pilihan anda untuk menguji ciri pelayan dan pelanggan.

### Menggunakan MCP Inspector

Kami telah menerangkan penggunaan alat ini dalam pengajaran sebelum ini tetapi mari kita bincangkan sedikit secara keseluruhan. Ia adalah alat yang dibina dalam Node.js dan anda boleh menggunakannya dengan memanggil program `npx` yang akan memuat turun dan memasang alat tersebut secara sementara dan akan membersihkan diri selepas selesai menjalankan permintaan anda.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) membantu anda:

- **Menemui Keupayaan Pelayan**: Mengenal pasti sumber, alat, dan arahan yang tersedia secara automatik
- **Uji Pelaksanaan Alat**: Cuba pelbagai parameter dan lihat respons secara langsung
- **Lihat Metadata Pelayan**: Meneliti maklumat pelayan, skema, dan konfigurasi

Contoh biasa menjalankan alat tersebut adalah seperti berikut:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

Arahan di atas memulakan MCP dan antara muka visualnya serta melancarkan antara muka web tempatan dalam pelayar anda. Anda boleh menjangkakan untuk melihat papan pemuka yang memaparkan pelayan MCP yang didaftarkan, alat, sumber, dan arahan yang tersedia. Antara muka ini membolehkan anda menguji pelaksanaan alat secara interaktif, memeriksa metadata pelayan, dan melihat respons masa sebenar, menjadikannya lebih mudah untuk mengesahkan dan mengatur cara pelaksanaan pelayan MCP anda.

Inilah bagaimana rupanya: ![Inspector](../../../../translated_images/ms/connect.141db0b2bd05f096.webp)

Anda juga boleh menjalankan alat ini dalam mod CLI di mana anda menambah atribut `--cli`. Berikut adalah contoh menjalankan alat dalam mod "CLI" yang menyenaraikan semua alat di pelayan:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### Ujian Manual

Selain menjalankan alat pemeriksa untuk menguji keupayaan pelayan, pendekatan serupa lain ialah menjalankan pelanggan yang mampu menggunakan HTTP seperti contohnya curl.

Dengan curl, anda boleh menguji pelayan MCP terus menggunakan permintaan HTTP:

```bash
# Contoh: Metadata pelayan ujian
curl http://localhost:3000/v1/metadata

# Contoh: Jalankan alat
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

Seperti yang anda lihat daripada penggunaan curl di atas, anda menggunakan permintaan POST untuk memanggil alat menggunakan muatan yang terdiri daripada nama alat dan parameternya. Gunakan pendekatan yang paling sesuai dengan anda. Alat CLI secara amnya lebih cepat digunakan dan sesuai untuk dijadikan skrip, yang berguna dalam persekitaran CI/CD.

### Ujian Unit

Cipta ujian unit untuk alat dan sumber anda bagi memastikan mereka berfungsi seperti yang dijangkakan. Berikut adalah contoh kod ujian.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Tandakan keseluruhan modul untuk ujian async
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
        # Uji tanpa parameter kursor (dihilangkan)
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
- Menggunakan pernyataan `assert` untuk memeriksa bahawa syarat tertentu dipenuhi.

Lihat [fail penuh di sini](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

Berdasarkan fail di atas, anda boleh menguji pelayan anda sendiri untuk memastikan keupayaan dicipta seperti sepatutnya.

Semua SDK utama mempunyai bahagian ujian yang serupa jadi anda boleh menyesuaikan mengikut runtime pilihan anda.

## Contoh

- [Kalkulator Java](../samples/java/calculator/README.md)
- [Kalkulator .Net](../../../../03-GettingStarted/samples/csharp)
- [Kalkulator JavaScript](../samples/javascript/README.md)
- [Kalkulator TypeScript](../samples/typescript/README.md)
- [Kalkulator Python](../../../../03-GettingStarted/samples/python)

## Sumber Tambahan

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Apa Seterusnya

- Seterusnya: [Penghantaran](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber utama. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->