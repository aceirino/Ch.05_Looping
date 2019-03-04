'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
print("You are on the run from the...")
print("You can choose to drink, moderate speed, speed up or stop for the night.")
miles=0
thirst=0
tiredness=0
natives=-20
drinksleft=5
done=False
while done==False:
    print("A. Drink water.")
    print("B. Moderate speed.")
    print("C. Full speed.")
    print("D. Stop for the night.")
    print("E. Status chech.")
    print("Q. Quit.")
    user_choice=input("What do you choose to do?: ")
    if user_choice.lower()=="q":
        break
    elif user_choice.lower()=="e":
        print("Miles traveled:", miles)
        print("water left:", drinksleft)
        print("The natives are", natives, ("behind you"))
    elif user_choice.lower()=="d":
        tiredness=0
    elif user_choice.lower()=="c":
        miles+=random.randrange(10, 21)
        print("miles traveled: ", miles)
        natives=+random.randrange(7, 15)
    elif user_choice.lower()=="b":
        miles+=random.randrange(5, 13)
        thirst+=1
        tiredness=+1
        natives+=random.randrange(7, 15)
    elif user_choice.lower()=="a":
        if drinksleft==0:
            print("error")
        else:
            thirst=0
            drinksleft+=-1
    if thirst>6:
        print("You died of thirst!")
        break
    elif thirst>4:
        print("You are thirsty.")
    if tiredness>8:
        print("Your camel is dead")
        break
    elif tiredness>5:
        print("Your camel is getting tired")
    if natives==miles:
        print("natives caught you")
        break
    elif (miles-natives)<16:
        print("the natives are getting close!")
    if miles==200:
        print("you won!")
    if random.randrange(1,21)==2:
        print("you found an oasis!")