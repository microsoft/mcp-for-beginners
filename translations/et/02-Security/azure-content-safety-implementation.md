# Azure Content Safety rakendamine MCP-ga

MCP turvalisuse tugevdamiseks prompt injection'i, tööriistade mürgitamise ja muude AI-spetsiifiliste haavatavuste vastu on väga soovitatav integreerida Azure Content Safety.

## Integreerimine MCP serveriga

Azure Content Safety integreerimiseks oma MCP serveriga lisage sisu turvafilter vahevara (middleware) oma päringute töötlemise torujuhtmesse:

1. Initsialiseerige filter serveri käivitamisel
2. Kontrollige kõiki sissetulevaid tööriistapäringuid enne nende töötlemist
3. Kontrollige kõiki väljaminevaid vastuseid enne nende klientidele tagastamist
4. Logige ja andke märku turvarikkumistest
5. Rakendage sobiv veakäsitlus ebaõnnestunud sisu turvakontrollide korral

See tagab tugeva kaitse järgmiste ohtude vastu:
- Prompt injection rünnakud
- Tööriistade mürgitamise katsed
- Andmete lekkimine pahatahtlike sisendite kaudu
- Kahjuliku sisu genereerimine

## Parimad tavad Azure Content Safety integreerimiseks

1. **Kohandatud blokeerimisnimekirjad**: Looge MCP injection mustrite jaoks spetsiaalsed kohandatud blokeerimisnimekirjad
2. **Tõsiduse häälestamine**: Kohandage tõsiduse läve vastavalt oma konkreetsele kasutusjuhtumile ja riskitaluvusele
3. **Põhjalik katvus**: Rakendage sisu turvakontrollid kõigile sisenditele ja väljunditele
4. **Jõudluse optimeerimine**: Kaaluge korduvate sisu turvakontrollide jaoks vahemälu kasutamist
5. **Varumehhanismid**: Määratlege selged varukäitumised juhuks, kui sisu turvateenused pole saadaval
6. **Kasutajate tagasiside**: Andke kasutajatele selget tagasisidet, kui sisu blokeeritakse turvakaalutlustel
7. **Pidev täiustamine**: Uuendage regulaarselt blokeerimisnimekirju ja mustreid vastavalt uutele ohtudele

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.