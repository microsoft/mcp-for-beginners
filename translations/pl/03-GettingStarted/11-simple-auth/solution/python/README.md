# Uruchom przykład

## Utwórz środowisko

```sh
python -m venv venv
source ./venv/bin/activate
```

## Zainstaluj zależności

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Wygeneruj token

Musisz wygenerować token, którego klient użyje do komunikacji z serwerem.

Wywołaj:

```sh
python util.py
```

## Uruchom kod

Uruchom kod za pomocą:

```sh
python server.py
```

W osobnym terminalu wpisz:

```sh
python client.py
```

W terminalu serwera powinieneś zobaczyć coś podobnego do:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

W oknie klienta powinien pojawić się tekst podobny do:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

To oznacza, że wszystko działa.

### Zmień informacje, aby zobaczyć, jak to nie działa

Znajdź ten kod w *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Zmień go tak, aby mówił "User.Write". Twój obecny token nie ma tego poziomu uprawnień, więc jeśli ponownie uruchomisz serwer i spróbujesz uruchomić klienta jeszcze raz, powinieneś zobaczyć błąd podobny do poniższego w terminalu serwera:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Możesz albo przywrócić kod serwera do poprzedniego stanu, albo wygenerować nowy token, który zawiera ten dodatkowy zakres uprawnień – wybór należy do Ciebie.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.