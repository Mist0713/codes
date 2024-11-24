#include <stdio.h>
#include <stdlib.h>
//��� ����ü ����
typedef struct Node {
	int data;
	struct Node* left;
	struct Node* right;
}Node;

//��� ����
Node* creatNode(int data) {
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;
	newNode->left = NULL;
	newNode->right = NULL;
	return newNode;
}

// ��ȸ : ����, ����, ���� ��ȸ�� ����
//���� ��ȸ : left-root-right


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
	//����Ʈ��
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