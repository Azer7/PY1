
#Working with lists

	#Just a list with element selection.
colors=["red", "blue", "green", "orange"]
print(colors)
print(colors[3].upper())
print(colors[-1].upper())
	#New list with using format or f.
cars=["bmw", "mercedes", "audi", "toyota"]
print("My favourite car is {0} Land Cruiser \n".format(cars[3].title()))
print(f"My favourite car is {cars[0].upper()} M5")
	#2 ways of adding new element to the list.
cars.append("suzuki")
print("\n",cars)

cars.insert(1, "jeep")
print("\n",cars)
	#Deleting element from the list by element number or elemen value.
poped_car=cars.pop(2)
print("\n", cars)
print("===", poped_car, "===")
	
cars.remove("suzuki")
print("\n" , cars)
	# Soring methods for lists
print("\n" , sorted(cars))

cars.reverse()
print("\n" ,cars)

cars.reverse()
print("\n" ,cars)

cars.sort()
print("\n" , cars)

cars.sort(reverse=True)
print("\n" , cars)

	#Element q-ty in lists
print("\n" ,len(cars))

print(cars[-4])

	#Homework
visit_places=["japan","korea","canada","new zeeland","italy"]


