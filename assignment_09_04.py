name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

words = list()
word_dict = dict()
maximum = None
maximum_count = 0

for line in handle:
    if line.startswith("From"):
        split = line.split()
        if len(split) < 3:
            continue
        word = split[1]
        words.append(word)
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

for word in words:
    if word_dict[word] > maximum_count:
        maximum = word
        maximum_count = word_dict[word]

print(maximum, maximum_count)
