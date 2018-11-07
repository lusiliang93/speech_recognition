# calculate P(chn|eng) 
mix = open('chn_eng.txt','w')
prob = []

chn_sw = []
sw_eng = []
switch = []
with open('chn_sw.txt','r') as f1:
    for l1 in f1:
        chn_sw.append(l1)
with open('sw_eng.txt','r') as f2:
    for l2 in f2:
        sw_eng.append(l2)
with open('switch_chn.txt','r') as file:
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
    chn = tokens[0]
    eng = tokens[1]
    new[1] = chn
    new[2] = eng
    for i in range(len(chn_sw)):
        tokens1 = chn_sw[i].split()
        if chn in tokens1:
            p1 = float(tokens1[0])
    for j in range(len(sw_eng)):
        tokens2 = sw_eng[j].split()
        if eng in tokens2:
            p2 = float(tokens2[0])
            
    p = p1+p2
    #print(p)
    prob.append(p)
    new[0] = str(p)
    mix.write(' '.join(new)+'\n')
    k += 1
    print(k)

mix.close()