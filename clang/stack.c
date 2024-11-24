#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

typedef struct Node {
	int data;
	struct Node* next;
}Node;

typedef struct Stack {
	Node* top;
}Stack;

//�ʱ�ȭ
void init_stack(Stack* stack) {
	stack->top = NULL;
}

//stack�� ����ִ��� Ȯ��(null �̸� �� �Լ��� ��ȯ���� 1)
int is_empty(Stack* stack) {
	return stack->top == NULL;
}

//push
void push(Stack* stack, int data) {
	Node* new_node = (Node*)malloc(sizeof(Node));
	new_node->data = data;
	new_node->next = stack->top;
	stack->top = new_node;
}

//pop
int pop(Stack* stack) {
	if (is_empty(stack)) {
		printf("�ش� ������ ������ϴ�\n");
		return -1;
	}
	Node* temp = stack->top;
	int pop_data = temp->data;
	stack->top = stack->top->next;
	free(temp);
	return pop_data;
}

void print_stack(Stack* stack) {
	Node* now_node = stack->top;
	while (now_node != NULL) {
		printf("%d ", now_node->data);
		now_node = now_node->next;
	}
	printf("\n");
}

int peek(Stack* stack) {
	if (is_empty(stack)) {
		printf("�ش� ������ ������ϴ�\n");
		return -1;
	}
	return stack->top->data;
}

int main(void) {
	Stack my_stack;
	init_stack(&my_stack);
	push(&my_stack, 10);
	push(&my_stack, 30);
	push(&my_stack, 50);
	push(&my_stack, 70);

	print_stack(&my_stack);

	printf("���� �� : %d\n", pop(&my_stack));
	print_stack(&my_stack);
	printf("top �� : %d\n", peek(&my_stack));
	return 0;
}