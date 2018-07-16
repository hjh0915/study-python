with open('planets.txt', 'r') as planets_file:
    planets = planets_file.readlines()

for planet in reversed(planets):
    print(planet.strip())

with open('planets.txt', 'r') as data_file:
    for line in data_file:
        print(len(line))

with open('planets.txt', 'r') as data_file:
    for line in data_file:
        print(len(line.strip()))