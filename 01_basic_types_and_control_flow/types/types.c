#include <stdio.h>
#include <string.h>
#include <math.h>

int main()
{
	printf("Hello, world\n");

	printf("%d, %d, %d, %d, %d\n", 2, 3, 5, 7, 11);

	printf("%f, %f, %f\n", 0.5, 1.27, 3.146);

	printf("%c%c%c%c%c\n", 'h', 'e', 'l', 'l', 'o');

	int i = 2;
	int j = 3;
	int k = 5;

	printf("%d, %d, %d\n", i, j, k);

	int m = 2 * 3;
	int n = 3 + 5;

	printf("%d, %d\n", m, n);

	float x = 0.5;
	float y = 1.27;
#define PI 3.146

	printf("%f, %f, %f\n", x, y, PI);

	float circumference_1 = PI * y;
	float circumference_2 = PI * n;

	printf("%f, %f\n", circumference_1, circumference_2);

	int average = (i + j + k) / 3;
	float average_2 = (i + j + k) / 3.0;

	printf("%d, %f\n", average, average_2);

	float a = 3.0;
	float b = 8.6;
	float c = 2.12;

	float discriminant = sqrt(b * b - 4 * a * c);
	float denominator = 2 * a;
	float x1 = (-b + discriminant) / denominator;
	float x2 = (-b - discriminant) / denominator;

	printf("%f %f", x1, x2);

	char* a = "Hello, world";
	char* c = "This is", " more text";

	printf("%s\n", a);
	printf("%s\n", c);

	printf("%d %d\n", strlen(a), strlen(c));

/*	printf(a.substring(4), b.substring(-4), c.substring(2, 9));*/

#define MIN_BALANCE 25
	int current_balance = 30;
	int transaction_amount = 10;

	if( (current_balance - transaction_amount) < MIN_BALANCE)
	{
		printf("This transaction is too large.\n");
	}
	else
	{
		current_balance -= transaction_amount;
	}
	printf("Your current balance is: $%d\n", current_balance);

	for(int l = 0; l < 10; l++)
	{
		printf("%d\n", l);
	}

	return 0;
}
