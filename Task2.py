from random import randint


def rand(arg, word):
    buf = []
    for i in range(0, len(arg)):
        if len(buf) == len(arg):
            break
        buf.append(arg[i])
        for k in range(i+1, len(arg)):
            if len(buf) == len(arg):
                break
            if arg[i][0] == arg[k][0]:
                buf.append(arg[k])
    for k in range(0, len(buf)):
        if word == buf[k][0]:
            return buf[randint(k, k + buf.count(buf[k]))][2]


def SynonymsFinding(filename):
    print('SYNONYMYZATOR 9000!!!\n')
    data = input('Input your sentence: ').lower()
    synonyms_list = []
    f = open(filename, 'r')
    for line in f:
        synonyms_list.append(line.lower().split())
    f.close()
    datalist = data.split()
    for i in range(0, len(datalist)):
        for k in range(0, len(synonyms_list)):
            if datalist[i] == synonyms_list[k][0]:
                datalist[i] = rand(synonyms_list, synonyms_list[k][0])
    return ' '.join(datalist)

print(SynonymsFinding('Synonyms.txt'))







