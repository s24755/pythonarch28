numbers = input("Podaj liczby rodzieloen przecinkami: ")
listNumber = numbers.split(",")
minNumber = int(listNumber[0])
maxNumber = int(listNumber[0])

for number in listNumber:
    if int(number) < minNumber:
        minNumber = int(number)
    if int(number) > maxNumber:
        maxNumber = int(number)

print("Najmniejsza liczba to:", minNumber)
print("Najwieksza liczba to:", maxNumber)