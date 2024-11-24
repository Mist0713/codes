#include <stdio.h>

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

	printf("이름 : ");
	scanf("%s", student1.name);
	printf("학번 : ");
	scanf("%d", & student1.id);
	printf("점수 : ");
	scanf("%f", & student1.score);
	printf("성별 : ");
	scanf("%s", student1.gender);

	printf("%s\n", student1.name);
	printf("%d\n", student1.id);
	printf("%.2f\n", student1.score);
	printf("%s", student1.gender);

	return 0;
}