import argparse
import math

def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

while True:
    liczby = input("Podaj ciąg liczb oddzielonych przecinkami: ")
    ciag = [int(x) for x in liczby.split(',')]
    for x in ciag:
        if czy_pierwsza(x):
            print(f"Liczba {x} jest liczbą pierwszą")
        else:
            print(f"Liczba {x} nie jest liczbą pierwszą")
