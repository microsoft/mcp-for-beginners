# Sicurezza Avanzata MCP con Azure Content Safety

Azure Content Safety offre diversi strumenti potenti che possono migliorare la sicurezza delle tue implementazioni MCP:

## Prompt Shields

I Prompt Shields di Microsoft per l’AI offrono una protezione solida contro attacchi di prompt injection sia diretti che indiretti attraverso:

1. **Rilevamento Avanzato**: Utilizza il machine learning per identificare istruzioni dannose nascoste nel contenuto.
2. **Evidenziazione**: Trasforma il testo di input per aiutare i sistemi AI a distinguere tra istruzioni valide e input esterni.
3. **Delimitatori e Datamarking**: Segna i confini tra dati affidabili e non affidabili.
4. **Integrazione con Content Safety**: Collabora con Azure AI Content Safety per rilevare tentativi di jailbreak e contenuti dannosi.
5. **Aggiornamenti Continui**: Microsoft aggiorna regolarmente i meccanismi di protezione contro le minacce emergenti.

## Implementazione di Azure Content Safety con MCP

Questo approccio offre una protezione a più livelli:
- Scansione degli input prima dell’elaborazione
- Validazione degli output prima della restituzione
- Utilizzo di blocklist per pattern dannosi noti
- Sfruttamento dei modelli di content safety di Azure costantemente aggiornati

## Risorse su Azure Content Safety

Per approfondire l’implementazione di Azure Content Safety con i tuoi server MCP, consulta queste risorse ufficiali:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Documentazione ufficiale di Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Come prevenire attacchi di prompt injection.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Riferimento API dettagliato per implementare Content Safety.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Guida rapida all’implementazione con C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Librerie client per vari linguaggi di programmazione.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Indicazioni specifiche per rilevare e prevenire tentativi di jailbreak.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Best practice per implementare efficacemente la content safety.

Per un’implementazione più approfondita, consulta la nostra [guida all’implementazione di Azure Content Safety](./azure-content-safety-implementation.md).

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.