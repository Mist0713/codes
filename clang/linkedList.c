/*#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
	int data;
	struct Node* next;
}Node;

Node* create_node(int data) {
	Node* new_node = (Node*)malloc(sizeof(Node));
	new_node->data = data;
	new_node->next = NULL;
	return new_node;
}

void append(Node** head, int data) {
	Node* new_node = create_node(data);

	if (*head == NULL) {
		*head = new_node;
		return;
	}
	Node* temp = *head;
	while (temp->next != NULL) {
		temp = temp->next;
	}
	temp->next = new_node;
}

void delect_node(Node** head, int key) {
	Node* temp = *head;
	Node* pery = NULL;

	//ù ��° ��� ����
	if (temp != NULL && temp->data == key) {
		*head = temp->next;
		free(temp);
		return 0;
	}
	while (temp != NULL && temp->data != key) {
		int prev = temp;
		temp = temp->next;
	}
	//ã�°� ����
	if (temp == NULL) return;

	prev->next = temp->next;
	free(temp);
}

void print_list(Node* head) {
	Node* temp = head;
	while (temp != NULL) {
		printf("%d - >", temp->data);
		temp = temp->next;
	}
	printf("NULL\n");
}

int main(void) {

	Node* head = NULL;

	append(&head, 1);
	append(&head, 2);
	append(&head, 3);
	append(&head, 4);
	append(&head, 5);
	append(&head, 6);

	print_list(head);

	return 0;
}*/

#include <stdio.h>
#include <stdlib.h>

// ��带 ����ü�� ����
typedef struct Node {
    int data;
    struct Node* next;
}Node;

//��� ����
Node* create_node(int data) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data = data;
    new_node->next = NULL;
    return new_node;
}

//����Ʈ�� ��带 �߰�
void append(Node** head, int data) {
    Node* new_node = create_node(data);
    if (*head == NULL) {
        *head = new_node;
        return;
    }
    Node* temp = *head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = new_node;
}
//����
void delete_node(Node** head, int key) {
    Node* temp = *head;
    Node* prev = NULL;

    //ù��° ��尡 ������ ����� ���
    if (temp != NULL && temp->data == key) {
        *head = temp->next;
        free(temp);
        return;
    }
    //������ ��� ã��
    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }
    //������ �����Ͱ� ���� ���
    if (temp == NULL) return;

    //��� ����
    prev->next = temp->next;
    free(temp);
}
void print_list(Node* head) {
    Node* temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}
int main(void) {

    Node* head = NULL;
    append(&head, 1);
    append(&head, 2);
    append(&head, 3);
    append(&head, 4);

    print_list(head);

    delete_node(&head, 2);
    print_list(head);
}