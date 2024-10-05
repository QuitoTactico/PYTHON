d, b = {} , {}
for _ in range(int(input())):
    for i in input().split(): d[i] = True
for _ in range(int(input())):
    for i in input().split(): b[i] = True
print(f"Reggaeton: {len(d.keys())} Rock: {len(b.keys())}")