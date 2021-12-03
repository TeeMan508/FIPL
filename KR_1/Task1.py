filename = input('Input file name')
buf = []
f = open(filename, 'r')
for line in f:
    buf.append(line.lower().split())
f.close()
res = []
for line in buf:
    for word in line:
        if len(word) > 5:
            res.append(word)
print(res)