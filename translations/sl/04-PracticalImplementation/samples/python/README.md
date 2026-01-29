# Protokol modelnega konteksta (MCP) Python implementacija

Ta repozitorij vsebuje Python implementacijo protokola modelnega konteksta (MCP), ki prikazuje, kako ustvariti tako strežniško kot odjemalsko aplikacijo, ki komunicirata z uporabo standarda MCP.

## Pregled

Implementacija MCP je sestavljena iz dveh glavnih komponent:

1. **MCP strežnik (`server.py`)** - Strežnik, ki omogoča:
   - **Orodja**: Funkcije, ki jih je mogoče klicati na daljavo
   - **Viri**: Podatki, ki jih je mogoče pridobiti
   - **Pozivi**: Predloge za ustvarjanje pozivov za jezikovne modele

2. **MCP odjemalec (`client.py`)** - Odjemalska aplikacija, ki se poveže s strežnikom in uporablja njegove funkcije

## Funkcionalnosti

Ta implementacija prikazuje več ključnih funkcij MCP:

### Orodja
- `completion` - Ustvarja besedilne zaključke iz AI modelov (simulirano)
- `add` - Preprost kalkulator, ki sešteje dve števili

### Viri
- `models://` - Vrne informacije o razpoložljivih AI modelih
- `greeting://{name}` - Vrne personaliziran pozdrav za dano ime

### Pozivi
- `review_code` - Ustvari poziv za pregled kode

## Namestitev

Za uporabo te MCP implementacije namestite zahtevane pakete:

```powershell
pip install mcp-server mcp-client
```

## Zagon strežnika in odjemalca

### Zagon strežnika

Strežnik zaženite v enem terminalskem oknu:

```powershell
python server.py
```

Strežnik lahko zaženete tudi v razvojni načinu z uporabo MCP CLI:

```powershell
mcp dev server.py
```

Ali pa ga namestite v Claude Desktop (če je na voljo):

```powershell
mcp install server.py
```

### Zagon odjemalca

Odjemalca zaženite v drugem terminalskem oknu:

```powershell
python client.py
```

S tem se povežete s strežnikom in preizkusite vse razpoložljive funkcije.

### Uporaba odjemalca

Odjemalec (`client.py`) prikazuje vse zmogljivosti MCP:

```powershell
python client.py
```

S tem se povežete s strežnikom in preizkusite vse funkcije, vključno z orodji, viri in pozivi. Izhod bo prikazal:

1. Rezultat orodja kalkulatorja (5 + 7 = 12)
2. Odgovor orodja za dokončanje na vprašanje "Kaj je smisel življenja?"
3. Seznam razpoložljivih AI modelov
4. Personaliziran pozdrav za "MCP Explorer"
5. Predlogo poziva za pregled kode

## Podrobnosti implementacije

Strežnik je implementiran z uporabo API-ja `FastMCP`, ki zagotavlja visokorazredne abstrakcije za definiranje MCP storitev. Tukaj je poenostavljen primer, kako so orodja definirana:

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of the two numbers
    """
    logger.info(f"Adding {a} and {b}")
    return a + b
```

Odjemalec uporablja MCP odjemalsko knjižnico za povezavo in klic strežnika:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## Več informacij

Za več informacij o MCP obiščite: https://modelcontextprotocol.io/

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.