#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX_VERTICES 100   // 최대 정점 개수
#define INF 1000000        // 간선이 없는 경우의 가중치(무한대)

// 우선순위 큐에 사용할 노드 구조체 정의
typedef struct {
    int vertex;      // 정점 번호
    int distance;    // 해당 정점까지의 최단 거리
} HeapNode;

// 우선순위 큐 구조체 정의
typedef struct {
    HeapNode heap[MAX_VERTICES];
    int size;
} PriorityQueue;

// 그래프 구조체 정의
typedef struct {
    int n;                         // 정점 개수
    int weight[MAX_VERTICES][MAX_VERTICES]; // 인접 행렬
} GraphType;

// 우선순위 큐 관련 함수들
void init(PriorityQueue* pq) {
    pq->size = 0; // 큐의 크기를 0으로 초기화
}

int is_empty(PriorityQueue* pq) {
    return pq->size == 0; // 큐가 비었는지 확인
}

void push(PriorityQueue* pq, int vertex, int distance) {
    int i = ++(pq->size); // 새 노드 삽입
    while (i != 1 && distance < pq->heap[i / 2].distance) { 
        // 부모 노드와 비교하여 자리 이동
        pq->heap[i] = pq->heap[i / 2];
        i /= 2;
    }
    pq->heap[i].vertex = vertex;   // 삽입할 정점 번호
    pq->heap[i].distance = distance; // 삽입할 거리
}

HeapNode pop(PriorityQueue* pq) {
    int parent, child;
    HeapNode item, temp;

    item = pq->heap[1]; // 최상단 노드(최소 거리)를 반환할 준비
    temp = pq->heap[(pq->size)--]; // 마지막 노드를 가져옴

    parent = 1; // 부모 노드부터 시작
    child = 2;  // 왼쪽 자식 노드

    while (child <= pq->size) {
        if (child < pq->size && pq->heap[child].distance > pq->heap[child + 1].distance) 
            child++; // 오른쪽 자식이 더 작으면 오른쪽 자식 선택
        if (temp.distance <= pq->heap[child].distance) 
            break; // 부모가 더 작으면 종료
        pq->heap[parent] = pq->heap[child];
        parent = child;
        child *= 2;
    }
    pq->heap[parent] = temp; // 적절한 위치에 삽입
    return item;
}

// 다익스트라 알고리즘
void dijkstra(GraphType* g, int start) {
    int distance[MAX_VERTICES]; // 최단 거리 저장 배열
    int found[MAX_VERTICES];    // 방문 여부 저장 배열
    PriorityQueue pq;           // 우선순위 큐

    // 초기화
    for (int i = 0; i < g->n; i++) {
        distance[i] = INF;  // 모든 정점까지의 거리를 무한대로 설정
        found[i] = 0;       // 모든 정점을 방문하지 않은 상태로 설정
    }
    distance[start] = 0;    // 시작 정점의 거리를 0으로 설정

    init(&pq);              // 우선순위 큐 초기화
    push(&pq, start, 0);    // 시작 정점을 큐에 삽입

    while (!is_empty(&pq)) {
        HeapNode node = pop(&pq);  // 최단 거리가 가장 작은 정점을 꺼냄
        int u = node.vertex;       // 현재 정점
        if (found[u]) continue;    // 이미 방문한 정점이면 무시
        found[u] = 1;              // 방문 처리

        for (int v = 0; v < g->n; v++) {
            if (g->weight[u][v] != INF && !found[v]) {
                int new_distance = distance[u] + g->weight[u][v];
                if (new_distance < distance[v]) {
                    distance[v] = new_distance; // 최단 거리 업데이트
                    push(&pq, v, new_distance); // 갱신된 거리로 큐에 삽입
                }
            }
        }
    }

    // 결과 출력
    printf("최단 거리:\n");
    for (int i = 0; i < g->n; i++) {
        if (distance[i] == INF) 
            printf("정점 %d: INF\n", i);
        else 
            printf("정점 %d: %d\n", i, distance[i]);
    }
}

// 메인 함수
int main(void) {
    GraphType g = { 7,
        {{ 0,  7,  INF, INF,   3,  10, INF },
         { 7,  0,    4,  10,   2,   6, INF },
         { INF,  4,    0,   2, INF, INF, INF },
         { INF, 10,    2,   0,  11,   9,   4 },
         { 3,  2,  INF,  11,   0, INF,   5 },
         { 10,  6,  INF,   9, INF,   0, INF },
         { INF, INF, INF,   4,   5, INF,   0 } }
    };

    dijkstra(&g, 0); // 0번 정점에서 시작
    return 0;
}
