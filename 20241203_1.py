import re

# example_input = '03\\example_input'
example_input = '03\\input'

with open(example_input, 'r', encoding='UTF-8') as file:
    sum = 0
    for line in file.readlines():
        x = re.findall("mul\(\d*,\d*\)", line)
        for hit in x:
            a, b = hit[4:-1].split(',')
            sum += int(a)*int(b)
    print(sum)