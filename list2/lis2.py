import ssl
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import cross_val_score, LeaveOneOut

ssl._create_default_https_context = ssl._create_unverified_context

#Wczytaj dane z adresu podanego w pliku tekstowym: pliktextowy.txt
# do ramki danych.
#Użyj reszty wierszy jako nagłówków ramki danych.
#Uwaga! Zobacz która zmienna jest zmienną objaśnianą, będzie to potrzebne do dalszych zadań.

# Wczytanie pliku tekstowego z adresami URL
with open('pliktextowy.txt') as file:
    lines = file.readlines()
headers = [header.strip() for header in lines[1:]]
df = pd.read_csv(lines[0], header=None, names=headers)

#Zadanie1 przypisz nazwy kolumn z df w jednej linii:   (2pkt)

wynik1 = df.columns.tolist()
print(wynik1)

#Zadanie 2: Wypisz liczbę wierszy oraz kolumn ramki danych w jednej linii.  (2pkt)
wynik2 =  f"Liczba wierszy: {len(df)}, Liczba kolumn: {len(df.columns)}"
print(wynik2)


#Zadanie Utwórz klasę Wine na podstawie wczytanego zbioru:
#wszystkie zmienne objaśniające powinny być w liscie.
#Zmienna objaśniana jako odrębne pole.
# metoda __init__ powinna posiadać 2 parametry:
#listę (zmienne objaśniające) oraz liczbę(zmienna objaśniana).
#nazwy mogą być dowolne.

# Klasa powinna umożliwiać stworzenie nowego obiektu na podstawie
# już istniejącego obiektu jak w pdf z lekcji lab6.
# podpowiedź: metoda magiczna __repr__
#Nie pisz metody __str__.

#Zadanie 3 Utwórz przykładowy obiekt:   (3pkt)
class Wine:
    def __init__(self, features, target):
        self.features = features
        self.target = target

    def __repr__(self):
        return f"Wine({self.features}, {self.target})"

features = df.iloc[0, :-1].tolist()
target = df.iloc[0, -1]
wine = Wine(features, target)
wynik3 = repr(wine)
#do podmiany. Pamiętaj - ilość elementów, jak w zbiorze danych.
#Uwaga! Pamiętaj, która zmienna jest zmienną objaśnianą
print(wynik3)

#Zadanie 4.                             (3pkt)
#Zapisz wszystkie dane z ramki danych do listy obiektów typu Wine.
#Nie podmieniaj listy, dodawaj elementy.
##Uwaga! zobacz w jakiej kolejności podawane są zmienne objaśniające i objaśniana.
# Podpowiedź zobacz w pliktextowy.txt
wineList = []
for _, row in df.iterrows():
    features = row[:-1].tolist()
    target = row[-1]
    wine = Wine(features, target)
    wineList.append(wine)

wynik4 = len(wineList)
print(wynik4)

#Zadanie5 - Weź ostatni element z listy i na podstawie         (3pkt)
#wyniku funkcji repr utwórz nowy obiekt - eval(repr(obiekt))
#do wyniku przypisz zmienną objaśnianą z tego obiektu:
last_wine = wineList[-1]
new_wine = eval(repr(last_wine))
wynik5 = new_wine.target
print(wynik5)


#Zadanie 6:                                                          (3pkt)
#Zapisz ramkę danych  do bazy SQLite nazwa bazy(dopisz swoje imię i nazwisko):
# wines_imie_nazwisko, nazwa tabeli: wines.
#Następnie wczytaj dane z tabeli wybierając z bazy danych tylko wiersze z typem wina nr 3
# i zapisz je do nowego data frame:
import sqlite3

conn = sqlite3.connect('wines_Jan_Dziekan.db')
df.to_sql('wines', conn, if_exists='replace', index=False)
query = "SELECT * FROM wines WHERE TypeOf = 3"
wynik6 = pd.read_sql_query(query, conn)
conn.close()

print(wynik6.shape)


#Zadanie 7                                                          (1pkt)
#Utwórz model regresji Logistycznej z domyślnymi ustawieniami:
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

wynik7 = model.__class__.__name__
print(wynik7)

# Zadanie 8:                                                        (3pkt)
#Dokonaj podziału ramki danych na dane objaśniające i  do klasyfikacji.
#Znormalizuj dane objaśniające za pomocą:
#X = preprocessing.normalize(X)
# Wytenuj model na wszystkich danych bez podziału na zbiór treningowy i testowy.
# Wykonaj sprawdzian krzyżowy, używając LeaveOneOut() zamiast KFold (Parametr cv)
#  Podaj średnią dokładność (accuracy)

X = df.drop(columns=['TypeOf'])
X = preprocessing.normalize(X)
y = df['TypeOf']
model = LogisticRegression()
scores = cross_val_score(model, X, y, cv=LeaveOneOut())

wynik8 = scores.mean()
print(wynik8)