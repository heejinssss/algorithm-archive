def solution(chicken):
    count = 0 # 서비스 치킨 수
    return service(count, chicken) # 서비스 치킨 수, 시켜 먹은 치킨 수

def service(count, chicken):
    if chicken//10 == 0:
        return count
    return service(count + chicken//10, chicken//10 + chicken%10)
