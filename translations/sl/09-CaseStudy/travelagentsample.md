# Študija primera: Azure AI Travel Agents – referenčna implementacija

## Pregled

[Azure AI Travel Agents](https://github.com/Azure-Samples/azure-ai-travel-agents) je celovita referenčna rešitev, ki jo je razvilo podjetje Microsoft in prikazuje, kako zgraditi aplikacijo za načrtovanje potovanj z več agenti, ki jo poganja umetna inteligenca, z uporabo Model Context Protocol (MCP), Azure OpenAI in Azure AI Search. Ta projekt prikazuje najboljše prakse za usklajevanje več AI agentov, integracijo podatkov podjetja in zagotavljanje varne, razširljive platforme za resnične scenarije.

## Ključne funkcije
- **Usklajevanje več agentov:** Uporablja MCP za koordinacijo specializiranih agentov (npr. agenti za lete, hotele in itinerarje), ki sodelujejo pri izpolnjevanju zahtevnih nalog načrtovanja potovanj.
- **Integracija podatkov podjetja:** Povezuje se z Azure AI Search in drugimi viri podatkov podjetja, da zagotovi ažurne in relevantne informacije za priporočila potovanj.
- **Varnostna in razširljiva arhitektura:** Izkorišča Azure storitve za avtentikacijo, avtorizacijo in razširljivo nameščanje, pri čemer sledi najboljšim varnostnim praksam podjetij.
- **Razširljiva orodja:** Uvaja ponovno uporabna MCP orodja in predloge pozivov, kar omogoča hitro prilagajanje novim področjem ali poslovnim zahtevam.
- **Uporabniška izkušnja:** Omogoča pogovorni vmesnik, preko katerega uporabniki komunicirajo z agenti za potovanja, ki jih poganjata Azure OpenAI in MCP.

## Arhitektura
![Architecture](https://raw.githubusercontent.com/Azure-Samples/azure-ai-travel-agents/main/docs/ai-travel-agents-architecture-diagram.png)

### Opis arhitekturne sheme

Rešitev Azure AI Travel Agents je zasnovana za modularnost, razširljivost in varno integracijo več AI agentov ter virov podatkov podjetja. Glavne komponente in potek podatkov so naslednji:

- **Uporabniški vmesnik:** Uporabniki komunicirajo s sistemom preko pogovornega UI (kot je spletni klepet ali Teams bot), ki pošilja uporabniške poizvedbe in prejema priporočila za potovanja.
- **MCP strežnik:** Deluje kot osrednji koordinator, prejema uporabniške vnose, upravlja kontekst in usklajuje delo specializiranih agentov (npr. FlightAgent, HotelAgent, ItineraryAgent) preko Model Context Protocol.
- **AI agenti:** Vsak agent je odgovoren za določeno področje (leti, hoteli, itinerarji) in je implementiran kot MCP orodje. Agenti uporabljajo predloge pozivov in logiko za obdelavo zahtev in generiranje odgovorov.
- **Azure OpenAI Service:** Omogoča napredno razumevanje in generiranje naravnega jezika, kar agentom pomaga razumeti uporabniške namene in ustvarjati pogovorne odgovore.
- **Azure AI Search & podatki podjetja:** Agenti poizvedujejo Azure AI Search in druge vire podatkov podjetja, da pridobijo ažurne informacije o letih, hotelih in možnostih potovanj.
- **Avtentikacija in varnost:** Integrira se z Microsoft Entra ID za varno avtentikacijo in uporablja načelo najmanjših privilegijev za dostop do vseh virov.
- **Nameščanje:** Zasnovano za nameščanje na Azure Container Apps, kar zagotavlja razširljivost, nadzor in operativno učinkovitost.

Ta arhitektura omogoča nemoteno usklajevanje več AI agentov, varno integracijo s podatki podjetja in robustno, razširljivo platformo za gradnjo AI rešitev, prilagojenih posameznim področjem.

## Korak za korakom pojasnilo arhitekturne sheme
Predstavljajte si, da načrtujete veliko potovanje in imate ekipo strokovnih pomočnikov, ki vam pomagajo pri vsakem detajlu. Sistem Azure AI Travel Agents deluje podobno, uporablja različne dele (kot člane ekipe), ki imajo vsak svojo specialno nalogo. Tako se vse poveže:

### Uporabniški vmesnik (UI):
To je kot recepcija vašega potovalnega agenta. Tukaj vi (uporabnik) postavljate vprašanja ali oddajate zahteve, na primer “Najdi mi let v Pariz.” To je lahko klepetalno okno na spletni strani ali aplikacija za sporočila.

### MCP strežnik (koordinator):
MCP strežnik je kot vodja, ki posluša vašo zahtevo na recepciji in odloči, kateri specialist naj obravnava posamezen del. Spremlja vaš pogovor in skrbi, da vse poteka gladko.

### AI agenti (specialistični pomočniki):
Vsak agent je strokovnjak za določeno področje – eden pozna vse o letih, drugi o hotelih, tretji o načrtovanju itinerarija. Ko zahtevate potovanje, MCP strežnik pošlje vašo zahtevo pravim agentom. Ti agenti uporabijo svoje znanje in orodja, da najdejo najboljše možnosti za vas.

### Azure OpenAI Service (jezikovni strokovnjak):
To je kot imeti jezikovnega strokovnjaka, ki razume natanko, kaj sprašujete, ne glede na to, kako to izrazite. Pomaga agentom razumeti vaše zahteve in odgovoriti v naravnem, pogovornem jeziku.

### Azure AI Search & podatki podjetja (informacijska knjižnica):
Predstavljajte si ogromno, ažurno knjižnico z vsemi najnovejšimi informacijami o potovanjih – urniki letov, razpoložljivost hotelov in še več. Agenti preiskujejo to knjižnico, da vam zagotovijo najbolj točne odgovore.

### Avtentikacija in varnost (varnostnik):
Tako kot varnostnik preverja, kdo lahko vstopi v določena območja, ta del zagotavlja, da do občutljivih informacij dostopajo le pooblaščene osebe in agenti. Vaše podatke varuje in ohranja zasebne.

### Nameščanje na Azure Container Apps (stavba):
Vsi ti pomočniki in orodja delujejo skupaj v varni, razširljivi stavbi (oblaku). To pomeni, da sistem lahko hkrati podpira veliko uporabnikov in je vedno na voljo, ko ga potrebujete.

## Kako vse skupaj deluje:

Najprej postavite vprašanje na recepciji (UI).  
Vodja (MCP strežnik) ugotovi, kateri specialist (agent) vam lahko pomaga.  
Specialist uporabi jezikovnega strokovnjaka (OpenAI), da razume vašo zahtevo, in knjižnico (AI Search), da najde najboljši odgovor.  
Varnostnik (avtentikacija) poskrbi, da je vse varno.  
Vse to poteka v zanesljivi, razširljivi stavbi (Azure Container Apps), zato je vaša izkušnja gladka in varna.  
Ta timsko delo omogoča sistemu, da vam hitro in varno pomaga načrtovati potovanje, kot bi delala ekipa strokovnih potovalnih agentov v sodobni pisarni!

## Tehnična implementacija
- **MCP strežnik:** Gostuje osnovno logiko usklajevanja, izpostavlja orodja agentov in upravlja kontekst za večstopenjske delovne tokove načrtovanja potovanj.
- **Agenti:** Vsak agent (npr. FlightAgent, HotelAgent) je implementiran kot MCP orodje s svojimi predlogami pozivov in logiko.
- **Integracija z Azure:** Uporablja Azure OpenAI za razumevanje naravnega jezika in Azure AI Search za pridobivanje podatkov.
- **Varnost:** Integrira se z Microsoft Entra ID za avtentikacijo in uporablja načelo najmanjših privilegijev za dostop do vseh virov.
- **Nameščanje:** Podpira nameščanje na Azure Container Apps za razširljivost in operativno učinkovitost.

## Rezultati in vpliv
- Prikazuje, kako se MCP lahko uporabi za usklajevanje več AI agentov v resničnem, produkcijskem okolju.
- Pospešuje razvoj rešitev z zagotavljanjem ponovno uporabnih vzorcev za koordinacijo agentov, integracijo podatkov in varno nameščanje.
- Služi kot načrt za gradnjo področju prilagojenih aplikacij, ki jih poganja umetna inteligenca, z uporabo MCP in Azure storitev.

## Reference
- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)
- [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.