import re
import glob
import string

def convert(word):
    splited = re.findall(u'[\u4e00-\u9fff]|[a-zA-Z0-9]+|[^a-zA-Z0-9_]', word)
    # print(splited)
    ret = []
    status = 0
    s = ''
    for w in splited:
        w = u"{}".format(w)
        if w in string.punctuation:
            s += w
            # print('punc', w)
        elif w > u'\u4e00' and w < u'\u9fff':
            # print('chn', w)
            if status == 1:
                ret.append(s)
                s = w
                status = 2
            else:
                s += w
                status = 2
        else:
            # print('eng', w)
            if status == 2:
                ret.append(s)
                s = w
                status = 1
            else:
                s += w
                status = 1
    if s != '':
        ret.append(s)
    return ret

read_files = glob.glob("train/*.txt")
with open("train.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
read_files = glob.glob("heldout/*.txt")
with open("heldout.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

g = open('train_plain.txt', 'w')
with open('train.txt') as f:
    for line in f:
        splited_line = line.split()
        n = len(splited_line)
        for i in range(3, n):
            words = convert(splited_line[i])
            for word in words:
                g.write(word)
                g.write('  ')
        g.write('\n')
g = open('heldout_plain.txt', 'w')
with open('heldout.txt') as f:
    for line in f:
        splited_line = line.split()
        n = len(splited_line)
        for i in range(3, n):
            words = convert(splited_line[i])
            for word in words:
                g.write(word)
                g.write('  ')
        g.write('\n')
