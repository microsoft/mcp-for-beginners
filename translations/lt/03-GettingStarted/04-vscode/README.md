<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ea28e5e566edd5969337fd0b191ba3f",
  "translation_date": "2025-08-26T16:51:03+00:00",
  "source_file": "03-GettingStarted/04-vscode/README.md",
  "language_code": "lt"
}
-->
# Naudojimasis serveriu iš GitHub Copilot Agent režimo

Visual Studio Code ir GitHub Copilot gali veikti kaip klientas ir naudoti MCP serverį. Kodėl tai gali būti naudinga? Na, tai reiškia, kad visos MCP serverio funkcijos dabar gali būti naudojamos tiesiai jūsų IDE. Įsivaizduokite, kad, pavyzdžiui, pridėjote GitHub MCP serverį – tai leistų valdyti GitHub naudojant užklausas vietoj konkrečių komandų rašymo terminale. Arba įsivaizduokite bet kokį kitą įrankį, kuris galėtų pagerinti jūsų kūrėjo patirtį, valdomą natūralia kalba. Dabar jau matote, kokia tai nauda, tiesa?

## Apžvalga

Šioje pamokoje aptarsime, kaip naudoti Visual Studio Code ir GitHub Copilot Agent režimą kaip klientą jūsų MCP serveriui.

## Mokymosi tikslai

Šios pamokos pabaigoje jūs galėsite:

- Naudoti MCP serverį per Visual Studio Code.
- Paleisti tokias funkcijas kaip įrankiai per GitHub Copilot.
- Suprasti, kaip sukonfigūruoti Visual Studio Code, kad rastumėte ir valdytumėte savo MCP serverį.

## Naudojimas

MCP serverį galite valdyti dviem būdais:

