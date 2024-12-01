# example_input = '01\\example_input'
example_input = '01\\input'

l1 = []
l2 = []

with open(example_input, 'r', encoding='UTF-8') as file:
    for line in file.readlines():
        a,b = list(map(int, line.strip().split('  ')))
        l1.append(a)
        l2.append(b)
# sort lists
l1.sort()
l2.sort()
diff = []
for one, two in zip(l1, l2):
    diff.append(abs(one-two))

print(sum(diff))