# Generator de Plan de Studiu cu Chainlit & Microsoft Learn Docs MCP

## Cerințe preliminare

- Python 3.8 sau o versiune mai recentă
- pip (managerul de pachete Python)
- Acces la internet pentru a conecta la serverul Microsoft Learn Docs MCP

## Instalare

1. Clonează acest depozit sau descarcă fișierele proiectului.
2. Instalează dependențele necesare:

   ```bash
   pip install -r requirements.txt
   ```

## Utilizare

### Scenariul 1: Interogare simplă către Docs MCP
Un client de linie de comandă care se conectează la serverul Docs MCP, trimite o interogare și afișează rezultatul.

1. Rulează scriptul:
   ```bash
   python scenario1.py
   ```
2. Introdu întrebarea ta despre documentație la prompt.

### Scenariul 2: Generator de Plan de Studiu (Aplicație Web Chainlit)
O interfață web (folosind Chainlit) care permite utilizatorilor să genereze un plan de studiu personalizat, organizat pe săptămâni, pentru orice subiect tehnic.

1. Pornește aplicația Chainlit:
   ```bash
   chainlit run scenario2.py
   ```
2. Deschide URL-ul local furnizat în terminalul tău (de exemplu, http://localhost:8000) în browserul tău.
3. În fereastra de chat, introdu subiectul de studiu și numărul de săptămâni în care dorești să studiezi (de exemplu, "certificare AI-900, 8 săptămâni").
4. Aplicația va răspunde cu un plan de studiu organizat pe săptămâni, incluzând linkuri către documentația relevantă de pe Microsoft Learn.

**Variabile de mediu necesare:**

Pentru a utiliza Scenariul 2 (aplicația web Chainlit cu Azure OpenAI), trebuie să setezi următoarele variabile de mediu într-un fișier `.env` din directorul `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Completează aceste valori cu detaliile resursei tale Azure OpenAI înainte de a rula aplicația.

> [!TIP]
> Poți să-ți implementezi cu ușurință propriile modele folosind [Azure AI Foundry](https://ai.azure.com/).

### Scenariul 3: Documentație în Editor cu Serverul MCP în VS Code

În loc să comuți între filele browserului pentru a căuta documentație, poți aduce Microsoft Learn Docs direct în VS Code folosind serverul MCP. Acest lucru îți permite să:
- Cauți și citești documentația direct în VS Code fără a părăsi mediul de codare.
- Referențiezi documentația și inserezi linkuri direct în README sau fișierele cursului.
- Utilizezi GitHub Copilot și MCP împreună pentru un flux de lucru integrat, alimentat de AI.

**Exemple de utilizare:**
- Adaugă rapid linkuri de referință într-un README în timp ce scrii documentația unui curs sau proiect.
- Folosește Copilot pentru a genera cod și MCP pentru a găsi și cita instant documentația relevantă.
- Rămâi concentrat în editorul tău și crește productivitatea.

> [!IMPORTANT]
> Asigură-te că ai o configurație validă [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) în spațiul tău de lucru (locația este `.vscode/mcp.json`).

## De ce Chainlit pentru Scenariul 2?

Chainlit este un framework modern open-source pentru construirea aplicațiilor web conversaționale. Face ușor să creezi interfețe de utilizator bazate pe chat care se conectează la servicii backend, cum ar fi serverul Microsoft Learn Docs MCP. Acest proiect folosește Chainlit pentru a oferi o modalitate simplă și interactivă de a genera planuri de studiu personalizate în timp real. Prin utilizarea Chainlit, poți construi și implementa rapid instrumente bazate pe chat care îmbunătățesc productivitatea și procesul de învățare.

## Ce face această aplicație

Această aplicație permite utilizatorilor să creeze un plan de studiu personalizat prin simpla introducere a unui subiect și a unei durate. Aplicația analizează inputul tău, interoghează serverul Microsoft Learn Docs MCP pentru conținut relevant și organizează rezultatele într-un plan structurat, săptămână cu săptămână. Recomandările pentru fiecare săptămână sunt afișate în chat, făcându-le ușor de urmat și de urmărit progresul. Integrarea asigură că primești mereu cele mai recente și relevante resurse de învățare.

## Exemple de interogări

Încearcă aceste interogări în fereastra de chat pentru a vedea cum răspunde aplicația:

- `certificare AI-900, 8 săptămâni`
- `Învață Azure Functions, 4 săptămâni`
- `Azure DevOps, 6 săptămâni`
- `Inginerie de date pe Azure, 10 săptămâni`
- `Fundamentele securității Microsoft, 5 săptămâni`
- `Power Platform, 7 săptămâni`
- `Servicii AI Azure, 12 săptămâni`
- `Arhitectură cloud, 9 săptămâni`

Aceste exemple demonstrează flexibilitatea aplicației pentru diferite obiective de învățare și intervale de timp.

## Referințe

- [Documentația Chainlit](https://docs.chainlit.io/)
- [Documentația MCP](https://github.com/MicrosoftDocs/mcp)

---

**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși depunem eforturi pentru a asigura acuratețea, vă rugăm să aveți în vedere că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.