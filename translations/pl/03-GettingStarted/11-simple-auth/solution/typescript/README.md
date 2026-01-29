# Uruchom przykład

## Zainstaluj zależności

```sh
npm install
```

## Budowanie

```sh
npm run build
```

## Generowanie tokenów

```sh
npm run generate
```

To tworzy token w pliku *.env*. Klient będzie odczytywał dane z tego pliku.

## Uruchom kod

Uruchom serwer za pomocą:

```sh
npm start
```

Uruchom klienta w osobnym terminalu za pomocą:

```sh
npm run client
```

W terminalu serwera powinieneś zobaczyć wynik podobny do:

```text
User exists
User has required scopes
Middleware executed
```

a w terminalu klienta powinieneś zobaczyć wynik podobny do:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### Zmiana ustawień

Upewnijmy się, że rozumiemy zakresy. Znajdź plik *server.ts* i ten kod:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

To oznacza, że przekazany token musi mieć "User.Read". Zmieńmy to na "User.Write". Teraz uruchom `npm run build` i ponownie uruchom serwer `npm start`. Powinieneś teraz zobaczyć, że uwierzytelnianie się nie powiodło, ponieważ nie mamy tego zakresu (mamy User.Read i Admin.Write):

Klient teraz wyświetla

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

a w terminalu serwera możesz zobaczyć, że wyświetla:

```text
User exists
```

i nie przechodzi dalej.

Możesz albo dodać ten zakres "User.Write", uruchomić `npm run generate` i ponownie uruchomić klienta, albo zmienić kod serwera z powrotem.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.