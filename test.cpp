#include <stdio.h>

int main(void) {
	int cnt = 12, num = 0, turn = 0;
	while (cnt >= 0) {
		printf("현재 스틱의 개수: %d\n", cnt);
		while (1) {
			printf("%d번 플레이어 몇개의 스틱을 가져가시겠습니까? ", turn % 2 + 1);
			scanf("%d", &num);
			if (num >= 0 && num <= 3) {
				cnt -= num;
				turn++;
				break;
			}
			else printf("0부터 3사이의 숫자를 입력하세요.\n");
		}
	}
	printf("%d번 플레이어가 승리했습니다!", turn%2+1);
	return 0;
} 
