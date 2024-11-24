#include <stdio.h>

int a = 20;
int* p;

int main() {
	p = &a;

	printf("a에 저장된 변수 : %d\n", a); // 20
	printf("a가 저장된 메모리의 주소: %p\n", &a); // 00007FF74A57D000
	printf("p가 가르키는 주소(a의 주소) : %p\n", p); // 00007FF74A57D000
	printf("p가 가르키는 주소에 저장된 수 : %d\n", *p); //20

	return 0;
}