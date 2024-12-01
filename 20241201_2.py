# example_input = '01\\example_input'
example_input = '01\\input'

d1 = {}
d2 = {}
l1 = []
l2 = []

with open(example_input, 'r', encoding='UTF-8') as file:
    for line in file.readlines():
        a,b = list(map(int, line.strip().split('  ')))
        l1.append(a)
        l2.append(b)
        if not a in d1:
            d1[a] = 1
        else:
            d1[a] += 1
        if not b in d2:
            d2[b] = 1
        else:
            d2[b] += 1

output = 0
for item in l1:
    if item in d2:
        output += item*d2[item]
print(output)
