# Generator plana učenja s Chainlitom i Microsoft Learn Docs MCP

## Preduvjeti

- Python 3.8 ili noviji
- pip (Pythonov upravitelj paketa)
- Pristup internetu za povezivanje s Microsoft Learn Docs MCP serverom

## Instalacija

1. Klonirajte ovaj repozitorij ili preuzmite datoteke projekta.
2. Instalirajte potrebne ovisnosti:

   ```bash
   pip install -r requirements.txt
   ```

## Korištenje

### Scenarij 1: Jednostavan upit prema Docs MCP
Klijent naredbenog retka koji se povezuje s Docs MCP serverom, šalje upit i ispisuje rezultat.

1. Pokrenite skriptu:
   ```bash
   python scenario1.py
   ```
2. Unesite svoje pitanje o dokumentaciji u upitnik.

### Scenarij 2: Generator plana učenja (Chainlit web aplikacija)
Web sučelje (koristeći Chainlit) koje omogućuje korisnicima generiranje personaliziranog, tjedan-po-tjedan plana učenja za bilo koju tehničku temu.

1. Pokrenite Chainlit aplikaciju:
   ```bash
   chainlit run scenario2.py
   ```
2. Otvorite lokalni URL koji se prikazuje u vašem terminalu (npr. http://localhost:8000) u pregledniku.
3. U prozoru za chat unesite svoju temu učenja i broj tjedana koliko želite učiti (npr. "AI-900 certifikacija, 8 tjedana").
4. Aplikacija će odgovoriti s tjedan-po-tjedan planom učenja, uključujući poveznice na relevantnu Microsoft Learn dokumentaciju.

**Potrebne varijable okruženja:**

Za korištenje Scenarija 2 (Chainlit web aplikacija s Azure OpenAI), morate postaviti sljedeće varijable okruženja u `.env` datoteku u direktoriju `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Unesite ove vrijednosti s detaljima vašeg Azure OpenAI resursa prije pokretanja aplikacije.

> [!TIP]
> Svoje modele možete jednostavno implementirati koristeći [Azure AI Foundry](https://ai.azure.com/).

### Scenarij 3: Dokumentacija u editoru s MCP serverom u VS Code

Umjesto prebacivanja između kartica preglednika za pretraživanje dokumentacije, možete donijeti Microsoft Learn Docs direktno u svoj VS Code koristeći MCP server. Ovo omogućuje:
- Pretraživanje i čitanje dokumentacije unutar VS Code bez napuštanja okruženja za kodiranje.
- Referenciranje dokumentacije i umetanje poveznica direktno u README ili datoteke tečaja.
- Korištenje GitHub Copilota i MCP-a zajedno za besprijekoran, AI-pogonjen tijek rada s dokumentacijom.

**Primjeri korištenja:**
- Brzo dodavanje referentnih poveznica u README dok pišete dokumentaciju za tečaj ili projekt.
- Korištenje Copilota za generiranje koda i MCP-a za trenutno pronalaženje i citiranje relevantne dokumentacije.
- Ostajanje fokusiranim u editoru i povećanje produktivnosti.

> [!IMPORTANT]
> Osigurajte da imate valjanu konfiguraciju [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) u svom radnom prostoru (lokacija je `.vscode/mcp.json`).

## Zašto Chainlit za Scenarij 2?

Chainlit je moderan open-source okvir za izradu konverzacijskih web aplikacija. Olakšava stvaranje chat-baziranih korisničkih sučelja koja se povezuju s backend servisima poput Microsoft Learn Docs MCP servera. Ovaj projekt koristi Chainlit za pružanje jednostavnog, interaktivnog načina generiranja personaliziranih planova učenja u stvarnom vremenu. Korištenjem Chainlita, možete brzo izraditi i implementirati chat-bazirane alate koji poboljšavaju produktivnost i učenje.

## Što ova aplikacija radi

Ova aplikacija omogućuje korisnicima stvaranje personaliziranog plana učenja jednostavnim unosom teme i trajanja. Aplikacija analizira vaš unos, šalje upit Microsoft Learn Docs MCP serveru za relevantan sadržaj i organizira rezultate u strukturirani, tjedan-po-tjedan plan. Preporuke za svaki tjedan prikazuju se u chatu, što olakšava praćenje i napredak. Integracija osigurava da uvijek dobijete najnovije i najrelevantnije resurse za učenje.

## Primjeri upita

Isprobajte ove upite u prozoru za chat kako biste vidjeli kako aplikacija odgovara:

- `AI-900 certifikacija, 8 tjedana`
- `Nauči Azure Functions, 4 tjedna`
- `Azure DevOps, 6 tjedana`
- `Inženjering podataka na Azureu, 10 tjedana`
- `Microsoft sigurnosni temelji, 5 tjedana`
- `Power Platform, 7 tjedana`
- `Azure AI usluge, 12 tjedana`
- `Cloud arhitektura, 9 tjedana`

Ovi primjeri pokazuju fleksibilnost aplikacije za različite ciljeve učenja i vremenske okvire.

## Reference

- [Chainlit Dokumentacija](https://docs.chainlit.io/)
- [MCP Dokumentacija](https://github.com/MicrosoftDocs/mcp)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.