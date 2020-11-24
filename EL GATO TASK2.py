# Build me a function that converts celsius to fahrenheit and vice versa depending on what user chooses.
print('Welcome to the function that converts celsius to fahrenheit and vice versa depending on what you choose')
def tempConverter():
    
    
    a=input(" Type 1 for °C to °F \n Type 2 for °F to °C \n   ")
    
    
    if a.isnumeric()==True:
        
        if int(a)==1:
            valueC=input("please enter °C value ")

            if valueC.isnumeric()==True:
                valueC=int(valueC)
                valueF = valueC * 1.8 + 32
                print(f"RESULT: {round(valueC,2)}°C = {valueF}°F ")
                print("\n")
            else:
                print("\n")
                print("ERROR. Please type correct value ")
                tempConverter() 

        elif int(a)==2:
            valueF=input("please enter °F value ")
            
            if valueF.isnumeric()==True:
                valueF=int(valueF)
                valueC= (valueF - 32) / 1.8
                print(f"RESULT: {round(valueF,2)}°F = {round(valueC,2)}°C ")
                print("\n")
            else:
                print("\n")
                print("ERROR. Please type correct value ")
                tempConverter() 
                
        else:
            print("\n")
            print("ERROR. Please type correct value ")
            tempConverter()
    else:
        print("\n")
        print("ERROR. Please type correct value ")
        tempConverter()         
        
    
tempConverter()

valueC=input("MANADESS")
