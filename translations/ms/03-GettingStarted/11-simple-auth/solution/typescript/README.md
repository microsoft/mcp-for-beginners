# Jalankan contoh

## Pasang kebergantungan

```sh
npm install
```

## Bina

```sh
npm run build
```

## Hasilkan token

```sh
npm run generate
```

Ini akan mencipta token dalam fail *.env*. Klien akan membaca dari fail ini.

## Jalankan kod

Mulakan pelayan dengan:

```sh
npm start
```

Jalankan klien, dalam terminal yang berasingan dengan:

```sh
npm run client
```

Dalam terminal pelayan, anda sepatutnya melihat output yang serupa dengan:

```text
User exists
User has required scopes
Middleware executed
```

dan dari terminal klien, anda sepatutnya melihat output yang serupa dengan:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Mengubah sesuatu

Mari pastikan kita memahami skop. Cari fail *server.ts* dan kod ini:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

Ini menunjukkan token yang diberikan perlu mempunyai "User.Read", mari ubah kepada "User.Write". Sekarang jalankan `npm run build` dan mulakan semula pelayan dengan `npm start`. Anda sepatutnya melihat pengesahan gagal kerana kita tidak mempunyai skop ini (kita hanya ada User.Read dan Admin.Write):

Klien sekarang mengatakan

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

dan anda boleh lihat di terminal pelayan bahawa ia mengatakan:

```text
User exists
```

dan ia tidak melangkaui titik ini.

Sama ada tambahkan skop ini "User.Write" dan jalankan `npm run generate` dan jalankan semula klien ATAU ubah semula kod pelayan.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.