#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
	int data;
	struct Node* next;
}Node;

typedef struct Queue {
	Node* front;
	Node* rear;
}Queue;

void init_queue(Queue* queue) {
	queue->front = queue->rear = NULL;
}

int is_empty(Queue* queue) {
	return queue->front == NULL;
}

void enqueue(Queue* queue, int data) {
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;
	newNode->next = NULL;

	if (is_empty(queue)) {
		queue->front = queue->rear = newNode;
	}
	else
	{
		queue->rear->next = newNode;
		queue->rear = newNode;
	}
}

int dequeue(Queue* queue) {
	if (is_empty(queue)) {
		printf("해당 큐가 비었습니다.\n");
		return -1;
	}
	Node *temp = queue->front;
	int dequeue_data = temp -> data;
	queue->front = queue->front->next;
	if (queue->front == NULL) {
		queue->rear = NULL;
	}
	free(temp);
	return dequeue;
}

void print_queue(Queue* queue) {
	Node* now_node = queue->front;
	while (now_node != NULL) {
		printf("%d -> ", now_node->data);
		now_node = now_node->next;
	}
	printf("NULL\n");
}

int main() {
	Queue my_queue;
	init_queue(&my_queue);

	enqueue(&my_queue, 11);
	enqueue(&my_queue, 21);
	enqueue(&my_queue, 31);
	print_queue(&my_queue);

	printf("dequeue data : %d\n", dequeue(&my_queue));
	print_queue(&my_queue);
	return 0;
}