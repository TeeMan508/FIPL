input_filename = input('Input initital file name: ')
output_filename = input('Input final file name: ') + '.txt'
buf = []
vowels = ['a','e','i','o','u','y']
f = open(input_filename, 'r')
for line in f:
    buf.append(line.lower().split())
f.close()
res = []
for line in buf:
    for word in line:
        if word[0] in vowels:
            res.append(word)
f = open(output_filename, 'w')
for word in res:
    f.write(word+'\n')
f.close()




