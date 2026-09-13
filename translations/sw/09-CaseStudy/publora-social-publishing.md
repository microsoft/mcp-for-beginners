# Uchunguzi wa Kesi: Kuchapisha kwa Mitandao ya Kijamii kutoka kwa Wakala na Serveri ya MCP ya Mbali

> **Onyo:** Huduma kadhaa na miradi ya chanzo huria inaweza kuchapisha kwa mitandao ya kijamii, na timu inaweza pia kuunganisha API ya kila mtandao moja kwa moja. Hali ifuatayo inatolewa kama mfano mmoja uliofanyiwa kazi wa jinsi **serveri ya mbali ya MCP yenye uwezo wa kuandika** inaweza kubuniwa na kutumika. Publora ni huduma ya kibiashara yenye ngazi ya bure; mifumo inayotajwa hapa inatumika kwa serveri yoyote ya MCP inayotekeleza vitendo visivyo vya kurekebishwa kwa niaba ya mtumiaji.

## Muhtasari

Wakala ni wazuri katika kuandaa maudhui na duni katika kuyapeleka. Mfano unaweza kuandika tangazo la kutolewa katika sekunde chache, kisha kazi inakoma: kuchapisha ina maana ya API kwa kila mtandao, programu ya OAuth kwa kila mtandao, na seti tofauti za sheria za vyombo vya habari kwa kila mmoja. Timu nyingi hutatua hili kwa kunakili maandishi kwenye kivinjari kwa mkono.

Uchunguzi huu wa kesi unaangalia jinsi hatua ya mwisho inavyofungwa na serveri moja ya mbali ya MCP, na — kwa njia inayosaidia zaidi kwa yeyote anayeijenga — maamuzi ya kubuni ambayo serveri **enye uwezo wa kuandika** lazima ifanye sawa. Kusoma data ni msamaha. Kuchapisha si hivyo: wito wa zana lisilo sahihi linaonekana kwa hadhira na haliwezi kutendolewa upya.

## Hali ya Kesi

Timu ndogo ya mahusiano ya waendelezaji huandaa machapisho ndani ya wakala (Claude, VS Code, Cursor — mteja hauna maana). Wanataka wakala afanye:

- kuona akaunti za mitandao zilizounganishwa na timu,
- kuandaa chapisho na kukihifadhi kama rasimu kwa binadamu kuikubali,
- kuambatanisha picha,
- kupanga kutolewa kwa mitandao kadhaa kwa wakati uliotolewa,
- na baadaye kuripoti jinsi kilivyofanya kazi.

Muhimu, wanataka wakala asiwe na uwezo wa kuchapisha bila makusudi wakati bado wanajaribu.

## Zana Zilitumika

