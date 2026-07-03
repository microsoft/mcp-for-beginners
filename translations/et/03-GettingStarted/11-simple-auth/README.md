# Lihtne autentimine

MCP SDK-d toetavad OAuth 2.1 kasutamist, mis on ausalt öeldes üsna keerukas protsess, mis hõlmab selliseid mõisteid nagu autentimisserver, ressursiserver, mandaadi saatmine, koodi saamine, koodi vahetamine bearer-tokeni vastu, kuni lõpuks omandatakse ressursi andmed. Kui sa pole OAuthiga harjunud, mis on suurepärane asi rakendamiseks, on mõistlik alustada mõnest põhilisest autentimisest ja minna edasi paremate ja paremate turvameetoditeni. Seepärast see peatükk eksisteerib, et sind samm-sammult viia arenenuma autentimiseni.

## Autentimine, mida me mõtleme?

Autentimine on lühend sõnadest authentication ja authorization. Idee on selles, et meil tuleb teha kaks asja:

- **Autentimine**, mis on protsess, mille käigus kontrollime, kas inimene võib meie majja siseneda, st kas tal on õigus olla "siin", ehk ligipääs meie ressursiserverile, kus meie MCP Serveri funktsioonid asuvad.
- **Autoriseerimine**, on protsess, mille käigus kontrollitakse, kas kasutajal peaks olema juurdepääs neile konkreetsetele ressurssidele, mida ta küsib, näiteks nendele tellimustele või toodetele või kas ta võib sisu lugeda, kuid mitte kustutada, näiteks.

## Mandaat: kuidas me süsteemile ütleme, kes me oleme

Enamik veebiarendajaid mõtleb enamasti mandaadi andmise kontseptsioonis serverile, tavaliselt salajane, mis ütleb, kas neil on õigus siin olla ("Autentimine"). See mandaat on tavaliselt kasutajanime ja parooli base64 kodeeritud versioon või API võti, mis identifitseerib unikaalselt konkreetse kasutaja.

See hõlmab selle saatmist päise kaudu nimega "Authorization" niimoodi:

```json
{ "Authorization": "secret123" }
```

Seda nimetatakse tavaliselt põhiliseks autentimiseks. Kuidas kogu protsess töötab, on järgnev:

```mermaid
sequenceDiagram
   participant User
   participant Client
   participant Server

   User->>Client: näita mulle andmeid
   Client->>Server: näita mulle andmeid, siin on minu volitused
   Server-->>Client: 1a, ma tunnen sind, siin on sinu andmed
   Server-->>Client: 1b, ma ei tunne sind, 401 
```

Nüüd kui mõistame, kuidas see töötab vooluna, siis kuidas me seda rakendame? Enamikul veebiserveritel on mõiste nimega middleware, koodilõik, mis käivitatakse päringu osana, mis suudab kontrollida mandaate ja kui mandaadid on kehtivad, lubab päringu läbi. Kui päringul pole kehtivaid mandaate, saad autentimisvea. Vaatame, kuidas seda rakendada:

**Python**

```python
class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):

        has_header = request.headers.get("Authorization")
        if not has_header:
            print("-> Missing Authorization header!")
            return Response(status_code=401, content="Unauthorized")

        if not valid_token(has_header):
            print("-> Invalid token!")
            return Response(status_code=403, content="Forbidden")

        print("Valid token, proceeding...")
       
        response = await call_next(request)
        # lisa mõned kliendi päised või muuda vastust mingil moel
        return response


starlette_app.add_middleware(CustomHeaderMiddleware)
```

Siin oleme:

- Loonud middleware'i nimega `AuthMiddleware`, mille `dispatch` meetodit veebiserver kutsub.
- Lisanud middleware'i veebiserverisse:

    ```python
    starlette_app.add_middleware(AuthMiddleware)
    ```

- Kirjutanud valideerimise loogika, mis kontrollib, kas Authorization päis on olemas ja kas saadetud salajane on kehtiv:

    ```python
    has_header = request.headers.get("Authorization")
    if not has_header:
        print("-> Missing Authorization header!")
        return Response(status_code=401, content="Unauthorized")

    if not valid_token(has_header):
        print("-> Invalid token!")
        return Response(status_code=403, content="Forbidden")
    ```

    kui salajane on olemas ja kehtiv, lubame päringu läbi, kutsudes `call_next` ja tagastades vastuse.

    ```python
    response = await call_next(request)
    # lisa mis tahes kliendi päised või tee vastuses mingisuguseid muudatusi
    return response
    ```

Kuidas see töötab: kui veebipäring suunatakse serverile, kutsub middleware enda rakendus välja ja antud rakenduse puhul lubab või keelab päringu vastavalt.

