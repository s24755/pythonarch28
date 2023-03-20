print("Ankieta czytelnicza\n")

# Pobranie imienia i nazwiska
imie = input("Jak masz na imię? ")
nazwisko = input("Jakie jest Twoje nazwisko? ")

# Pobranie odpowiedzi na pytania
pytanie1 = input("Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie?\nA. Oglądanie telewizji\nB. Czytanie książek\nC. Słuchanie muzyki\n")
pytanie2 = input("W jakich okolicznościach czytasz książki najczęściej?\nA. podczas podróży\nB. w czasie wolnym (po pracy, na urlopie)\nC. podczas pracy/nauki (to ich element)\n")
pytanie3 = input("Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?\nA. chęć poszerzenia wiedzy\nB. czytanie mnie relaksuje/odpręża\nC. fakt, że czytanie jest modne\n")
pytanie4 = input("Po książki w jakiej formie sięgasz najczęściej?\nA. papierowej (tradycyjnej)\nB. e-booki (książki elektroniczne) na komputerze\nC. e-booki na tablecie/telefonie\n")
pytanie5 = input("Ile książek czytasz średnio w ciągu roku?\nA. 0\nB. 1\nC. 2 lub 3\n")
pytanie6 = input("Jak często średnio czytasz książki?\nA. codziennie\nB. raz w tygodniu\nC. raz w miesiącu\n")
pytanie7 = input("Po jakie gatunki książek sięgasz najczęściej?\nA. kryminały/thrillery\nB. naukowe\nC. horrory\n")

# Wyświetlenie odpowiedzi w formacie pytanie: odpowiedź
print("\nWyniki ankiety:")
print("Pytanie: Jak masz na imię oraz nazwisko?")
print(f"Odpowiedź: {imie} {nazwisko}")
print("\nPytanie: Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie?")
print(f"Odpowiedź: {pytanie1}")
print("\nPytanie: W jakich okolicznościach czytasz książki najczęściej?")
print(f"Odpowiedź: {pytanie2}")
print("\nPytanie: Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?")
print(f"Odpowiedź: {pytanie3}")
print("\nPytanie: Po książki w jakiej formie sięgasz najczęściej?")
print(f"Odpowiedź: {pytanie4}")
print("\nPytanie: Ile książek czytasz średnio w ciągu roku?")
print(f"Odpowiedź: {pytanie5}")
print("\nPytanie: Jak często średnio czytasz książki?")
print(f"Odpowiedź: {pytanie6}")
print("\nPytanie: Po jakie gatunki książek sięgasz najczęściej?")
print(f"Odpowiedź: {pytanie7}")


