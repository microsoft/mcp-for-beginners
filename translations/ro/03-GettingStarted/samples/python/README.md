# Server MCP Calculator (Python)

O implementare simplă a unui server Model Context Protocol (MCP) în Python care oferă funcționalități de bază pentru un calculator.

## Instalare

Instalează dependențele necesare:

```bash
pip install -r requirements.txt
```
  
Sau instalează direct MCP Python SDK:

```bash
pip install mcp>=1.18.0
```
  
## Utilizare

### Rularea Serverului

Serverul este conceput pentru a fi utilizat de clienți MCP (cum ar fi Claude Desktop). Pentru a porni serverul:

```bash
python mcp_calculator_server.py
```
  
**Notă**: Când este rulat direct într-un terminal, vei vedea erori de validare JSON-RPC. Acest comportament este normal - serverul așteaptă mesaje formatate corect de la clienții MCP.

### Testarea Funcțiilor

Pentru a testa dacă funcțiile calculatorului funcționează corect:

```bash
python test_calculator.py
```
  
## Depanare

### Erori de Import

Dacă vezi `ModuleNotFoundError: No module named 'mcp'`, instalează MCP Python SDK:

```bash
pip install mcp>=1.18.0
```
  
### Erori JSON-RPC la Rularea Directă

Erori precum "Invalid JSON: EOF while parsing a value" atunci când rulezi serverul direct sunt de așteptat. Serverul are nevoie de mesaje de la clienți MCP, nu de input direct din terminal.

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.