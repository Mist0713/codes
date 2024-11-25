#include <stdio.h>
#include <stdlib.h>

//노드를 구조체로 정의
typedef struct Node {
    int data;
    struct Node* next;
}Node;

//노드 생성
Node* create_node(int data) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data = data;
    new_node->next = NULL;
    return new_node;
}

//리스트에 노드를 추가
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
//삭제
void delete_node(Node** head, int key) {
    Node* temp = *head;
    Node* prev = NULL;

    //첫번째 노드가 삭제할 노드일 경우
    if (temp != NULL && temp->data == key) {
        *head = temp->next;
        free(temp);
        return;
    }
    //삭제할 노드 찾기
    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }
    //삭제할 데이터가 없는 경우
    if (temp == NULL) return;

    //노드 삭제
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