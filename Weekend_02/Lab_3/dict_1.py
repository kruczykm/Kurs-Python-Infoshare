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

# Przykładowy tekst do przetestowania szyfru
s = "Hello World! Tajna wiadomosc."

# Pętla testująca różne warianty przesunięcia (od 1 do 13)
for shift in range(1, 13 + 1):
    d = {}  # Słownik mapujący: znak początkowy -> znak zaszyfrowany
    
    # 65 to kod ASCII dla 'A' (wielkie litery), 97 to kod ASCII dla 'a' (małe litery)
    for c in (65, 97): 
        # Przechodzimy przez wszystkie 26 liter alfabetu
        for i in range(26):
            # Klucz: aktualna litera (np. 'A' lub 'a')
            # Wartość: litera przesunięta o 'shift'. 
            # Modulo % 26 dba o to, żeby po 'Z' lub 'z' wrócić na początek alfabetu.
            d[chr(i + c)] = chr((i + shift) % 26 + c) 

    # Wyświetlamy zaszyfrowany tekst. 
    # d.get(c, c) oznacza: "pobierz zaszyfrowany znak ze słownika, a jeśli go tam nie ma (np. spacja, wykrzyknik), zostaw oryginał".
    print("Zaszyfrowane:", "".join([d.get(c, c) for c in s]))

    print(f"--- Przesunięcie o {shift} znaków ---")
    
    # POPRAWKA TUTAJ: Zamiast d.key() musi być d.keys() (z literką 's' na końcu)
    print("Klucze:  ", " ".join(d.keys()))
    print("Wartości:", " ".join(d.values()))
    print()  # Pusta linia dla czytelności w terminalu


