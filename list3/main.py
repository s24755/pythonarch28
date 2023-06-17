#Zadanie 1 (4pkt):
#Utwórz klasę iteratora dla listy. Użyj go do wstawienia elementów listy lista1 do strina.
# elementy mają znajdować się w stringu jednym wierszu niczym nierozdzielone:

class ListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.lst):
            result = self.lst[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
wynik1 = ""

for i in ListIterator(lista1):
    wynik1 += str(i)

print(wynik1)


#Zadanie2: (4pkt)
#Napisz funkcję fizzbuzz(n), która używając listy składanej zwróci
#listę od 1 do n włącznie liczb lub wyrazów Fizz, Buzz, FizzBuzz, zgodnie ze standradową
#reguła gry w FizzBuzz:
#Jeśli liczba jest podzielna przez 3 i niepodzielna przez 5, zamiast liczby mamy "Fizz".
#Jeśli liczba jest podzielna przez 5 i niepodzielna przez 3, zamiast liczby mamy "Buzz".
#Jeśli liczba jest zarówno podzielna przez 3, jak i przez 5, zamiast liczby mamy "FizzBuzz".
def fizbuzz(n):
    return ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in
            range(1, n + 1)]

wynik2 = fizbuzz(16)
print(wynik2)

#Zadanie 3 (4pkt):
#Napisz generator zwracający n wyrazów ciągu Lucasa
#do wyniku zapisz 6 element tego ciągu.

def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

wynik3 = list(lucas(6))[5]
print(wynik3)

#Zadanie4 (4pkt):
#Uzyj klasy napisanej na ostatnich zajęciach - wersji z iteratorem (wklej tutaj klasę)
#Do przechowywania znaków kodu javy z pliku Main.java.

class MyClass:
    def __init__(self):
        self.data = []

    def __iter__(self):
        return iter(self.data)

    def add(self, value):
        self.data.append(value)

    def size(self):
        return len(self.data)

obiekt = MyClass()
wynik4 = ""

#następnie wstaw do niej znaki z kodu javy, które wczytasz z pliku Main.java
#ODKOMENTUJ poniższą linijkę, gdy utworzysz obiekt i dodasz do niego znaki:
'''
!odkomentuj wynik4!:
'''
with open("Main.java", "r") as f:
    for line in f:
        for char in line:
            obiekt.add(char)

wynik4 = obiekt.size()
print(wynik4)

#Zadanie 5 (4pkt):
#Napisz funkcję, która sprawdzi poprawność kodu javy, używając obiektu z poprzedniego zadania
# i uwzględniając tylko nawiasy w kodzie.
#funkcja ma zwrocic True albo False w zależności czy kod jest poprawny czy nie.

def validation(kod_o):
    stack = []
    for char in kod_o:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            top = stack.pop()
            if char == ")" and top != "(":
                return False
            elif char == "}" and top != "{":
                return False
            elif char == "]" and top != "[":
                return False
    return not stack

wynik5 = validation(kod_o=obiekt)
print(wynik5)







