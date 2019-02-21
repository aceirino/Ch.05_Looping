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

    if choice == 1:
        choice = "Rock"
    elif choice == 2:
        choice = "Paper"
    elif choice == 3:
        choice = "Scissors"
    elif choice == 4:
        choice = "Status"
    else:
        break

    for i in range (1):
        computer = random.randrange(3)
        if computer == 0:
            computer = "rock"
        elif computer == 1:
            computer = "paper"
        else:
            computer = "scissors"

    if choice == computer:
        print("tie")
    elif choice=="Rock" and computer=="paper":
        print("lose")
        losses=losses+1
    elif choice=="Paper" and computer=="scissors":
        print("lose")
        losses = losses + 1
    elif choice=="Scissors" and computer=="rock":
        print("lose")
        losses = losses + 1
    else:
        print("win")
        wins=wins+1

print("wins", wins)
print("losses", losses)