from random import randint
import nltk
from nltk.corpus import wordnet

story_ballets = []

# read in files
nutcracker = open("nutcracker.txt")
nut_lines = nutcracker.readlines()
story_ballets.append(nut_lines)
nutcracker.close()

swanlake = open("swanlake.txt")
swan_lines = swanlake.readlines()
story_ballets.append(swan_lines)
swanlake.close()

giselle = open("giselle.txt")
giselle_lines = giselle.readlines()
story_ballets.append(giselle_lines)
giselle.close()

sleepingbeauty = open("sleepingbeauty.txt")
sleeping_lines = sleepingbeauty.readlines()
story_ballets.append(sleeping_lines)
sleepingbeauty.close()

raymonda = open("Raymonda.txt")
raymonda_lines = raymonda.readlines()
story_ballets.append(raymonda_lines)
raymonda.close()

lecorsaire = open("lecorsaire.txt")
lecorsaire_lines = lecorsaire.readlines()
story_ballets.append(lecorsaire_lines)
lecorsaire.close()

guythoughts = open("guythoughts.txt")
guys_lines = guythoughts.readlines()
guythoughts.close()

hesintoyou = open("hesintoyou.txt")
guys_lines.append(hesintoyou.readlines())
hesintoyou.close()

notcute = open("notcute.txt")
guys_lines.append(notcute.readlines())
notcute.close()

righttype = open("righttype.txt")
guys_lines.append(righttype.readlines())
righttype.close()

#trigger_words = ['prince', 'run', 'wedding']
trigger_words = ['eye', 'kiss', 'look']

# for i,j in enumerate(wn.synsets('dog')):
#   print "Meaning",i, "NLTK ID:", j.name
#   print "Definition:",j.definition
#   print "Synonyms:", ", ".join(j.lemma_names)
#   print

def next_line(new_line):
	last_word = new_line.split(' ')[-2].replace('.','')
	# words = [last_word]
	# for i,j in enumerate(wordnet.synsets(last_word)):
	# 	words = (j.lemma_names)
	words = [j.lemma_names for i,j in enumerate(wordnet.synsets(last_word))][0]
	# print "WORDS"
	# print words
	for word in words:
		for lines in guys_lines:
			for line in lines:
				for word in line.split(' '):
					if word == last_word:
						print line[line.index(word):]
						return


last_word = ""
for word in trigger_words:
	for story in story_ballets:
		for line in story:
			if line.find(word) != -1:
				# print line
				text = nltk.word_tokenize(line.lower())
				tagged = nltk.pos_tag(text)
				# print tagged
				something = [i for i, v in enumerate(tagged) if word in v[0]]
				if something:
					if word == 'eye':
						new_line = ""
						found = False
						for item in tagged[something[0]-1:]:
							new_line += item[0] + " "
							if "VB" in item[1] or item[1] == "NNS":
								found = True
								print new_line
								next_line(new_line)
								break
						if found == False:
							# print 'HERE'
							new_line = " "
							for i in range(something[0],0,-1):
								new_line = " " + tagged[i][0] + new_line
								if "VB" in item[1]:
									print new_line
									next_line(new_line)
									break
					if word == 'kiss' or word == 'look':
						new_line = ""
						found = False
						for item in tagged[something[0]-1:]:
							new_line += item[0] + " "
							if "NN" in item[1] or item[1] == "NNP":
								found = True
								print new_line
								next_line(new_line)
								break
						if found == False:
							# print 'HERE'
							new_line = " "
							for i in range(something[0],0,-1):
								new_line = " " + tagged[i][0] + new_line
								if "NN" in item[1]:
									print new_line
									next_line(new_line)
									break
					
				#if word == 'prince':
					#print guys_lines[randint(0,len(guys_lines)-1)]


