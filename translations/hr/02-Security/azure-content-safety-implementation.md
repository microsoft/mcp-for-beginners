# Implementacija Azure Content Safety s MCP-om

Za jačanje sigurnosti MCP-a protiv prompt injectiona, trovanja alata i drugih AI-specifičnih ranjivosti, toplo se preporučuje integracija Azure Content Safety.

## Integracija s MCP serverom

Za integraciju Azure Content Safety s vašim MCP serverom, dodajte content safety filter kao middleware u vaš pipeline obrade zahtjeva:

1. Inicijalizirajte filter prilikom pokretanja servera  
2. Validirajte sve dolazne zahtjeve alata prije obrade  
3. Provjerite sve odlazne odgovore prije nego ih vratite klijentima  
4. Zabilježite i upozorite na kršenja sigurnosti  
5. Implementirajte odgovarajuće rukovanje greškama za neuspjele provjere content safety

Ovo pruža snažnu obranu protiv:  
- Napada prompt injection  
- Pokušaja trovanja alata  
- Eksfiltracije podataka putem zlonamjernih unosa  
- Generiranja štetnog sadržaja

## Najbolje prakse za integraciju Azure Content Safety

1. **Prilagođeni blok-liste**: Kreirajte prilagođene blok-liste posebno za MCP obrasce injekcija  
2. **Podešavanje ozbiljnosti**: Prilagodite pragove ozbiljnosti prema vašem specifičnom slučaju i toleranciji rizika  
3. **Sveobuhvatna pokrivenost**: Primijenite provjere content safety na sve ulaze i izlaze  
4. **Optimizacija performansi**: Razmotrite implementaciju keširanja za ponovljene provjere content safety  
5. **Mehanizmi za rezervu**: Definirajte jasne fallback mehanizme kada servisi content safety nisu dostupni  
6. **Povratne informacije korisnicima**: Pružite jasne povratne informacije korisnicima kada je sadržaj blokiran zbog sigurnosnih razloga  
7. **Kontinuirano poboljšanje**: Redovito ažurirajte blok-liste i obrasce na temelju novih prijetnji

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.