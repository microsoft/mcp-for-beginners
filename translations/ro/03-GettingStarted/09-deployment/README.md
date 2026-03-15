# Implementarea serverelor MCP

Implementarea serverului tău MCP permite altora să acceseze instrumentele și resursele sale dincolo de mediul local. Există mai multe strategii de implementare de luat în considerare, în funcție de cerințele tale privind scalabilitatea, fiabilitatea și ușurința gestionării. Mai jos vei găsi ghiduri pentru implementarea serverelor MCP local, în containere și în cloud.

## Prezentare generală

Această lecție acoperă modul de a implementa aplicația ta MCP Server.

## Obiective de învățare

La finalul acestei lecții, vei putea:

- Evalua diferite abordări de implementare.
- Implementa aplicația ta.

## Dezvoltare și implementare locală

Dacă serverul tău este destinat a fi folosit în execuție pe mașina utilizatorului, poți urma pașii următori:

1. **Descarcă serverul**. Dacă nu ai scris serverul, descarcă-l mai întâi pe mașina ta.  
1. **Pornește procesul serverului**: Rulează aplicația ta MCP server

Pentru SSE (nu este necesar pentru servere de tip stdio)

1. **Configurează rețeaua**: Asigură-te că serverul este accesibil pe portul așteptat  
1. **Conectează clienții**: Folosește URL-uri de conexiune locală precum `http://localhost:3000`

## Implementarea în cloud

Serverele MCP pot fi implementate pe diverse platforme cloud:

- **Funcții serverless**: Implementează servere MCP ușoare ca funcții serverless  
- **Servicii cu containere**: Folosește servicii precum Azure Container Apps, AWS ECS sau Google Cloud Run  
- **Kubernetes**: Implementează și gestionează serverele MCP în clustere Kubernetes pentru disponibilitate ridicată

### Exemplu: Azure Container Apps

Azure Container Apps suportă implementarea serverelor MCP. Este încă în lucru și în prezent suportă servere SSE.

Iată cum poți proceda:

1. Clonează un depozit:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Rulează-l local pentru a testa:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Pentru a-l încerca local, creează un fișier *mcp.json* într-un director *.vscode* și adaugă următorul conținut:

  ```json
  {
      "inputs": [
          {
              "type": "promptString",
              "id": "weather-api-key",
              "description": "Weather API Key",
              "password": true
          }
      ],
      "servers": {
          "weather-sse": {
              "type": "sse",
              "url": "http://localhost:8000/sse",
              "headers": {
                  "x-api-key": "${input:weather-api-key}"
              }
          }
      }
  }
  ```

  Odată ce serverul SSE este pornit, poți face clic pe pictograma de redare din fișierul JSON, ar trebui să vezi acum uneletele de pe server preluate de GitHub Copilot, vezi pictograma Unealtă.

1. Pentru a implementa, rulează următoarea comandă:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Iată-l, implementează-l local, implementează-l pe Azure urmând acești pași.

## Resurse suplimentare

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Articol Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Depozitul MCP pentru Azure Container Apps](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## Ce urmează

- Următor: [Subiecte avansate despre server](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să aveți în vedere că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă o traducere profesională realizată de un translator uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->