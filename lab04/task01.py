import math
def ilosc_opakowan(dlugosc_podlogi, szerokosc_podlogi, dlugosc_panela, szerokosc_panela, ilosc_paneli_w_opakowaniu):
    powierzchnia_pomieszczenia = (dlugosc_podlogi * szerokosc_podlogi) * 1.1
    powierzchnia_pakietu_paneli = dlugosc_panela * szerokosc_panela * ilosc_paneli_w_opakowaniu
    ilosc_paneli = math.ceil(powierzchnia_pomieszczenia / powierzchnia_pakietu_paneli)
    ilosc_opakowan = math.ceil(ilosc_paneli / ilosc_paneli_w_opakowaniu)
    return ilosc_opakowan