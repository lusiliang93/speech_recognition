# calculate P(chn|eng) 
mix = open('eng_chn.txt','w')
prob = []

eng_sw = []
sw_chn = []
switch = []
with open('eng_sw.txt','r') as f1:
    for l1 in f1:
        eng_sw.append(l1)
with open('sw_chn.txt','r') as f2:
    for l2 in f2:
        sw_chn.append(l2)
with open('switch.txt','r') as file:
    for l in file:
        switch.append(l)
# print(len(switch))
# print(len(sw_chn))
# print(len(eng_sw))
f1.close()
f2.close()
file.close()

k = 0
for line in switch:
    new = [0,'','']
    tokens = line.split()
    eng = tokens[0]
    chn = tokens[1]
    new[1] = eng
    new[2] = chn
    for i in range(len(eng_sw)):
        tokens1 = eng_sw[i].split()
        if eng in tokens1:
            p1 = float(tokens1[0])
    for j in range(len(sw_chn)):
        tokens2 = sw_chn[j].split()
        if chn in tokens2:
            p2 = float(tokens2[0])
    p = p1+p2
    #print(p)
    prob.append(p)
    new[0] = str(p)
    mix.write(' '.join(new)+'\n')

mix.close()