# Напредна MCP безбедност са Azure Content Safety

Azure Content Safety пружа неколико моћних алата који могу побољшати безбедност ваших MCP имплементација:

## Prompt Shields

Microsoft-ови AI Prompt Shields обезбеђују јаку заштиту од директних и индиректних напада убацивањем инструкција кроз:

1. **Напредно откривање**: Користи машинско учење за идентификовање злонамерних упутстава уграђених у садржај.
2. **Истакнуто приказивање**: Претвара улазни текст како би AI системи могли да разликују важеће инструкције од спољних уноса.
3. **Делимитери и означавање података**: Обележава границе између поузданих и непоузданих података.
4. **Интеграција са Content Safety**: Сарађује са Azure AI Content Safety за откривање покушаја заобилажења и штетног садржаја.
5. **Континуирана ажурирања**: Microsoft редовно ажурира механизме заштите против нових претњи.

## Имплементација Azure Content Safety са MCP

Овај приступ пружа вишеслојну заштиту:
- Скенирање уноса пре обраде
- Валидација излаза пре враћања
- Коришћење блок-листа за познате штетне обрасце
- Коришћење континуирано ажурираних модела за безбедност садржаја из Azure-а

## Ресурси за Azure Content Safety

За више информација о имплементацији Azure Content Safety са вашим MCP серверима, консултујте ове званичне ресурсе:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Званична документација за Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Сазнајте како спречити нападе убацивањем инструкција.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Детаљна API референца за имплементацију Content Safety.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Брзи водич за имплементацију користећи C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Клијентске библиотеке за различите програмске језике.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Посебна упутства за откривање и спречавање покушаја заобилажења.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Најбоље праксе за ефикасну имплементацију безбедности садржаја.

За детаљнију имплементацију, погледајте наш [водич за имплементацију Azure Content Safety](./azure-content-safety-implementation.md).

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.