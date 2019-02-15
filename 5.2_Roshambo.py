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
ties = 0
computer =0
while False:

    print("1: Rock")
    print("2: Paper")
    print("3: Scissors")
    print("4: Status")
    print("5: Quit")


# Renames the computer's choice to a word.
    for i in range (1):
        computer = random.randrange(3)
        if computer == 0:
            computer = "rock"
        elif computer == 1:
            computer = "paper"
        else:
            computer = "scissors"

#Ask the user for their choice
choice = int(input("Please shoot! "))

# Renames the user's choice to a word.
if choice == 1:
    choice = "Rock"
elif choice == 2:
    choice = "Paper"
elif choice == 3:
    choice = "Scissors"
elif choice == 4:
    choice = "Status"
else:
    choice = "Quit"

if "Rock"

print(wins)
print(losses)
print(ties)