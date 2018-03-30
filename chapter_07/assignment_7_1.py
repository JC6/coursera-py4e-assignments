file_name = input("Enter file name: ")
fh = open(file_name)
for line in fh:
    print(line.strip().upper())
