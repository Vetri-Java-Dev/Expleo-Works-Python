inputSet = eval(input())
targetSum = int(input())

lst = list(inputSet)
n = len(lst)

res = []

for i in range(1 << n):
    subset = set()
    total = 0
    for j in range(n):
        if i & (1 << j):
            subset.add(lst[j])
            total += lst[j]
    if total == targetSum:
        res.append(subset)

print(res)
