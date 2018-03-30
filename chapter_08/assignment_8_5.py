file_name = input("Enter file name: ")
if len(file_name) < 1:
    file_name = "mbox-short.txt"
fh = open(file_name)
count = 0
for line in fh:
    if line.startswith("From"):
        words = line.split()
        if len(words) > 2:
            print(words[1])
            count += 1
print("There were", count, "lines in the file with From as the first word")
