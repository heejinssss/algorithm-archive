# 다시보기
def solution(number, k):
    stack = []  # 스택 초기화
    for num in number:  # 숫자를 하나씩 확인
        # 스택이 비어있지 않고, 스택의 마지막 요소가 현재 숫자보다 작고, 아직 제거할 숫자가 남아있는 경우
        while stack and stack[-1] < num and k > 0:
            k -= 1  # 제거할 숫자를 하나 줄임
            stack.pop()  # 스택의 마지막 요소 제거
        stack.append(num)  # 현재 숫자를 스택에 추가
    if k != 0:  # 아직 제거할 숫자가 남아있는 경우
        stack = stack[:-k]  # 스택의 마지막 k개 요소 제거
    return ''.join(stack)  # 스택의 요소를 문자열로 변환하여 반환