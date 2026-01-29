# Suorita tämä esimerkki

> [!NOTE]
> Tämä esimerkki olettaa, että käytät GitHub Codespaces -instanssia. Jos haluat suorittaa tämän paikallisesti, sinun täytyy luoda henkilökohtainen käyttöoikeustunnus (PAT) GitHubissa.
>
> ```bash
> # zsh/bash
> export GITHUB_TOKEN="{{YOUR_GITHUB_PAT}}"
> ```
>
> ```powershell
> # PowerShell
> $env:GITHUB_TOKEN = "{{YOUR_GITHUB_PAT}}"
> ```

## Asenna kirjastot

```sh
dotnet restore
```

Tämän pitäisi asentaa seuraavat kirjastot: Azure AI Inference, Azure Identity, Microsoft.Extension, Model.Hosting, ModelContextProtcol

## Suorita

```sh 
dotnet run
```

Näet tulosteen, joka on samanlainen kuin:

```text
Setting up stdio transport
Listing tools
Connected to server with tools: Add
Tool description: Adds two numbers
Tool parameters: {"title":"Add","description":"Adds two numbers","type":"object","properties":{"a":{"type":"integer"},"b":{"type":"integer"}},"required":["a","b"]}
Tool definition: Azure.AI.Inference.ChatCompletionsToolDefinition
Properties: {"a":{"type":"integer"},"b":{"type":"integer"}}
MCP Tools def: 0: Azure.AI.Inference.ChatCompletionsToolDefinition
Tool call 0: Add with arguments {"a":2,"b":4}
Sum 6
```

Suurin osa tulosteesta on vain virheenkorjausta, mutta tärkeää on, että listaat työkalut MCP Serveriltä, muutat ne LLM-työkaluiksi ja lopulta saat MCP-asiakasvastauksen "Sum 6".

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.