- [Serveri ya MCP ya Publora](https://github.com/publora/mcp-server) — serveri ya mbali ya MCP (`streamable-http`) inayotolea huduma za kuchapisha, kupanga, vyombo vya habari na zana za uchambuzi za LinkedIn. Imesajiliwa katika rejistu rasmi ya MCP kama `com.publora/mcp-server`.

## Mchakato Hatua kwa Hatua

1. **Unganisha serveri.** Wateja wanaozungumza OAuth hukamilisha mchakato wa msimbo wa idhini kwa PKCE dhidi ya skrini ya ruhusa ya serveri; wateja wasiofanya hivyo, kama CLI zisizo na kichwa, hutumia ufunguo wa API wa Publora kichwani. Njia zote mbili zinasaidiwa, na unayopata hutegemea mteja, si serveri.
2. **Ona orodha ya muunganisho.** Wakala huita `list_connections` na anapokea akaunti zilizounganishwa na vitambulisho vyao.
3. **Tengeneza rasimu.** Wakala huita `create_post` *bila* wakati wa kupanga. Chapisho huhifadhiwa kama rasimu — hakuna kinachochapishwa.
4. **Ambatisha media.** Anuani za picha za umma hupitishwa katika wito huo huo; serveri hupakua na kuthibitisha.
5. **Panga ratiba.** Baada ya binadamu kukubali, `update_post` huweka hali kuwa imepangwa kwa wakati wa ISO 8601.
6. **Pima.** Kwa LinkedIn, `linkedin_post_stats` hurudisha ushiriki mara chapisho linapokuwa hai.

## Mfano wa Ombi

```text
Which social accounts do I have connected?
Draft a post announcing our new changelog page, attach the screenshot at
https://example.com/changelog.png, and keep it as a draft — do not publish it.
Once I approve, schedule it to LinkedIn and Bluesky for tomorrow at 09:00 UTC.
```

## Chati ya Mtiririko ya Mermaid

```mermaid
flowchart TD
    A[Ombi la mtumiaji katika mteja wa MCP] --> B[Mteja hufanya OAuth na seva]
    B --> C[orodha_ya_mitungo]
    C --> D{Mitandao lengwa imeunganishwa?}
    D -- No --> E[Wakala anaripoti ni zipi zilizokosekana]
    D -- Yes --> F[unda_post bila scheduledTime -> rasimu]
    F --> G[Binadamu anapitia rasimu]
    G -- Approved --> H[update_post: hali=imepangwa]
    G -- Rejected --> I[futa_post]
    H --> J[Seva huchapisha wakati uliopangwa]
    J --> K[takwimu_ya_post_ya_linkedin kwa ushiriki]
```

## Utekelezaji wa Kiufundi

Mafunzo yaliyo hapa chini ni sehemu inayoweza kuhamishwa ya uchunguzi huu wa kesi.

### Ugunduzi wazi, utekelezaji uliothibitishwa

`tools/list` hutolewa bila vyeti; kila `tools/call` inahitaji tokeni
na vinginevyo hurudisha `401` na kichwa `WWW-Authenticate` kinachoelekeza kwenye

metadata ya rasilimali iliyolindwa. Sehemu ya zamani ya seva pia hujibu
`initialize` isiyothibitishwa kwa wateja katika toleo za itifaki kabla ya
`2026-07-28`; wateja wa sasa hawatumii mkusanyiko huo.

Ugawanyiko huu maalum wa seva huruhusu rejista, katalogi, na wateja kuchunguza majina ya zana,
skimu, na maelezo kwa siri bila siri wakati wakizuia utekelezaji usiojulikana.
Ugunduzi wazi ni chaguo la usambazaji, si sharti la MCP; usambazaji uliolindwa pia unaweza kuhitaji idhini kwa `tools/list`.


### Usajili: usajili wa mteja unaobadilika, na kinachobadilisha

Seva hupangaza `/.well-known/oauth-protected-resource` na `/.well-known/oauth-authorization-server`, na inaunga mkono mchakato wa ruhusa ya msimbo na PKCE (`S256`), tokeni za kusasisha, na **usajili wa mteja unaobadilika**.

Usajili unaobadilika umeondoa hatua ya mikono kwa wateja wa zamani: bila huo,
kila mteja alikuwa na `client_id` aliyetolewa awali na muuzaji.

Tendea hili kama mwenendo wa uthabiti badala ya muundo wa kunakili. Marekebisho ya `2026-07-28` ya masharti yanaondoa usajili wa mteja unaobadilika kwa faida ya Hati za Metadata za Kitambulisho cha Mteja, ambapo mteja hushikilia hati ya metadata kwenye URL salama ya HTTPS na URL hiyo *ndiyo* `client_id`. DCR inaendelea kufanya kazi kwa sasa, lakini seva inayojengwa leo inapaswa kupanga kwa CIMD na kuweka DCR kwa wateja wa zamani tu.

### Maelezo ya zana si mapambo

Kila zana hubeba `title` na vidokezo vinavyotumika: `readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`.

Sababu mbili za kuwekeza ndani yake. Kwanza, wateja hutumia vidokezo kuamua ni nini kuthibitisha na mtumiaji — mteja anaweza kuendesha moja kwa moja utafutaji wa kusoma tu na kusubiri idhini kabla ya kufuta. Maandalizi ni wazi kwamba maelezo ni vidokezo visivyoaminika, si njia ya idhini: huathiri kile mteja anachotoa kufanya, hazuishi chochote kwenye seva, na seva lazima bado ifuate sheria zake. Pili, saraka kuu za kiunganishi sasa *zinahitaji* hizo kwa mapitio; seva ambayo zana zake hazina majina na vidokezo itarejeshwa hata kama inafanya kazi vizuri.

### Fanya vitambulisho visivyoweza kuvumbuliwa

Vitambulisho vya jukwaa ni mistari isiyo wazi inayopelekwa na `list_connections`, na maelezo ya skimu husema wazi kuwa lazima zikopiwe kama zilivyo na zisitafutwe. Seva inakatia rejea chochote kingine.

Modeli ni wachunguzi wenye mtiririko. Seva yoyote inayoweza kuandika inapaswa kudhani kuwa kitambulisho kitagunduliwa kusuasua na kufanya njia hiyo ishindwe kwa sauti na mapema, badala ya kutekeleza thamani inayoweza kuonekana kuwa halisi.

### Shindwa kabla ya kuchapisha, kwa ujumbe wa vitendo

Mitandao mingine hukataa chapisho la maandishi tu na kuhitaji picha au video. Hiyo huhakikiwa wakati chapisho linapopangwa, na kosa linaeleza jukwaa na mahitaji yaliyokosekana.

Wakala anaweza kurejesha kutoka "Instagram inahitaji media — ambatanisha picha au video" bila ziara nyingine. Haiwezi kurejesha kutoka `400` jumla.

### Fanya jaribio la upya salama

Zana mbili zinazounda maudhui, `create_post` na `update_post`, zinakubali ufunguo wa idempotency: kutumia tena na ombi sawa hurudia jibu halisi badala ya kuunda chapisho la pili. Runtime za wakala hurudia kwenye muda wa kusubiri; bila idempotency, jibu polepole hubadilika kuwa chapisho la nakala. Zana nyingine za kuandika — kufuta, hatua za media, mizozo na maoni ya LinkedIn — hazikubali, hivyo jaribio la upya sio salama moja kwa moja huko. Ni vyema kujua ni mabadiliko yapi yako salama na ni yapi siyo.


### Toa njia ya kujaribu ambayo haichapishi chochote


Seva inapokea lengo lililohifadhiwa, `publora-playground`, ambalo linathibitishwa na kukubaliwa kama eneo halisi na kisha kulifuta — hakuna kinachofikia akaunti hai. Linaelezewa ndani ya muundo wa chombo hicho chenyewe, ambacho mteja yeyote anaweza kusoma bila vyeti vya kuingia: sehemu ya `platforms` ya `create_post` linaelezea hili kama "lengo la kujaribu muunganisho ambalo halihitaji muunganisho halisi — chapisho linakubaliwa na kufutwa, hakuna kinachochapishwa". Laitaje kwa kuipatia kama ingizo pekee: `platforms: ["publora-playground"]`.

Hili lilionekana kuwa moja ya maelezo muhimu zaidi ya uso mzima. Wakaguzi wa orodha za viunganishi, wachangiaji na CI wanaweza kufanya njia kamili ya kuandika kutoka mwanzo hadi mwisho bila hatari kwa hadhira halisi. Seva yeyote ya MCP yenye vitendo visivyorekebishika inafaidika na lengo la no-op lililoandikwa.

## Matokeo na Mwitikio

- Hatua ya kuchapisha ilihamishwa kutoka kivinjari kwenda kwenye mazungumzo yale yale ambapo maudhui yanaandikwa, na tabia ya drftu kwanza huweka mtu katika mzunguko. Kuwa sahihi kuhusu hiyo: drftu ni mkataba, si mpaka. Cheti kilekile kinaweza kupanga au kuchapisha, kwa hivyo mtu yeyote anaye hitaji lango halali la kibali lazima alilazimishe nje ya uso wa chombo — vyeti tofauti, au safu ya sera mbele ya seva.
- Tofauti kwa mitandao — mahitaji ya vyombo vya habari, kuunganisha mazungumzo, udhibiti wa majibu — zinashughulikiwa mara moja kwenye seva badala ya kwa kila wakala anayezungumza nayo.
- Seva ile ile inaunga mkono wateja wengi wa MCP bila vyeti vilivyotolewa awali.
    Wateja wa sasa wanaweza kutumia Nyaraka za Metadata za Kitambulisho cha Mteja; DCR bado ni mbadala
    kwa wateja wa zamani.
- Vizingiti vya muundo vilivyo juu viliumbwa na mapitio ya orodha za viunganishi pamoja na watumiaji: maelezo, OAuth na lengo salama la majaribio kila moja lilihitajika na angalau mmoja wao.

## Marejeleo

- [Seva ya Publora MCP (chanzo)](https://github.com/publora/mcp-server)
- [API ya Publora na nyaraka za MCP](https://docs.publora.com)
- [Kuingia kwa rejista ya MCP: `com.publora/mcp-server`](https://registry.modelcontextprotocol.io/v0/servers?search=com.publora/mcp-server)
- [Maelezo ya MCP — Idhini](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [Maelezo ya MCP — Maelezo ya zana](https://modelcontextprotocol.io/docs/concepts/tools)

## Kile Kifuatacho

- Chukua seva ya MCP unayojenga na angalia mafanikio matatu ya bei nafuu hapa: maelezo kwenye kila chombo, ufunguo wa uhakikisho wa mara moja kwenye kila uandishi, na lengo la no-op lililoandikwa.
- Jaribu mgawanyo wa ugunduzi wazi: piga `tools/list` dhidi ya seva ya mbali ya umma bila vyeti, kisha piga chombo na angalia changamoto ya `401`.
- Fikiria maana ya "kurejesha" kwa eneo lako. Kuchapisha kuna drftu na kufuta; kama vitendo vyako havina kinachofanana, uthibitisho unastahili katika muundo wa chombo, si kwenye daraja.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->