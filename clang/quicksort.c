#include <stdio.h>

//�迭 ����
int partition(int arr[], int start, int end) {
	int pivot = arr[start];
	int i = start + 1;
	int j = end;

	while (1) {
		while (i <= end && arr[i] <= pivot) { //���� �͵� �߿��� ū�� ã��
			i++;
		}
		while (i >= start && arr[j] > pivot) {//ū �͵� �߿��� ������ ã��
			j--;
		}
		if (i < j) { //���� ��ȯ
			int temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
		}
		else {
			break;
		}
	}
	//�ǹ� �����͸� �ùٸ� ��ġ(j�� i���� �� ���� ������ �̹Ƿ�)�� ����
	int temp = arr[start];
	arr[start] = arr[j];
	arr[j] = temp;

	return j; //�ǹ��� ���� ��ġ
}

void quick_sort(int arr[], int start, int end) {
	if (start < end) {
		int pivot = partition(arr, start, end); //[������][�ǹ�][ū��]
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