- Naudojant vartotojo sąsają – kaip tai padaryti, pamatysite vėliau šiame skyriuje.
- Terminale – galima valdyti serverį naudojant `code` vykdomąjį failą:

  Norėdami pridėti MCP serverį prie savo vartotojo profilio, naudokite komandų eilutės parinktį --add-mcp ir pateikite JSON serverio konfigūraciją formatu {\"name\":\"server-name\",\"command\":...}.

  ```
  code --add-mcp "{\"name\":\"my-server\",\"command\": \"uvx\",\"args\": [\"mcp-server-fetch\"]}"
  ```

### Ekrano nuotraukos

![Vadovaujama MCP serverio konfigūracija Visual Studio Code](../../../../translated_images/chat-mode-agent.729a22473f822216dd1e723aaee1f7d4a2ede571ee0948037a2d9357a63b9d0b.lt.png)
![Įrankių pasirinkimas kiekvienai agento sesijai](../../../../translated_images/agent-mode-select-tools.522c7ba5df0848f8f0d1e439c2e96159431bc620cb39ccf3f5dc611412fd0006.lt.png)
![Lengvas klaidų derinimas MCP kūrimo metu](../../../../translated_images/mcp-list-servers.fce89eefe3f30032bed8952e110ab9d82fadf043fcfa071f7d40cf93fb1ea9e9.lt.png)

Apie tai, kaip naudoti vizualią sąsają, kalbėsime kituose skyriuose.

## Požiūris

Štai kaip turime prieiti prie šio proceso aukštu lygiu:

- Sukonfigūruoti failą, kad rastume savo MCP serverį.
- Paleisti/prisijungti prie serverio, kad jis pateiktų savo galimybes.
- Naudoti šias galimybes per GitHub Copilot pokalbių sąsają.

Puiku, dabar, kai suprantame procesą, pabandykime naudoti MCP serverį per Visual Studio Code atlikdami pratimą.

## Pratimas: Naudojimasis serveriu

Šiame pratime sukonfigūruosime Visual Studio Code, kad rastume jūsų MCP serverį ir galėtume jį naudoti per GitHub Copilot pokalbių sąsają.

### -0- Paruošiamasis žingsnis: įgalinkite MCP serverio aptikimą

Gali reikėti įgalinti MCP serverių aptikimą.

1. Eikite į `File -> Preferences -> Settings` Visual Studio Code.

1. Ieškokite „MCP“ ir įjunkite `chat.mcp.discovery.enabled` nustatymuose.json faile.

### -1- Sukurkite konfigūracijos failą

Pradėkite nuo konfigūracijos failo sukūrimo savo projekto šaknyje. Jums reikės failo pavadinimu MCP.json, kurį reikia įdėti į aplanką .vscode. Jis turėtų atrodyti taip:

```text
.vscode
|-- mcp.json
```

Toliau pažiūrėkime, kaip pridėti serverio įrašą.

### -2- Suveskite serverio konfigūraciją

Pridėkite šį turinį į *mcp.json*:

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

Aukščiau pateiktas pavyzdys parodo, kaip paleisti serverį, parašytą Node.js. Kitiems vykdymo laikams nurodykite tinkamą komandą serverio paleidimui naudojant `command` ir `args`.

### -3- Paleiskite serverį

Dabar, kai pridėjote įrašą, paleiskite serverį:

1. Suraskite savo įrašą *mcp.json* ir įsitikinkite, kad matote „play“ piktogramą:

  ![Serverio paleidimas Visual Studio Code](../../../../translated_images/vscode-start-server.8e3c986612e3555de47e5b1e37b2f3020457eeb6a206568570fd74a17e3796ad.lt.png)  

1. Spustelėkite „play“ piktogramą. Turėtumėte matyti, kaip GitHub Copilot pokalbių įrankių piktograma padidina prieinamų įrankių skaičių. Jei spustelėsite šią įrankių piktogramą, pamatysite registruotų įrankių sąrašą. Galite pažymėti/nuimti kiekvieną įrankį, priklausomai nuo to, ar norite, kad GitHub Copilot juos naudotų kaip kontekstą:

  ![Serverio paleidimas Visual Studio Code](../../../../translated_images/vscode-tool.0b3bbea2fb7d8c26ddf573cad15ef654e55302a323267d8ee6bd742fe7df7fed.lt.png)

1. Norėdami paleisti įrankį, įveskite užklausą, kuri atitiktų vieno iš jūsų įrankių aprašymą, pavyzdžiui, užklausą „pridėk 22 prie 1“:

  ![Įrankio paleidimas iš GitHub Copilot](../../../../translated_images/vscode-agent.d5a0e0b897331060518fe3f13907677ef52b879db98c64d68a38338608f3751e.lt.png)

  Turėtumėte matyti atsakymą „23“.

## Užduotis

Pabandykite pridėti serverio įrašą į savo *mcp.json* failą ir įsitikinkite, kad galite paleisti/sustabdyti serverį. Taip pat įsitikinkite, kad galite bendrauti su savo serverio įrankiais per GitHub Copilot pokalbių sąsają.

## Sprendimas

[Sprendimas](./solution/README.md)

## Pagrindinės išvados

Šio skyriaus pagrindinės išvados:

- Visual Studio Code yra puikus klientas, leidžiantis naudoti kelis MCP serverius ir jų įrankius.
- GitHub Copilot pokalbių sąsaja yra būdas bendrauti su serveriais.
- Galite prašyti vartotojo įvesties, pvz., API raktų, kuriuos galima perduoti MCP serveriui konfigūruojant serverio įrašą *mcp.json* faile.

## Pavyzdžiai

- [Java skaičiuotuvas](../samples/java/calculator/README.md)
- [.Net skaičiuotuvas](../../../../03-GettingStarted/samples/csharp)
- [JavaScript skaičiuotuvas](../samples/javascript/README.md)
- [TypeScript skaičiuotuvas](../samples/typescript/README.md)
- [Python skaičiuotuvas](../../../../03-GettingStarted/samples/python)

## Papildomi ištekliai

- [Visual Studio dokumentacija](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)

## Kas toliau

- Toliau: [SSE serverio kūrimas](../05-sse-server/README.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.