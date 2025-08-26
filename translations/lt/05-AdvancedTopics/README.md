<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d204bc94ea6027d06a703b21b711ca57",
  "translation_date": "2025-08-26T16:21:30+00:00",
  "source_file": "05-AdvancedTopics/README.md",
  "language_code": "lt"
}
-->
# Pažangios MCP Temos

[![Pažangios MCP: Saugūs, Skalabilūs ir Daugiarūšiai AI Agentai](../../../translated_images/06.42259eaf91fccfc6d06ef1c126c9db04bbff9e5f60a87b782a2ec2616163142f.lt.png)](https://youtu.be/4yjmGvJzYdY)

_(Spustelėkite aukščiau esančią nuotrauką, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

Šiame skyriuje aptariamos pažangios Model Context Protocol (MCP) įgyvendinimo temos, įskaitant daugiarūšę integraciją, skalabilumą, saugumo geriausias praktikas ir integraciją su įmonių sistemomis. Šios temos yra itin svarbios kuriant patikimas ir gamybai paruoštas MCP programas, kurios atitinka šiuolaikinių AI sistemų poreikius.

## Apžvalga

Šioje pamokoje nagrinėjami pažangūs Model Context Protocol įgyvendinimo aspektai, daugiausia dėmesio skiriant daugiarūšiai integracijai, skalabilumui, saugumo geriausioms praktikoms ir integracijai su įmonių sistemomis. Šios temos yra būtinos kuriant gamybai pritaikytas MCP programas, kurios gali patenkinti sudėtingus reikalavimus įmonių aplinkose.

## Mokymosi Tikslai

Šios pamokos pabaigoje galėsite:

- Įgyvendinti daugiarūšes galimybes MCP sistemose
- Kurti skalabilias MCP architektūras didelės apkrovos scenarijams
- Taikyti saugumo geriausias praktikas, atitinkančias MCP saugumo principus
- Integruoti MCP su įmonių AI sistemomis ir platformomis
- Optimizuoti našumą ir patikimumą gamybinėje aplinkoje

## Pamokos ir Pavyzdiniai Projektai

| Nuoroda | Pavadinimas | Aprašymas |
|---------|-------------|-----------|
| [5.1 Integracija su Azure](./mcp-integration/README.md) | Integracija su Azure | Sužinokite, kaip integruoti savo MCP serverį su Azure |
| [5.2 Daugiarūšiai pavyzdžiai](./mcp-multi-modality/README.md) | MCP Daugiarūšiai pavyzdžiai | Pavyzdžiai su garsu, vaizdais ir daugiarūšiais atsakymais |
| [5.3 MCP OAuth2 pavyzdys](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 Demonstracija | Minimalus Spring Boot programos pavyzdys, rodantis OAuth2 su MCP kaip autorizacijos ir resursų serveriu. Demonstracija apima saugių žetonų išdavimą, apsaugotus galinius taškus, Azure Container Apps diegimą ir API valdymo integraciją. |
| [5.4 Pagrindiniai Kontekstai](./mcp-root-contexts/README.md) | Pagrindiniai kontekstai | Sužinokite daugiau apie pagrindinius kontekstus ir kaip juos įgyvendinti |
| [5.5 Maršrutizavimas](./mcp-routing/README.md) | Maršrutizavimas | Sužinokite apie skirtingus maršrutizavimo tipus |
| [5.6 Imčių Rinkimas](./mcp-sampling/README.md) | Imčių rinkimas | Sužinokite, kaip dirbti su imčių rinkimu |
| [5.7 Skalavimas](./mcp-scaling/README.md) | Skalavimas | Sužinokite apie MCP skalavimą |
| [5.8 Saugumas](./mcp-security/README.md) | Saugumas | Užtikrinkite savo MCP serverio saugumą |
| [5.9 Tinklo Paieškos Pavyzdys](./web-search-mcp/README.md) | Tinklo Paieška MCP | Python MCP serveris ir klientas, integruojantis su SerpAPI realaus laiko tinklo, naujienų, produktų paieškai ir klausimų-atsakymų funkcijoms. Demonstracija apima daugių įrankių koordinavimą, išorinių API integraciją ir patikimą klaidų valdymą. |
| [5.10 Realaus Laiko Transliavimas](./mcp-realtimestreaming/README.md) | Transliavimas | Realaus laiko duomenų transliavimas yra būtinas šiuolaikiniame duomenų valdomame pasaulyje, kur verslai ir programos reikalauja greitos prieigos prie informacijos, kad galėtų priimti laiku sprendimus. |
| [5.11 Realaus Laiko Tinklo Paieška](./mcp-realtimesearch/README.md) | Tinklo Paieška | Kaip MCP keičia realaus laiko tinklo paiešką, suteikdamas standartizuotą požiūrį į konteksto valdymą tarp AI modelių, paieškos variklių ir programų. |
| [5.12 Entra ID Autentifikacija MCP Serveriams](./mcp-security-entra/README.md) | Entra ID Autentifikacija | Microsoft Entra ID siūlo patikimą debesų pagrindu veikiančią tapatybės ir prieigos valdymo sprendimą, padedantį užtikrinti, kad tik įgalioti vartotojai ir programos galėtų sąveikauti su jūsų MCP serveriu. |
| [5.13 Azure AI Foundry Agentų Integracija](./mcp-foundry-agent-integration/README.md) | Azure AI Foundry Integracija | Sužinokite, kaip integruoti Model Context Protocol serverius su Azure AI Foundry agentais, leidžiant galingą įrankių koordinavimą ir įmonių AI galimybes su standartizuotais išorinių duomenų šaltinių ryšiais. |
| [5.14 Konteksto Inžinerija](./mcp-contextengineering/README.md) | Konteksto Inžinerija | Ateities galimybės konteksto inžinerijos technikoms MCP serveriuose, įskaitant konteksto optimizavimą, dinaminį konteksto valdymą ir efektyvaus užklausų inžinerijos strategijas MCP sistemose. |

## Papildomi Šaltiniai

Norėdami gauti naujausią informaciją apie pažangias MCP temas, žr.:
- [MCP Dokumentacija](https://modelcontextprotocol.io/)
- [MCP Specifikacija](https://spec.modelcontextprotocol.io/)
- [GitHub Saugykla](https://github.com/modelcontextprotocol)

## Pagrindinės Išvados

- Daugiarūšės MCP įgyvendinimo galimybės išplečia AI funkcionalumą už teksto apdorojimo ribų
- Skalavimas yra būtinas įmonių diegimams ir gali būti pasiektas horizontaliu bei vertikaliu būdu
- Išsamios saugumo priemonės apsaugo duomenis ir užtikrina tinkamą prieigos kontrolę
- Integracija su tokiomis platformomis kaip Azure OpenAI ir Microsoft AI Foundry sustiprina MCP galimybes
- Pažangūs MCP įgyvendinimai naudingi dėl optimizuotų architektūrų ir kruopštaus išteklių valdymo

## Užduotis

Sukurkite įmonės lygio MCP įgyvendinimą konkrečiam naudojimo atvejui:

1. Nustatykite daugiarūšius reikalavimus savo naudojimo atvejui
2. Apibrėžkite saugumo kontrolės priemones jautrių duomenų apsaugai
3. Sukurkite skalabilią architektūrą, galinčią susidoroti su kintama apkrova
4. Suplanuokite integracijos taškus su įmonių AI sistemomis
5. Dokumentuokite galimus našumo trūkumus ir jų šalinimo strategijas

## Papildomi Ištekliai

- [Azure OpenAI Dokumentacija](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft AI Foundry Dokumentacija](https://learn.microsoft.com/en-us/ai-services/)

---

## Kas Toliau

- [5.1 MCP Integracija](./mcp-integration/README.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.