# Näidise käivitamine

Siin eeldame, et teil on juba töötav serverikood. Palun leidke server ühest varasemast peatükist.

## mcp.json seadistamine

Siin on viitamiseks kasutatav fail, [mcp.json](../../../../../03-GettingStarted/04-vscode/solution/mcp.json).

Muutke serveri kirjet vastavalt vajadusele, et osutada serveri absoluutsele teele, sealhulgas täielik käsk selle käivitamiseks.

Ülalviidatud näidisfailis näeb serveri kirje välja selline:

<details>
<summary>node.js</summary>
```json
"hello-mcp": {
    "command": "node",
    "args": [
        "build/index.js"
    ]
}
```
</details>

<details>
<summary>.NET</summary>

Teil võib olla vaja sisestada GitHubi repositooriumi juurkataloog, mille saab käsuga `git rev-parse --show-toplevel`.

```jsonc
{
  "inputs": [
    {
      "type": "promptString",
      "id": "repository-root",
      "description": "The absolute path to the repository root"
    }
  ],
  "servers": {
    "calculator-mcp-dotnet": {
      "type": "stdio",
      "command": "dotnet",
      "args": [
        "run",
        "--project",
        "${input:repository-root}/03-GettingStarted/02-client/solution/server/server.csproj"
      ]
    }
  }
}
```

</details>

See vastab käsu käivitamisele, mis näeb välja selline: `node build/index.js`.

- Muutke see serveri kirje vastavalt sellele, kus teie serverifail asub, või vastavalt sellele, mis on vajalik serveri käivitamiseks, sõltuvalt valitud käitusajast ja serveri asukohast.

## Serveri funktsioonide kasutamine

- Klõpsake `play` ikooni, kui olete lisanud *mcp.json* faili *./vscode* kausta.

    Jälgige, kuidas tööriistade ikoon muutub, suurendades saadaolevate tööriistade arvu. Tööriistade ikoon asub GitHub Copiloti vestlusvälja kohal.

## Tööriista käivitamine

- Sisestage vestlusaknas käsk, mis vastab teie tööriista kirjeldusele. Näiteks tööriista `add` käivitamiseks sisestage midagi sellist nagu "add 3 to 20".

    Peaksite nägema tööriista, mis kuvatakse vestluse tekstikasti kohal, andes teile võimaluse valida tööriista käivitamine, nagu näidatud selles visuaalis:

    ![VS Code näitab tööriista käivitamise võimalust](../../../../../translated_images/et/vscode-agent.d5a0e0b897331060518fe3f13907677ef52b879db98c64d68a38338608f3751e.png)

    Tööriista valimine peaks andma numbrilise tulemuse "23", kui teie käsk oli nagu eelnevalt mainitud.

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.