**TypeScript**

Siin loome middleware'i populaarse raamistiku Express abil ja püüame päringu kinni enne, kui see jõuab MCP Serverini. Siin on kood selle jaoks:

```typescript
function isValid(secret) {
    return secret === "secret123";
}

app.use((req, res, next) => {
    // 1. Kas autoriseerimispealkiri on olemas?
    if(!req.headers["Authorization"]) {
        res.status(401).send('Unauthorized');
    }
    
    let token = req.headers["Authorization"];

    // 2. Kontrolli kehtivust.
    if(!isValid(token)) {
        res.status(403).send('Forbidden');
    }

   
    console.log('Middleware executed');
    // 3. Edastab päringu järgmisele etapile päringutöötluses.
    next();
});
```

Selles koodis:

1. Kontrollime esmalt, kas Authorization päis on olemas, kui mitte, saadame 401 vea.
2. Veendume, et mandaat/token on kehtiv, kui mitte, saadame 403 vea.
3. Lõpuks lastakse päring edasi päringu torus ja tagastatakse soovitud ressurss.

## Harjutus: Rakenda autentimine

Võtame oma teadmised ja proovime seda rakendada. Siin on plaan:

Server

- Loo veebiserver ja MCP eksemplar.
- Rakenda middleware serverile.

Kliendi pool 

- Saada veebipäring koos mandaadiga päises.

### -1- Loo veebiserver ja MCP eksemplar

