import re


g = open('english_train.txt', 'w')
with open('train_plain.txt') as f:
	for line in f:
		english_tokens = re.findall(u'[a-zA-Z0-9\'.]+', line)
		splited_line = line.split()
		n = len(splited_line)
		if n > 0:
			flag = splited_line[0] in english_tokens
			if not flag:
				g.write('<sw>  ')
			for token in splited_line:
				if token in english_tokens:
					if flag:
						g.write(token)
						g.write('  ')
					else:
						flag = True
						g.write(token)
						g.write('  ')
				else:
					if flag:
						g.write('<sw>')
						g.write('  ')
						flag = False
			g.write('\n')
g = open('english_heldout.txt', 'w')
with open('heldout_plain.txt') as f:
	for line in f:
		english_tokens = re.findall(u'[a-zA-Z0-9]+', line)
		splited_line = line.split()
		n = len(splited_line)
		if n > 0:
			flag = splited_line[0] in english_tokens
			if not flag:
				g.write('<sw>  ')
			for token in splited_line:
				if token in english_tokens:
					if flag:
						g.write(token)
						g.write('  ')
					else:
						flag = True
						g.write(token)
						g.write('  ')
				else:
					if flag:
						g.write('<sw>')
						g.write('  ')
						flag = False
			g.write('\n')