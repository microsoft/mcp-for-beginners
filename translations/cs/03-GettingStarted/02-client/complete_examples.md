# Kompletní příklady MCP klientů

Tento adresář obsahuje kompletní, funkční příklady MCP klientů v různých programovacích jazycích. Každý klient demonstruje plnou funkcionalitu popsanou v hlavním návodu README.md.

## Dostupní klienti

### 1. Java klient (`client_example_java.java`)

- **Transport**: SSE (Server-Sent Events) přes HTTP
- **Cílový server**: `http://localhost:8080`
- **Funkce**:
  - Navázání spojení a ping
  - Výpis nástrojů
  - Operace kalkulačky (sčítání, odčítání, násobení, dělení, nápověda)
  - Zpracování chyb a extrakce výsledků

**Jak spustit:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. C# klient (`client_example_csharp.cs`)

- **Transport**: Stdio (Standardní vstup/výstup)
- **Cílový server**: Lokální .NET MCP server přes dotnet run
- **Funkce**:
  - Automatické spuštění serveru přes stdio transport
  - Výpis nástrojů a zdrojů
  - Operace kalkulačky
  - Parsování výsledků v JSON formátu
  - Komplexní zpracování chyb

**Jak spustit:**

```bash
dotnet run
```

### 3. TypeScript klient (`client_example_typescript.ts`)

- **Transport**: Stdio (Standardní vstup/výstup)
- **Cílový server**: Lokální Node.js MCP server
- **Funkce**:
  - Plná podpora MCP protokolu
  - Operace s nástroji, zdroji a výzvami
  - Operace kalkulačky
  - Čtení zdrojů a provádění výzev
  - Robustní zpracování chyb

**Jak spustit:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Python klient (`client_example_python.py`)

- **Transport**: Stdio (Standardní vstup/výstup)  
- **Cílový server**: Lokální Python MCP server
- **Funkce**:
  - Vzor async/await pro operace
  - Objevování nástrojů a zdrojů
  - Testování operací kalkulačky
  - Čtení obsahu zdrojů
  - Organizace založená na třídách

**Jak spustit:**

```bash
python client_example_python.py
```

## Společné funkce napříč všemi klienty

Každá implementace klienta demonstruje:

1. **Správa spojení**
   - Navázání spojení s MCP serverem
   - Zpracování chyb při spojení
   - Správné uvolnění zdrojů

2. **Objevování serveru**
   - Výpis dostupných nástrojů
   - Výpis dostupných zdrojů (pokud je podporováno)
   - Výpis dostupných výzev (pokud je podporováno)

3. **Volání nástrojů**
   - Základní operace kalkulačky (sčítání, odčítání, násobení, dělení)
   - Příkaz nápovědy pro informace o serveru
   - Správné předávání argumentů a zpracování výsledků

4. **Zpracování chyb**
   - Chyby při spojení
   - Chyby při provádění nástrojů
   - Elegantní selhání a zpětná vazba uživateli

5. **Zpracování výsledků**
   - Extrakce textového obsahu z odpovědí
   - Formátování výstupu pro čitelnost
   - Zpracování různých formátů odpovědí

## Předpoklady

Před spuštěním těchto klientů se ujistěte, že máte:

1. **Běžící odpovídající MCP server** (z `../01-first-server/`)
2. **Nainstalované požadované závislosti** pro zvolený jazyk
3. **Správné síťové připojení** (pro transporty založené na HTTP)

## Klíčové rozdíly mezi implementacemi

| Jazyk      | Transport | Spuštění serveru | Async model | Klíčové knihovny       |
|------------|-----------|------------------|-------------|------------------------|
| Java       | SSE/HTTP  | Externí          | Sync        | WebFlux, MCP SDK       |
| C#         | Stdio     | Automatické      | Async/Await | .NET MCP SDK           |
| TypeScript | Stdio     | Automatické      | Async/Await | Node MCP SDK           |
| Python     | Stdio     | Automatické      | AsyncIO     | Python MCP SDK         |
| Rust       | Stdio     | Automatické      | Async/Await | Rust MCP SDK, Tokio    |

## Další kroky

Po prozkoumání těchto příkladů klientů:

1. **Upravte klienty**, abyste přidali nové funkce nebo operace
2. **Vytvořte vlastní server** a otestujte ho s těmito klienty
3. **Experimentujte s různými transporty** (SSE vs. Stdio)
4. **Vytvořte komplexnější aplikaci**, která integruje MCP funkcionalitu

## Řešení problémů

### Běžné problémy

1. **Spojení odmítnuto**: Ujistěte se, že MCP server běží na očekávaném portu/cestě
2. **Modul nenalezen**: Nainstalujte požadovaný MCP SDK pro váš jazyk
3. **Přístup odepřen**: Zkontrolujte oprávnění souborů pro stdio transport
4. **Nástroj nenalezen**: Ověřte, že server implementuje očekávané nástroje

### Tipy pro ladění

1. **Povolte podrobné logování** ve vašem MCP SDK
2. **Zkontrolujte logy serveru** pro chybové zprávy
3. **Ověřte názvy a podpisy nástrojů**, že odpovídají mezi klientem a serverem
4. **Nejprve otestujte pomocí MCP Inspector**, abyste ověřili funkčnost serveru

## Související dokumentace

- [Hlavní návod pro klienty](./README.md)
- [Příklady MCP serverů](../../../../03-GettingStarted/01-first-server)
- [MCP s integrací LLM](../../../../03-GettingStarted/03-llm-client)
- [Oficiální dokumentace MCP](https://modelcontextprotocol.io/)

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.