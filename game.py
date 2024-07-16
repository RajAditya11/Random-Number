import math
import random

def game( random , guess , usedMoves , state ) :
    if random == guess :
        print("Congratulation you did it in ", usedMoves , "moves\n")
        state = True
    elif random > guess :
        print("The number is too small.\n")
        state = False
    elif random < guess :
        print("The number is too large.\n")
        state = False


#Driver Code

#Taking Lower and Upper Bound as input from user.
print("Enter Lower Bound :")
x = int(input())
print("Enter Upper Bound :")
y = int(input())

#Using bool to handle the end outcome.
state = False

#Generating random number using random.randominit(lower,upper) for range.
randomNumber = random.randint(x , y)

#Find total moves using formula ( log2(upper-lower) + 1 )  and taking ceiling or floor value of the outcome to get total chances.
totalMoves = math.floor(math.log((y-x) + 1,2))

usedMoves = 0

while usedMoves < totalMoves :
    usedMoves += 1
    print("Remaining Moves : ", totalMoves-usedMoves)
    print("Enter your guess b/w range (" , x , "," , y , ")" , " :")
    guess = int(input())
    game( randomNumber , guess , usedMoves , state)
    if state == True :
        break

if state == False :
    print("You are out of Moves.\n\nGame Over")