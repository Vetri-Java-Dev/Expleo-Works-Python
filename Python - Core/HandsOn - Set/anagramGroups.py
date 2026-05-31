words = eval(input())
groups = {}
for w in words:
    key = tuple(sorted(w.replace(" ", "")))
    if key not in groups:
        groups[key] = set()
    groups[key].add(w)
print(list(groups.values()))
