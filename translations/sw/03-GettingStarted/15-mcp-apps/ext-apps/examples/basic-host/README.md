# Mfano: Mwenyeji Msingi

Utekelezaji wa rejea unaoonyesha jinsi ya kujenga programu mwenyeji wa MCP inayounganisha na seva za MCP na kuonyesha UI za zana katika sandbox salama.

Mwenyeji huyu wa msingi pia unaweza kutumika kupima Programu za MCP wakati wa maendeleo ya ndani.

## Faili Muhimu

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - Mwenyeji wa UI wa React na uteuzi wa zana, ingizo la vigezo, na usimamizi wa iframe
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - Proxy ya iframe ya nje na uthibitishaji wa usalama na upitishaji wa ujumbe wa upande mbili
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - Mantiki kuu: kuunganishwa kwa seva, kuitwa kwa zana, na usanidi wa AppBridge

## Kuanzia

```bash
npm install
npm run start
# Fungua http://localhost:8080
```

Kwa default, programu mwenyeji itajaribu kuungana na seva ya MCP kwenye `http://localhost:3001/mcp`. Unaweza kusanidi tabia hii kwa kuweka mazingira ya `SERVERS` yenye safu ya URL za seva kwa muundo wa JSON:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## Mimaribo

Mfano huu unatumia mtindo wa sandbox wa iframe mara mbili kwa izolishaji salama wa UI:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**Kwa nini iframes mbili?**

- Iframe ya nje inaendesha kwenye chanzo tofauti (bandari 8081) kuzuia ufikiaji wa moja kwa moja kwa mwenyeji
- Iframe ya ndani hupokea HTML kupitia `srcdoc` na iko chini ya vizuizi vya sandbox
- Ujumbe hupitia iframe ya nje ambayo inathibitisha na kuzipeleka kwa upande mbili

Mimaribo hii inahakikisha kwamba hata kama msimbo wa UI wa zana ni mbaya, hauwezi kufikia DOM, vidakuzi, au muktadha wa JavaScript wa programu mwenyeji.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tangazo la Kukataa**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuwa sahihi, tafadhali fahamu kwamba tafsiri za moja kwa moja zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na watu inapendekezwa. Hatuna dhamana kwa kutokuelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->