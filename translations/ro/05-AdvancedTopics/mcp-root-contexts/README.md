# Rădăcini MCP (Funcționalitate moștenită)

> [!WARNING]
> Rădăcinile sunt învechite începând cu MCP `2026-07-28`. Ele rămân în această revizie pentru
> compatibilitate și sunt eligibile pentru eliminare în prima revizie a specificației
> lansată la sau după 28 iulie 2027. Implementările noi ar trebui să transmită
> directoare sau fișiere prin parametrii instrumentului, URI-uri de resurse sau
> configurația serverului.

## Prezentare generală

Rădăcinile permit unui client MCP să comunice unui server ce locații din sistemul de fișiere sunt relevante
pentru cererea curentă. O rădăcină conține un URI `file://` obligatoriu și un nume opțional
lizibil de om.

Rădăcinile sunt indicii informaționale. Ele nu sunt containere de istoric de conversație,
sesiuni de protocol sau un mecanism de control al accesului. Protocolul nu
impune ca un server să rămână în limitele rădăcinilor specificate.

## Obiective de învățare

La sfârșitul acestei lecții, veți putea:

- Explica ce reprezintă Rădăcinile MCP și ce nu reprezintă.
- Recunoaște fluxul actual `roots/list` cu mai multe runde de comunicare.
- Aplică controale de securitate independent de Rădăcini.
- Migrează implementările noi către alternative suportate.

## Date despre rădăcini

Un client returnează fiecare rădăcină ca un URI `file://` cu un nume opțional pentru afișare:

```json
{
  "roots": [
    {
      "uri": "file:///home/user/projects/weather-service",
      "name": "Weather Service"
    }
  ]
}
```

Clienții ar trebui să expună doar locațiile aprobate de utilizator. Serverele ar trebui să trateze
rezultatul ca o indicație despre fișiere relevante, nu ca o dovadă de autorizare.

## Flux MCP 2026-07-28

Un client care suportă Rădăcini declară această capabilitate în fiecare cerere:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

În timpul procesării unei cereri de la client, un server poate returna un
`InputRequiredResult` care conține o solicitare de input `roots/list`:

```json
{
  "resultType": "input_required",
  "inputRequests": {
    "workspaceRoots": {
      "method": "roots/list"
    }
  },
  "requestState": "opaque-state-from-server"
}
```

Clientul colectează rădăcinile aprobate și retrimite cererea originală cu
`inputResponses` corespunzătoare și `requestState` neschimbat. Acest model cu mai multe runde
menține protocolul stateless; nu există o strângere de mână `initialize` sau
sesiune la nivel de protocol.

## Comportament moștenit 2025-11-25

În MCP `2025-11-25`, clienții anunțau Rădăcinile în timpul inițializării. Un server
putea face o solicitare directă `roots/list`, iar un client putea trimite
`notifications/roots/list_changed` când rădăcinile sale se schimbau.

Acest ciclu de viață este comportament moștenit. Nu combinați exemplele de inițializare sau
notificare cu o implementare `2026-07-28`.

## Înlocuiri recomandate

### Parametri instrument

Faceți explicit directorul sau fișierul necesar în schema instrumentului:

```json
{
  "name": "analyze_project",
  "inputSchema": {
    "type": "object",
    "properties": {
      "projectDirectory": {
        "type": "string",
        "description": "Approved project directory to analyze"
      }
    },
    "required": ["projectDirectory"]
  }
}
```

### URI-uri de resurse

Folosiți Resurse MCP când serverul poate expune fișierele relevante prin URI-uri stabile.
Acest lucru menține descoperirea și recuperarea explicită.

### Configurarea serverului

Pentru implementări fixe, configurați directoarele permise când serverul pornește.
Acest lucru este adesea mai clar decât descoperirea lor în timpul unui apel de instrument.

## Cerințe de securitate

Oricare înlocuire ați alege:

- Obțineți consimțământul utilizatorului înainte de a expune locațiile din sistemul de fișiere.
- Canonicalizați și validați căile pentru a preveni traversarea.
- Impuneți autorizarea și sandboxing-ul independent de valorile rădăcinii.
- Verificați din nou permisiunile când un fișier este accesat, nu doar când este listat.
- Evitați returnarea căilor sensibile în jurnale sau mesaje de eroare.

## Concluzii cheie

- Rădăcinile descriu locațiile relevante din sistemul de fișiere; nu stochează
  starea conversației.
- Rădăcinile sunt ghiduri, nu o frontieră de control al accesului.
- MCP `2026-07-28` poartă capabilitatea per cerere și folosește
  `InputRequiredResult` pentru `roots/list`.
- Implementările noi ar trebui să folosească parametri instrument,
  URI-uri de resurse sau configurarea serverului în schimb.

## Resurse suplimentare

- [Rădăcini în MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Registrul funcționalităților învechite](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [Ce s-a schimbat în MCP: Specificația 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->