import random

def zgadywanie_liczby():
    print("Witaj w grze 'Zgadywanie Liczby'!")

    while True:
        # Losowanie liczby
        wylosowana_liczba = random.randint(1, 100)
        liczba_prob = 0  # Licznik prób

        print("\nZgadnij liczbę z zakresu od 1 do 100.")
        while True:
            try:
                # Odczyt liczby od użytkownika
                zgadnij = int(input("Wprowadź swoją liczbę: "))
                liczba_prob += 1

                if zgadnij < wylosowana_liczba:
                    print("Za mało! Spróbuj większej liczby.")
                elif zgadnij > wylosowana_liczba:
                    print("Za dużo! Spróbuj mniejszej liczby.")
                else:
                    print(f"Gratulacje! Odgadłeś liczbę {wylosowana_liczba} w {liczba_prob} próbach.")
                    break
            except ValueError:
                print("To nie jest poprawna liczba. Spróbuj ponownie!")

        # Pytanie o kolejną grę
        decyzja = input("\nCzy chcesz zagrać jeszcze raz? (t/n): ").strip().lower()
        if decyzja == "n":
            print("Dziękuję za grę. Miłego dnia!")
            break

# Uruchomienie gry
zgadywanie_liczby()
