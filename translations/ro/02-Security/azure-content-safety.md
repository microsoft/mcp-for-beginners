# Securitate avansată MCP cu Azure Content Safety

Azure Content Safety oferă mai multe instrumente puternice care pot îmbunătăți securitatea implementărilor tale MCP:

## Prompt Shields

Prompt Shields de la Microsoft oferă o protecție solidă împotriva atacurilor de tip prompt injection, atât directe, cât și indirecte, prin:

1. **Detectare avansată**: Folosește machine learning pentru a identifica instrucțiuni malițioase ascunse în conținut.
2. **Evidențiere**: Transformă textul de intrare pentru a ajuta sistemele AI să distingă între instrucțiuni valide și inputuri externe.
3. **Delimitatori și marcaje de date**: Marchează granițele dintre datele de încredere și cele neîncredere.
4. **Integrare Content Safety**: Colaborează cu Azure AI Content Safety pentru a detecta încercările de jailbreak și conținutul dăunător.
5. **Actualizări continue**: Microsoft actualizează regulat mecanismele de protecție împotriva amenințărilor emergente.

## Implementarea Azure Content Safety cu MCP

Această abordare oferă o protecție în mai multe straturi:
- Scanarea inputurilor înainte de procesare
- Validarea outputurilor înainte de returnare
- Utilizarea listelor de blocare pentru tipare cunoscute ca fiind dăunătoare
- Folosirea modelelor de content safety actualizate continuu de Azure

## Resurse Azure Content Safety

Pentru a afla mai multe despre implementarea Azure Content Safety cu serverele tale MCP, consultă aceste resurse oficiale:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Documentația oficială pentru Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Află cum să previi atacurile de tip prompt injection.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Referință detaliată API pentru implementarea Content Safety.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Ghid rapid de implementare folosind C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Biblioteci client pentru diverse limbaje de programare.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Ghid specific pentru detectarea și prevenirea încercărilor de jailbreak.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Cele mai bune practici pentru implementarea eficientă a content safety.

Pentru o implementare mai detaliată, consultă ghidul nostru [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md).

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.