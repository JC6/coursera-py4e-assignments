# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
s = 0
count = 0
for line in fh:
    line = line.strip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    s += float(line[line.find('0'):len(line)])
    count += 1
print("Average spam confidence:", s / count)
