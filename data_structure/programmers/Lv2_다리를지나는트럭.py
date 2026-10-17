# 다시 풀기

"""
트럭은 1초에 다리 길이 1씩 전진한다.
트럭은 (올라갈 수 있으면) 1초에 한 대씩 다리에 올라갈 수 있다
"""

def solution(bridge_length, weight, truck_weights):
    second = 0
    cur_truck = 0
    on_bridge = []

    while truck_weights:
        print("on_bridge", on_bridge, "cur_truck", cur_truck, "second", second)
        if len(on_bridge) <= bridge_length and sum(on_bridge) + truck_weights[0] <= weight:
            on_bridge.append(truck_weights.pop(0))
        else:
            on_bridge.pop(0)
        second += 1

    print("on_bridge", on_bridge, "cur_truck", cur_truck, "second", second)

    if on_bridge:
        num = (sum(on_bridge) // bridge_length) if (sum(on_bridge) // bridge_length) else 1
        return second + (bridge_length * num)
    else:
        return second