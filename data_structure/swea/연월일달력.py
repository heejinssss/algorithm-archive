T = int(input())
dic = { 1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31 }

for test_case in range(1, T + 1):
    n = str(input())
    if 1 <= int(n[4:6]) <= 12 and dic[int(n[4:6])] >= int(n[6:8]):
        print(f"#{test_case} {n[:4]}/{n[4:6]}/{n[6:8]}")
    else:
        print(f"#{test_case} -1")