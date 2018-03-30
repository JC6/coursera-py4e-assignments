file_name = input("Enter file name: ")
fh = open(file_name)
lst = list()
for line in fh:
    words = line.split()
    count = 0
    while count < len(words):
        if words[count] not in lst:
            lst.append(words[count])
        count += 1
lst.sort()
print(lst)
