#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable:4996)

int sum(int a, int b) {
	return a + b;
}

typedef struct {
	char name[50];
	int id;
	float score;
	char gender[5];
}Student;

int main(void) {
	Student student1;

	printf("�̸� : ");
	scanf("%s", student1.name);
	printf("�й� : ");
	scanf("%d", & student1.id);
	printf("���� : ");
	scanf("%f", & student1.score);
	printf("�� : ");
	scanf("%s", student1.gender);

	printf("%s\n", student1.name);
	printf("%d\n", student1.id);
	printf("%.2f\n", student1.score);
	printf("%s", student1.gender);

	return 0;
}