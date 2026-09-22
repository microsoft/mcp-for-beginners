# MCP Rooti (zastarala funkcija)

> [!WARNING]
> Rooti so od MCP `2026-07-28` zastareli. Ostajajo v tej reviziji zaradi
> združljivosti in so primerni za odstranitev v prvi različici specifikacije,
> izdani 28. julija 2027 ali pozneje. Nove implementacije naj posredujejo
> imenike ali datoteke preko parametrov orodja, URI-jev virov ali strežniške
> konfiguracije.

## Pregled

Rooti omogočajo MCP klientu, da strežniku sporoči, katere lokacije v datotečnem sistemu so relevantne
za trenutni zahtevek. Root vsebuje zahtevan `file://` URI in neobvezno
čitljivo ime.

Rooti so informativne namige. Niso kontejnerji zgodovine pogovora,
protokolarne seje ali mehanizem za nadzor dostopa. Protokol ne
zagotavlja, da strežnik ostane znotraj navedenih rootov.

## Cilji učenja

Do konca te lekcije boste lahko:

- Razložili, kaj rooti predstavljajo in česa ne predstavljajo.
- Prepoznali trenutni večkrožni potek `roots/list`.
- Neodvisno uporabljali varnostne kontrole od rootov.
- Migrirali nove implementacije na podprte alternative.

## Podatki o rootih

Klient vrne vsak root kot `file://` URI z neobveznim prikaznim imenom:

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

Klienti naj razkrijejo samo lokacije, ki jih je odobril uporabnik. Strežniki naj
rezultat obravnavajo kot usmeritev glede relevantnih datotek, ne kot dokaz za avtorizacijo.

## MCP 2026-07-28 potek

Klient, ki podpira roote, deklarira to zmožnost pri vsakem zahtevku:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Med obdelavo zahtevka klienta lahko strežnik vrne
`InputRequiredResult`, ki vsebuje zahtevo za vnos `roots/list`:

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

Klient zbere odobrene roote in ponovno pošlje prvotni zahtevek z
ustreznimi `inputResponses` in nespremenjenim `requestState`. Ta večkrožni vzorec
ohranja protokol brezstatusen; ni rokopisa `initialize` ali
protokolne seje.

## Zastaralo vedenje 2025-11-25

Pri MCP `2025-11-25` so klienti objavljali roote med inicializacijo. Strežnik
je lahko poslal neposredno zahtevo `roots/list`, klient pa je lahko poslal
`notifications/roots/list_changed`, ko so se rooti spremenili.

Ta življenjski cikel je zastarelo vedenje. Ne kombinirajte njegovih primerov inicializacije ali
obvestil z implementacijo `2026-07-28`.

## Priporočene nadomestitve

### Parametri orodja

Naredite zahtevan imenik ali datoteko eksplicitno v shemi orodja:

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

### URI-ji virov

Uporabite MCP vire, kadar lahko strežnik razkrije relevantne datoteke preko stabilnih
URI-jev. To ohranja odkrivanje in pridobivanje eksplicitno.

### Strežniška konfiguracija

Za fiksne namestitve konfigurirajte dovoljena imenike ob zagonu strežnika.
To je pogosto bolj jasno kot jih odkrivati med klicem orodja.

## Varnostne zahteve

Ne glede na izbrano nadomestilo:

- Pridobite soglasje uporabnika pred razkritjem lokacij v datotečnem sistemu.
- Kanonizirajte in validirajte poti, da preprečite prestop.
- Neodvisno izvajajte avtorizacijo in peskovnik.
- Dovoljenja ponovno preverjajte, ko se datoteka dostopa, ne samo ob navajanju.
- Izogibajte se vračanju občutljivih poti v dnevnikih ali sporočilih o napakah.

## Glavne ugotovitve

- Rooti opisujejo relevantne lokacije datotečnega sistema; ne shranjujejo stanja
  pogovora.
- Rooti so usmeritve, ne meja nadzora dostopa.
- MCP `2026-07-28` nosi zmožnost na zahtevo in uporablja
  `InputRequiredResult` za `roots/list`.
- Nove implementacije naj uporabijo parametre orodja, URI-je virov ali strežniško
  konfiguracijo.

## Dodatni viri

- [Rooti v MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Register zastarelih funkcij](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [Kaj je spremenjeno v MCP: Specifikacija 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->