> **Edasivaade:** allpool toodud TypeScript näide jälgib HTTP transpordid kaardil `transports`, mille võti on `mcp-session-id`, vastavalt **MCP spetsifikatsioonile 2025-11-25**. Versioonikandidaat `2026-07-28` eemaldab täielikult `initialize` kättesaamise ja sessiooni ID, nii et iga sessiooni transpordikaart kaob ja asemele tulevad olekuta, iseseisvalt toimivad päringud. Vaata [Mis muutub MCP-s: 2026-07-28 versioonikandidaat](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

Esimeses sammus peame looma veebiserveri instantsi ja MCP Serveri.

**Python**

Siin loome MCP serveri eksemplari, loome starlette veebirakenduse ja hostime selle uvicorniga.

```python
# MCP serveri loomine

app = FastMCP(
    name="MCP Resource Server",
    instructions="Resource Server that validates tokens via Authorization Server introspection",
    host=settings["host"],
    port=settings["port"],
    debug=True
)

# starlette veebirakenduse loomine
starlette_app = app.streamable_http_app()

# rakenduse teenindamine uvicorn abil
async def run(starlette_app):
    import uvicorn
    config = uvicorn.Config(
            starlette_app,
            host=app.settings.host,
            port=app.settings.port,
            log_level=app.settings.log_level.lower(),
        )
    server = uvicorn.Server(config)
    await server.serve()

run(starlette_app)
```

Selles koodis:

- Loome MCP Serveri.
- Koostame starlette veebirakenduse MCP Serverist, `app.streamable_http_app()`.
- Hostime ja serveerime rakendust uvicorniga `server.serve()`.

**TypeScript**

Siin loome MCP Serveri instantsi.

```typescript
const server = new McpServer({
      name: "example-server",
      version: "1.0.0"
    });

    // ... seadista serveri ressursid, tööriistad ja käsud ...
```

See MCP Serveri loomine peab toimuma meie POST /mcp marsruudis, nii et võtame ülaltoodud koodi ja viime selle niimoodi üle:

```typescript
import express from "express";
import { randomUUID } from "node:crypto";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { isInitializeRequest } from "@modelcontextprotocol/sdk/types.js"

const app = express();
app.use(express.json());

// Kaart transpordi salvestamiseks sessiooni ID järgi
const transports: { [sessionId: string]: StreamableHTTPServerTransport } = {};

// Töötle POST-päringuid kliendist serverisse suhtluseks
app.post('/mcp', async (req, res) => {
  // Kontrolli olemasolevat sessiooni ID-d
  const sessionId = req.headers['mcp-session-id'] as string | undefined;
  let transport: StreamableHTTPServerTransport;

  if (sessionId && transports[sessionId]) {
    // Kasuta olemasolevat transporti uuesti
    transport = transports[sessionId];
  } else if (!sessionId && isInitializeRequest(req.body)) {
    // Uus initsialiseerimisnõue
    transport = new StreamableHTTPServerTransport({
      sessionIdGenerator: () => randomUUID(),
      onsessioninitialized: (sessionId) => {
        // Salvesta transport sessiooni ID järgi
        transports[sessionId] = transport;
      },
      // DNS-uuesti sidumise kaitse on vaikimisi keelatud tagurpidi ühilduvuse tõttu. Kui sa jooksutad seda serverit
      // lokaalselt, siis veendu, et määraksid:
      // enableDnsRebindingProtection: true,
      // allowedHosts: ['127.0.0.1'],
    });

    // Puhasta transport pärast sulgemist
    transport.onclose = () => {
      if (transport.sessionId) {
        delete transports[transport.sessionId];
      }
    };
    const server = new McpServer({
      name: "example-server",
      version: "1.0.0"
    });

    // ... seadista serveri ressursid, tööriistad ja käsud ...

    // Ühenda MCP serveriga
    await server.connect(transport);
  } else {
    // Vigane päring
    res.status(400).json({
      jsonrpc: '2.0',
      error: {
        code: -32000,
        message: 'Bad Request: No valid session ID provided',
      },
      id: null,
    });
    return;
  }

  // Töötle päringut
  await transport.handleRequest(req, res, req.body);
});

// Taaskasutatav töötleja GET ja DELETE päringute jaoks
const handleSessionRequest = async (req: express.Request, res: express.Response) => {
  const sessionId = req.headers['mcp-session-id'] as string | undefined;
  if (!sessionId || !transports[sessionId]) {
    res.status(400).send('Invalid or missing session ID');
    return;
  }
  
  const transport = transports[sessionId];
  await transport.handleRequest(req, res);
};

// Töötle GET-päringuid serverist kliendi teadete jaoks SSE kaudu
app.get('/mcp', handleSessionRequest);

// Töötle DELETE-päringuid sessiooni lõpetamiseks
app.delete('/mcp', handleSessionRequest);

app.listen(3000);
```

Nüüd näed, kuidas MCP Serveri loomine viidi `app.post("/mcp")` sees.

Liigume järgmise sammu juurde, middleware'i loomise juurde, et saaksime sissetuleva mandaadi valideerida.

### -2- Rakenda middleware serverile

Vaatame nüüd middleware'ile. Siin loome middleware'i, mis otsib `Authorization` päisest mandaati ja valideerib selle. Kui see on vastuvõetav, teeb päring seda, mida vaja (nt tööriistade loendamist, ressursi lugemist või mõnda MCP funktsionaalsust, mida klient soovis).

**Python**

Middleware loomiseks peame looma klassi, mis pärib `BaseHTTPMiddleware`-st. On kaks huvipakkuvat elementi:

- Päring `request`, kust loeme päise andmed.
- `call_next` on tagasikõne, mida kutsume, kui klient on toonud mandaadi, mida me aktsepteerime.

Esmalt käsitleme olukorra, kui `Authorization` päis puudub:

```python
has_header = request.headers.get("Authorization")

# päist pole olemas, ebaõnnestu 401-ga, vastasel juhul jätka.
if not has_header:
    print("-> Missing Authorization header!")
    return Response(status_code=401, content="Unauthorized")
```

Siin saadame 401 lubamata sõnumi, kuna klient ei läbi autentimist.

Edasi, kui mandaat esitati, kontrollime selle kehtivust niimoodi:

```python
 if not valid_token(has_header):
    print("-> Invalid token!")
    return Response(status_code=403, content="Forbidden")
```

Näed, et saadetakse 403 keelatud sõnum. Vaatame täielikku middleware'i koodi, mis teeb kõik ülalnimetatu:

```python
class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):

        has_header = request.headers.get("Authorization")
        if not has_header:
            print("-> Missing Authorization header!")
            return Response(status_code=401, content="Unauthorized")

        if not valid_token(has_header):
            print("-> Invalid token!")
            return Response(status_code=403, content="Forbidden")

        print("Valid token, proceeding...")
        print(f"-> Received {request.method} {request.url}")
        response = await call_next(request)
        response.headers['Custom'] = 'Example'
        return response

```

Hea, aga mis siis on `valid_token` funktsioon? Siin see on:

```python
# ÄRA kasuta tootmises - paranda see !!
def valid_token(token: str) -> bool:
    # eemalda "Bearer " eesliide
    if token.startswith("Bearer "):
        token = token[7:]
        return token == "secret-token"
    return False
```

See vajaks muidugi parandamist.

TÄHTIS: Selliseid salasõnu ei tohiks kunagi koodis hoida. Ideaalis tuleks võrdluseks väärtus hankida andmeallikast või identiteediteenuselt (IDP) või veel parem, las IDP kontrollib mandaati.

**TypeScript**

Selle rakendamiseks Expressiga peame kasutama `use` meetodit, mis võtab middleware funktsioone.

Peame:

- Töötlema päringut, kontrollides mandaati `Authorization` omaduses.
- Valideerima mandaati ja kui see kehtib, laskma päringu edasi, et kliendi MCP päring teeks oma töö (nt tööriistade loendamine, ressursi lugemine vm MCP-ga seotud).

Siin kontrollime, kas `Authorization` päis on olemas ja kui ei ole, peatame päringu:

```typescript
if(!req.headers["authorization"]) {
    res.status(401).send('Unauthorized');
    return;
}
```

Kui päist ei saadeta, saadakse 401.

Edasi kontrollime, kas mandaat on kehtiv, kui mitte, peatame päringu teatega:

```typescript
if(!isValid(token)) {
    res.status(403).send('Forbidden');
    return;
} 
```

Nüüd saad 403 vea.

Täiskood on siin:

```typescript
app.use((req, res, next) => {
    console.log('Request received:', req.method, req.url, req.headers);
    console.log('Headers:', req.headers["authorization"]);
    if(!req.headers["authorization"]) {
        res.status(401).send('Unauthorized');
        return;
    }
    
    let token = req.headers["authorization"];

    if(!isValid(token)) {
        res.status(403).send('Forbidden');
        return;
    }  

    console.log('Middleware executed');
    next();
});
```

Oleme seadistanud veebiserveri, et aktsepteerida middleware'i, mis kontrollib mandaati, mida klient loodetavasti meile saadab. Aga mis siis kliendi pool?

### -3- Saada veebipäring mandaadiga päises

Peame veenduma, et klient edastab mandaadi päises. Kuna kasutame MCP klienti, peame välja mõtlema, kuidas seda teha.

**Python**

Kliendi jaoks peame saatma päise koos mandaadiga niimoodi:

```python
# ÄRGE kodeerige väärtust koodis, hoidke see vähemalt keskkonnamuutujas või turvalisemas salvestusruumis
token = "secret-token"

async with streamablehttp_client(
        url = f"http://localhost:{port}/mcp",
        headers = {"Authorization": f"Bearer {token}"}
    ) as (
        read_stream,
        write_stream,
        session_callback,
    ):
        async with ClientSession(
            read_stream,
            write_stream
        ) as session:
            await session.initialize()
      
            # TODO, mida soovite kliendis teha, nt tööriistade loetelu, tööriistade kutsumine jne.
```

Siin täidame `headers` omaduse niimoodi ` headers = {"Authorization": f"Bearer {token}"}`.

**TypeScript**

Seda saab lahendada kahel sammul:

1. Täita konfiguratsioon objekt oma mandaadiga.
2. Saata konfiguratsioon objekt transpordile.

```typescript

// ÄRA kõvenda väärtust nagu siin näidatud. Vähemalt hoia seda keskkonnamuutujana ja kasuta midagi nagu dotenv (arendusrežiimis).
let token = "secret123"

// määra kliendi transpordi valikute objekt
let options: StreamableHTTPClientTransportOptions = {
  sessionId: sessionId,
  requestInit: {
    headers: {
      "Authorization": "secret123"
    }
  }
};

// edasta valikute objekt transpordile
async function main() {
   const transport = new StreamableHTTPClientTransport(
      new URL(serverUrl),
      options
   );
```

Siin näed, kuidas lõime `options` objekti ja panime päised `requestInit` omadusse.

TÄHTIS: Kuidas seda paremaks teha? Praegune lahendus on riskantne, eriti ilma HTTPS-ta. Isegi siis saab mandaadi varastada, seega vajad süsteemi, kus saab tokenit hõlpsalt tühistada ja lisada täiendavaid kontrollimisi, näiteks kust maailmast päring tuleb, kas päring toimub liiga tihti (botilaadne käitumine). Kokkuvõttes on palju muresid.

Tuleb siiski öelda, et väga lihtsate API-de puhul, kus sa ei taha, et keegi juhuslikult sinu API-le ligi pääseks ilma autentimiseta, on see hea algus.

Sellepärast proovimegi turvalisust tugevdada, kasutades standardiseeritud vormingut nagu JSON Web Token ehk JWT või "JOT" tokenid.

## JSON Web Tokenid, JWT

Püüame edendada olukorda, kus saatmine on keerulisemate mandaaditaoliste andmete asemel. Millised on otsesed eelised JWT kasutuselevõtmisel?

- **Turvaparandused**. Põhilises autentimises saadad kasutajanime ja parooli base64 kodeeritult tokenina (või API võtit) ikka ja jälle, mis suurendab riski. JWT-s saad sa kasutajanime ja parooli ning vastu saad tokeni, mis on aja piiratud ehk aegub. JWT võimaldab kasutada peenhäälestatud juurdepääsu kontrolli — rolle, ulatusi ja õigusi.
- **Olekuvabadus ja skaleeritavus**. JWT-d on iseseisvad, need kannavad kogu kasutaja infot ja kaotavad vajaduse serveripoolse sessioonihalduse jaoks. Tokeni saab ka lokaalselt valideerida.
- **Interoperatiivsus ja föderatsioon**. JWT on Open ID Connecti keskne osa ja seda kasutatakse tuntud identiteedipakkujate nagu Entra ID, Google Identity ja Auth0 juures. Samuti võimaldavad need sisselogimist ühekordse autentimisega ja palju muud, muutes need ettevõtte tasemele sobivaks.
- **Moodulaarsus ja paindlikkus**. JWT-d saab kasutada API väravate juures nagu Azure API Management, NGINX ja teised. Toetab kasutaja autentimise stsenaariume ja server-teenuse kommunikatsiooni, kaasa arvatud esindamis- ja volitamisstsenaariumid.
- **Jõudlus ja vahemällu salvestamine**. JWT-d saab dekrüpteerimise järel vahemällu salvestada, mis vähendab vajadust neid korduvalt parsida. See aitab eriti kõrge koormusega rakendustes, parandades läbilaskevõimet ja vähendades infrastruktuuri koormust.
- **Arenenud funktsioonid**. Toetatakse introspektiooni (kehtivuse kontroll serveris) ja tühistamist (tokeni muutmine kehtetuks).

Kõigi nende eelistega vaatame, kuidas oma rakendust järgmisele tasemele viia.

## Põhilisest autentimisest JWT külge üleminek

Üldine ülesanne on:

- **Õppida JWT tokeni konstrueerimist** ja teha see valmis kliendilt serverile saatmiseks.
- **Valideerida JWT tokenit**, ning kui kehtib, lubada klientidel kasutada meie ressursse.
- **Tokeni turvaline hoidmine**. Kuidas hoida seda tokenit.
- **Marsruutide kaitsmine**. Peame kaitsma marsruute, meie puhul kindlaid MCP funktsioone.
- **Lisa uuendustokenid**. Tagada, et me loome lühiajalisi tavalisi tokeneid, aga ka pikaajalisi uuendus tokeneid, mida saab kasutada uute tokenite saamiseks, kui need aeguvad. Samuti peab olema uuendamise lõpp-punkt ja rotatsiooni strateegia.

### -1- Loo JWT token

JWT tokenil on kolm osa:

- **päis**, milles on algoritm ja tokeni tüüp.
- **maandumine** (payload), väited, nt sub (kasutaja või entiteet, keda token esindab – autentimiststsenaariumis tavaliselt kasutaja ID), exp (aegumistähtaeg), roll (roll).
- **allkiri**, mis on allkirjastatud salajase võtme või privaatvõtmega.

Selleks peame konstrueerima päise, mahamise ja kodeeritud tokeni.

**Python**

```python

import jwt
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
import datetime

# Saladusvõti, mida kasutatakse JWT allkirjastamiseks
secret_key = 'your-secret-key'

header = {
    "alg": "HS256",
    "typ": "JWT"
}

# kasutaja info ning selle nõuded ja aegumisaeg
payload = {
    "sub": "1234567890",               # Teema (kasutaja ID)
    "name": "User Userson",                # Kohandatud nõue
    "admin": True,                     # Kohandatud nõue
    "iat": datetime.datetime.utcnow(),# Väljaandmise aeg
    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Aegumisaeg
}

# kodeeri see
encoded_jwt = jwt.encode(payload, secret_key, algorithm="HS256", headers=header)
```

Ülalolevas koodis oleme:

- Määratlenud päise, kasutades algoritmina HS256 ja tokeni tüübiks JWT.
- Konstrueerinud mahamise, mis sisaldab alateemat või kasutaja ID-d, kasutajanime, rolli, millal see anti välja ja millal aegub, rakendades sellega eelnevalt mainitud aja piirangut.

**TypeScript**

Siin vajame mõningaid sõltuvusi, mis aitavad meil JWT tokenit konstrueerida.

Sõltuvused

```sh

npm install jsonwebtoken
npm install --save-dev @types/jsonwebtoken
```

Nüüd, kui see on olemas, teeme päise, mahamise ja sellest kodeeritud tokeni.

```typescript
import jwt from 'jsonwebtoken';

const secretKey = 'your-secret-key'; // Kasuta tootmises keskkonnamuutujaid

// Määra kasulik koormus
const payload = {
  sub: '1234567890',
  name: 'User usersson',
  admin: true,
  iat: Math.floor(Date.now() / 1000), // Väljastatud kell
  exp: Math.floor(Date.now() / 1000) + 60 * 60 // Aegub 1 tunni pärast
};

// Määra päis (valikuline, jsonwebtoken seab vaikimisi väärtused)
const header = {
  alg: 'HS256',
  typ: 'JWT'
};

// Loo token
const token = jwt.sign(payload, secretKey, {
  algorithm: 'HS256',
  header: header
});

console.log('JWT:', token);
```

See token on:

Allkirjastatud HS256-ga, kehtib 1 tund, sisaldab väiteid nagu sub, name, admin, iat ja exp.

### -2- Tokeni valideerimine

Peame tokeni valideerima, see on asi, mida peaksime tegema serveris, et tagada, et klient saadab tõepoolest kehtiva tokeni. Seal tuleb teha mitmeid kontrollimisi, alates struktuuri valideerimisest kuni kehtivuse kontrollini. Soovitame lisada ka muid kontrollimisi, näiteks kas kasutaja on meie süsteemis jm.

Tokeni valideerimiseks tuleb see dekodeerida, et seda lugeda ja alustada kehtivuse kontrollimist:

**Python**

```python

# Dekodeeri ja kontrolli JWT-d
try:
    decoded = jwt.decode(token, secret_key, algorithms=["HS256"])
    print("✅ Token is valid.")
    print("Decoded claims:")
    for key, value in decoded.items():
        print(f"  {key}: {value}")
except ExpiredSignatureError:
    print("❌ Token has expired.")
except InvalidTokenError as e:
    print(f"❌ Invalid token: {e}")

```

Selles koodis kutsume `jwt.decode` funktsiooni, kasutades sisendina tokenit, salajast võtit ja valitud algoritmi. Pange tähele, kuidas kasutame try-catch konstruktsiooni, kuna valesti läinud valideerimine põhjustab vea tekkimise.

**TypeScript**

Siin peame kutsuma `jwt.verify`, et saada tokeni lahtidekooditud versioon, mida saame edasi analüüsida. Kui see kutsumine ebaõnnestub, tähendab see, et tokeni struktuur on vale või see pole enam kehtiv.

```typescript

try {
  const decoded = jwt.verify(token, secretKey);
  console.log('Decoded Payload:', decoded);
} catch (err) {
  console.error('Token verification failed:', err);
}
```

MÄRKUS: nagu eelnevalt mainitud, peaksime tegema täiendavaid kontrolle, et veenduda, et see token viitab meie süsteemis olevale kasutajale ja kasutajal on õigused, mida ta väidab omavat.

Järgmisena vaatame rollipõhist ligipääsu kontrolli, tuntud ka kui RBAC.

## Rollipõhise ligipääsu kontrolli lisamine

Idee on, et tahame väljendada, et erinevatel rollidel on erinevad õigused. Näiteks eeldame, et admin saab teha kõike ja tavaline kasutaja saab lugeda/kirjutada ning külaline saab ainult lugeda. Seega on mõned võimalikud õigustasemed:

- Admin.Write
- User.Read
- Guest.Read

Vaatame, kuidas saame sellist kontrolli implementeerida vahendustarkvara (middleware) abil. Vahendustarkvara saab lisada iga marsruudi jaoks eraldi või kõigi marsruutide jaoks.

**Python**

```python
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
import jwt

# ÄRA hoia saladust koodis sees, see on mõeldud vaid näitamiseks. Loe see turvalisest kohast.
SECRET_KEY = "your-secret-key" # pane see keskkonnamuutujasse
REQUIRED_PERMISSION = "User.Read"

class JWTPermissionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse({"error": "Missing or invalid Authorization header"}, status_code=401)

        token = auth_header.split(" ")[1]
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return JSONResponse({"error": "Token expired"}, status_code=401)
        except jwt.InvalidTokenError:
            return JSONResponse({"error": "Invalid token"}, status_code=401)

        permissions = decoded.get("permissions", [])
        if REQUIRED_PERMISSION not in permissions:
            return JSONResponse({"error": "Permission denied"}, status_code=403)

        request.state.user = decoded
        return await call_next(request)


```

Vahendustarkvara lisamiseks on mitu erinevat võimalust nagu allpool:

```python

# Alt 1: lisa vahevara Starlette rakenduse konstruktsiooni ajal
middleware = [
    Middleware(JWTPermissionMiddleware)
]

app = Starlette(routes=routes, middleware=middleware)

# Alt 2: lisa vahevara pärast Starlette rakenduse konstrueerimist
starlette_app.add_middleware(JWTPermissionMiddleware)

# Alt 3: lisa vahevara iga marsruudi kohta
routes = [
    Route(
        "/mcp",
        endpoint=..., # käsitleja
        middleware=[Middleware(JWTPermissionMiddleware)]
    )
]
```

**TypeScript**

Võime kasutada `app.use` ja vahendustarkvara, mis jookseb kõigi päringute puhul.

```typescript
app.use((req, res, next) => {
    console.log('Request received:', req.method, req.url, req.headers);
    console.log('Headers:', req.headers["authorization"]);

    // 1. Kontrolli, kas autoriseerimis päis on saadetud

    if(!req.headers["authorization"]) {
        res.status(401).send('Unauthorized');
        return;
    }
    
    let token = req.headers["authorization"];

    // 2. Kontrolli, kas token on kehtiv
    if(!isValid(token)) {
        res.status(403).send('Forbidden');
        return;
    }  

    // 3. Kontrolli, kas tokeni kasutaja eksisteerib meie süsteemis
    if(!isExistingUser(token)) {
        res.status(403).send('Forbidden');
        console.log("User does not exist");
        return;
    }
    console.log("User exists");

    // 4. Kontrolli, kas tokenil on õiged õigused
    if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }

    console.log("User has required scopes");

    console.log('Middleware executed');
    next();
});

```

On päris palju asju, mida meie vahendustarkvara saab teha ja mida TA PEAB tegema, nimelt:

1. Kontrollida, kas autoriseerimis päis on olemas
2. Kontrollida, kas token on valide, kutsume `isValid` meetodit, mille me kirjutasime, mis kontrollib JWT tokeni terviklikkust ja kehtivust.
3. Kontrollida, kas kasutaja eksisteerib meie süsteemis, seda peaksime kontrollima.

   ```typescript
    // kasutajad andmebaasis
   const users = [
     "user1",
     "User usersson",
   ]

   function isExistingUser(token) {
     let decodedToken = verifyToken(token);

     // TEGEMATA, kontrolli, kas kasutaja on andmebaasis olemas
     return users.includes(decodedToken?.name || "");
   }
   ```

   Ülal oleme loonud väga lihtsa `users` listi, mis peaks ilmselgelt olema andmebaasis.

4. Lisaks peaksime kontrollima, kas tokenil on õiged õigused.

   ```typescript
   if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
   }
   ```

   Selles vahendustarkvara koodis kontrollime, et token sisaldab User.Read õigust, kui ei, siis saadame 403 vea. Allpool on abifunktsioon `hasScopes`.

   ```typescript
   function hasScopes(scope: string, requiredScopes: string[]) {
     let decodedToken = verifyToken(scope);
    return requiredScopes.every(scope => decodedToken?.scopes.includes(scope));
  }
   ```

Have a think which additional checks you should be doing, but these are the absolute minimum of checks you should be doing.

Using Express as a web framework is a common choice. There are helpers library when you use JWT so you can write less code.

- `express-jwt`, helper library that provides a middleware that helps decode your token.
- `express-jwt-permissions`, this provides a middleware `guard` that helps check if a certain permission is on the token.

Here's what these libraries can look like when used:

```typescript
const express = require('express');
const jwt = require('express-jwt');
const guard = require('express-jwt-permissions')();

const app = express();
const secretKey = 'your-secret-key'; // put this in env variable

// Decode JWT and attach to req.user
app.use(jwt({ secret: secretKey, algorithms: ['HS256'] }));

// Check for User.Read permission
app.use(guard.check('User.Read'));

// multiple permissions
// app.use(guard.check(['User.Read', 'Admin.Access']));

app.get('/protected', (req, res) => {
  res.json({ message: `Welcome ${req.user.name}` });
});

// Error handler
app.use((err, req, res, next) => {
  if (err.code === 'permission_denied') {
    return res.status(403).send('Forbidden');
  }
  next(err);
});

```

Nüüd olete näinud, kuidas vahendustarkvara saab kasutada nii autentimiseks kui ka autoriseerimiseks, aga kuidas on MCP-ga, kas see muudab meie autentimise viisi? Vaatame järgmist peatükki.

### -3- Lisa RBAC MCP-le

Olete seni näinud, kuidas lisada RBAC-i vahendustarkvara kaudu, kuid MCP juures pole lihtsat viisi per-MCP-funktsiooni RBAC lisamiseks, siis mida me teeme? Lihtsalt lisame sellise koodi, mis kontrollib, kas klientil on õigus kutsuda konkreetset tööriista:

Teil on mõned erinevad võimalused per funktsiooni RBAC saavutamiseks, siin on mõned:

- Lisada kontroll iga tööriista, ressursi, päringu puhul, kus on vaja kontrollida õigustasandit.

   **python**

   ```python
   @tool()
   def delete_product(id: int):
      try:
          check_permissions(role="Admin.Write", request)
      catch:
        pass # klient ebaõnnestus autoriseerimisel, tõsta autoriseerimisviga
   ```

   **typescript**

   ```typescript
   server.registerTool(
    "delete-product",
    {
      title: Delete a product",
      description: "Deletes a product",
      inputSchema: { id: z.number() }
    },
    async ({ id }) => {
      
      try {
        checkPermissions("Admin.Write", request);
        // teha, saada id productService'ile ja kaugentryle
      } catch(Exception e) {
        console.log("Authorization error, you're not allowed");  
      }

      return {
        content: [{ type: "text", text: `Deletected product with id ${id}` }]
      };
    }
   );
   ```


- Kasutada arenenumat serveri lähenemist ja päringu töötlejaid, et minimeerida kontrolli kohti.

   **Python**

   ```python
   
   tool_permission = {
      "create_product": ["User.Write", "Admin.Write"],
      "delete_product": ["Admin.Write"]
   }

   def has_permission(user_permissions, required_permissions) -> bool:
      # user_permissions: kasutaja õiguste nimekiri
      # required_permissions: tööriista jaoks vajalik õiguste nimekiri
      return any(perm in user_permissions for perm in required_permissions)

   @server.call_tool()
   async def handle_call_tool(
     name: str, arguments: dict[str, str] | None
   ) -> list[types.TextContent]:
    # Eeldades, et request.user.permissions on kasutaja õiguste nimekiri
     user_permissions = request.user.permissions
     required_permissions = tool_permission.get(name, [])
     if not has_permission(user_permissions, required_permissions):
        # Viga "Teil puudub õigus tööriista {name} kutsumiseks"
        raise Exception(f"You don't have permission to call tool {name}")
     # jätka ja kutsu tööriist
     # ...
   ```   
   

   **TypeScript**

   ```typescript
   function hasPermission(userPermissions: string[], requiredPermissions: string[]): boolean {
       if (!Array.isArray(userPermissions) || !Array.isArray(requiredPermissions)) return false;
       // Tagasta true, kui kasutajal on vähemalt üks vajalik luba
       
       return requiredPermissions.some(perm => userPermissions.includes(perm));
   }
  
   server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const { params: { name } } = request;
  
      let permissions = request.user.permissions;
  
      if (!hasPermission(permissions, toolPermissions[name])) {
         return new Error(`You don't have permission to call ${name}`);
      }
  
      // jätka..
   });
   ```

   Märkus: peate tagama, et teie vahendustarkvara määrab lahtidekooditud tokeni päringu user omadusse, et ülaltoodud kood oleks lihtne.

### Kokkuvõte

Nüüd, kui oleme arutanud, kuidas üldiselt ja MCP puhul RBAC-i tugi lisada, on aeg proovida turvalisust ise rakendada, et veenduda, et olete esitatud kontseptsioonid mõistnud.

## Ülesanne 1: Ehita mcp server ja mcp klient, kasutades põhilist autentimist

Siin kasutate seda, mida olete õppinud, edastamaks mandaadid päiste kaudu.

## Lahendus 1

[Lahendus 1](./code/basic/README.md)

## Ülesanne 2: Uuenda lahendust Ülesandest 1, kasutades JWT-d

Võta esimene lahendus ja seekord parendame seda.

Basic Authe asemel kasutame JWT-d.

## Lahendus 2

[Lahendus 2](./solution/jwt-solution/README.md)

## Väljakutse

Lisa RBAC igale tööriistale, nagu kirjeldatud jaotises "Lisa RBAC MCP-le".

## Kokkuvõte

Loodetavasti õppisite selles peatükis palju, alates turvata olemisest kuni põhitõdede, JWT ja selle lisamiseni MCP-sse.

Oleme loonud tugeva aluse kohandatud JWT-dega, kuid kui kasvame, liigume standardipõhise identiteedimudeli suunas. Sellise IdP nagu Entra või Keycloak kasutuselevõtt võimaldab meil usaldusväärsele platvormile üle anda tokenite väljastamise, valideerimise ja elutsükli haldamise – vabastades meid rakenduse loogika ja kasutajakogemuse peale keskendumiseks.

Selle jaoks on meil olemas arenenum [peatükk Entrast](../../05-AdvancedTopics/mcp-security-entra/README.md)

## Mis järgmiseks

- Edasi: [MCP hostide seadistamine](../12-mcp-hosts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->