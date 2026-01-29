# Implementazione di Azure Content Safety con MCP

Per rafforzare la sicurezza di MCP contro l’iniezione di prompt, il poisoning degli strumenti e altre vulnerabilità specifiche dell’IA, si consiglia vivamente di integrare Azure Content Safety.

## Integrazione con MCP Server

Per integrare Azure Content Safety con il tuo server MCP, aggiungi il filtro di content safety come middleware nella pipeline di elaborazione delle richieste:

1. Inizializza il filtro durante l’avvio del server  
2. Valida tutte le richieste degli strumenti in ingresso prima di elaborarle  
3. Controlla tutte le risposte in uscita prima di restituirle ai client  
4. Registra e segnala le violazioni di sicurezza  
5. Implementa una gestione degli errori adeguata per i controlli di content safety non superati  

Questo garantisce una difesa solida contro:  
- Attacchi di iniezione di prompt  
- Tentativi di poisoning degli strumenti  
- Esfiltrazione di dati tramite input dannosi  
- Generazione di contenuti nocivi  

## Best Practice per l’Integrazione di Azure Content Safety

1. **Blocklist personalizzate**: Crea blocklist personalizzate specifiche per i pattern di iniezione MCP  
2. **Regolazione della severità**: Adatta le soglie di severità in base al tuo caso d’uso e alla tolleranza al rischio  
3. **Copertura completa**: Applica i controlli di content safety a tutti gli input e output  
4. **Ottimizzazione delle prestazioni**: Valuta l’implementazione di caching per i controlli di content safety ripetuti  
5. **Meccanismi di fallback**: Definisci comportamenti di fallback chiari quando i servizi di content safety non sono disponibili  
6. **Feedback agli utenti**: Fornisci un feedback chiaro agli utenti quando i contenuti vengono bloccati per motivi di sicurezza  
7. **Miglioramento continuo**: Aggiorna regolarmente blocklist e pattern in base alle minacce emergenti

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.