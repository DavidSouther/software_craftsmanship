#include <stdlib.h>
#include <stdio.h>

#define true 1
#define false 0

main(){

printf("HiLo\n");

printf("HiLo\n");
printf("\n");
printf("This is the game of HiLo.\n");
printf("\n");
printf("You will have 6 tries to guess the amount of money in the\n");
printf("HiLo jackpot, which is between 1 and 100 dollars. If you\n");
printf("guess the amount, you win all the money in the jackpot!\n");
printf("Then you get another change to win more money. However,\n");
printf("if you do not guess the amount, the game ends!\n");

int winnings = 0;
char done = false;

while(!done){
    int guesses = 0;
    int number = (rand() % 100) + 1;
    char lost = false;
    char again;

    while(!lost) {
    	int guess;
    	printf("What is your guess? ");
        int in = scanf("%d", &guess);

        if(in == 0){
            done = true;
            break;
        }

        if(guess == number){
            printf("Got it! You won %d dollars!\n", number);
            winnings = winnings + number;
            printf("Your total winnings are %d dollars!\n", winnings);
            printf("Play again? (Y/n) ");
            scanf("%c", &again);
            if(again != 'Y'){
                done = true;
        	}
            continue;
        } else {
            if (guess > number) {
                printf("Your guess was too high!\n");
            } else {
                printf("Your guess was too low!\n");
            }
        }

        guesses = guesses + 1;
        if(guesses >= 6){
            printf("You took too many guesses!\n");
            lost = done = true;
        }
    }
}

printf("Goodbye!\n");

}