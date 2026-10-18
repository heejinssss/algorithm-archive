"""
트럭은 1초에 다리 길이 1씩 전진한다.
트럭은 (올라갈 수 있으면) 1초에 한 대씩 다리에 올라갈 수 있다
"""

def solution(bridge_length, weight, truck_weights):
    second = 0
    bridge = [0] * bridge_length

    while bridge:
        second += 1
        bridge.pop(0)

        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return second
