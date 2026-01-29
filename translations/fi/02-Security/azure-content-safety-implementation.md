# Azure Content Safetyn toteuttaminen MCP:ssä

MCP:n suojaamiseksi promptin injektointia, työkalujen myrkyttämistä ja muita tekoälyyn liittyviä haavoittuvuuksia vastaan Azure Content Safetyn integrointi on erittäin suositeltavaa.

## Integrointi MCP-palvelimen kanssa

Integroidaksesi Azure Content Safetyn MCP-palvelimeesi, lisää sisältöturvafiltteri middlewareksi pyyntöjen käsittelyputkeen:

1. Alusta filtteri palvelimen käynnistyessä
2. Tarkista kaikki saapuvat työkalupyyntöjen ennen käsittelyä
3. Tarkista kaikki lähtevät vastaukset ennen niiden palauttamista asiakkaille
4. Kirjaa ja hälytä turvallisuusrikkomuksista
5. Toteuta asianmukainen virheenkäsittely epäonnistuneille sisältöturvatarkistuksille

Tämä tarjoaa vahvan suojan seuraavia vastaan:
- Promptin injektointihyökkäykset
- Työkalujen myrkytysyritykset
- Tietojen vuotaminen haitallisten syötteiden kautta
- Vahingollisen sisällön tuottaminen

## Parhaat käytännöt Azure Content Safetyn integrointiin

1. **Mukautetut estolistat**: Luo MCP-injektointimalleihin räätälöityjä estolistoja
2. **Vakavuuden säätö**: Säädä vakavuuskynnyksiä käyttötapauksesi ja riskinsietokykysi mukaan
3. **Laaja kattavuus**: Käytä sisältöturvatarkistuksia kaikissa syötteissä ja tulosteissa
4. **Suorituskyvyn optimointi**: Harkitse välimuistin käyttöä toistuvissa sisältöturvatarkistuksissa
5. **Varajärjestelmät**: Määrittele selkeät varatoiminnot, kun sisältöturvapalvelut eivät ole käytettävissä
6. **Käyttäjäpalautteet**: Tarjoa käyttäjille selkeät palautteet, kun sisältö estetään turvallisuussyistä
7. **Jatkuva parantaminen**: Päivitä estolistat ja mallit säännöllisesti uusien uhkien perusteella

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.