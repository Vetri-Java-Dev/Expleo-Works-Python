sets = eval(input())
if len(sets) == 0:
    print(0)
else:
    common = sets[0]
    for s in sets[1:]:
        common = common & s
    print(len(common))
