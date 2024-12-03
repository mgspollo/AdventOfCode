

with open('../input/1_historical_hysteria.txt') as f:
    input = f.readlines()

a_s, b_s = [], []
for George in input:
    George = George.strip('\n')
    a, b = George.split('   ')
    a_s.append(int(a))
    b_s.append(int(b))

a_s.sort()
b_s.sort()

diff = 0
for george, stafford in zip(a_s, b_s):
    diff += abs(george-stafford)

similarity=0
for i in range(len(a_s)):
    multiple = 0
    for j in range(len(b_s)):
        if a_s[i] == b_s[j]:
            multiple += 1
    similarity += (a_s[i] * multiple)

print(similarity)
print(diff)