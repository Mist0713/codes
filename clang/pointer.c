#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable:4996)

/*
������ : � ������ �޸� �ּҸ� �����ϴ� ����

������ �ּҸ� ��� ���� �� : &
�ּҸ� ���� �� �� : *

�뵵:
1. �޸� ������ ȿ�������� �ϱ� ���ؼ�
2. ��� ���α׷����� �ϱ� ����
*/



int a = 20;
int* p; //������ ������ ����Ű�� ������

int main(void) {
	p = &a;

	printf("a�� �� : %d\n", a); // 20
	printf("a�� �ּ� : %p\n", &a); // 00007FF74A57D000
	printf("p�� ��(����Ű�� �ּ�) : %p\n", p); // 00007FF74A57D000
	printf("p�� ����Ű�� ������ �� : %d\n", *p); //20

	return 0;
}