#include <stdio.h>

void swap(int *a, int *b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

void bubble_sort(int arr[], int n) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n - 1; j++) {
			if (arr[j] > arr[j + 1]) {
				swap(&arr[j], &arr[j + 1]);
				/*int temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;*/
			}
		}
	}
}

int main() {
	int arr[] = { 20, 50, 40, 10, 30, 60 };
	int n = sizeof(arr) / sizeof(arr[0]);


	printf("���� �� : ");
	for (int i = 0; i < n; i++) {
		printf("%d ", arr[i]);
	}

	bubble_sort(arr, n);
	printf("\n���� �� : ");
	
	for (int i = 0; i < n; i++) {
		printf("%d ", arr[i]);
	}

	return 0;
}