# Zgadywanie Liczby

Gra w zgadywanie liczby to prosty, ale angażujący projekt w Pythonie, stworzony z myślą o nauce i zabawie. Program losuje liczbę, a gracz próbuje ją odgadnąć na podstawie podpowiedzi. Gra posiada dodatkowe funkcjonalności, takie jak poziomy trudności, limit prób oraz zapis wyników do pliku.

---

## Funkcjonalności

- **Poziomy trudności**:
  - Łatwy: liczba z zakresu 1–50, limit 10 prób.
  - Średni: liczba z zakresu 1–100, limit 7 prób.
  - Trudny: liczba z zakresu 1–200, limit 5 prób.
  
- **Limit prób**: 
  - Gracz ma ograniczoną liczbę prób, w zależności od wybranego poziomu trudności.

- **Zapis wyników do pliku**:
  - Wyniki są zapisywane w pliku `wyniki.txt`, aby monitorować postępy gracza.

- **Podpowiedzi**:
  - Gra informuje, czy zgadywana liczba jest "za mała" lub "za duża".

- **Kontynuacja gry**:
  - Po każdej rundzie gracz decyduje, czy grać ponownie, czy zakończyć grę.

---

## Wymagania

- Python w wersji 3.6 lub nowszej.

---

## Jak uruchomić

1. **Krok 1**: Upewnij się, że Python jest zainstalowany na Twoim komputerze.
2. **Krok 2**: Pobierz plik `zgadywanie_liczby.py` i zapisz go w wybranym folderze.
3. **Krok 3**: Otwórz terminal w folderze z plikiem (lub użyj terminala VS Code).
4. **Krok 4**: Uruchom grę za pomocą polecenia:

   ```bash
   python zgadywanie_liczby.py
