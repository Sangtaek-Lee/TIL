import sys
sys.stdin = open('input_5.txt')

T = 10
# height_list = [0]*1000
# length = int(input())
# print(length)
# height_list_temp = list(map(int, input().split()))
# print(height_list_temp)
# height_list[0:length] = height_list_temp
# print(height_list)
# print(len(height_list))
# print(list(range(1,5)))

for tc in range(1, T + 1):                          # Test Case 반복
    length = int(input())                           # 전체 가로길이를 받아온다. 앞뒤로 0값으로 여유를 주려 했지만 앞뒤 두 값이 0으로 되어 있어 그냥 받아 왔다.
    height_list = list(map(int, input().split()))   # 각 건물의 층을 list로 받아 왔다.
    cnt = 0                                         # 조망이 확보된 칸을 카운트 하기 위해 선언
    for i in range(2, length-2):                    # n-2, n-1, n+1, n+2 중 max 값을 대비 n 값이 얼마나 더 큰지 ( 잡담이지만 다 풀고 나서 뭔가 코드가 짧은거 같아 다른 사람은 어떻게 풀었나 구글에 쳐봤는데 첫번째 글이 나랑 똑같이 풀었다 사람 생각 하는게 다 비슷하구나 놀라웠다.) 
        if height_list[i] == 0:
            continue
        temp_list = [height_list[i-2], height_list[i-1], height_list[i+1], height_list[i+2]] # n-2, n-1, n+1, n+2 값 중 가장 큰 값을 가져오기 위해 일시적인 list로 만들었다
        temp_list_max = 0                           # max값을 선언 and 초기화 시켜준다.
        for j in range(len(temp_list)):             # n-2, n-1, n+1, n+2 중 max 값을 구하기 위한 for
            if temp_list_max < temp_list[j]:        # 처음 선언한 max 값을 기준으로 for 문을 돌며 temp_list 중에서 max값을 찾는다.
                temp_list_max = temp_list[j]        # 찾으면 max 값 바꿔준다.
        if height_list[i] > temp_list_max:          # 이 때 n-2, n-1, n+1, n+2 의 max 값이 n 값 보다 작다면 조망권이 1개 이상이므로 카운트한다.
            cnt += (height_list[i] - temp_list_max) # n값에서 max 값을 빼면 조망권이 몇칸인지 알 수 있다. cnt에 계속 더한다.
    print(f'#{tc}', cnt)                            # 결과값 출력

##( 잡담이지만 다 풀고 나서 뭔가 코드가 짧은거 같아 다른 사람은 어떻게 풀었나 구글에 쳐봤는데 첫번째 글이 나랑 똑같이 풀었다 사람 생각 하는게 다 비슷하구나 놀라웠다.)