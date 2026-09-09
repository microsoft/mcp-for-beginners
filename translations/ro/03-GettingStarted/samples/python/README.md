# Server Calculator MCP (Python)



O implementare simplă a unui server Model Context Protocol (MCP) în Python care oferă funcționalitate de calculator de bază.


## Instalare

Instalează dependențele necesare:

```bash
pip install -r requirements.txt
```

Sau instalează direct SDK-ul MCP pentru Python:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## Utilizare

### Pornirea serverului

Serverul este proiectat să fie folosit de clienți MCP (ca Claude Desktop). Pentru a porni serverul:

```bash
python mcp_calculator_server.py
```

**Notă**: Când este rulat direct într-un terminal, vei vedea erori de validare JSON-RPC. Acest comportament este normal - serverul așteaptă mesaje MCP de la clienți, corect formatate.

### Testarea funcțiilor

Pentru a testa că funcțiile calculatorului funcționează corect:

```bash
python test_calculator.py
```

## Depanare

### Erori la import

Dacă vezi `ModuleNotFoundError: No module named 'mcp'`, instalează SDK-ul MCP pentru Python:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### Erori JSON-RPC când rulezi direct

Erori de genul "Invalid JSON: EOF while parsing a value" când rulezi serverul direct sunt așteptate. Serverul are nevoie de mesaje MCP de la clienți, nu de input direct din terminal.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->