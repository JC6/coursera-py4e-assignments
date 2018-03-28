import re

handle = open("regex_sum.txt")
numbers = list()
number_sum = 0
for line in handle:
    numbers += re.findall('[0-9]+', line)
for number in numbers:
    number_sum += int(number)
print(number_sum)
