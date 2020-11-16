colors=["red", "blue", "green", "orange"]
print(colors)

print(colors[3].upper())

print(colors[-1].upper())

cars=["bmw", "mercedes", "audi", "toyota"]

print("My favourite car is {0} Land Cruiser \n".format(cars[3].title()))
print(f"My favourite car is {cars[0].upper()} M5")

cars.append("suzuki")
print("\n",cars)

cars.insert(1, "jeep")
print("\n",cars)

poped_car=cars.pop(2)
print("\n", cars)
print("===", poped_car, "===")

cars.remove("suzuki")
print("\n" , cars)

print("\n" , sorted(cars))

cars.reverse()
print("\n" ,cars)

cars.reverse()
print("\n" ,cars)


cars.sort()
print("\n" , cars)

cars.sort(reverse=True)
print("\n" , cars)


print("\n" ,len(cars))

print(cars[-4])


visit_places=["japan","korea","canada","new zeeland","italy"]


