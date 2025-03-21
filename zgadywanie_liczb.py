import random

def zapisz_wynik(imie, proby, poziom):
    with open("wyniki.txt", "a") as plik:
        plik.write(f"Gracz: {imie}, Próby: {proby}, Poziom: {poziom}\n")

def zgadywanie_liczby():
    print("Witaj w grze 'Zgadywanie Liczby'!")
    imie_gracza = input("Podaj swoje imię: ").strip()

    while True:
        # Wybór poziomu trudności
        print("\nWybierz poziom trudności:")
        print("1. Łatwy (1-50, 10 prób)")
        print("2. Średni (1-100, 7 prób)")
        print("3. Trudny (1-200, 5 prób)")

        poziom = input("Wybierz poziom (1/2/3): ").strip()
        if poziom == "1":
            zakres = 50
            maks_proby = 10
        elif poziom == "2":
            zakres = 100
            maks_proby = 7
        elif poziom == "3":
            zakres = 200
            maks_proby = 5
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            continue

        # Losowanie liczby
        wylosowana_liczba = random.randint(1, zakres)
        liczba_prob = 0

        print(f"\nZgadnij liczbę z zakresu od 1 do {zakres}. Masz {maks_proby} prób.")
        while liczba_prob < maks_proby:
            try:
                zgadnij = int(input("Wprowadź swoją liczbę: "))
                liczba_prob += 1

                if zgadnij < wylosowana_liczba:
                    print("Za mało! Spróbuj większej liczby.")
                elif zgadnij > wylosowana_liczba:
                    print("Za dużo! Spróbuj mniejszej liczby.")
                else:
                    print(f"Gratulacje, {imie_gracza}! Odgadłeś liczbę {wylosowana_liczba} w {liczba_prob} próbach.")
                    zapisz_wynik(imie_gracza, liczba_prob, poziom)
                    break
            except ValueError:
                print("To nie jest poprawna liczba. Spróbuj ponownie.")

        # Sprawdzenie limitu prób
        if liczba_prob >= maks_proby and zgadnij != wylosowana_liczba:
            print(f"Przegrałeś! Wylosowana liczba to {wylosowana_liczba}.")
        
        # Pytanie o kolejną grę
        decyzja = input("\nCzy chcesz zagrać jeszcze raz? (t/n): ").strip().lower()
        if decyzja == "n":
            print("Dziękuję za grę. Miłego dnia!")
            break

# Uruchomienie gry
zgadywanie_liczby()
