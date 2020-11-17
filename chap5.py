	#CHAPTER 5

cars = ['audi', 'bMw', 'subaru', 'toyota']

for car in cars:
	if car.lower() == "bmw":
		print(car.upper())
	else:
		print(car.title())

print("\n")

for car in cars:
	if car.lower() != "bmw":
		print(car.upper())
	else:
		print(car.title())	

print("\n")

age1=18
age2=19
age3=22

if age3>=22 and age2>22 or age1<17:
	print ("Проходите")
else:
	print("Запрет")	


print("\n")


if "subaru" in cars:
	print("Subrik est")

if "subru" not in cars:
	print("Subru netu")



