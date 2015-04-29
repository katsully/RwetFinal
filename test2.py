# -*- coding: utf-8 -*-

import markov

lines = []
for line in open("test_text.txt"):
	line = line.strip()
	lines.append(line)

print '\n'.join(markov.word_level_generate(lines,1,count=15))

