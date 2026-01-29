# Serviciu Calculator de Bază MCP

Acest serviciu oferă operații de bază pentru calculator prin Model Context Protocol (MCP). Este conceput ca un exemplu simplu pentru începători care învață despre implementările MCP.

Pentru mai multe informații, vezi [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Funcționalități

Acest serviciu de calculator oferă următoarele capabilități:

1. **Operații aritmetice de bază**:
   - Adunarea a două numere
   - Scăderea unui număr din altul
   - Înmulțirea a două numere
   - Împărțirea unui număr la altul (cu verificare pentru împărțirea la zero)

## Utilizarea tipului `stdio`
  
## Configurare

1. **Configurează serverele MCP**:
   - Deschide spațiul de lucru în VS Code.
   - Creează un fișier `.vscode/mcp.json` în folderul spațiului de lucru pentru a configura serverele MCP. Exemplu de configurare:

     ```jsonc
     {
       "inputs": [
         {
           "type": "promptString",
           "id": "repository-root",
           "description": "The absolute path to the repository root"
         }
       ],
       "servers": {
         "calculator-mcp-dotnet": {
           "type": "stdio",
           "command": "dotnet",
           "args": [
             "run",
             "--project",
             "${input:repository-root}/03-GettingStarted/samples/csharp/src/calculator.csproj"
           ]
         }
       }
     }
     ```

   - Ți se va cere să introduci rădăcina depozitului GitHub, care poate fi obținută cu comanda `git rev-parse --show-toplevel`.

## Utilizarea Serviciului

Serviciul expune următoarele endpoint-uri API prin protocolul MCP:

- `add(a, b)`: Adună două numere
- `subtract(a, b)`: Scade al doilea număr din primul
- `multiply(a, b)`: Înmulțește două numere
- `divide(a, b)`: Împarte primul număr la al doilea (cu verificare pentru zero)
- isPrime(n): Verifică dacă un număr este prim

## Testare cu Github Copilot Chat în VS Code

1. Încearcă să faci o cerere către serviciu folosind protocolul MCP. De exemplu, poți întreba:
   - "Adună 5 și 3"
   - "Scade 10 din 4"
   - "Înmulțește 6 și 7"
   - "Împarte 8 la 2"
   - "Este 37854 prim?"
   - "Care sunt cele 3 numere prime înainte și după 4242?"
2. Pentru a te asigura că folosește uneltele, adaugă #MyCalculator în prompt. De exemplu:
   - "Adună 5 și 3 #MyCalculator"
   - "Scade 10 din 4 #MyCalculator"

## Versiunea Containerizată

Soluția anterioară este excelentă când ai instalat .NET SDK și toate dependențele sunt în regulă. Totuși, dacă dorești să distribui soluția sau să o rulezi într-un mediu diferit, poți folosi versiunea containerizată.

1. Pornește Docker și asigură-te că rulează.
1. Dintr-un terminal, navighează în folderul `03-GettingStarted\samples\csharp\src`
1. Pentru a construi imaginea Docker pentru serviciul calculator, execută următoarea comandă (înlocuiește `<YOUR-DOCKER-USERNAME>` cu numele tău de utilizator Docker Hub):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. După ce imaginea este construită, hai să o urcăm pe Docker Hub. Rulează comanda următoare:
   ```bash
    docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
  ```

## Folosirea Versiunii Dockerizate

1. În fișierul `.vscode/mcp.json`, înlocuiește configurația serverului cu următoarea:
   ```json
    "mcp-calc": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calc"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   Privind configurația, poți observa că comanda este `docker` iar argumentele sunt `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calc`. Flag-ul `--rm` asigură că containerul este șters după ce se oprește, iar flag-ul `-i` îți permite să interacționezi cu inputul standard al containerului. Ultimul argument este numele imaginii pe care tocmai am construit-o și încărcat-o pe Docker Hub.

## Testarea Versiunii Dockerizate

Pornește serverul MCP făcând clic pe butonul mic Start de deasupra `"mcp-calc": {`, și la fel ca înainte, poți cere serviciului calculator să facă niște calcule pentru tine.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.