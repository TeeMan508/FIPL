def mestoimenie(word):
    if :
        return True
    else:
        return False


def glagol(word):
    if :
        return True
    else:
        return False


def prilagatelnoe(word):
    if :
        return True
    else:
        return False


def counter(filename):
    f = open(filename, 'r')
    Mcount = 0
    Pcount = 0
    Gcount = 0
    text = []
    for line in f:
        text.append(line.lower().split())
    f.close()
    for line in text:
        for word in line:
            if mestoimenie(word):
                Mcount += 1
            if glagol(word):
                Gcount += 1
            if prilagatelnoe(word):
                Pcount += 1
    return {'Number of verbs: ': Gcount, 'Number of adjectives: ': Pcount, 'Number of pronouns': Mcount}

print(counter('ChastiRechi.txt'))


