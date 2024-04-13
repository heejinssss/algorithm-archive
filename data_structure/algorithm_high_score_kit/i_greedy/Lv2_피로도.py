def solution(k, dungeons):

    answer = []
    
    def dfs(ds, cnt, k):
        if not ds: # 만약 더 이상 검증할 던전이 없다면
            answer.append(cnt) # 현재까지의 count 값 저장
            return # dfs 종료
        
        for min, damage in ds:
            if k < min:
                answer.append(cnt)
                continue
            else:
                next_ds = ds[:] # 현재 던전부터 마지막 던전까지 저장
                next_ds.remove([min, damage]) # 현재 던전을 후보에서 제거
                dfs(next_ds, cnt+1, k-damage) # 이후 던전부터 마지막 던전까지 다시 탐색

    dfs(dungeons, 0, k)
    return max(answer)