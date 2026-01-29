# Napredna varnost MCP z Azure Content Safety

Azure Content Safety ponuja več zmogljivih orodij, ki lahko izboljšajo varnost vaših MCP implementacij:

## Prompt Shields

Microsoftovi AI Prompt Shields nudijo močno zaščito pred neposrednimi in posrednimi napadi z vbrizgavanjem ukazov z:

1. **Napredno zaznavanje**: Uporablja strojno učenje za prepoznavanje zlonamernih navodil, vgrajenih v vsebino.  
2. **Osvetlitev**: Pretvori vhodno besedilo, da AI sistemi lažje ločijo veljavna navodila od zunanjih vhodov.  
3. **Omejitve in označevanje podatkov**: Označuje meje med zaupanja vrednimi in nezaupljivimi podatki.  
4. **Integracija z Content Safety**: Sodeluje z Azure AI Content Safety za zaznavanje poskusov jailbreaka in škodljive vsebine.  
5. **Nenehne posodobitve**: Microsoft redno posodablja zaščitne mehanizme proti novim grožnjam.

## Implementacija Azure Content Safety z MCP

Ta pristop zagotavlja večplastno zaščito:  
- Pregled vhodov pred obdelavo  
- Preverjanje izhodov pred vrnitvijo  
- Uporaba blok seznamov za znane škodljive vzorce  
- Izraba stalno posodobljenih modelov Azure Content Safety

## Viri za Azure Content Safety

Za več informacij o implementaciji Azure Content Safety z vašimi MCP strežniki si oglejte te uradne vire:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Uradna dokumentacija za Azure Content Safety.  
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Naučite se, kako preprečiti napade z vbrizgavanjem ukazov.  
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Podroben API referenčni vodič za implementacijo Content Safety.  
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Hitri vodič za implementacijo z uporabo C#.  
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Knjižnice za odjemalce v različnih programskih jezikih.  
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Posebna navodila za zaznavanje in preprečevanje poskusov jailbreaka.  
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Najboljše prakse za učinkovito implementacijo varnosti vsebine.

Za bolj poglobljeno implementacijo si oglejte naš [vodnik za implementacijo Azure Content Safety](./azure-content-safety-implementation.md).

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.