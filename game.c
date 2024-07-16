#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int x , y , random , guess, usedLives = 0, flag = 0;
    int totalLives;

    // Lower Bound
    printf("Enter Lower bound: ");
    scanf("%d", &x);

    // Upper Bound
    printf("Enter Upper bound: ");
    scanf("%d", &y);

    // Seed the random number generator (To get more random outcome / unpredicatable outcome ) basically giving time to the rand().
    srand(time(0));

    // Generating random number between the lower and upper ! use ceil to get maximum chance and floor to get minimum chance.
    random = (rand() % (y - x + 1)) + x;
    totalLives = (int)ceil(log(y - x + 1) / log(2));

    printf("\n\tYou've only %d chances to guess the " "integer!\n\n" ,totalLives);

    while (usedLives < totalLives) {
        usedLives++;

        // Taking guessing number as input
        printf("Guess a number: ");
        scanf("%d", &guess);

        // Condition testing
        if (random == guess) {
            printf("Congratulations you did it in %d try!\n", usedLives);
            // Once guessed, loop will break
            flag = 1;
            break;
        }
        else if (random > guess) {
            printf("You guessed too small!\n");
        }
        else if (random < guess) {
            printf("You guessed too high!\n");
        }
    }

    // If Guessing is more than required guesses, shows this
    // output.
    if (!flag) {
        printf("\nThe number is %d\n", x);
        printf("\tBetter Luck Next time!\n");
    }
    return 0;
}
