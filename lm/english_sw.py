import re
import numpy as np


g = open('english_train.txt', 'w')
switch = []
with open('train_plain.txt') as f:
	for line in f:
		english_tokens = re.findall(u'[a-zA-Z0-9\'.]+', line)
		splited_line = line.split()
		n = len(splited_line)
		sw = ['','']
		if n > 0: 
			flag = splited_line[0] in english_tokens
			if not flag:
				g.write('<sw>  ')
			else:
				sw[0] = splited_line[0]

			for token in splited_line:
				if token in english_tokens:
					if flag:
						g.write(token)
						g.write('  ')
						sw[0] = token
					else:
						flag = True
						g.write(token)
						g.write('  ')
						sw[0] = token
				else:
					if flag:
						g.write('<sw>')
						g.write('  ')
						sw[1]=token
						switch.append(sw)
						flag = False
			g.write('\n')

g = open('english_heldout.txt', 'w')
switch1 = []
with open('heldout_plain.txt') as f:
	for line in f:
		english_tokens = re.findall(u'[a-zA-Z0-9]+', line)
		splited_line = line.split()
		n = len(splited_line)
		sw1 = ['','']
		if n > 0:
			flag = splited_line[0] in english_tokens
			if not flag:
				g.write('<sw>  ')
			else:
				sw1[0] = token

			for token in splited_line:
				if token in english_tokens:
					if flag:
						g.write(token)
						g.write('  ')
						sw1[0] = token
					else:
						flag = True
						g.write(token)
						g.write('  ')
						sw1[0] = token
				else:
					if flag:
						g.write('<sw>')
						g.write('  ')
						sw1[1] = token
						switch1.append(sw1)
						flag = False
			g.write('\n')

g = open('switch.txt','w')
for sw in switch:
	g.write(' '.join(sw) + '\n')

g = open('switch1.txt','w')
for sw1 in switch1:
	g.write(' '.join(sw1) +'\n')