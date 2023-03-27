import random

cities = ["Warszawa", "Kraków", "Łódź", "Wrocław", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"]
visitedCities = []

for i in range(10):
    city = random.choice(cities)
    visitedCities.append(city)
    cities.remove(city)

print("Plan wycieczki:")
for i, city in enumerate(visitedCities):
    print(i+1, city)