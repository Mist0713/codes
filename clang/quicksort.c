#include <stdio.h>

//배열 분할
int partition(int arr[], int start, int end) {
	int pivot = arr[start];
	int i = start + 1;
	int j = end;

	while (1) {
		while (i <= end && arr[i] <= pivot) { //작은 것들 중에서 큰것 찾기
			i++;
		}
		while (i >= start && arr[j] > pivot) {//큰 것들 중에서 작은것 찾기
			j--;
		}
		if (i < j) { //서로 교환
			int temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
		}
		else {
			break;
		}
	}
	//피벗 데이터를 올바른 위치(j가 i보다 더 작은 데이터 이므로)에 놓음
	int temp = arr[start];
	arr[start] = arr[j];
	arr[j] = temp;

	return j; //피벗의 최종 위치
}

void quick_sort(int arr[], int start, int end) {
	if (start < end) {
		int pivot = partition(arr, start, end); //[작은거][피벗][큰거]
		quick_sort(arr, start, pivot - 1);
		quick_sort(arr, pivot + 1, end);
	}
}

void print_array(int arr[], int size) {
	for (int i=0; i < size; i++) {
		printf("%d ", arr[i]);
	}
	printf("\n");
}

int main() {
	int arr[] = { 10,8,1,5,7 };
	int arr_size = sizeof(arr) / sizeof(arr[0]);

	print_array(arr, arr_size);
	quick_sort(arr, 0, arr_size - 1);
	print_array(arr, arr_size);

	return 0;
}