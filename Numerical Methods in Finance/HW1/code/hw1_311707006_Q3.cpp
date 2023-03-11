#include <iostream>
//#include <stdio.h>
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
	int day;
	double price,rate;
	printf("Please enter the rate(%%):");
	scanf("%lf",&rate);
	printf("Please enter the term(day):");
	scanf("%d",&day);
	price = 100000 - (100000 * (double(rate)/100) * (double(day)/365) );
	printf("The price of $100,000 commercial paper is %lf\n", price);

	system("pause");
	return 0;
}
