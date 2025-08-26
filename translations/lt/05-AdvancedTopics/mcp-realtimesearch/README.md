<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "333a03e51f90bdf3e6f1ba1694c73f36",
  "translation_date": "2025-08-26T16:34:14+00:00",
  "source_file": "05-AdvancedTopics/mcp-realtimesearch/README.md",
  "language_code": "lt"
}
-->
## Atsakomybės apribojimas dėl kodo pavyzdžių

> **Svarbi pastaba**: Žemiau pateikti kodo pavyzdžiai demonstruoja Model Context Protocol (MCP) integraciją su interneto paieškos funkcionalumu. Nors jie atitinka oficialių MCP SDK struktūras ir modelius, jie yra supaprastinti edukaciniais tikslais.
> 
> Šie pavyzdžiai parodo:
> 
> 1. **Python įgyvendinimas**: FastMCP serverio įgyvendinimas, kuris teikia interneto paieškos įrankį ir jungiasi prie išorinio paieškos API. Šis pavyzdys demonstruoja tinkamą gyvavimo ciklo valdymą, konteksto tvarkymą ir įrankio įgyvendinimą pagal [oficialaus MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) modelius. Serveris naudoja rekomenduojamą Streamable HTTP transportą, kuris pakeitė senesnį SSE transportą gamybos aplinkoje.
> 
> 2. **JavaScript įgyvendinimas**: TypeScript/JavaScript įgyvendinimas naudojant FastMCP modelį iš [oficialaus MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk), siekiant sukurti paieškos serverį su tinkamais įrankių apibrėžimais ir klientų jungtimis. Jis laikosi naujausių rekomenduojamų modelių sesijos valdymui ir konteksto išsaugojimui.
> 
> Šiems pavyzdžiams reikėtų papildomo klaidų tvarkymo, autentifikacijos ir specifinio API integracijos kodo, kad jie būtų tinkami naudoti gamybos aplinkoje. Pateikti paieškos API galiniai taškai (`https://api.search-service.example/search`) yra tik pavyzdiniai ir turėtų būti pakeisti tikrais paieškos paslaugų galiniais taškais.
> 
> Norėdami gauti išsamią įgyvendinimo informaciją ir naujausius metodus, apsilankykite [oficialioje MCP specifikacijoje](https://spec.modelcontextprotocol.io/) ir SDK dokumentacijoje.

## Pagrindinės sąvokos

### Model Context Protocol (MCP) sistema

MCP pagrindas yra standartizuotas būdas AI modeliams, programoms ir paslaugoms keistis kontekstu. Realaus laiko interneto paieškoje ši sistema yra būtina kuriant nuoseklias, daugiapakopes paieškos patirtis. Pagrindiniai komponentai apima:

1. **Kliento-serverio architektūra**: MCP aiškiai atskiria paieškos klientus (užklausų teikėjus) ir paieškos serverius (paslaugų teikėjus), leidžiant lanksčius diegimo modelius.

2. **JSON-RPC komunikacija**: Protokolas naudoja JSON-RPC žinučių mainams, todėl jis suderinamas su interneto technologijomis ir lengvai įgyvendinamas įvairiose platformose.

3. **Konteksto valdymas**: MCP apibrėžia struktūrizuotus metodus, kaip išlaikyti, atnaujinti ir naudoti paieškos kontekstą per kelias sąveikas.

4. **Įrankių apibrėžimai**: Paieškos galimybės pateikiamos kaip standartizuoti įrankiai su aiškiai apibrėžtais parametrais ir grąžinimo reikšmėmis.

5. **Srautinio perdavimo palaikymas**: Protokolas palaiko rezultatų srautinį perdavimą, kuris yra būtinas realaus laiko paieškai, kur rezultatai gali būti pateikiami palaipsniui.

### Interneto paieškos integracijos modeliai

Integruojant MCP su interneto paieška, išryškėja keli modeliai:

#### 1. Tiesioginė paieškos paslaugų teikėjo integracija

```mermaid
graph LR
    Client[MCP Client] --> |MCP Request| Server[MCP Server]
    Server --> |API Call| SearchAPI[Search API]
    SearchAPI --> |Results| Server
    Server --> |MCP Response| Client
```

Šiame modelyje MCP serveris tiesiogiai sąveikauja su viena ar keliomis paieškos API, MCP užklausas paversdamas API specifiniais skambučiais ir formatuodamas rezultatus kaip MCP atsakymus.

#### 2. Federuota paieška su konteksto išsaugojimu

```mermaid
graph LR
    Client[MCP Client] --> |MCP Request| Federation[MCP Federation Layer]
    Federation --> |MCP Request 1| Search1[Search Provider 1]
    Federation --> |MCP Request 2| Search2[Search Provider 2]
    Federation --> |MCP Request 3| Search3[Search Provider 3]
    Search1 --> |MCP Response 1| Federation
    Search2 --> |MCP Response 2| Federation
    Search3 --> |MCP Response 3| Federation
    Federation --> |Aggregated MCP Response| Client
```

Šis modelis paskirsto paieškos užklausas keliems MCP suderinamiems paieškos paslaugų teikėjams, kurie gali specializuotis skirtinguose turinio ar paieškos galimybių tipuose, tuo pačiu išlaikant vieningą kontekstą.

#### 3. Kontekstu praturtinta paieškos grandinė

```mermaid
graph LR
    Client[MCP Client] --> |Query + Context| Server[MCP Server]
    Server --> |1. Query Analysis| NLP[NLP Service]
    NLP --> |Enhanced Query| Server
    Server --> |2. Search Execution| Search[Search Engine]
    Search --> |Raw Results| Server
    Server --> |3. Result Processing| Enhancement[Result Enhancement]
    Enhancement --> |Enhanced Results| Server
    Server --> |Final Results + Updated Context| Client
```

Šiame modelyje paieškos procesas yra padalintas į kelis etapus, kuriuose kontekstas praturtinamas kiekviename žingsnyje, todėl rezultatai tampa vis labiau aktualūs.

### Paieškos konteksto komponentai

MCP pagrįstoje interneto paieškoje kontekstas paprastai apima:

- **Užklausų istoriją**: Ankstesnės paieškos užklausos sesijoje
- **Vartotojo nuostatas**: Kalba, regionas, saugios paieškos nustatymai
- **Sąveikos istoriją**: Kurie rezultatai buvo paspausti, laikas praleistas ties rezultatais
- **Paieškos parametrus**: Filtrai, rūšiavimo tvarka ir kiti paieškos modifikatoriai
- **Domeno žinias**: Kontekstas, susijęs su konkrečia tema
- **Laiko kontekstą**: Su laiku susijusius aktualumo veiksnius
- **Šaltinių nuostatas**: Patikimi ar pageidaujami informacijos šaltiniai

## Naudojimo atvejai ir taikymas

### Tyrimai ir informacijos rinkimas

MCP pagerina tyrimų darbo eigą:

- Išlaikant tyrimų kontekstą per paieškos sesijas
- Leidžiant sudėtingesnes ir kontekstiškai aktualias užklausas
- Palaikant daugiakryptę paieškos federaciją
- Palengvinant žinių išgavimą iš paieškos rezultatų

### Realaus laiko naujienų ir tendencijų stebėjimas

MCP pagrįsta paieška siūlo privalumus naujienų stebėjimui:

- Beveik realaus laiko naujų naujienų istorijų atradimas
- Kontekstiškai filtruojama aktuali informacija
- Temų ir subjektų stebėjimas per kelis šaltinius
- Personalizuoti naujienų pranešimai pagal vartotojo kontekstą

### AI papildytas naršymas ir tyrimai

MCP sukuria naujas galimybes AI papildytam naršymui:

- Kontekstiškai pritaikytos paieškos rekomendacijos pagal dabartinę naršyklės veiklą
- Sklandi interneto paieškos integracija su LLM pagrįstais asistentais
- Daugiapakopė paieškos tobulinimas su išlaikytu kontekstu
- Patobulintas faktų tikrinimas ir informacijos patvirtinimas

## Ateities tendencijos ir inovacijos

### MCP evoliucija interneto paieškoje

Žvelgiant į ateitį, tikimasi, kad MCP evoliucionuos, kad spręstų:

- **Multimodalinę paiešką**: Teksto, vaizdų, garso ir vaizdo paieškos integraciją su išlaikytu kontekstu
- **Decentralizuotą paiešką**: Palaikant paskirstytas ir federuotas paieškos ekosistemas
- **Paieškos privatumas**: Kontekstui jautrūs privatumo užtikrinimo mechanizmai paieškoje  
- **Užklausų supratimas**: Gili semantinė natūralios kalbos paieškos užklausų analizė  

### Galimi technologijų pažangos žingsniai  

Atsirandančios technologijos, kurios formuos MCP paieškos ateitį:  

1. **Neuroninės paieškos architektūros**: MCP optimizuotos paieškos sistemos, pagrįstos įterpimais  
2. **Personalizuotas paieškos kontekstas**: Individualių vartotojų paieškos modelių mokymasis laikui bėgant  
3. **Žinių grafų integracija**: Kontekstinė paieška, sustiprinta specifinių sričių žinių grafais  
4. **Kryžminis modalinis kontekstas**: Konteksto išlaikymas tarp skirtingų paieškos modalumų  

## Praktinės užduotys  

### Užduotis 1: Pagrindinio MCP paieškos proceso nustatymas  

Šioje užduotyje išmoksite:  
- Konfigūruoti pagrindinę MCP paieškos aplinką  
- Įgyvendinti konteksto valdiklius interneto paieškai  
- Testuoti ir patikrinti konteksto išlaikymą per kelias paieškos iteracijas  

### Užduotis 2: Tyrimų asistento kūrimas su MCP paieška  

Sukurkite pilną programą, kuri:  
- Apdoroja natūralios kalbos tyrimų klausimus  
- Atlieka kontekstui jautrias interneto paieškas  
- Sintezuoja informaciją iš kelių šaltinių  
- Pateikia organizuotus tyrimų rezultatus  

### Užduotis 3: MCP pagrįstos daugiakanalės paieškos federacijos įgyvendinimas  

Pažengusi užduotis, apimanti:  
- Kontekstui jautrų užklausų paskirstymą keliems paieškos varikliams  
- Rezultatų reitingavimą ir agregavimą  
- Kontekstinį paieškos rezultatų dublikatų šalinimą  
- Šaltiniui specifinių metaduomenų tvarkymą  

## Papildomi ištekliai  

- [Model Context Protocol Specification](https://spec.modelcontextprotocol.io/) - Oficialus MCP specifikacijos ir protokolo dokumentacijos šaltinis  
- [Model Context Protocol Documentation](https://modelcontextprotocol.io/) - Išsamūs vadovai ir įgyvendinimo gairės  
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Oficialus MCP protokolo Python įgyvendinimas  
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Oficialus MCP protokolo TypeScript įgyvendinimas  
- [MCP Reference Servers](https://github.com/modelcontextprotocol/servers) - MCP serverių pavyzdiniai įgyvendinimai  
- [Bing Web Search API Documentation](https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/overview) - „Microsoft“ interneto paieškos API  
- [Google Custom Search JSON API](https://developers.google.com/custom-search/v1/overview) - „Google“ programuojamos paieškos variklis  
- [SerpAPI Documentation](https://serpapi.com/search-api) - Paieškos variklio rezultatų puslapio API  
- [Meilisearch Documentation](https://www.meilisearch.com/docs) - Atvirojo kodo paieškos variklis  
- [Elasticsearch Documentation](https://www.elastic.co/guide/index.html) - Paskirstytas paieškos ir analizės variklis  
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction) - Programų kūrimas su LLM  

## Mokymosi rezultatai  

Baigę šį modulį, galėsite:  

- Suprasti realaus laiko interneto paieškos pagrindus ir jos iššūkius  
- Paaiškinti, kaip Model Context Protocol (MCP) pagerina realaus laiko interneto paieškos galimybes  
- Įgyvendinti MCP pagrįstas paieškos sprendimus naudojant populiarias sistemas ir API  
- Kurti ir diegti mastelio keičiamas, aukštos našumo MCP paieškos architektūras  
- Taikyti MCP koncepcijas įvairiems atvejams, įskaitant semantinę paiešką, tyrimų asistavimą ir AI papildytą naršymą  
- Įvertinti atsirandančias tendencijas ir ateities inovacijas MCP pagrįstose paieškos technologijose  

### Pasitikėjimo ir saugumo aspektai  

Įgyvendinant MCP pagrįstus interneto paieškos sprendimus, prisiminkite šiuos svarbius MCP specifikacijos principus:  

1. **Vartotojo sutikimas ir kontrolė**: Vartotojai turi aiškiai sutikti ir suprasti visus duomenų prieigos ir operacijų aspektus. Tai ypač svarbu interneto paieškos įgyvendinimuose, kurie gali pasiekti išorinius duomenų šaltinius.  

2. **Duomenų privatumas**: Užtikrinkite tinkamą paieškos užklausų ir rezultatų tvarkymą, ypač kai jie gali apimti jautrią informaciją. Įgyvendinkite tinkamas prieigos kontrolės priemones vartotojų duomenų apsaugai.  

3. **Įrankių saugumas**: Įgyvendinkite tinkamą įrankių autorizaciją ir validaciją, nes jie gali kelti saugumo riziką vykdant savavališką kodą. Įrankių elgsenos aprašymai turėtų būti laikomi nepatikimais, nebent jie gauti iš patikimo serverio.  

4. **Aiški dokumentacija**: Pateikite aiškią dokumentaciją apie savo MCP pagrįsto paieškos įgyvendinimo galimybes, apribojimus ir saugumo aspektus, laikantis MCP specifikacijos gairių.  

5. **Tvirti sutikimo procesai**: Sukurkite tvirtus sutikimo ir autorizacijos procesus, kurie aiškiai paaiškina, ką daro kiekvienas įrankis prieš jį autorizuojant, ypač įrankiams, kurie sąveikauja su išoriniais interneto ištekliais.  

Išsamią informaciją apie MCP saugumo ir pasitikėjimo aspektus rasite [oficialioje dokumentacijoje](https://modelcontextprotocol.io/specification/2025-03-26#security-and-trust-%26-safety).  

## Kas toliau  

- [5.12 Entra ID Authentication for Model Context Protocol Servers](../mcp-security-entra/README.md)  

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.