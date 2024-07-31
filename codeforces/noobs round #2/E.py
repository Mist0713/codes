def count_valid_combinations(s: str) -> int:
    def dfs(idx, prev):
        # idx가 문자열의 끝에 도달하면 유효한 조합을 찾은 것이므로 1을 반환
        if idx == len(s):
            return 1
        
        count = 0
        if s[idx] == '-':
            # 빈칸에는 0부터 9까지의 숫자를 넣을 수 있다.
            for digit in range(10):
                if prev <= digit:
                    count += dfs(idx + 1, digit)
        else:
            # 빈칸이 아닌 경우 해당 숫자가 오름차순을 유지하는지 확인
            current_digit = int(s[idx])
            if prev <= current_digit:
                count += dfs(idx + 1, current_digit)
        
        return count

    return dfs(0, -1)  # 초기 인덱스와 이전 숫자를 설정하여 시작

# 테스트

T = int(input())

for i in range(T):
    n = int(input())
    print(count_valid_combinations(input()))
