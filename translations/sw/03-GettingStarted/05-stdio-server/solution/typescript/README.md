# MCP stdio Server - Suluhisho la TypeScript

> **⚠️ Muhimu**: Suluhisho hili limeboreshwa kutumia **stdio transport** kama ilivyopendekezwa na MCP Specification 2025-06-18. Njia ya awali ya SSE imeachwa.

## Muhtasari

Suluhisho hili la TypeScript linaonyesha jinsi ya kujenga seva ya MCP kwa kutumia stdio transport ya sasa. Stdio transport ni rahisi zaidi, salama zaidi, na inatoa utendaji bora kuliko njia ya zamani ya SSE.

## Mahitaji

- Node.js 18+ au toleo jipya zaidi
- Meneja wa kifurushi cha npm au yarn

## Maelekezo ya Usanidi

### Hatua ya 1: Sakinisha utegemezi

```bash
npm install
```

### Hatua ya 2: Jenga mradi

```bash
npm run build
```

## Kuendesha Seva

Seva ya stdio inaendeshwa tofauti na seva ya zamani ya SSE. Badala ya kuanzisha seva ya wavuti, inawasiliana kupitia stdin/stdout:

```bash
npm start
```

**Muhimu**: Seva itaonekana kama imekwama - hili ni jambo la kawaida! Inasubiri ujumbe wa JSON-RPC kutoka stdin.

## Kupima Seva

### Njia ya 1: Kutumia MCP Inspector (Inapendekezwa)

```bash
npm run inspector
```

Hii itafanya:
1. Kuzindua seva yako kama subprocess
2. Kufungua kiolesura cha wavuti kwa ajili ya kupima
3. Kukuruhusu kupima zana zote za seva kwa njia ya mwingiliano

### Njia ya 2: Kupima moja kwa moja kupitia mstari wa amri

Unaweza pia kupima kwa kuzindua Inspector moja kwa moja:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Zana Zinazopatikana

Seva inatoa zana hizi:

- **add(a, b)**: Jumlisha namba mbili
- **multiply(a, b)**: Zidisha namba mbili  
- **get_greeting(name)**: Tengeneza salamu ya kibinafsi
- **get_server_info()**: Pata taarifa kuhusu seva

### Kupima na Claude Desktop

Ili kutumia seva hii na Claude Desktop, ongeza usanidi huu kwenye `claude_desktop_config.json` yako:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## Muundo wa Mradi

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Tofauti Muhimu kutoka SSE

**stdio transport (Ya sasa):**
- ✅ Usanidi rahisi - hakuna seva ya HTTP inayohitajika
- ✅ Usalama bora - hakuna endpoints za HTTP
- ✅ Mawasiliano yanayotegemea subprocess
- ✅ JSON-RPC kupitia stdin/stdout
- ✅ Utendaji bora

**SSE transport (Imeachwa):**
- ❌ Ilihitaji usanidi wa seva ya Express
- ❌ Ilihitaji uratibu mgumu na usimamizi wa vikao
- ❌ Utegemezi zaidi (Express, usimamizi wa HTTP)
- ❌ Masuala ya ziada ya usalama
- ❌ Sasa imeachwa katika MCP 2025-06-18

## Vidokezo vya Maendeleo

- Tumia `console.error()` kwa kuandika kumbukumbu (kamwe usitumie `console.log()` kwani inaandika kwenye stdout)
- Jenga kwa `npm run build` kabla ya kupima
- Pima na Inspector kwa ufuatiliaji wa kuona
- Hakikisha ujumbe wote wa JSON umeundwa vizuri
- Seva inashughulikia kuzimwa kwa heshima kiotomatiki kwenye SIGINT/SIGTERM

Suluhisho hili linafuata maelezo ya sasa ya MCP na linaonyesha mbinu bora za utekelezaji wa stdio transport kwa kutumia TypeScript.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.