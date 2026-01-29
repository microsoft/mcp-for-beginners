# MCP stdio Server - Soluție Python

> **⚠️ Important**: Această soluție a fost actualizată pentru a utiliza **stdio transport**, conform recomandărilor din Specificația MCP 2025-06-18. Transportul SSE original a fost depreciat.

## Prezentare generală

Această soluție Python demonstrează cum să construiești un server MCP utilizând transportul stdio actual. Transportul stdio este mai simplu, mai sigur și oferă performanțe mai bune decât abordarea SSE depreciată.

## Cerințe preliminare

- Python 3.8 sau o versiune ulterioară
- Se recomandă instalarea `uv` pentru gestionarea pachetelor, vezi [instrucțiuni](https://docs.astral.sh/uv/#highlights)

## Instrucțiuni de configurare

### Pasul 1: Creează un mediu virtual

```bash
python -m venv venv
```

### Pasul 2: Activează mediul virtual

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Pasul 3: Instalează dependențele

```bash
pip install mcp
```

## Rularea serverului

Serverul stdio funcționează diferit față de vechiul server SSE. În loc să pornească un server web, comunică prin stdin/stdout:

```bash
python server.py
```

**Important**: Serverul va părea că se blochează - acest lucru este normal! Așteaptă mesaje JSON-RPC de la stdin.

## Testarea serverului

### Metoda 1: Utilizarea MCP Inspector (Recomandată)

```bash
npx @modelcontextprotocol/inspector python server.py
```

Aceasta va:
1. Lansa serverul ca un subprocess
2. Deschide o interfață web pentru testare
3. Permite testarea interactivă a tuturor instrumentelor serverului

### Metoda 2: Testare directă JSON-RPC

Poți testa și prin trimiterea directă de mesaje JSON-RPC:

1. Pornește serverul: `python server.py`
2. Trimite un mesaj JSON-RPC (exemplu):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Serverul va răspunde cu instrumentele disponibile

### Instrumente disponibile

Serverul oferă următoarele instrumente:

- **add(a, b)**: Adună două numere
- **multiply(a, b)**: Înmulțește două numere  
- **get_greeting(name)**: Generează un mesaj de salut personalizat
- **get_server_info()**: Oferă informații despre server

### Testarea cu Claude Desktop

Pentru a utiliza acest server cu Claude Desktop, adaugă această configurație în `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## Diferențe cheie față de SSE

**Transport stdio (Actual):**
- ✅ Configurare mai simplă - nu este necesar un server web
- ✅ Securitate mai bună - fără endpoint-uri HTTP
- ✅ Comunicare bazată pe subprocess
- ✅ JSON-RPC prin stdin/stdout
- ✅ Performanțe mai bune

**Transport SSE (Depreciat):**
- ❌ Necesita configurarea unui server HTTP
- ❌ Necesita un framework web (Starlette/FastAPI)
- ❌ Gestionare mai complexă a rutării și sesiunilor
- ❌ Considerații suplimentare de securitate
- ❌ Acum depreciat în MCP 2025-06-18

## Sfaturi pentru depanare

- Folosește `stderr` pentru logare (niciodată `stdout`)
- Testează cu Inspector pentru depanare vizuală
- Asigură-te că toate mesajele JSON sunt delimitate prin newline
- Verifică dacă serverul pornește fără erori

Această soluție urmează specificația actuală MCP și demonstrează cele mai bune practici pentru implementarea transportului stdio.

---

**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși depunem eforturi pentru a asigura acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea umană realizată de profesioniști. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.