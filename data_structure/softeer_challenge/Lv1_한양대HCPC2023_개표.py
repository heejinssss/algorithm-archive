T = int(input())
nlist = [int(input()) for _ in range(T)]
results = []
result = ''

for n in nlist:
    Jung = n//5
    Jick = n % 5
    result = {'++++ ' * Jung + '|' * Jick}
    results += result

for result in results:
    print(result)