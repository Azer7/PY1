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


print("\n")

age10 = input("how old are you ")

while age10.isnumeric()!=True:
    age10 = input("Please enter correct value ")
    
age11=int(age10)    

if age11 in range(18,151):
    print("You are old enough for vote")
elif age11>150 or age11<0:
    print("out of range")
else:
    print("you are too young for vote")









