N = int(input().strip())
sg_crds = set(map(int, input().strip().split()))

M = int(input().strip())
ck_crds = list(map(int, input().strip().split()))

result = []
for card in ck_crds:
    if card in sg_crds:
        result.append(1)
    else:
        result.append(0)

print(" ".join(map(str, result)))