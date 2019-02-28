'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
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
        tiredness==0