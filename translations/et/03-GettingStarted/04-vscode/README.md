# GitHub Copilot Agent režiimis serveri kasutamine

Visual Studio Code ja GitHub Copilot võivad toimida kliendina ja kasutada MCP serverit. Miks me seda teha tahaksime, võite küsida? Noh, see tähendab, et kõik MCP serveri funktsioonid on nüüd saadaval otse teie IDE-s. Kujutage ette, et lisate näiteks GitHubi MCP serveri – see võimaldaks GitHubi juhtimist loomuliku keele kaudu, ilma et peaksite terminalis konkreetseid käske sisestama. Või kujutage ette midagi, mis üldiselt parandaks teie arendajakogemust, kõik juhitav loomuliku keele abil. Nüüd hakkate mõistma, miks see on kasulik, eks?

## Ülevaade

See õppetund käsitleb, kuidas kasutada Visual Studio Code'i ja GitHub Copiloti Agent režiimi kliendina teie MCP serveri jaoks.

## Õpieesmärgid

Selle õppetunni lõpuks suudate:

- Kasutada MCP serverit Visual Studio Code'i kaudu.
- Käivitada tööriistu ja muid funktsioone GitHub Copiloti abil.
- Konfigureerida Visual Studio Code'i, et leida ja hallata oma MCP serverit.

## Kasutamine

Te saate oma MCP serverit juhtida kahel erineval viisil:

- Kasutajaliidese kaudu – seda näete hiljem selles peatükis.
- Terminali kaudu – asju on võimalik juhtida terminalist, kasutades `code` käivitatavat faili:

  MCP serveri lisamiseks oma kasutajaprofiilile kasutage käsurea valikut --add-mcp ja esitage JSON serveri konfiguratsioon kujul {\"name\":\"server-name\",\"command\":...}.

  ```
  code --add-mcp "{\"name\":\"my-server\",\"command\": \"uvx\",\"args\": [\"mcp-server-fetch\"]}"
  ```

### Ekraanipildid

![Juhendatud MCP serveri konfiguratsioon Visual Studio Code'is](../../../../translated_images/et/chat-mode-agent.729a22473f822216dd1e723aaee1f7d4a2ede571ee0948037a2d9357a63b9d0b.png)
![Tööriistade valik iga agendi sessiooni jaoks](../../../../translated_images/et/agent-mode-select-tools.522c7ba5df0848f8f0d1e439c2e96159431bc620cb39ccf3f5dc611412fd0006.png)
![Lihtne vigade silumine MCP arenduse ajal](../../../../translated_images/et/mcp-list-servers.fce89eefe3f30032bed8952e110ab9d82fadf043fcfa071f7d40cf93fb1ea9e9.png)

Räägime järgnevates osades rohkem sellest, kuidas kasutada visuaalset liidest.

## Lähenemine

Siin on üldine lähenemine:

- Konfigureerige fail, et leida oma MCP server.
- Käivitage/ühendage serveriga, et näha selle funktsioone.
- Kasutage neid funktsioone GitHub Copiloti vestlusliidese kaudu.

Suurepärane, nüüd kui me mõistame protsessi, proovime MCP serverit kasutada Visual Studio Code'i kaudu harjutuse abil.

## Harjutus: Serveri kasutamine

Selles harjutuses konfigureerime Visual Studio Code'i, et leida teie MCP server, nii et seda saab kasutada GitHub Copiloti vestlusliidese kaudu.

### -0- Eeltoiming: MCP serverite avastamise lubamine

Teil võib olla vaja lubada MCP serverite avastamine.

1. Minge Visual Studio Code'is `File -> Preferences -> Settings`.

1. Otsige "MCP" ja lubage `chat.mcp.discovery.enabled` settings.json failis.

### -1- Konfiguratsioonifaili loomine

Alustage konfiguratsioonifaili loomisega oma projekti juurkausta. Teil on vaja faili nimega MCP.json, mis tuleb paigutada kausta .vscode. See peaks välja nägema järgmiselt:

```text
.vscode
|-- mcp.json
```

Järgmisena vaatame, kuidas lisada serveri kirje.

### -2- Serveri konfigureerimine

Lisage järgmine sisu *mcp.json* faili:

```json
{
    "inputs": [],
    "servers": {
       "hello-mcp": {
           "command": "node",
           "args": [
               "build/index.js"
           ]
       }
    }
}
```

Ülaltoodud näide näitab, kuidas käivitada server Node.js-is. Teiste käituskeskkondade jaoks määrake sobiv käsk serveri käivitamiseks, kasutades `command` ja `args`.

### -3- Serveri käivitamine

Kui olete kirje lisanud, käivitage server:

1. Leidke oma kirje *mcp.json* failis ja veenduge, et näete "play" ikooni:

  ![Serveri käivitamine Visual Studio Code'is](../../../../translated_images/et/vscode-start-server.8e3c986612e3555de47e5b1e37b2f3020457eeb6a206568570fd74a17e3796ad.png)  

1. Klõpsake "play" ikooni. Peaksite nägema, et GitHub Copiloti vestlusliidese tööriistade ikoonil suureneb saadaval olevate tööriistade arv. Kui klõpsate tööriistade ikoonil, näete registreeritud tööriistade loendit. Saate iga tööriista sisse/välja lülitada, sõltuvalt sellest, kas soovite, et GitHub Copilot neid kontekstis kasutaks:

  ![Serveri käivitamine Visual Studio Code'is](../../../../translated_images/et/vscode-tool.0b3bbea2fb7d8c26ddf573cad15ef654e55302a323267d8ee6bd742fe7df7fed.png)

1. Tööriista käivitamiseks sisestage käsk, mis vastab ühe teie tööriista kirjeldusele, näiteks käsk "add 22 to 1":

  ![Tööriista käivitamine GitHub Copilotist](../../../../translated_images/et/vscode-agent.d5a0e0b897331060518fe3f13907677ef52b879db98c64d68a38338608f3751e.png)

  Peaksite nägema vastust, mis ütleb 23.

## Ülesanne

Proovige lisada serveri kirje oma *mcp.json* faili ja veenduge, et saate serveri käivitada/peatada. Veenduge, et saate suhelda serveri tööriistadega GitHub Copiloti vestlusliidese kaudu.

## Lahendus

[Lahendus](./solution/README.md)

## Olulised punktid

Selle peatüki olulised punktid on järgmised:

- Visual Studio Code on suurepärane klient, mis võimaldab kasutada mitmeid MCP servereid ja nende tööriistu.
- GitHub Copiloti vestlusliides on viis, kuidas serveritega suhelda.
- Saate küsida kasutajalt sisendeid, nagu API võtmed, mida saab MCP serverile edastada serveri kirje konfigureerimisel *mcp.json* failis.

## Näited

- [Java kalkulaator](../samples/java/calculator/README.md)
- [.Net kalkulaator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulaator](../samples/javascript/README.md)
- [TypeScript kalkulaator](../samples/typescript/README.md)
- [Python kalkulaator](../../../../03-GettingStarted/samples/python)

## Lisamaterjalid

- [Visual Studio dokumentatsioon](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)

## Mis edasi?

- Järgmine: [Stdio serveri loomine](../05-stdio-server/README.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.