#include <stdlib.h>
#include <stdio.h>
int main(){
	double r = 0;
	double a = 0;
	double b = 0;
	double sum = 0; //total
	printf("請輸入a: ");
	scanf_s("%lf", &a);
	printf("請輸入b: ");
	scanf_s("%lf", &b);
	printf("請輸入r: ");
	scanf_s("%lf", &r);
	sum = a * (1 + r); // 第一期期末
	sum = (sum + b) * (1 + r); //第二期期末
	printf("結果: %lf\n", sum);
	system("pause");
	return 0;
}