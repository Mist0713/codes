#include <stdio.h>
#include <stdlib.h>
//노드 구조체 정의
typedef struct Node {
	int data;
	struct Node* left;
	struct Node* right;
}Node;

//노드 생성
Node* creatNode(int data) {
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;
	newNode->left = NULL;
	newNode->right = NULL;
	return newNode;
}

// 순회 : 중위, 후위, 전위 순회로 나뉨
//중위 순회 : left-root-right


void inOrder(Node* node) {
	if (node == NULL) return;

	inOrder(node->left);
	printf("%d ", node->data);
	inOrder(node->right);
}

void preOrder(Node* node) {
	if (node == NULL) return;

	printf("%d ", node->data);
	preOrder(node->left);
	preOrder(node->right);
}

void postOrder(Node* node){
	if (node == NULL) return;
	
	postOrder(node->left);
	postOrder(node->right);
	printf("%d ", node->data);
}


int main(void) {
	//이진트리
	Node* root = creatNode(1);
	root->left = creatNode(3);
	root->right = creatNode(5);
	root->left->left = creatNode(2);
	root->left->right = creatNode(4);

	inOrder(root);
	printf("\n");
	preOrder(root);
	printf("\n");
	postOrder(root);
	return 0;
}