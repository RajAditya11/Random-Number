#Hangman Game
import random 
from collections import Counter 

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split() 
word = random.choice(someWords) 

if __name__ == '__main__': 
    print('Guess the word! HINT: word is a name of a fruit') 

    for _ in word: 
        print('_', end=' ') 
    print() 

    letterGuessed = '' 
    chances = len(word) + 2
    flag = 0
    
    try: 
        while chances != 0 and flag == 0:
            print() 
            chances -= 1

            guess = input('Enter a letter to guess: ') 

            # Validation of the guess 
            if not guess.isalpha(): 
                print('Enter only a LETTER') 
                continue
            elif len(guess) > 1: 
                print('Enter only a SINGLE letter') 
                continue
            elif guess in letterGuessed: 
                print('You have already guessed that letter') 
                continue

            # If letter is guessed correctly 
            if guess in word: 
                k = word.count(guess) 
                for _ in range(k): 
                    letterGuessed += guess 

            # Print the word 
            for char in word: 
                if char in letterGuessed: 
                    print(char, end=' ') 
                else: 
                    print('_', end=' ') 

            if Counter(letterGuessed) == Counter(word): 
                print("\nThe word is:", word) 
                flag = 1
                print('Congratulations, You won!') 
        
        if chances == 0 and Counter(letterGuessed) != Counter(word): 
            print() 
            print('You lost! Try again..') 
            print('The word was {}'.format(word)) 

    except KeyboardInterrupt: 
        print() 
        print('Bye! Try again.') 
        exit() 

#MaterMind Game

import random

# the .randrange() function generates a random number within the specified range.
num = random.randrange(1000, 10000)

n = int(input("Guess the 4 digit number: "))

# condition to test equality of the guess made. Program terminates if true.
if n == num:
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    # ctr variable initialized. It will keep count of the number of tries the Player takes to guess the number.
    ctr = 0

    # while loop repeats as long as the Player fails to guess the number correctly.
    while n != num:
        # variable increments every time the loop is executed, giving an idea of how many guesses were made.
        ctr += 1

        count = 0

        # explicit type conversion of an integer to a string in order to ease extraction of digits
        n = str(n)

        # explicit type conversion of a string to an integer
        num = str(num)

        # for loop runs 4 times since the number has 4 digits.
        for i in range(4):
            # checking for equality of digits
            if n[i] == num[i]:
                # number of digits guessed correctly increments
                count += 1

        # when not all the digits are guessed correctly.
        if count > 0:
            print("Not quite the number. But you did get", count, "digit(s) correct!")
        else:
            print("None of the numbers in your input match.")

        print('\n')
        n = int(input("Enter your next choice of numbers: "))

    # condition for equality.
    ctr += 1
    print("You've become a Mastermind!")
    print("It took you only", ctr, "tries.")





#2048 Game

# logic.py to be 
# imported in the 2048.py file

# importing random package
# for methods to generate random
# numbers.
import random

# function to initialize game / grid
# at the start
def start_game():

	# declaring an empty list then
	# appending 4 list each with four
	# elements as 0.
	mat =[]
	for i in range(4):
		mat.append([0] * 4)

	# printing controls for user
	print("Commands are as follows : ")
	print("'W' or 'w' : Move Up")
	print("'S' or 's' : Move Down")
	print("'A' or 'a' : Move Left")
	print("'D' or 'd' : Move Right")

	# calling the function to add
	# a new 2 in grid after every step
	add_new_2(mat)
	return mat

# function to add a new 2 in
# grid at any random empty cell
def add_new_2(mat):

# choosing a random index for
# row and column.
	r = random.randint(0, 3)
	c = random.randint(0, 3)

	# while loop will break as the
	# random cell chosen will be empty
	# (or contains zero)
	while(mat[r] != 0):
		r = random.randint(0, 3)
		c = random.randint(0, 3)

	# we will place a 2 at that empty
	# random cell.
	mat[r] = 2

# function to get the current
# state of game
def get_current_state(mat):

	# if any cell contains
	# 2048 we have won
	for i in range(4):
		for j in range(4):
			if(mat[i][j]== 2048):
				return 'WON'

	# if we are still left with
	# atleast one empty cell
	# game is not yet over
	for i in range(4):
		for j in range(4):
			if(mat[i][j]== 0):
				return 'GAME NOT OVER'

	# or if no cell is empty now
	# but if after any move left, right,
	# up or down, if any two cells
	# gets merged and create an empty
	# cell then also game is not yet over
	for i in range(3):
		for j in range(3):
			if(mat[i][j]== mat[i + 1][j] or mat[i][j]== mat[i][j + 1]):
				return 'GAME NOT OVER'

	for j in range(3):
		if(mat[3][j]== mat[3][j + 1]):
			return 'GAME NOT OVER'

	for i in range(3):
		if(mat[i][3]== mat[i + 1][3]):
			return 'GAME NOT OVER'

	# else we have lost the game
	return 'LOST'

# all the functions defined below
# are for left swap initially.

