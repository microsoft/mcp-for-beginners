# MCP Korijeni (Zastarjela značajka)

> [!WARNING]
> Korijeni su zastarjeli od MCP `2026-07-28`. Ostaju u ovoj reviziji radi
> kompatibilnosti i mogu se ukloniti u prvoj reviziji specifikacije
> objavljenoj ili nakon 28. srpnja 2027. Nove implementacije trebaju prosljeđivati
> direktorije ili datoteke putem parametara alata, URI-ja resursa ili konfiguracije poslužitelja.


## Pregled

Korijeni omogućuju MCP klijentu da serveru kaže koje lokacije datotečnog sustava su relevantne
za trenutačni zahtjev. Korijen sadrži obavezni `file://` URI i neobavezni
ljudski čitljiv naziv.

Korijeni su informativni pokazatelji. Nisu spremnici povijesti razgovora,
protokolarne sesije ili mehanizam kontrole pristupa. Protokol ne
zahtijeva da se poslužitelj drži unutar navedenih korijena.

## Ciljevi učenja

Do kraja ove lekcije moći ćete:

- Objasniti što MCP Korijeni predstavljaju, a što ne predstavljaju.
- Prepoznati trenutačni `roots/list` višekratni tijek.
- Primijeniti sigurnosne kontrole neovisno o Korijenima.
- Migrirati nove implementacije na podržane alternative.

## Podaci o korijenu

Klijent vraća svaki korijen kao `file://` URI s neobaveznim prikaznim imenom:

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

Klijenti trebaju izložiti samo lokacije odobrene od strane korisnika. Poslužitelji trebaju tretirati
rezultat kao smjernicu o relevantnim datotekama, a ne kao dokaz ovlaštenja.

## MCP 2026-07-28 tijek

Klijent koji podržava Korijene deklarira tu mogućnost u svakom zahtjevu:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Tijekom obrade zahtjeva klijenta, poslužitelj može vratiti
`InputRequiredResult` koji sadrži zahtjev za unos `roots/list`:

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

Klijent prikuplja odobrene korijene i ponovno šalje izvornik zahtjeva s
odgovarajućim `inputResponses` i nepromijenjenim `requestState`. Ovaj višekratni
obrazac zadržava protokol bez statusa; nema rukovanja `initialize` ili
sesije na razini protokola.

## Zastarjelo ponašanje 2025-11-25

U MCP `2025-11-25`, klijenti su oglašavali Korijene tijekom inicijalizacije. Poslužitelj
je mogao poslati izravan zahtjev `roots/list`, a klijent je mogao slati
`notifications/roots/list_changed` kada su se njegovi korijeni promijenili.

Taj životni ciklus je zastarjelo ponašanje. Nemojte kombinirati njegove primjere inicijalizacije ili
obavijesti sa implementacijom `2026-07-28`.

## Preporučene zamjene

### Parametri alata

Napravite obavezni direktorij ili datoteku eksplicitnim u shemi alata:

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

### URI resursa

Koristite MCP Resurse kad poslužitelj može izložiti relevantne datoteke putem stabilnih
URI-ja. Time su otkrivanje i dohvat eksplicitni.

### Konfiguracija poslužitelja

Za fiksne implementacije, konfigurirajte dopuštene direktorije pri pokretanju poslužitelja.
Ovo je često jasnije nego otkrivanje tijekom poziva alata.

## Sigurnosni zahtjevi

Koju god zamjenu odabrali:

- Dobijte pristanak korisnika prije izlaganja lokacija datotečnog sustava.
- Kanonizirajte i provjerite putanje radi sprečavanja prelaska (traversal).
- Provodite ovlaštenje i sandboxing neovisno o vrijednostima korijena.
- Ponovno provjeravajte dozvole prilikom pristupa datoteci, ne samo kada se navodi.
- Izbjegavajte vraćanje osjetljivih putanja u zapisima ili porukama o pogreškama.

## Ključne točke

- Korijeni opisuju relevantne lokacije datotečnog sustava; ne pohranjuju stanje
  razgovora.
- Korijeni su smjernice, nisu granica kontrole pristupa.
- MCP `2026-07-28` nosi mogućnost po zahtjevu i koristi
  `InputRequiredResult` za `roots/list`.
- Nove implementacije trebaju koristiti parametre alata, URI-je resursa ili konfiguraciju
  poslužitelja.

## Dodatni izvori

- [Korijeni u MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Registar zastarjelih značajki](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [Što se promijenilo u MCP-u: Specifikacija 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->