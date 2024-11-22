#include <stdio.h>

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

//? 최대 힙을 유지하는 함수
void heapify(int arr[], int n, int i){
    int root = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    
    //* 왼쪽 자식이 있는데 부모보다 큰 경우
    if (left < n && arr[left]>arr[root]){
        root = left;
    }
    //* 오른쪽 자식이 있는데, 부모보다 큰 경우
    if (right < n && arr[right] > arr[root]){
        root = right;
    }
    //* 가장 큰 값이 root가 아니면 교환한 다음, 힙을 정렬(최대힙으로)
    if(root != i){
        swap(&arr[i], &arr[root]);
        heapify(arr, n, root);
    }
}

void heapSort(int arr[], int n){
    //* 1. 배열을 최대 힙으로
    for(int i = n/2-1; i>=0; i--){
        heapify(arr, n, i);
    }
    //* 2. 정렬
    for(int i=n-1; i>=0; i-- ){
        //! 가장 큰 값을 뒤로 보냄
        swap(&arr[0], &arr[i]);
        //! 나머지에서 다시 힙정렬을 수행
        heapify(arr, i, 0);
    }
}

int main(void){
    int arr[] = {12,13,1,3,7,5};
    int n = sizeof(arr)/sizeof(arr[0]);

    //정렬 전 배열
    for(int i=0; i<n;i++){
        printf("%d ", arr[i]);
    }   
    printf("\n");

    //힙 정렬
    heapSort(arr, n);

    //정렬 후 배열
    for(int i=0; i<n;i++){
        printf("%d ", arr[i]);
    }   

    return 0;
}