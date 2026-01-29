# Kompletné príklady MCP klientov

Tento adresár obsahuje kompletné, funkčné príklady MCP klientov v rôznych programovacích jazykoch. Každý klient demonštruje plnú funkcionalitu popísanú v hlavnom návode README.md.

## Dostupní klienti

### 1. Java klient (`client_example_java.java`)

- **Transport**: SSE (Server-Sent Events) cez HTTP
- **Cieľový server**: `http://localhost:8080`
- **Funkcie**:
  - Zriadenie spojenia a ping
  - Zoznam nástrojov
  - Operácie kalkulačky (sčítanie, odčítanie, násobenie, delenie, pomoc)
  - Spracovanie chýb a extrakcia výsledkov

**Spustenie:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. C# klient (`client_example_csharp.cs`)

- **Transport**: Stdio (Štandardný vstup/výstup)
- **Cieľový server**: Lokálny .NET MCP server cez dotnet run
- **Funkcie**:
  - Automatické spustenie servera cez stdio transport
  - Zoznam nástrojov a zdrojov
  - Operácie kalkulačky
  - Parsovanie výsledkov vo formáte JSON
  - Komplexné spracovanie chýb

**Spustenie:**

```bash
dotnet run
```

### 3. TypeScript klient (`client_example_typescript.ts`)

- **Transport**: Stdio (Štandardný vstup/výstup)
- **Cieľový server**: Lokálny Node.js MCP server
- **Funkcie**:
  - Plná podpora MCP protokolu
  - Operácie s nástrojmi, zdrojmi a promptmi
  - Operácie kalkulačky
  - Čítanie zdrojov a vykonávanie promptov
  - Robustné spracovanie chýb

**Spustenie:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Python klient (`client_example_python.py`)

- **Transport**: Stdio (Štandardný vstup/výstup)  
- **Cieľový server**: Lokálny Python MCP server
- **Funkcie**:
  - Vzor async/await pre operácie
  - Objavovanie nástrojov a zdrojov
  - Testovanie operácií kalkulačky
  - Čítanie obsahu zdrojov
  - Organizácia na báze tried

**Spustenie:**

```bash
python client_example_python.py
```

## Spoločné funkcie pre všetkých klientov

Každá implementácia klienta demonštruje:

1. **Správa spojenia**
   - Zriadenie spojenia s MCP serverom
   - Spracovanie chýb spojenia
   - Správne ukončenie a správa zdrojov

2. **Objavovanie servera**
   - Zoznam dostupných nástrojov
   - Zoznam dostupných zdrojov (ak je podporované)
   - Zoznam dostupných promptov (ak je podporované)

3. **Vykonávanie nástrojov**
   - Základné operácie kalkulačky (sčítanie, odčítanie, násobenie, delenie)
   - Príkaz pomoc pre informácie o serveri
   - Správne odovzdávanie argumentov a spracovanie výsledkov

4. **Spracovanie chýb**
   - Chyby spojenia
   - Chyby pri vykonávaní nástrojov
   - Elegantné zlyhanie a spätná väzba pre používateľa

5. **Spracovanie výsledkov**
   - Extrakcia textového obsahu z odpovedí
   - Formátovanie výstupu pre čitateľnosť
   - Spracovanie rôznych formátov odpovedí

## Predpoklady

Pred spustením týchto klientov sa uistite, že máte:

1. **Spustený príslušný MCP server** (z `../01-first-server/`)
2. **Nainštalované požadované závislosti** pre zvolený jazyk
3. **Správne sieťové pripojenie** (pre transporty založené na HTTP)

## Kľúčové rozdiely medzi implementáciami

| Jazyk      | Transport | Spustenie servera | Async model | Kľúčové knižnice       |
|------------|-----------|-------------------|-------------|------------------------|
| Java       | SSE/HTTP  | Externé           | Sync        | WebFlux, MCP SDK       |
| C#         | Stdio     | Automatické       | Async/Await | .NET MCP SDK           |
| TypeScript | Stdio     | Automatické       | Async/Await | Node MCP SDK           |
| Python     | Stdio     | Automatické       | AsyncIO     | Python MCP SDK         |
| Rust       | Stdio     | Automatické       | Async/Await | Rust MCP SDK, Tokio    |

## Ďalšie kroky

Po preskúmaní týchto príkladov klientov:

1. **Upravte klientov** na pridanie nových funkcií alebo operácií
2. **Vytvorte vlastný server** a otestujte ho s týmito klientmi
3. **Experimentujte s rôznymi transportmi** (SSE vs. Stdio)
4. **Vytvorte komplexnejšiu aplikáciu**, ktorá integruje MCP funkcionalitu

## Riešenie problémov

### Bežné problémy

1. **Spojenie odmietnuté**: Uistite sa, že MCP server beží na očakávanom porte/ceste
2. **Modul nenájdený**: Nainštalujte požadovaný MCP SDK pre váš jazyk
3. **Prístup odmietnutý**: Skontrolujte oprávnenia súborov pre stdio transport
4. **Nástroj nenájdený**: Overte, že server implementuje očakávané nástroje

### Tipy na ladenie

1. **Povoľte podrobné logovanie** vo vašom MCP SDK
2. **Skontrolujte logy servera** pre chybové hlásenia
3. **Overte názvy a podpisy nástrojov**, či sa zhodujú medzi klientom a serverom
4. **Najskôr otestujte s MCP Inspector**, aby ste overili funkcionalitu servera

## Súvisiaca dokumentácia

- [Hlavný návod pre klienta](./README.md)
- [Príklady MCP serverov](../../../../03-GettingStarted/01-first-server)
- [MCP s integráciou LLM](../../../../03-GettingStarted/03-llm-client)
- [Oficiálna dokumentácia MCP](https://modelcontextprotocol.io/)

**Upozornenie**:  
Tento dokument bol preložený pomocou služby na automatický preklad [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie odporúčame profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.