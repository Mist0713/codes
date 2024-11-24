#include <stdio.h>

int main(void)
{
    int* ptr;     // 포인터 선언
    int** dptr;    // 이중 포인터 선언
    int num = 10;

    ptr = &num;    // 포인터에 num 주소 대입 

    dptr = &ptr;    // 이중 포인터에 ptr 주소 대입

    printf("%d\n", **dptr);    // 포인터를 두 번 역참조하여 num의 메모리 주소에 접근
    printf("*dptr :  %p, ptr : %p \n", *dptr, ptr);
    /*
    *dptr : ptr의 값
    ptr : num의 주소
    &ptr : 포인터 ptr의 주소
    *ptr : num
    */
    return 0;
}
/*
* : 포인터가 가르키는 변수 출력
& : 포인터 주소 출력
*/