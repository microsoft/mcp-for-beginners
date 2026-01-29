# Implementacja Azure Content Safety z MCP

Aby wzmocnić bezpieczeństwo MCP przed atakami typu prompt injection, tool poisoning oraz innymi specyficznymi zagrożeniami AI, zdecydowanie zaleca się integrację z Azure Content Safety.

## Integracja z serwerem MCP

Aby zintegrować Azure Content Safety z serwerem MCP, dodaj filtr bezpieczeństwa treści jako middleware w potoku przetwarzania żądań:

1. Zainicjuj filtr podczas uruchamiania serwera  
2. Waliduj wszystkie przychodzące żądania narzędzi przed ich przetworzeniem  
3. Sprawdzaj wszystkie wychodzące odpowiedzi przed zwróceniem ich do klientów  
4. Rejestruj i zgłaszaj naruszenia bezpieczeństwa  
5. Wdróż odpowiednie obsługi błędów dla nieudanych kontroli bezpieczeństwa treści  

Zapewnia to solidną ochronę przed:  
- Atakami typu prompt injection  
- Próbami tool poisoning  
- Wyciekiem danych poprzez złośliwe dane wejściowe  
- Generowaniem szkodliwych treści  

## Najlepsze praktyki integracji Azure Content Safety

1. **Własne listy blokujące**: Twórz dedykowane listy blokujące dla wzorców ataków MCP injection  
2. **Dopasowanie poziomu zagrożenia**: Dostosuj progi ważności w zależności od konkretnego zastosowania i poziomu ryzyka  
3. **Kompleksowe pokrycie**: Stosuj kontrole bezpieczeństwa treści do wszystkich danych wejściowych i wyjściowych  
4. **Optymalizacja wydajności**: Rozważ wdrożenie mechanizmów cache’owania dla powtarzających się kontroli bezpieczeństwa  
5. **Mechanizmy awaryjne**: Zdefiniuj jasne zachowania awaryjne na wypadek niedostępności usług bezpieczeństwa treści  
6. **Informowanie użytkowników**: Zapewnij czytelną informację zwrotną dla użytkowników, gdy treść zostanie zablokowana ze względów bezpieczeństwa  
7. **Ciągłe doskonalenie**: Regularnie aktualizuj listy blokujące i wzorce na podstawie pojawiających się zagrożeń

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.