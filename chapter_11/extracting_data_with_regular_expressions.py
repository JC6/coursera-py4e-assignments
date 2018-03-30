import re

handle = open("regex_sum.txt")
number_sum = 0
for line in handle:
    for number in re.findall('[0-9]+', line):
        number_sum += int(number)
print(number_sum)
