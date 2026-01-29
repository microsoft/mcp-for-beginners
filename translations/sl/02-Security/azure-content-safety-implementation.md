# Implementacija Azure Content Safety z MCP

Za krepitev varnosti MCP pred vbrizgavanjem ukazov, zastrupljanjem orodij in drugimi ranljivostmi, specifičnimi za AI, je močno priporočena integracija Azure Content Safety.

## Integracija z MCP strežnikom

Za integracijo Azure Content Safety z vašim MCP strežnikom dodajte filter za varnost vsebine kot vmesno programsko opremo v vaš procesni tok zahtev:

1. Inicializirajte filter ob zagonu strežnika  
2. Preverite vse dohodne zahteve orodij pred obdelavo  
3. Preverite vse odhodne odgovore pred vrnitvijo strankam  
4. Beležite in opozarjajte na kršitve varnosti  
5. Uvedite ustrezno obravnavo napak za neuspešne varnostne preglede vsebine  

To zagotavlja močno zaščito pred:  
- Napadi vbrizgavanja ukazov  
- Poskusi zastrupljanja orodij  
- Izvlekom podatkov preko zlonamernih vhodov  
- Generiranjem škodljive vsebine  

## Najboljše prakse za integracijo Azure Content Safety

1. **Prilagojeni seznami blokad**: Ustvarite prilagojene sezname blokad posebej za vzorce vbrizgavanja MCP  
2. **Prilagajanje resnosti**: Prilagodite pragove resnosti glede na vaš specifičen primer uporabe in toleranco do tveganja  
3. **Celovito pokritje**: Uporabite varnostne preglede vsebine na vseh vhodih in izhodih  
4. **Optimizacija zmogljivosti**: Razmislite o uvedbi predpomnjenja za ponavljajoče se varnostne preglede vsebine  
5. **Mehanizmi za rezervne rešitve**: Določite jasna vedenja v primeru nedosegljivosti varnostnih storitev vsebine  
6. **Povratne informacije uporabnikom**: Zagotovite jasne povratne informacije uporabnikom, ko je vsebina blokirana zaradi varnostnih razlogov  
7. **Nenehno izboljševanje**: Redno posodabljajte sezname blokad in vzorce glede na nove grožnje

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.