## Test with markov chain
import markov

#lines = []

giselle = open("giselle.txt")
lines = (giselle.readlines())
giselle.close()

guythoughts = open("guythoughts.txt")
lines.extend(guythoughts.readlines())
guythoughts.close()

hesintoyou = open("hesintoyou.txt")
lines.extend(hesintoyou.readlines())
hesintoyou.close()

notcute = open("notcute.txt")
lines.extend(notcute.readlines())
notcute.close()

righttype = open("righttype.txt")
lines.extend(righttype.readlines())
righttype.close()

print markov.word_level_generate(lines, 3, 50, 200);

