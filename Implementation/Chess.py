# 나이트의 위치 입력 받기
data = input()
row = int(data([1]))
# 문자열 인덱스를 숫자로 표현하기 위해 다음의 식 사용
column = int(ord(input[0])) - int(ord('a')) + 1

# 8가지 이동 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)