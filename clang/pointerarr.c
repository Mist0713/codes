#include <stdio.h>
#pragma warning(disable:4996)

int arr[3] = { 10, 20, 30 };
int *p_arr = arr;

int main() {
	printf("arr[0] : %d\n", arr[0]);
	//printf("pointer value : %p\n", &arr);
	printf("p_arr�� ����Ű�� ��(ù��° �ּ�) : %d\n", *p_arr);
	p_arr++;
	printf("p_arr�� ����Ű�� ��(ù��° �ּ�) : %d\n", *p_arr);
	p_arr--;
	printf("p_arr�� ����Ű�� ��(ù��° �ּ�) : %d\n", *p_arr);
	return 0;
}