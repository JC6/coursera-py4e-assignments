import sqlite3

conn = sqlite3.connect('org.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')
file_name = input('Enter file name: ')
if len(file_name) < 1:
    file_name = 'org.txt'
fh = open(file_name)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    org = pieces[1]
    position = org.find('@')
    org = org[position + 1:len(org)]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    conn.commit()
cur.close()
