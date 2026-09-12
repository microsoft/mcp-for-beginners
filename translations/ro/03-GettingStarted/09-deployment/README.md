# Implementarea Serverelor MCP

> [!NOTE]
> Exemplele de configurare care folosesc un endpoint `/sse` vizează transportul vechi HTTP+SSE.
> Serverele MCP `2026-07-28` la distanță folosesc Streamable HTTP, de obicei la un
> endpoint definit de server, cum ar fi `/mcp`.

Implementarea serverului MCP permite altora să acceseze uneltele și resursele sale dincolo de mediul local. Există mai multe strategii de implementare de luat în considerare, în funcție de cerințele tale pentru scalabilitate, fiabilitate și ușurință în gestionare. Mai jos găsești îndrumări pentru implementarea serverelor MCP local, în containere și în cloud.

## Prezentare generală

Această lecție acoperă cum să implementezi aplicația server MCP.

## Obiective de învățare

La finalul acestei lecții vei putea să:

- Evaluezi diferite abordări de implementare.
- Implementezi aplicația ta.

## Dezvoltare și implementare locală

Dacă serverul tău este destinat să fie folosit rulând pe mașina utilizatorului, poți urma următorii pași:

1. **Descarcă serverul**. Dacă nu ai scris serverul, descarcă-l mai întâi pe mașina ta.
1. **Porneste procesul serverului**: Rulează aplicația serverului MCP

Pentru SSE (nu este necesar pentru servere de tip stdio)

1. **Configurează rețeaua**: Asigură-te că serverul este accesibil pe portul așteptat
1. **Conectează clienții**: Folosește URL-uri locale ca `http://localhost:3000`

## Implementare în cloud

Serverele MCP pot fi implementate pe diverse platforme cloud:

- **Funcții fără server**: Implementează servere MCP ușoare ca funcții fără server
- **Servicii de containere**: Folosește servicii precum Azure Container Apps, AWS ECS sau Google Cloud Run
- **Kubernetes**: Implementează și gestionează servere MCP în clustere Kubernetes pentru disponibilitate ridicată

### Exemplu: Azure Container Apps

Azure Container Apps suportă implementarea Serverelor MCP. Este încă în dezvoltare și în prezent susține serverele SSE.

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

1. Pentru a încerca local, creează un fișier *mcp.json* într-un director *.vscode* și adaugă următorul conținut:

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

  Odată ce serverul SSE este pornit, poți apăsa pe iconița de redare din fișierul JSON; acum ar trebui să vezi uneltele de pe server preluate de GitHub Copilot, vezi iconița Unelte.

1. Pentru implementare, rulează următoarea comandă:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Așa ai implementat local, ai implementat pe Azure prin acești pași.

## Resurse suplimentare

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Articol Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Repo Azure Container Apps MCP](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Ce urmează

- Următorul: [Subiecte avansate pentru server](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->