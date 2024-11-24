#include <stdio.h> 
#include <stdlib.h>

struct Node {
    int vertex;
    struct Node* next;
};

struct Graph {
    int numVertices; //총 노드의 갯수
    struct Node** adjLists;
};

// 노드 생성 함수
struct Node* createNode(int v) {
    struct Node* newNode = malloc(sizeof(struct Node));
    newNode->vertex = v;
    newNode->next = NULL;
    return newNode;
}

// 그래프 생성 함수
struct Graph* createGraph(int vertices) {
    struct Graph* graph = malloc(sizeof(struct Graph));
    graph->numVertices = vertices;

    graph->adjLists = malloc(vertices * sizeof(struct Node*));

    for (int i = 0; i < vertices; i++) {
        graph->adjLists[i] = NULL;
    }
    return graph;
}

// 간선 추가 함수
void addEdge(struct Graph* graph, int start, int end) {
    // start에서 end로 가는 간선 추가
    struct Node* newNode = createNode(end);
    newNode->next = graph->adjLists[start];
    graph->adjLists[start] = newNode;

    // end에서 start로 가는 간선 추가 (무방향 그래프)
    newNode = createNode(start);
    newNode->next = graph->adjLists[end];
    graph->adjLists[end] = newNode;
}

// 그래프 출력 함수
void printGraph(struct Graph* graph) {
    for (int v = 0; v < graph->numVertices; v++) {
        struct Node* temp = graph->adjLists[v];
        printf("정점 %d: ", v);
        while (temp) {
            printf("%d ", temp->vertex);
            temp = temp->next;
        }
        printf("\n");
    }
}

int main() {
    struct Graph* graph = createGraph(5);

    addEdge(graph, 0, 1);
    addEdge(graph, 0, 4);
    addEdge(graph, 1, 2);
    addEdge(graph, 1, 3);
    addEdge(graph, 1, 4);
    addEdge(graph, 2, 3);
    addEdge(graph, 3, 4);

    printGraph(graph);

    return 0;
}