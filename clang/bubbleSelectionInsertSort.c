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
	for (int i = 1; i < n; i++) {  //0���� ���ĵǾ��ٰ� ����, 1�� �ε��� ���� ������ ����
		int key = arr[i]; //���� ��Ҹ� key��� �̸����� ����, key�� ���ĵ��� ���� �κ��� ���� �տ� �ش���
		int j = i - 1; //���� ��ġ

		while (i >= 0 && arr[j] > key) { //�迭�� ������ ���۱��� ���鼭 &&key ���� ū ���� ã����
			arr[j + 1] = arr[j]; //j+1 ��ġ�� j���� ����(��ĭ �ڷ� �δ�)
			j = j - 1; //j�� ���� ��ĭ ����
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

	printf("���� ���� ��� : ");
	for (int i = 0; i < n; i++) {
		printf("%d ", arr0[i]);
	}
	printf("\n���� ���� ��� : ");
	for (int i = 0; i < n; i++) {
		printf("%d ", arr1[i]);
	}
	printf("\n���� ���� ��� : ");
	for (int i = 0; i < n; i++) {
		printf("%d ", arr2[i]);
	}

	return 0;
}