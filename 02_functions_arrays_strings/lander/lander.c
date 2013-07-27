#include <stdio.h>

#define true 1
#define false 0

void title(){
	printf("Lunar\n");
}

void instructions(){
	printf(
"This is a simulation of an Apollo Lunar\n"
"landing capsule.\n\n\n"
"The on-board computer has failed, so you\n"
"have to land the capsule manually.\n\n"
"Set the burn rate of the retro rockets\n"
"to any value between 0 (free fall) and 200\n"
"(maximum thrust) pounds per second. Set a new\n"
"burn rate every 10 seconds.\n\n"
"Capsule weight is 32,500 lbs; fuel weight 16,500 lbs\n"
"\n\n\nGood luck!\n\n\n"
	);
}

void header(){
	printf("SEC\tMI + FT\tMPH\tLB Fuel\tBurn Rate\n");
}

int line(int round, float height, float mph, int fuel){
	int thrust = 0;

	printf("%d\t%d %d\t%d\t%d\t? ",
		round,
		(int)height, (int)(5280 * (height - (int) height)),
		mph, fuel
	);

	do {
		scanf("%d\n", &thrust);
		if(thrust < 0) {
			printf("Can't accelerate into the moon.\n");
		} else if (thrust > 200) {
			printf("This capsule's engine can't produce that much thrust.\n");
		} else {
			return thrust;
		}

	} while(true);
}

void main(){
	title();
	instructions();

	int playing = true;

	while(playing){
		int L = 0;
		float A=120, V=1, N=32500, M=16500, G = 1E-03, Z = 1.8;

		header();
		int k = line(L, A, 3600*V, N-M);

	}
}