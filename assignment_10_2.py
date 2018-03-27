name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

words = list()
word_dict = dict()

for line in handle:
    if line.startswith("From") and len(line.split()) > 2:
        pos = line.find(":")
        word = line[pos - 2:pos]
        if word not in words:
            words.append(word)
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

words.sort()

for word in words:
    print(word, word_dict[word])
