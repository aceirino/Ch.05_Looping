'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
import random
wins = 0
losses = 0
computer =0
quit = False
while quit == False:

    print("1: Rock")
    print("2: Paper")
    print("3: Scissors")
    print("4: Status")
    print("5: Quit")

    choice = int(input("Please shoot! "))

    if choice==5:
        break

    if choice!=4:

        if choice == 1:
            choicename = "Rock"
        elif choice == 2:
            choicename = "Paper"
        elif choice == 3:
            choicename = "Scissors"



        computer = random.randrange(1,4)
        if computer == 1:
            computername = "Rock"
        elif computer == 2:
            computername = "Paper"
        else:
            computername = "Scissors"

        print("You chose ",choicename," and the computer chose ", computername)


        if choice == computer:
            print("tie")
        elif choice==1 and computer==2:
            print("lose")
            losses=losses+1
        elif choice==2 and computer==3:
            print("lose")
            losses = losses + 1
        elif choice==3 and computer==1:
            print("lose")
            losses = losses + 1
        else:
            print("win")
            wins=wins+1
    else:
        print("wins", wins)
        print("losses", losses)

print("wins", wins)
print("losses", losses)