#include <stdio.h>

int main(void)
{
    int* ptr;     // ������ ����
    int** dptr;    // ���� ������ ����
    int num = 10;

    ptr = &num;    // �����Ϳ� num �ּ� ���� 

    dptr = &ptr;    // ���� �����Ϳ� ptr �ּ� ����

    printf("%d\n", **dptr);    // �����͸� �� �� �������Ͽ� num�� �޸� �ּҿ� ����
    printf("*dptr :  %p, ptr : %p \n", *dptr, ptr);
    /*
    *dptr : ptr�� ��
    ptr : num�� �ּ�
    &ptr : ������ ptr�� �ּ�
    *ptr : num
    */
    return 0;
}
/*
* : �����Ͱ� ����Ű�� ���� ���
& : ������ �ּ� ���
*/