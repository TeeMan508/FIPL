from random import randint


def StringShuffle(string):
    buf = string.lower().split()
    buf2 = []
    for i in range(0, len(buf)):
        k = randint(0, len(buf) - 1)
        buf2.append(buf[k])
        buf.pop(k)
    return ' '.join(buf2)

print(StringShuffle(input('Input your sentence: ')))
