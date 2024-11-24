#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable:4996)

/*
포인터 : 어떤 변수의 메모리 주소를 저장하는 변수

변수의 주소를 얻고 싶을 때 : &
주소를 참조 할 때 : *

용도:
1. 메모리 관리를 효율적으로 하기 위해서
2. 고급 프로그래밍을 하기 위해
*/



int a = 20;
int* p; //정수형 변수를 가리키는 포인터

int main(void) {
	p = &a;

	printf("a의 값 : %d\n", a); // 20
	printf("a의 주소 : %p\n", &a); // 00007FF74A57D000
	printf("p의 값(가리키는 주소) : %p\n", p); // 00007FF74A57D000
	printf("p가 가리키는 변수의 값 : %d\n", *p); //20

	return 0;
}