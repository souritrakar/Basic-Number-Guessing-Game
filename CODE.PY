import random 
chance = 4
randomnumber = random.randint(1,100)
mylimit= 100



while(chance>0):
    userinput = int(input("Enter guess for the generated random number"))
    if(userinput==randomnumber):
        print("You won!")
        break
    elif(userinput!=randomnumber):
        if(userinput>randomnumber and userinput<100):
            print("Lower")
            chance-=1
            print("Chances left:" , chance)
        elif(userinput<randomnumber and userinput<100):
            print("Higher")
            chance-=1
            print("Chances left:" , chance)
    
    elif(userinput>100):
        print("Guess can't be more than limit")

        
  


print("Your chances are over, the number was " , randomnumber)