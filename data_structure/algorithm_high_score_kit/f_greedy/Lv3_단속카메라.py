def solution(routes):
    routes.sort()
    
    # 첫번째 차량 루트는 무조건 pivot에 추가
    cam = 1
    pivot = routes[0][1]
    
    # 첫번째 차량 루트 제거
    routes.pop(0)
    
    for route in routes:
        # 현재 카메라 위치가, 다음 차량 루트를 커버하면
        if pivot >= route[0]:
            # 현재 카메라 위치와 다음 차량 루트의 끝 부분을 비교해서 더 작은 쪽 선택
            pivot = min(pivot, route[1])
        # 현재 카메라 위치가, 다음 차량 루트를 커버하지 못하면
        else:
            # pivot 추가
            pivot = route[1]
            cam += 1

    return cam