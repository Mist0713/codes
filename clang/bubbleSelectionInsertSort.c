#include <stdio.h>

void bubbleSort(int arr[], int n) {
	for (int i = 0; i < n - 1; i++) {
		for (int j = 0; j < n - i - 1; j++) {
			if (arr[j] > arr[j + 1]) {
				//swap
				int temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}
}

void selectionSort(int arr[], int n) {
	for (int i = 0; i < n - 1; i++) {
		int min_idx = i;
		for (int j = i + 1; j < n; j++) {
			if (arr[j] < arr[min_idx]) {
				min_idx = j;
			}
		}
		//swap
		int temp = arr[min_idx];
		arr[min_idx] = arr[i];
		arr[i] = temp;

	}
}

void insertionSort(int arr[], int n) {
	for (int i = 1; i < n; i++) {  //0번은 정렬되었다고 가정, 1번 인덱스 부터 정렬할 예정
		int key = arr[i]; //비교할 요소를 key라는 이름으로 저장, key는 정렬되지 않은 부분의 가장 앞에 해당함
		int j = i - 1; //비교할 위치

		while (i >= 0 && arr[j] > key) { //배열의 끝부터 시작까지 돌면서 &&key 보다 큰 값을 찾으면
			arr[j + 1] = arr[j]; //j+1 위치에 j값을 넣음(한칸 뒤로 민다)
			j = j - 1; //j의 값을 한칸 줄임
		}
		arr[j + 1] = key;
	}
}

int main(void) {
	int arr0[] = { 64, 34, 25, 12, 22, 11, 90 };
	int arr1[] = { 64, 34, 25, 12, 22, 11, 90 };
	int arr2[] = { 64, 34, 25, 12, 22, 11, 90 };
	int n = sizeof(arr0) / sizeof(arr0[0]);

	bubbleSort(arr0, n);
	selectionSort(arr1, n);
	insertionSort(arr2, n);

	printf("버블 정렬 결과 : ");
	for (int i = 0; i < n; i++) {
		printf("%d ", arr0[i]);
	}
	printf("\n선택 정렬 결과 : ");
	for (int i = 0; i < n; i++) {
		printf("%d ", arr1[i]);
	}
	printf("\n삽입 정렬 결과 : ");
	for (int i = 0; i < n; i++) {
		printf("%d ", arr2[i]);
	}

	return 0;
}