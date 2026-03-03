# Pavyzdys: Pagrindinis Šeimininkas

Referencinė implementacija, rodanti, kaip sukurti MCP šeimininko programą, kuri jungiasi prie MCP serverių ir saugioje aplinkoje pateikia įrankių vartotojo sąsajas.

Šis paprastas šeimininkas taip pat gali būti naudojamas MCP programų testavimui vietinio vystymo metu.

## Pagrindiniai Failai

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - React UI šeimininkas su įrankių pasirinkimu, parametrų įvedimu ir iframe valdymu
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Išorinis iframe tarpininkas su saugumo patikra ir dvikrypčiu pranešimų persiuntimu
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Pagrindinė logika: serverio jungtis, įrankių iškvietimas ir AppBridge nustatymas

## Pradžia

```bash
npm install
npm run start
# Atidarykite http://localhost:8080
```

Pagal numatytuosius nustatymus, šeimininko programa bandys prisijungti prie MCP serverio adresu `http://localhost:3001/mcp`. Šį elgesį galite konfigūruoti nustatydami `SERVERS` aplinkos kintamąjį su serverių URL sąrašu JSON formatu:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Architektūra

Šis pavyzdys naudoja dvigubo iframe saugios vartotojo sąsajos izoliacijos modelį:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Kodėl du iframe?**

- Išorinis iframe veikia kitoje kilmėje (portas 8081), neleidžiantis tiesiogiai pasiekti šeimininko
- Vidinis iframe gauna HTML per `srcdoc` ir yra apribotas sandbox atributais
- Pranešimai pereina per išorinį iframe, kuris juos patikrina ir perduoda abiem kryptimis

Ši architektūra užtikrina, kad net jei įrankio vartotojo sąsajos kodas yra kenksmingas, jis negali pasiekti šeimininko programos DOM, slapukų ar JavaScript konteksto.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turi būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogaus atliktas vertimas. Mes neatsakome už jokius nesusipratimus ar neteisingus interpretavimus, kylančius naudojant šį vertimą.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->