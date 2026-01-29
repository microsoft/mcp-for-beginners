# Implementarea serverelor MCP

Implementarea serverului MCP permite altora să acceseze uneltele și resursele acestuia dincolo de mediul tău local. Există mai multe strategii de implementare de luat în considerare, în funcție de cerințele tale legate de scalabilitate, fiabilitate și ușurința în administrare. Mai jos vei găsi îndrumări pentru implementarea serverelor MCP local, în containere și în cloud.

## Prezentare generală

Această lecție acoperă modul de implementare a aplicației tale MCP Server.

## Obiective de învățare

La finalul acestei lecții, vei putea:

- Evalua diferite abordări de implementare.
- Implementa aplicația ta.

## Dezvoltare și implementare locală

Dacă serverul tău este destinat să fie folosit rulând pe mașina utilizatorului, poți urma pașii următori:

1. **Descarcă serverul**. Dacă nu ai scris serverul, descarcă-l mai întâi pe mașina ta.  
1. **Pornește procesul serverului**: Rulează aplicația MCP server.

Pentru SSE (nu este necesar pentru serverele de tip stdio)

1. **Configurează rețeaua**: Asigură-te că serverul este accesibil pe portul așteptat.  
1. **Conectează clienții**: Folosește URL-uri de conexiune locală, cum ar fi `http://localhost:3000`.

## Implementare în cloud

Serverele MCP pot fi implementate pe diverse platforme cloud:

- **Funcții serverless**: Implementarea serverelor MCP ușoare ca funcții serverless.  
- **Servicii de containere**: Folosește servicii precum Azure Container Apps, AWS ECS sau Google Cloud Run.  
- **Kubernetes**: Implementarea și gestionarea serverelor MCP în clustere Kubernetes pentru disponibilitate ridicată.

### Exemplu: Azure Container Apps

Azure Container Apps suportă implementarea serverelor MCP. Este încă în curs de dezvoltare și în prezent suportă serverele SSE.

Iată cum poți proceda:

1. Clonează un repo:

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

1. Pentru a-l testa local, creează un fișier *mcp.json* într-un director *.vscode* și adaugă următorul conținut:

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

  Odată ce serverul SSE este pornit, poți da click pe iconița de redare din fișierul JSON; acum ar trebui să vezi uneltele serverului preluate de GitHub Copilot, vezi iconița Tool.

1. Pentru a implementa, rulează următoarea comandă:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Asta este tot, implementează-l local sau în Azure urmând acești pași.

## Resurse suplimentare

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)  
- [Articol Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)  
- [Repo Azure Container Apps MCP](https://github.com/anthonychu/azure-container-apps-mcp-sample)  


## Ce urmează

- Următorul: [Implementare practică](../../04-PracticalImplementation/README.md)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.