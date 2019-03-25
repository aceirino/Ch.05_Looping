'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: aidan kugley
 1. Make the following program work.
   '''
print("This program takes three numbers and returns the sum.")
total=0

for i in range(3):
    x=int(input("Enter a number: "))
    total=total+x
print("The total is:", total)



'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(2,101):
    if i%2==0:
        print(i)





'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
countdown=10
while countdown>=0:
    print(countdown)
    countdown-=1
print("blast off!")





'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random
number=random.randrange(1,11)
print(number)





'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the number entries equal to zero,
     and the number of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
positive=0
negative=0
zero=0
total=0
for i in range(7):
    x=int(input("give me a number: "))
    total=total+x
    if x>=1:
        positive+=1
    elif x<=-1:
        negative+=1
    else:
        zero+=1
print("total:",total)
print("positives:",positive)
print("negatives:",negative)
print("zeroes:",zero)