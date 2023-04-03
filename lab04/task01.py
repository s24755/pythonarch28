import math
def ilosc_opakowan(podlogiA, podlogiB, paneliA,  paneliB, iloscPaneli):
    powierzchnia = podlogiA*podlogiB*1.1
    powierzchniaPanelaOpakowanie = paneliA*paneliB*iloscPaneli
    iloscOpakowan = powierzchnia/powierzchniaPanelaOpakowanie
    return print(round(iloscOpakowan, 1))

ilosc_opakowan(25, 50, 2.4, 5, 10)