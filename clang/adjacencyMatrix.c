/*����ġ�� ������ ��� ���� �׷���

���� ��� : ��� ���� ���
���� ����Ʈ
*/

#include <stdio.h>
#define MAX 5

void initGraph(int graph[MAX][MAX]) {
	for (int i = 0; i < MAX; i++) {
		for (int j = 0; j < MAX; j++) {
			graph[i][j] = 0;
		}
	}
}

void addEdge(int graph[MAX][MAX], int start, int end) {
	graph[start][end] = 1;
	graph[end][start] = 1;  //������ �׷����� ���
}

void printGraph(int graph[MAX][MAX]) {
	for (int i = 0; i < MAX; i++) {
		for (int j = 0; j < MAX; j++) {
			printf("%d ", graph[i][j]);
		}
		printf("\n");
	}
}

int main(void) {
	int graph[MAX][MAX];
	initGraph(graph); //�׷��� �ʱ�ȭ

	addEdge(graph, 0, 1);
	addEdge(graph, 0, 4);
	addEdge(graph, 1, 2);
	addEdge(graph, 1, 3);
	addEdge(graph, 1, 4);
	addEdge(graph, 2, 3);
	addEdge(graph, 3, 4);

	printf("graph matrix\n");
	printGraph(graph);

	return 0;
}