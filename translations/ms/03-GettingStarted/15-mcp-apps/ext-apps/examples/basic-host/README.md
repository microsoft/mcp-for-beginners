# Contoh: Host Asas

Satu pelaksanaan rujukan yang menunjukkan cara membina aplikasi hos MCP yang menyambung ke pelayan MCP dan memaparkan UI alat dalam sandbox yang selamat.

Host asas ini juga boleh digunakan untuk menguji Aplikasi MCP semasa pembangunan tempatan.

## Fail Utama

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - Hos UI React dengan pemilihan alat, input parameter, dan pengurusan iframe
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Proksi iframe luar dengan pengesahan keselamatan dan perantara mesej dua hala
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Logik teras: sambungan pelayan, panggilan alat, dan penyediaan AppBridge

## Mula

```bash
npm install
npm run start
# Buka http://localhost:8080
```

Secara lalai, aplikasi hos akan cuba menyambung ke pelayan MCP di `http://localhost:3001/mcp`. Anda boleh mengkonfigurasi tingkah laku ini dengan menetapkan pembolehubah persekitaran `SERVERS` dengan tatasusunan JSON URL pelayan:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Seni Bina

Contoh ini menggunakan corak sandbox dwi-iframe untuk pengasingan UI yang selamat:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Mengapa dua iframe?**

- Iframe luar berjalan pada asal yang berbeza (port 8081) menghalang akses langsung ke hos
- Iframe dalam menerima HTML melalui `srcdoc` dan dihadkan oleh atribut sandbox
- Mesej mengalir melalui iframe luar yang mengesah dan meneruskannya secara dua hala

Seni bina ini memastikan bahawa walaupun kod UI alat berniat jahat, ia tidak boleh mengakses DOM aplikasi hos, kuki, atau konteks JavaScript.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Bagi maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->