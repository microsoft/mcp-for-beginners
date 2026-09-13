# MCP Roots (Perintöominaisuus)

> [!WARNING]
> Roots on poistettu käytöstä MCP:ssä `2026-07-28` alkaen. Ne säilyvät tässä julkaisussa
> yhteensopivuuden vuoksi ja ne voidaan poistaa ensimmäisessä määrittelymuutoksessa,
> joka julkaistaan 28. heinäkuuta 2027 tai sen jälkeen. Uusissa toteutuksissa tulisi
> välittää hakemistot tai tiedostot työkalun parametreina, resurssi-URI:ina tai palvelimen
> konfiguraation kautta.

## Yleiskatsaus

Roots sallivat MCP-asiakkaan ilmoittaa palvelimelle, mitkä tiedostojärjestelmän sijainnit
ovat olennaisia nykyisen pyynnön kannalta. Juuri sisältää pakollisen `file://` URI:n
ja valinnaisen ihmisen luettavissa olevan nimen.

Roots ovat informatiivisia vihjeitä. Ne eivät ole keskusteluhistorian säilytyspaikkoja,
protokolla-istuntoja tai käyttöoikeuksien valvontamekanismeja. Protokolla ei pakota
palvelinta pysymään luetelluissa juurissa.

## Oppimistavoitteet

Tämän oppitunnin lopuksi osaat:

- Selittää, mitä MCP Roots edustavat ja mitä ne eivät edusta.
- Tunnistaa nykyisen `roots/list` monikierroksisen vuorovaikutusmallin.
- Soveltaa suojaustoimenpiteitä erillään Roots:ista.
- Siirtyä uusissa toteutuksissa tuettuihin vaihtoehtoihin.

## Root-tiedot

Asiakas palauttaa jokaisen juuren `file://` URI:na, johon voi sisältyä valinnainen näyttönimi:

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

Asiakkaiden tulee näyttää vain käyttäjän hyväksymät sijainnit. Palvelinten tulisi
käsitellä tulosta ohjeistuksena olennaisista tiedostoista, ei valtuutuksen todisteena.

## MCP 2026-07-28 -virtaus

Rooteja tukevat asiakkaat ilmoittavat kyvykkyytensä jokaisessa pyynnössä:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Asiakaspyynnön käsittelyssä palvelin voi palauttaa `InputRequiredResult`-vastauksen,
joka sisältää `roots/list` -syötepyynnön:

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

Asiakas kerää hyväksytyt rootit ja yrittää uudelleen alkuperäisen pyynnön vastaavat
`inputResponses` ja muuttumattoman `requestState` kanssa. Tämä monikierroksinen
malli pitää protokollan tilattomana; ei ole `initialize`-kättelyä tai
protokollatason istuntoa.

## Perintökäyttäytyminen 2025-11-25

MCP `2025-11-25` -versiossa asiakkaat ilmoittivat Rootit alustusvaiheessa. Palvelin
saattoi tehdä suoran `roots/list`-pyynnön, ja asiakas saattoi lähettää
`notifications/roots/list_changed` kun sen juuret muuttuivat.

Tämä elinkaarimalli on perintökäyttäytymistä. Älä yhdistä sen alustus- tai
ilmoitus-esimerkkejä `2026-07-28` -toteutukseen.

## Suositellut korvaavat menetelmät

### Työkalun parametrit

Tee vaadittu hakemisto tai tiedosto eksplisiittiseksi työkalun kaavassa:

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

### Resurssi-URI:t

Käytä MCP-resursseja silloin, kun palvelin voi näyttää olennaiset tiedostot stabiilien
URI:iden kautta. Tämä tekee löytämisestä ja hakemisesta selkeää.

### Palvelimen konfiguraatio

Kiinteissä käyttöönotossa konfiguroi sallitut hakemistot palvelimen käynnistyessä.
Tämä on usein selkeämpää kuin niiden löytäminen työkalukutsun aikana.

## Turvavaatimukset

Valitsemasi korvaava menetelmä riippumatta:

- Hanki käyttäjän suostumus ennen tiedostojärjestelmän sijaintien näyttämistä.
- Kanonisoida ja validoida polut estääksesi hakemistojen läpikäynnin.
- Pakota valtuutus ja hiekkalaatikkotoiminnot erillään root-arvoista.
- Tarkista oikeudet uudelleen tiedostoon käytettäessä, ei pelkästään listattaessa.
- Vältä herkän polun palauttamista lokeissa tai virheilmoituksissa.

## Keskeiset havainnot

- Roots kuvaavat olennaisia tiedostojärjestelmän sijainteja; ne eivät säilytä keskustelun
  tilaa.
- Roots ovat ohjeita, eivät käyttöoikeuksien hallintaraja.
- MCP `2026-07-28` kantaa kyvykkyyden pyyntökohtaisesti ja käyttää
  `InputRequiredResult`-tasoa `roots/list`:in kanssa.
- Uusien toteutusten tulisi käyttää sen sijaan työkaluparametreja, resurssi-URI:ita tai
  palvelimen konfiguraatiota.

## Lisäresurssit

- [Roots MCP 2026-07-28:ssa](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Poistetut ominaisuudet](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [Mitä MCP:ssä on muuttunut: 2026-07-28 -määrittely](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->