# function to compress the grid
# after every step before and
# after merging cells.
def compress(mat):

	# bool variable to determine
	# any change happened or not
	changed = False

	# empty grid 
	new_mat = []

	# with all cells empty
	for i in range(4):
		new_mat.append([0] * 4)
		
	# here we will shift entries
	# of each cell to it's extreme
	# left row by row
	# loop to traverse rows
	for i in range(4):
		pos = 0

		# loop to traverse each column
		# in respective row
		for j in range(4):
			if(mat[i][j] != 0):
				
				# if cell is non empty then
				# we will shift it's number to
				# previous empty cell in that row
				# denoted by pos variable
				new_mat[i][pos] = mat[i][j]
				
				if(j != pos):
					changed = True
				pos += 1

	# returning new compressed matrix
	# and the flag variable.
	return new_mat, changed

# function to merge the cells
# in matrix after compressing
def merge(mat):
	
	changed = False
	
	for i in range(4):
		for j in range(3):

			# if current cell has same value as
			# next cell in the row and they
			# are non empty then
			if(mat[i][j] == mat[i][j + 1] and mat[i][j] != 0):

				# double current cell value and
				# empty the next cell
				mat[i][j] = mat[i][j] * 2
				mat[i][j + 1] = 0

				# make bool variable True indicating
				# the new grid after merging is
				# different.
				changed = True

	return mat, changed

# function to reverse the matrix
# means reversing the content of
# each row (reversing the sequence)
def reverse(mat):
	new_mat =[]
	for i in range(4):
		new_mat.append([])
		for j in range(4):
			new_mat[i].append(mat[i][3 - j])
	return new_mat

# function to get the transpose
# of matrix means interchanging
# rows and column
def transpose(mat):
	new_mat = []
	for i in range(4):
		new_mat.append([])
		for j in range(4):
			new_mat[i].append(mat[j][i])
	return new_mat

# function to update the matrix
# if we move / swipe left
def move_left(grid):

	# first compress the grid
	new_grid, changed1 = compress(grid)

	# then merge the cells.
	new_grid, changed2 = merge(new_grid)
	
	changed = changed1 or changed2

	# again compress after merging.
	new_grid, temp = compress(new_grid)

	# return new matrix and bool changed
	# telling whether the grid is same
	# or different
	return new_grid, changed

# function to update the matrix
# if we move / swipe right
def move_right(grid):

	# to move right we just reverse
	# the matrix 
	new_grid = reverse(grid)

	# then move left
	new_grid, changed = move_left(new_grid)

	# then again reverse matrix will
	# give us desired result
	new_grid = reverse(new_grid)
	return new_grid, changed

# function to update the matrix
# if we move / swipe up
def move_up(grid):

	# to move up we just take
	# transpose of matrix
	new_grid = transpose(grid)

	# then move left (calling all
	# included functions) then
	new_grid, changed = move_left(new_grid)

	# again take transpose will give
	# desired results
	new_grid = transpose(new_grid)
	return new_grid, changed

# function to update the matrix
# if we move / swipe down
def move_down(grid):

	# to move down we take transpose
	new_grid = transpose(grid)

	# move right and then again
	new_grid, changed = move_right(new_grid)

	# take transpose will give desired
	# results.
	new_grid = transpose(new_grid)
	return new_grid, changed

# this file only contains all the logic
# functions to be called in main function
# present in the other file




#ROCK PAPER SCISSER GAME

# import random module
import random
# print multiline instruction
# performstring concatenation of string
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    # take the input from user

    choice = int(input("Enter your choice :"))

    # OR is the short-circuit operator
    # if any one of the condition is true
    # then it return True value

    # looping until user enter invalid input
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please '))

        # initialize value of choice_name variable
    # corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

        # print user choice
    print('User choice is \n', choice_name)
    print('Now its Computers Turn....')

    # Computer chooses randomly any number
    # among 1 , 2 and 3. Using randint method
    # of random module
    comp_choice = random.randint(1, 3)

    # looping until comp_choice value
    # is equal to the choice value
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

     # initialize value of comp_choice_name
    # variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'RocK'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    print("Computer choice is \n", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)
    # we need to check of a draw
    if choice == comp_choice:
        print('Its a Draw', end="")
        result = "DRAW"
    # condition for winning
    if (choice == 1 and comp_choice == 2):
        print('paper wins =>', end="")
        result = 'Paper'
    elif (choice == 2 and comp_choice == 1):
        print('paper wins =>', end="")
        result = 'Paper'

    if (choice == 1 and comp_choice == 3):
        print('Rock wins =>\n', end="")
        result = 'Rock'
    elif (choice == 3 and comp_choice == 1):
        print('Rock wins =>\n', end="")
        result = 'RocK'

    if (choice == 2 and comp_choice == 3):
        print('Scissors wins =>', end="")
        result = 'Scissors'
    elif (choice == 3 and comp_choice == 2):
        print('Scissors wins =>', end="")
        result = 'Rock'
     # Printing either user or computer wins or draw
    if result == 'DRAW':
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("Do you want to play again? (Y/N)")
    # if user input n or N then condition is True
    ans = input().lower()
    if ans == 'n':
        break
# after coming out of the while loop
# we print thanks for playing
print("thanks for playing")
