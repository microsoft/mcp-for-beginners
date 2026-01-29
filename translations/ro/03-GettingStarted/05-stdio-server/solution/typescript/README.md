# MCP stdio Server - Soluție TypeScript

> **⚠️ Important**: Această soluție a fost actualizată pentru a utiliza **stdio transport**, conform recomandărilor din Specificația MCP 2025-06-18. Transportul original SSE a fost depreciat.

## Prezentare generală

Această soluție TypeScript demonstrează cum să construiești un server MCP folosind transportul stdio actual. Transportul stdio este mai simplu, mai sigur și oferă performanțe mai bune decât abordarea SSE depreciată.

## Cerințe preliminare

- Node.js 18+ sau o versiune ulterioară
- Manager de pachete npm sau yarn

## Instrucțiuni de configurare

### Pasul 1: Instalează dependențele

```bash
npm install
```

### Pasul 2: Construiește proiectul

```bash
npm run build
```

## Rularea serverului

Serverul stdio funcționează diferit față de vechiul server SSE. În loc să pornească un server web, comunică prin stdin/stdout:

```bash
npm start
```

**Important**: Serverul va părea că se blochează - acest lucru este normal! Așteaptă mesaje JSON-RPC de la stdin.

## Testarea serverului

### Metoda 1: Utilizarea MCP Inspector (Recomandată)

```bash
npm run inspector
```

Aceasta va:
1. Lansa serverul ca un subproces
2. Deschide o interfață web pentru testare
3. Permite testarea interactivă a tuturor instrumentelor serverului

### Metoda 2: Testare directă din linia de comandă

Poți testa și lansând Inspectorul direct:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### Instrumente disponibile

Serverul oferă următoarele instrumente:

- **add(a, b)**: Adună două numere
- **multiply(a, b)**: Înmulțește două numere  
- **get_greeting(name)**: Generează un mesaj de salut personalizat
- **get_server_info()**: Oferă informații despre server

### Testarea cu Claude Desktop

Pentru a utiliza acest server cu Claude Desktop, adaugă această configurație în fișierul `claude_desktop_config.json`:

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

## Structura proiectului

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## Diferențe cheie față de SSE

**Transport stdio (Actual):**
- ✅ Configurare mai simplă - nu este necesar un server HTTP
- ✅ Securitate mai bună - fără endpoint-uri HTTP
- ✅ Comunicare bazată pe subproces
- ✅ JSON-RPC prin stdin/stdout
- ✅ Performanțe mai bune

**Transport SSE (Depreciat):**
- ❌ Necesita configurarea unui server Express
- ❌ Necesita rutare complexă și gestionarea sesiunilor
- ❌ Mai multe dependențe (Express, gestionare HTTP)
- ❌ Considerații suplimentare de securitate
- ❌ Acum depreciat în MCP 2025-06-18

## Sfaturi pentru dezvoltare

- Folosește `console.error()` pentru logare (niciodată `console.log()`, deoarece scrie în stdout)
- Construiește cu `npm run build` înainte de testare
- Testează cu Inspector pentru depanare vizuală
- Asigură-te că toate mesajele JSON sunt formatate corect
- Serverul gestionează automat oprirea grațioasă la SIGINT/SIGTERM

Această soluție urmează specificația MCP actuală și demonstrează cele mai bune practici pentru implementarea transportului stdio folosind TypeScript.

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.