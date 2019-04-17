ip = [['x', 'o', 'o'], ['o', 'B', 'o'], ['B', 'B', 'x']]
op = []
for word in ip:
    op.append(''.join(word))
for i in range(len(ip)):
    print(op[i])
