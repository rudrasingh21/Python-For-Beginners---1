cities = ["mumbai","new york","paris"]
countries = ["india","usa","france"]

#ZIP function clube two list together

z=zip(cities,countries)

print(z)

for a in z:
    print(a)

#Comprihension
d={city:countries for city in zip(cities,countries)}

print(d)