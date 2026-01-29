# Täiustatud MCP turvalisus Azure Content Safety abil

Azure Content Safety pakub mitmeid võimsaid tööriistu, mis aitavad parandada teie MCP rakenduste turvalisust:

## Prompt Shields

Microsofti AI Prompt Shields pakub tugevat kaitset nii otseste kui ka kaudsete prompt injection rünnakute vastu, kasutades:

1. **Täiustatud tuvastamine**: Kasutab masinõpet, et tuvastada pahatahtlikke juhiseid, mis on sisus peidetud.
2. **Spotlighting**: Muudab sisendteksti, et aidata AI-süsteemidel eristada kehtivaid juhiseid ja väliseid sisendeid.
3. **Piiritlemine ja andmemärgistamine**: Märgib usaldusväärse ja ebausaldusväärse andmevahelised piirid.
4. **Content Safety integratsioon**: Töötab koos Azure AI Content Safety-ga, et tuvastada jailbreak-katseid ja kahjulikku sisu.
5. **Pidevad uuendused**: Microsoft uuendab regulaarselt kaitsemehhanisme, et vastata uutele ohtudele.

## Azure Content Safety rakendamine MCP-ga

See lähenemine pakub mitmekihilist kaitset:
- Sisendite skaneerimine enne töötlemist
- Väljundite valideerimine enne tagastamist
- Blokiloendite kasutamine teadaolevate kahjulike mustrite jaoks
- Azure'i pidevalt uuendatavate sisuturvalisuse mudelite kasutamine

## Azure Content Safety ressursid

Lisateabe saamiseks Azure Content Safety rakendamise kohta MCP serveritega tutvuge nende ametlike ressurssidega:

1. [Azure AI Content Safety dokumentatsioon](https://learn.microsoft.com/azure/ai-services/content-safety/) - Ametlik dokumentatsioon Azure Content Safety kohta.
2. [Prompt Shield dokumentatsioon](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Õppige, kuidas vältida prompt injection rünnakuid.
3. [Content Safety API viide](https://learn.microsoft.com/rest/api/contentsafety/) - Üksikasjalik API viide Content Safety rakendamiseks.
4. [Kiirstart: Azure Content Safety C#-ga](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Kiire rakendamise juhend C# abil.
5. [Content Safety klienditeegid](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Klienditeegid erinevatele programmeerimiskeeltele.
6. [Jailbreak-katsete tuvastamine](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Spetsiifilised juhised jailbreak-katsete tuvastamiseks ja ennetamiseks.
7. [Parimad praktikad sisuturvalisuse jaoks](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Parimad praktikad sisuturvalisuse tõhusaks rakendamiseks.

Põhjalikuma rakendamise jaoks vaadake meie [Azure Content Safety rakendamise juhendit](./azure-content-safety-implementation.md).

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.