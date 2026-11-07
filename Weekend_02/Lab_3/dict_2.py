s = """Gur Mra bs Clguba, ol Gvz Crgref

Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyrk.
Pbzcyrk vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcnefr vf orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orngf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""

# Przykładowy tekst do zaszyfrowania (zawiera małe/wielkie litery, spacje oraz interpunkcję)
s = "Hello World! Tajna wiadomosc."

print(f"Tekst oryginalny: {s}\n")

# Zewnętrzna pętla testuje różne warianty przesunięcia w szyfrze Cezara (od 1 do 13 znaków)
for shift in range(1, 13 + 1):
    
    # Tworzymy pusty słownik, który posłuży nam jako "mapa zamian" (klucz -> wartość)
    d = {} 
    
    # Alfabet ma dwie formy: wielkie litery ('A'-'Z') oraz małe litery ('a'-'z').
    # 65 to kod ASCII dla wielkiej litery 'A'.
    # 97 to kod ASCII dla małej litery 'a'.
    for c in (65, 97): 
        
        # Alfabet łaciński ma dokładnie 26 liter, więc iterujemy indeksy od 0 do 25.
        for i in range(26):
            
            # --- TWORZENIE MAPOWANIA (SZYFROWANIE JEDNEJ LITERY) ---
            # 1. chr(i + c): Pobiera aktualną czystą literę (np. 'a') i robi z niej KLUCZ.
            # 2. i + shift: Przesuwa literę o określoną liczbę miejsc w przód.
            # 3. % 26 (Modulo): Magiczny mechanizm "zawijania". Kiedy przekroczymy indeks 25 
            #    (koniec alfabetu, np. 'z'), reszta z dzielenia automatycznie wrzuca nas 
            #    z powrotem na początek alfabetu (czyli odlicza od 'a').
            # 4. chr(... + c): Zamienia wyliczony nowy indeks z powrotem na znak z tabeli ASCII (WARTOŚĆ).
            d[chr(i + c)] = chr((i + shift) % 26 + c) 

    # =========================================================================
    # --- SPRYTNE SZYFROWANIE CAŁEGO TEKSTU (List Comprehension + .join) ---
    # =========================================================================
    # Rozłóżmy tę potężną linijkę na czynniki pierwsze:
    #
    # 1. "for c in s": Pętla bierze po kolei każdy znak z naszego tekstu 's' 
    #    (najpierw 'H', potem 'e', spację, wykrzyknik itd.).
    #
    # 2. "d.get(c, c)": Metoda .get() sprawdza słownik 'd' dla danego znaku:
    #    - Jeśli znak JEST w słowniku (to litera): zwraca jej zaszyfrowany odpowiednik.
    #    - Jeśli znaku NIE MA w słowniku (np. spacja, kropka, wykrzyknik): metoda .get() 
    #      nie wyrzuca błędu, tylko zwraca drugą podaną wartość, czyli oryginalny znak 'c'.
    #
    # 3. [...] (List Comprehension): Zamykamy powyższą logikę w nawiasy kwadratowe, 
    #    co tworzy gotową listę przetworzonych pojedynczych znaków.
    #
    # 4. "".join(...): Biorę tę listę osobnych literek i sklejam je w jeden 
    #    spójny napis, używając pustego ciągu znaków "" jako łącznika (bez dodatkowych spacji).
    zaszyfrowana_wiadomosc = "".join([d.get(c, c) for c in s])

    # Wyświetlamy wynik dla aktualnego przesunięcia
    print(f"Przesunięcie o {shift:2d} znaków: {zaszyfrowana_wiadomosc}")

    # Poniżej opcjonalny podgląd mapy (używamy d.keys() oraz d.values())
    # print("Klucze:  ", "".join(d.keys()))
    # print("Wartości:", "".join(d.values()))
    # print("-" * 50)


