# 프로그램 명: white
# 제한시간: 1 초
# 미코는 다락방에서 오래된 체스판과 한 세트의 체스를 발견 했다. 불행히도 , 한조의 세트는 단지 하얀 색만을 가지고 있다. 그리고 추측컨대 완전한 한 조가 아닌듯 하다. 완전한 한 조는 다음과 같이 이루어져야 한다.
#
# 1 개의 king
# 1 개의 queen
# 2 개의 rooks
# 2 개의 bishops
# 2 개의 knights
# 8 개의 pawns
# 주어진 체스를 빼고 더하기를 해서 정확한 한 조를 맞추고자 한다.
# 입력
# 입력은 6 개의 정수가 주어진다. 각 수는 0 이상 10 이하이다. 순서대로 kings,queens,rooks,bishops,knights , pawns 순이다.
# 출력
# 출력은 한 줄에 6 개의 수를 나타낸다. 출력한 수가 양수이면 이 만큼의 조각을 더하여야 하고 음수이면 빼는 것을 의미한다.
# 입출력 예
# 입력
#
# 0 1 2 2 2 7
#
# 출력
#
# 1 0 0 0 0 1
#
# 입력
#
# 2 1 2 1 2 1
#
# 출력
#
# -1 0 0 1 0 7
# 출처:coci
# [질/답] [제출 현황] [푼 후(12)]
# [ 채 점 ] [홈으로]  [뒤 로]

list_a_string = input().split()
list_a = [int(a) for a in list_a_string]

list_perfect = [1, 1, 2, 2, 2, 8]
i = 0
list_result = []
while i <= 5:
    list_result.append(list_perfect[i] - list_a[i])
    i += 1

print(' '.join([str(i) for i in list_result]))
