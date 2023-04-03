def cezar_szyfruj(wiadomosc, klucz, alfabet='abcdefghijklmnopqrstuvwxyz'):
    zaszyfrowana_wiadomosc = ""
    for znak in wiadomosc:
        if znak.lower() in alfabet:
            indeks_znaku = alfabet.index(znak.lower())
            indeks_znaku_zaszyfrowany = (indeks_znaku + klucz) % len(alfabet)
            if znak.isupper():
                zaszyfrowana_wiadomosc += alfabet[indeks_znaku_zaszyfrowany].upper()
            else:
                zaszyfrowana_wiadomosc += alfabet[indeks_znaku_zaszyfrowany]
        else:
            zaszyfrowana_wiadomosc += znak
    return zaszyfrowana_wiadomosc

print(cezar_szyfruj("Jan Dziekan", 3))
'Mdq Gclhndq'

print(cezar_szyfruj("Jan Dziekan", 3, alfabet='ABCDEFGHIOKLMNOPQRSTUVWXYZ'))
'Jan Dziekan'

