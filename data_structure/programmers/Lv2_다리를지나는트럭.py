def solution(bridge_length, weight, truck_weights):
    answer = 1
    x = truck_weights.pop(0)
    on_bridge = [x]

    for w in truck_weights:
        print(on_bridge, w)
        if not(len(on_bridge) <= bridge_length and sum(on_bridge) + w <= weight):
            on_bridge.pop(0)
            answer += bridge_length
        on_bridge.append(w)

    return answer + len(on_bridge)
