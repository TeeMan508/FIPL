def ReadLinesFromFile(filename):
    text = []
    f = open(filename, 'r')
    for line in f:
        text.append(line.split())
    f.close()
    return text

def Procesing(arg):
    result = []
    for line in arg:
        for word in line:
            if len(word)!=1 and word[0] == word[len(word)-1]:
                result.append(word)
    return result

def WriteResultToFile(arg):
    f = open('Result.txt', 'w')
    for word in arg:
        f.write(word+'\n')
    f.close()

MyLines = ReadLinesFromFile('Text.txt')
MyResult = Procesing(MyLines)
WriteResultToFile(MyResult)
