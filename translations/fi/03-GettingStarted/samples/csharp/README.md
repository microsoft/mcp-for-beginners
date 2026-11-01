# Peruslaskin MCP-palvelu

Tämä palvelu tarjoaa peruslaskinoperaatiot Model Context Protocolin (MCP) kautta. Se on suunniteltu yksinkertaiseksi esimerkiksi aloittelijoille, jotka opettelevat MCP:n toteutuksia.

Lisätietoja löytyy osoitteesta [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Ominaisuudet

Tämä laskinpalvelu tarjoaa seuraavat toiminnot:

1. **Perusaritmeettiset operaatiot**:
   - Kaksi luvun yhteenlasku
   - Toisen luvun vähentäminen toisesta
   - Kaksi luvun kertolasku
   - Toisen luvun jakaminen toisella (nollalla jakamisen tarkistus)

## `stdio`-tyypin käyttö
  
## Konfigurointi

1. **Konfiguroi MCP-palvelimet**:
   - Avaa työtila VS Codessa.
   - Luo `.vscode/mcp.json`-tiedosto työtilakansioosi MCP-palvelimien konfigurointia varten. Esimerkki konfiguraatiosta:

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
             "${input:repository-root}/03-GettingStarted/samples/csharp/src/calculator.csproj"
           ]
         }
       }
     }
     ```

   - Sinulta kysytään GitHub-repositorion juurihakemisto, joka voidaan hakea komennolla `git rev-parse --show-toplevel`.

## Palvelun käyttö

Palvelu tarjoaa seuraavat API-päätepisteet MCP-protokollan kautta:

- `add(a, b)`: Kaksi luvun yhteenlasku
- `subtract(a, b)`: Toisen luvun vähentäminen ensimmäisestä
- `multiply(a, b)`: Kaksi luvun kertolasku
- `divide(a, b)`: Ensimmäisen luvun jakaminen toisella (nollatarkistuksella)
- isPrime(n): Tarkistaa, onko luku alkuluku

## Testaa Github Copilot Chatilla VS Codessa

1. Yritä tehdä pyyntö palvelulle MCP-protokollan avulla. Esimerkiksi voit kysyä:
   - "Laske 5 ja 3 yhteen"
   - "Vähennä 10:stä 4"
   - "Kertaa 6 ja 7"
   - "Jaa 8 kahdella"
   - "Onko 37854 alkuluku?"
   - "Mitkä ovat 3 alkulukua ennen ja jälkeen 4242?"
2. Varmistaaksesi, että käytetään työkaluja, lisää kehotteeseen #MyCalculator. Esimerkiksi:
   - "Laske 5 ja 3 yhteen #MyCalculator"
   - "Vähennä 10:stä 4 #MyCalculator


## Kontitettavissa oleva versio

Edellinen ratkaisu on hyvä, kun sinulla on .NET SDK asennettuna ja kaikki riippuvuudet paikallaan. Jos kuitenkin haluat jakaa ratkaisun tai ajaa sitä eri ympäristössä, voit käyttää kontitettua versiota.

1. Käynnistä Docker ja varmista, että se on käynnissä.
1. Avaa terminaali ja siirry kansioon `03-GettingStarted\samples\csharp\src` 
1. Rakentaaksesi Docker-kuvan laskinpalvelulle, suorita seuraava komento (korvaa `<YOUR-DOCKER-USERNAME>` omalla Docker Hub -käyttäjätunnuksellasi):
   ```bash
   docker build -t <YOUR-DOCKER-USERNAME>/mcp-calculator .
   ``` 
1. Kun kuva on rakennettu, lataa se Docker Hubiin suorittamalla seuraava komento:
   ```bash
   docker push <YOUR-DOCKER-USERNAME>/mcp-calculator
   ```

## Käytä Docker-versiota

1. Korvaa `.vscode/mcp.json`-tiedostossa palvelimen määritykset seuraavalla:
   ```json
    "mcp-calculator": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "<YOUR-DOCKER-USERNAME>/mcp-calculator"
      ],
      "envFile": "",
      "env": {}
    }
   ```
   Katsoessasi määritystä näet, että komento on `docker` ja argumentit ovat `run --rm -i <YOUR-DOCKER-USERNAME>/mcp-calculator`. `--rm`-lipuke varmistaa, että kontti poistetaan sen pysäytyksen jälkeen, ja `-i`-lipuke antaa sinun käyttää kontin standardisyöttöä. Viimeinen argumentti on juuri rakentamamme ja Docker Hubiin työntämämme kuvan nimi.

## Testaa Docker-versiota

Käynnistä MCP-palvelin napsauttamalla pientä Käynnistä-painiketta kohdassa `"mcp-calculator": {`, ja kuten aiemmin, voit pyytää laskinpalvelua tekemään laskutoimituksia puolestasi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->