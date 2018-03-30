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
        if len(split) > 2:
            word = split[1]
            words.append(word)
            word_dict[word] = word_dict.get(word, 0) + 1
for word in words:
    if word_dict[word] > maximum_count:
        maximum = word
        maximum_count = word_dict[word]
print(maximum, maximum_count)
