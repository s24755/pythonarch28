import getpass
import random

import prompt as prompt


def playerChoice(playerName):
    choice = input(playerName + ", wybierz papier (P), nożyce (N) lub kamień (K): ")
    while choice not in ["P", "N", "K"]:
        choice = input("Nieprawidłowy wybór. " + playerName + ", wybierz papier (P), nożyce (N) lub kamień (K): ")
    return choice

def computerChoice():
    return random.choice(["P", "N", "K"])

def round(p1Name, p2Name=None):
    if p2Name is None:
        p2Name = "Komputer"
        p2Choice = computerChoice()
    else:
        if p2Name == "Komputer":
            p2Choice = computerChoice()
        else:
            p2Choice = playerChoice(p2Name)

    p1Choice = playerChoice(p1Name)

    print(p1Name + " wybral: ", p1Choice)
    print(p2Name + " wybral: ", p2Choice)

    if p1Choice == p2Choice:
        print("Remis")
        return None

    if p1Choice == "P" and p2Choice == "N" or \
            p1Choice == "N" and p2Choice == "K" or \
            p1Choice == "K" and p2Choice == "P":
        print(p1Name + " wygrywa rundę!")
        return p1Name

    print(p2Name + " wygrywa rundę!")
    return p2Name
def game(rounds, p1Name, p2Name = None):
    p1Score = 0;
    p2Score = 0;

    for i in range(rounds):
        print("Runda", i+1, ":")
        roundWinner = round(p1Name, p2Name)

        if roundWinner is None:
            continue
        elif roundWinner == p1Name:
            p1Score += 1
        else:
            p2Score += 1

        print("Wynik po rundzie", i+1, ":", p1Name, p1Score, "-", p2Score, p2Name)
    print("\nWynik końcowy:", p1Name, p1Score, "-", p2Score, p2Name)
    if p1Score > p2Score:
        print(p1Name, "wygral gre")
    elif p2Score > p1Score:
        print(p2Name, "wygral gre")
    else:
        print("remis")


print("Witaj w grze Papier, Nozyce, Kamien\n")
rounds = int(input("Ile rund chcesz zagrac?"))
p1Name = input("Podaj imie gracza 1:")
p2Choice = input("Czy chcesz grac z komputerem? (t/n)")

if p2Choice =="t":
    p2Name = "Komputer"
else:
    p2Name = input("Podaj imie gracza 2:")

if  p2Name != "Komputer":
    p2Name = getpass.getpass(prompt="Podaj haslo dla gracza2:")

game(rounds, p1Name, p2Name)