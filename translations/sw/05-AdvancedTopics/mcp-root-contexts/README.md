# Mizizi ya MCP (Sifa ya Kale)

> [!WARNING]
> Mizizi imeachwa rasmi kuanzia MCP `2026-07-28`. Zinabaki katika marekebisho haya kwa ajili ya
> usawazishaji na zinaweza kuondolewa katika marekebisho ya kwanza ya
> vipengele yatakayotolewa tarehe au baada ya Julai 28, 2027. Utekelezaji mpya unapaswa kupitisha
> folda au faili kupitia vigezo vya zana, URI za rasilimali, au usanidi wa seva.


## Muhtasari

Mizizi huruhusu mteja wa MCP kumuambia seva ni maeneo gani ya mfumo wa faili yanayohusiana
na ombi lililopo sasa. Mizizi ina URI inayotakiwa ya `file://` na jina la hiari
linaloweza kusomwa na binadamu.

Mizizi ni vidokezo vya taarifa. Sio vyombo vya kuhifadhi historia ya mazungumzo,
vikao vya itifaki, au njia ya udhibiti wa upatikanaji. Itifaki haina nguvu
ya kulazimisha seva kubaki ndani ya mizizi iliyoorodheshwa.

## Malengo ya Kujifunza

Mwisho wa somo hili, utakuwa na uwezo wa:

- Eleza ni nini Mizizi ya MCP inawakilisha na isiyowakilisha.
- Tambua mchakato wa `roots/list` wa mizunguko mingi ya sasa.
- Tumia udhibiti wa usalama huru na Mizizi.
- Hamisha utekelezaji mpya kwa mbadala zinazotegemewa.

## Data za Mizizi

Mteja hurudisha kila mzizi kama URI ya `file://` yenye jina la kuonyesha la hiari:

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

Wateja wanapaswa kuonyesha maeneo tu yaliyoruhusiwa na mtumiaji. Seva zinapaswa
kutambua matokeo hayo kama mwongozo kuhusu faili muhimu, si kama uthibitisho wa ruhusa.

## Mchakato wa MCP 2026-07-28

Mteja anayeoana na Mizizi hutoa uwezo wake katika kila ombi:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Wakati wa kushughulikia ombi la mteja, seva inaweza kurudisha
`InputRequiredResult` iliyo na ombi la ingizo la `roots/list`:

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

Mteja hukusanya mizizi iliyoruhusiwa na kurudia ombi la awali kwa
`inputResponses` zinazolingana na `requestState` isiyobadilika. Mizunguko hii mingi
hufanya itifaki iwe isiyo na hali; hakuna mkutano wa `initialize` au
kikao cha ngazi ya itifaki.

## Tabia ya Kale ya 2025-11-25

Katika MCP `2025-11-25`, wateja walitangaza Mizizi wakati wa kuanzisha. Seva
ingeweza kutoa ombi la moja kwa moja la `roots/list`, na mteja angeweza kutuma
`notifications/roots/list_changed` wakati mizizi yake ilibadilika.

Mzunguko huu ni tabia ya kale. Usichanganye mifano yake ya uanzishaji au
ya taarifa na utekelezaji wa `2026-07-28`.

## Mbadala Inayopendekezwa

### Vigezo vya Zana

Fanya folda au faili inayotakiwa iwe wazi katika muundo wa zana:

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

### URI za Rasilimali

Tumia Rasilimali za MCP wakati seva inaweza kuonyesha faili zinazohusiana kupitia URI
imara. Hii hufanya ugunduzi na upokeaji kuwa wazi.

### Usanidi wa Seva

Kwa usanifu thabiti, sanidi folda zilizoruhusiwa wakati seva inapoanza.
Hii mara nyingi ni wazi zaidi kuliko kugundua wakati wa wito wa zana.

## Mahitaji ya Usalama

Mbali na mbadala unaochagua:

- Pata idhini ya mtumiaji kabla ya kuonyesha maeneo ya mfumo wa faili.
- Fanya njia kuwa za kawaida na zikague ili kuzuia kupita kwenye mipaka isiyoruhusiwa.
- Tekeleza uthibitishaji na sandbox bila kuhusiana na thamani za mizizi.
- Tathmini ruhusa tena wakati faili inapotakiwa kufikiwa, si tu wakati inaporejelewa.
- Epuka kurudisha njia nyeti katika rekodi za kumbukumbu au ujumbe wa makosa.

## Muhimu Kumbuka

- Mizizi huelezea maeneo muhimu ya mfumo wa faili; hazi hifadhi hali za mazungumzo.

- Mizizi ni mwongozo, si ukomo wa udhibiti wa upatikanaji.
- MCP `2026-07-28` huleta uwezo kwa kila ombi na hutumia
  `InputRequiredResult` kwa `roots/list`.
- Utekelezaji mpya unapaswa kutumia vigezo vya zana, URI za rasilimali, au
  usanidi wa seva badala yake.

## Rasilimali Zaidi

- [Mizizi katika MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Kurikulum ya sifa zilizoezwa](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [Mabadiliko katika MCP: Maelezo ya 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->