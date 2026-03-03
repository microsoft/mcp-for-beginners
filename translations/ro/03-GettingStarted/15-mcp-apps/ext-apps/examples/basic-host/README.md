# Exemplu: Host de bază

O implementare de referință care arată cum să construiești o aplicație host MCP care se conectează la serverele MCP și redă interfețele de utilizator ale uneltelor într-un sandbox sigur.

Acest host de bază poate fi folosit și pentru a testa aplicațiile MCP în timpul dezvoltării locale.

## Fișiere cheie

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - Host UI React cu selecție de unelte, introducere de parametri și gestionare iframe
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Proxy iframe exterior cu validare de securitate și retransmitere bidirecțională a mesajelor
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Logică centrală: conectare la server, apelare unelte și configurare AppBridge

## Începerea

```bash
npm install
npm run start
# Deschide http://localhost:8080
```

Implicit, aplicația host va încerca să se conecteze la un server MCP la `http://localhost:3001/mcp`. Poți configura acest comportament setând variabila de mediu `SERVERS` cu un array JSON de URL-uri ale serverelor:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Arhitectură

Acest exemplu folosește un model cu dublu iframe sandbox pentru izolare sigură a interfeței UI:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**De ce două iframe-uri?**

- Iframe-ul exterior rulează pe o origine separată (port 8081) prevenind accesul direct la host
- Iframe-ul interior primește HTML prin `srcdoc` și este restricționat de atributele sandbox
- Mesajele circulă prin iframe-ul exterior care le validează și le retransmite bidirecțional

Această arhitectură asigură că, chiar dacă codul UI al uneltei este malițios, acesta nu poate accesa DOM-ul aplicației host, cookie-urile sau contextul JavaScript.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să aveți în vedere că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un traducător uman. Nu ne asumăm responsabilitatea pentru eventuale neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->