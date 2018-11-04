import re


g = open('chinese_train.txt', 'w')
with open('train_plain.txt') as f:
	for line in f:
		chinese_tokens = re.findall(u'[\u4e00-\u9fff]+', line)
		splited_line = line.split()
		n = len(splited_line)
		if n > 0:
			flag = splited_line[0] in chinese_tokens
			if not flag:
				g.write('<sw>  ')
			for token in splited_line:
				if token in chinese_tokens:
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

g = open('chinese_heldout.txt', 'w')
with open('heldout_plain.txt') as f:
	for line in f:
		chinese_tokens = re.findall(u'[\u4e00-\u9fff]+', line)
		splited_line = line.split()
		n = len(splited_line)
		if n > 0:
			flag = splited_line[0] in chinese_tokens
			if not flag:
				g.write('<sw>  ')
			for token in splited_line:
				if token in chinese_tokens:
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