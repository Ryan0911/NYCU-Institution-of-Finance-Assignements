#include <stdlib.h>
#include <stdio.h>
int main(){
	double r = 0;
	double a = 0;
	double b = 0;
	double sum = 0; //total
	printf("�п�Ja: ");
	scanf_s("%lf", &a);
	printf("�п�Jb: ");
	scanf_s("%lf", &b);
	printf("�п�Jr: ");
	scanf_s("%lf", &r);
	sum = a * (1 + r); // �Ĥ@������
	sum = (sum + b) * (1 + r); //�ĤG������
	printf("���G: %lf\n", sum);
	system("pause");
	return 0;
}