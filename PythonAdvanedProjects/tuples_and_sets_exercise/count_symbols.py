text = input()
occ = {}
for char in text:
    if char not in occ:
        occ[char] = 1
    else:
        occ[char] += 1
for ch in sorted(occ):
    print(f"{ch}: {occ[ch]} time/s")