import numpy as np

# example_input = '02\\example_input'
example_input = '02\\input'

l1 = []
l2 = []

with open(example_input, 'r', encoding='UTF-8') as file:
    count = 0
    for line in file.readlines():
        levels = list(map(int, line.strip().split(' ')))
        if (int(sum(np.sign(np.diff(levels)))) == len(levels)-1 or int(sum(np.sign(np.diff(levels)))) == -len(levels)+1) and max(np.diff(levels)) < 4 and min(np.diff(levels)) > -4:
            # print(f'levels{levels} safe')
            count += 1
    print(count)