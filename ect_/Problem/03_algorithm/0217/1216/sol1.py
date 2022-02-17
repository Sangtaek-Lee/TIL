import sys

sys.stdin = open('input.txt')

T = 10

# 회문 검사 반환값은 회문 길이로 반환
def circular_word(N, length, word):
    i = 0
    while i + length <= N:
        # i ~ i+length 까지를 회문 검사
        mid = length // 2                               # 중간을 기준으로 왼쪽과 오른쪽 역배열을 비교
        if length % 2 == 0:                             # 짝수
            right_word = word[i:mid+i]
            left_word = word[i+length-1:mid+i-1:-1]
        else:                                           # 홀수
            right_word = word[i:mid+i]
            left_word = word[i+length-1:mid+i:-1]
        if right_word == left_word:
            return length
        i += 1
    return 0

# 100개에 알파벳으로 이루어진 100개의 가로 문자열과 세로 문자열을 한 리스트에 담아
# 그것을 length를 100 가변하면서 최댓값을 찾는다

for tc in range(1, T + 1):
    case_num = int(input())
    N = 100
    words_list = [input() for _ in range(N)]
    max_length = 0
    for i in range(N):
        temp_str = ''                               # 일시적인 빈 문자열을 만들어
        for j in range(N):
            temp_str = temp_str + words_list[j][i]  # 0,0 ~ 9,0 알파벳 추가
        words_list = words_list + [temp_str]        # 문자열 리스트에 추가

    for len in range(99 ,0 ,-1):                        # 위에서 부터 회문을 구하고, 구하면 멈추기
        for i in range(N*2):
            if max_length < circular_word(N, len, words_list[i]):
                max_length = circular_word(N, len, words_list[i])

    print(f'#{tc}', max_length)
