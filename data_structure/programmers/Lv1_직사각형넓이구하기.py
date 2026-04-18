def solution(dots):
    
    # dots = sorted(dots, key=lambda x: (x[0], x[1]))

    return (max(dots)[0]-min(dots)[0])*(max(dots)[1]-min(dots)[1])
