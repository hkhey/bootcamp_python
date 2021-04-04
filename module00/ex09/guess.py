import random

n = random.randint(0, 99)
print(n)
print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")
attempts=0
x=''
while(x!=n):
    x=input("What\'s your guess between 1 and 99?\n")
    if(x=="exit"):
        print("Goodbye!")
        break
    if(x.isalpha()):
        print("Error")
    else:
        x=int(x)
        if(x<n):
            print("Too low!")
        if(x>n):
            print("Too high!")
        attempts+=1
if attempts == 1:
	print("The answer to the ultimate question of life, the universe and everything is",n,".\nCongratulation! You got it on the first try!")
elif attempts > 1:
	print("You won with in ",attempts,"attemps")
