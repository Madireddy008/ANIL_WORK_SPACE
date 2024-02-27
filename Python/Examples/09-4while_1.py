'''

Sentinel Controlled Statement
In this, we don’t use any counter variable because we don’t know how many times the loop will execute. Here user decides how many times he wants to execute the loop. For this, we use a sentinel value. A sentinel value is a value that is used to terminate a loop whenever a user enters it, generally, the sentinel value is -1.

Python while loop with user input

Here, It first asks the user to input a number. if the user enters -1 then the loop will not execute, i.e.

The user enters 6 and the body of the loop executes and again asks for input
Here user can input many times until he enters -1 to stop the loop
User can decide how many times he wants to enter input

'''




a = int(input('Enter a number (-1 to quit): ')) 

while a != -1: 
	a = int(input('Enter a number (-1 to quit): '))
