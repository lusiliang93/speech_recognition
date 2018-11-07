import re


g = open('cleaned_chn.lm', 'w')
with open('chn.lm') as f:
	for line in f:
		splited_line = line.split()
		if '<sw>' not in splited_line:
			g.write(line)
g = open('cleaned_eng.lm', 'w')
with open('eng.lm') as f:
	for line in f:
		splited_line = line.split()
		if '<sw>' not in splited_line:
			g.write(line)
		# chinese_tokens = re.findall(u'[\u4e00-\u9fff]+', line)
		# splited_line = line.split()
		# n = len(splited_line)
		# if n > 0:
		# 	flag = splited_line[0] in chinese_tokens
		# 	if not flag:
		# 		g.write('<sw>  ')
		# 	for token in splited_line:
		# 		if token in chinese_tokens:
		# 			if flag:
		# 				g.write(token)
		# 				g.write('  ')
		# 			else:
		# 				flag = True
		# 				g.write(token)
		# 				g.write('  ')
		# 		else:
		# 			if flag:
		# 				g.write('<sw>')
		# 				g.write('  ')
		# 				flag = False
		# 	g.write('\n')
