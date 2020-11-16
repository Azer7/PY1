	#CHAPTER 4

cars=["bmw", "mercedes", "audi", "toyota", "suzuki"]

for car in cars:
	print(f"Do you want to bay this cool {car.upper()} ?")
	print(f"This brand new {car.upper()} looks really cool!\n")

print("=== All cars are cool! ===\n")	
print(car)

	#Exercise1
print("\n")

pizzas=["pepperoni", "margarita", "hawaian"]

for pizza in pizzas:
	print(pizza.upper())
	print(f"I like {pizza} pizza \n")

print("=== I really love pizza === \n")		


b=0
for a in range(1,65):
	print(a)
	b=b+a
print("\n")
print(b)	
print("\n")

numbers=list(range(1,65))
print(len(numbers))
print("\n")

for a in range(2,65,10):
	print(a)


print("\n")
squares=[]
for value in range(1,25,3):
	square=value**2
	squares.append(square)

print(squares)
print("\n")
aa1=sum(squares)
aa2=max(squares)
aa3=min(squares)
print(aa1)
print(aa2)
print(aa3)
print("\n")

	#Exercise2

for number in range(1,21):
	print(number)
print("\n")

million=[value for value in range(1,1000001)]	

print(min(million))
print("\n")
print(max(million))
print("\n")
print(sum(million))

for number in range(1,21,2):
	print(number)
print("\n")

for number in range(3,31,3):
	print(number)
print("\n")

for number in range(1,11):
	print(number**3)
print("\n")

cubes=[value**3 for value in range(1,11)]
print(cubes)
print("\n")

lands=["usa", "canada", "mexico", "UK", "Germany"]
print(lands[1:3])










