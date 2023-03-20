num1 = float(input("Podaj pierwszą liczbę: "))
num2 = float(input("Podaj drugą liczbę: "))
operator = input("Podaj operator (+, -, *, /): ")

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    if num2 == 0:
        print("Nie można dzielić przez 0")
    else:
        print(num1 / num2)
else:
    print("Nieznany operator")
