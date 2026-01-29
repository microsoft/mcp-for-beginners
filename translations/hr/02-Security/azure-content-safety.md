# Napredna MCP sigurnost s Azure Content Safety

Azure Content Safety nudi nekoliko moćnih alata koji mogu poboljšati sigurnost vaših MCP implementacija:

## Prompt Shields

Microsoftovi AI Prompt Shields pružaju snažnu zaštitu od izravnih i neizravnih napada ubrizgavanja prompta kroz:

1. **Napredna detekcija**: Koristi strojno učenje za prepoznavanje zlonamjernih uputa ugrađenih u sadržaj.
2. **Isticanje**: Pretvara ulazni tekst kako bi AI sustavi lakše razlikovali valjane upute od vanjskih unosa.
3. **Ograničivači i označavanje podataka**: Označava granice između pouzdanih i nepouzdanih podataka.
4. **Integracija Content Safety**: Radi s Azure AI Content Safety za otkrivanje pokušaja jailbreaka i štetnog sadržaja.
5. **Kontinuirana ažuriranja**: Microsoft redovito ažurira mehanizme zaštite protiv novih prijetnji.

## Implementacija Azure Content Safety s MCP

Ovaj pristup pruža višeslojnu zaštitu:
- Skeniranje unosa prije obrade
- Validacija izlaza prije vraćanja
- Korištenje bloklista za poznate štetne obrasce
- Iskorištavanje kontinuirano ažuriranih modela sigurnosti sadržaja iz Azurea

## Resursi za Azure Content Safety

Za više informacija o implementaciji Azure Content Safety s vašim MCP serverima, konzultirajte ove službene izvore:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Službena dokumentacija za Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Naučite kako spriječiti napade ubrizgavanja prompta.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Detaljan API referentni vodič za implementaciju Content Safety.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Brzi vodič za implementaciju koristeći C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Klijentske biblioteke za različite programske jezike.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Specifične upute za otkrivanje i sprječavanje pokušaja jailbreaka.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Najbolje prakse za učinkovitu implementaciju sigurnosti sadržaja.

Za detaljniju implementaciju, pogledajte naš [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md).

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.