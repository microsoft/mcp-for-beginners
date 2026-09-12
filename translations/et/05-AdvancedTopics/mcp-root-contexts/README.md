# MCP Roots (pärandfunktsioon)

> [!WARNING]
> Roots on MCP `2026-07-28` seisuga aegunud. Need jäävad sellesse versiooni ühilduvuse eesmärgil ning neid võib esimeses spetsifikatsiooni
> uuenduses alates 28. juulist 2027 eemaldada. Uued rakendused peaksid
> edastama kaustasid või faile tööriista parameetrite, ressursi URI-de või serveri
> konfiguratsiooni kaudu.


## Ülevaade

Roots võimaldavad MCP kliendil öelda serverile, millised failisüsteemi asukohad on hetke päringu jaoks olulised. Root sisaldab kohustuslikku `file://` URI-d ja vabatahtlikku
inimesele loetavat nime.


protokolli sessioonid ega ligipääsukontrolli mehhanism. Protokoll ei
sunni serverit jääma nimetatud roots piiridesse.


## Õpieesmärgid

Õppetunni lõpuks oskad sa:

- Selgitada, mida MCP Roots tähistavad ja mida mitte.
- Tunda ära jooksva `roots/list` mitme ringi päringu voo.
- Rakendada turvameetmeid sõltumatult Roots'ist.
- Migratsiooniks võtta kasutusele toetatud alternatiivid.

## Root andmed

Klient tagastab iga root'i `file://` URI-na koos vabatahtliku kuvamisnimega:

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

Kliendid peaksid avalikustama ainult kasutaja poolt kinnitatud asukohad. Serverid käsitlevad
tulemust juhisena oluliste failide kohta, mitte tõendina autoriseerimiseks.

## MCP 2026-07-28 voog

Roots toetav klient deklareerib selle võimaluse iga päringu juures:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Kliendi päringu töötlemisel võib server tagastada
`InputRequiredResult`, mis sisaldab `roots/list` sisestuspäringut:

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

Klient kogub kinnitatud roots ja proovib originaalset päringut uuesti koos sobivate `inputResponses` ja muutmata `requestState`-ga. See mitme ringi päring
hoiab protokolli stateless; puudub `initialize` kättesaadavus või
protokolli tasemel sessioon.


## Pärandkäitumine 2025-11-25

MCP `2025-11-25` versioonis reklaamisid kliendid Roots'it algatamisel. Server võis esitada otsese `roots/list` päringu ning klient saatis
`notifications/roots/list_changed` kui tema roots muutusid.


teavituse näiteid `2026-07-28` rakendusega.


## Soovitatud asendused

### Tööriista parameetrid

Tee tööriista skeemi abil kohustuslik kaust või fail selgeks:

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

### Ressursi URI-d

Kasuta MCP Ressursse, kui server saab näidata olulisi faile stabiilsete
URI-de kaudu. See hoiab avastamise ja pärimise selgena.

### Serveri konfiguratsioon

Fikseeritud paigaldiste puhul konfigureeri lubatud kaustad serveri käivitamisel.
See on sageli selgem kui nende avastamine tööriista kõne ajal.

## Turvanõuded

Millise asenduse sa ka ei valiks:

- Saa kasutajalt luba enne failisüsteemi asukohtade avalikustamist.
- Kanoniseeri ja valideeri teed, et vältida läbikäiku.
- Jõusta autoriseerimine ja sandboximine sõltumatult root väärtustest.
- Luba õigusi uuesti kontrollida faili avamisel, mitte ainult selle loetlemisel.
- Väldi tundlike teede tagastamist logides või veateadetes.

## Peamised kokkuvõtted

- Roots kirjeldavad olulisi failisüsteemi asukohti; need ei talleta vestluse
  seisundit.
- Roots on juhised, mitte ligipääsu piirded.
- MCP `2026-07-28` kannab võimekust päringu kohta ja kasutab
  `InputRequiredResult` `roots/list` jaoks.
- Uued rakendused peaksid kasutama hoopis tööriista parameetreid, ressursi URI-sid või serveri
  konfiguratsiooni.

## Lisamaterjalid

- [Roots MCP 2026-07-28-s](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Aegunud funktsioonide register](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [MCP muudatused: 2026-07-28 spetsifikatsioon](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->