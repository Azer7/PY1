	#CHAPTER 5

cars = ['audi', 'bMw', 'subaru', 'toyota']
	# using IF equal
for car in cars:
	if car.lower() == "bmw":
		print(car.upper())
	else:
		print(car.title())

print("\n")
	# using IF Not equal
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

	# using IN
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

print("\n")
	
	# Exercise1

alien_color=input("color ")

if alien_color=="green":
	print("You get 5 points")
elif alien_color=="yellow":
	print("You get 15 points")
else:
	print("You get 10 points")

	# Exercise2
age=int(input("Please input age"))

if age<2 and age>0:
    print("младенец")
elif age>=2 and age<4:
    print("малыш")
elif age>=4 and age<13:
    print("ребенок")
elif age>=13 and age<20:
    print("подросток")
elif age>=20 and age<65:
    print("взрослый")
elif age>=65 and age<=150:
    print ("пожилой")
else:
    print("need correct age")

	# Exercise3
favorite_fruits=["banana", "orange", "apple"]

fruit=input("check if you like this fruit")

if fruit in favorite_fruits:
    print(f"you really like {fruit}")
else:
    print(f"you don't really like {fruit}")








