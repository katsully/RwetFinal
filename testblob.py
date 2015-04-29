import itertools
from random import randint
from textblob import TextBlob, Word

story_ballets = []

# read in files
# swanlake = open("swanlake.txt")
# swan_lines = swanlake.readlines()
# story_ballets.append(swan_lines)
# swanlake.close()

# giselle = open("giselle.txt")
# giselle_lines = giselle.readlines()
# story_ballets.append(giselle_lines)
# giselle.close()

sleepingbeauty = open("sleepingbeauty.txt")
sleeping_lines = sleepingbeauty.readlines()
story_ballets.append(sleeping_lines)
sleepingbeauty.close()

# raymonda = open("Raymonda.txt")
# raymonda_lines = raymonda.readlines()
# story_ballets.append(raymonda_lines)
# raymonda.close()

# cinderella = open("cinderella.txt")
# cinderella_lines = cinderella.readlines()
# story_ballets.append(cinderella_lines)
# cinderella.close()

guythoughts = open("guythoughts.txt")
lines = guythoughts.readlines()
guys_lines = [lines]
guythoughts.close()

hesintoyou = open("hesintoyou.txt")
lines = hesintoyou.readlines()
guys_lines.append(lines)
hesintoyou.close()

notcute = open("notcute.txt")
lines = notcute.readlines()
guys_lines.append(lines)
notcute.close()

righttype = open("righttype.txt")
lines = righttype.readlines()
guys_lines.append(lines)
righttype.close()

unavailable = open("unavailable.txt")
lines = unavailable.readlines()
guys_lines.append(lines)
unavailable.close()

rival = open("rival.txt")
lines = rival.readlines()
guys_lines.append(lines)
rival.close()

lover = open("lover.txt")
lover_lines = lover.readlines()
#guys_lines.append(lines)
lover.close()

drama = open("drama.txt")
lines = drama.readlines()
guys_lines.append(lines)
drama.close()

distance = open("distance.txt")
distance_lines = distance.readlines()
distance.close()

cheating = open("cheating.txt")
lines = cheating.readlines()
guys_lines.append(lines)
cheating.close()

reject = open('rejection.txt')
reject_lines = reject.readlines()
reject.close()

wedding = open("wedding.txt")
wedding_lines = wedding.readlines()
guys_lines.append(wedding_lines)
wedding.close()

mom = open("mom.txt")
mom_lines = mom.readlines()
mom.close()

skimpy = open("skimpy.txt")
skimpy_lines = skimpy.readlines()
skimpy.close()

wrongguy = open("wrongguy.txt")
wrongguy_lines = wrongguy.readlines()
guys_lines.append(wrongguy_lines)
wrongguy.close()

def distance():
	print distance_lines[0]
	print distance_lines[randint(1,len(distance_lines)-1)]

def reject():
	print reject_lines[0]
	print reject_lines[randint(1,len(reject_lines)-1)]

def wedding():
	print wedding_lines[0]
	print wedding_lines[randint(1,len(wedding_lines)-1)]

def lover():
	print lover_lines[0]
	print lover_lines[randint(1,len(lover_lines)-1)]

def mother():
	print mom_lines[0]
	print mom_lines[randint(1,len(mom_lines)-1)]

def skimpy():
	print skimpy_lines[0]
	print skimpy_lines[randint(1,len(skimpy_lines)-1)]

def wrongguy():
	print wrongguy_lines[0]
	print wrongguy_lines[randint(1,len(wrongguy_lines)-1)]

for i in range(20):
	#random_ballet = story_ballets[randint(0,len(story_ballets)-1)]
	section = len(sleeping_lines) / 20
	random_line = sleeping_lines[randint(i*section, (i+1)*section)]

	random_line = random_line.decode('utf-8')
	blob = TextBlob(random_line)
	nouns = []
	verbs = []
	adjs = []
	advs = []
	prps = []
	for word,pos in blob.tags:
		#print word, pos
		if pos == "NNS" or pos == "NNP" or pos == "NN" or pos == "PRP":
			w = Word(word.lower())
			nouns.append(w.lemmatize())
		elif pos == "VBZ" or pos == "VBG" or pos == "VBD":
			w = Word(word)
			verbs.append(w.lemmatize())
			#print w.lemmatize(word)
		elif pos == "JJ":
			adjs.append(word)
		elif pos == "RB":
			advs.append(word)
		elif pos == "PRP$":
			prps.append(word)

	loop = True
	search_for = []
	print random_line
	if 'his' in prps and 'mother' in nouns:
		mother()
		loop = False
	elif any(word in nouns for word in ["wedding", "marriage", 'festivity']):
		wedding()
		loop = False
	elif "betrothed" in verbs:
		wedding()
		loop = False
	elif any(word in nouns for word in ["cursade", "goodbye"]):
		distance()
		loop = False
	elif 'reject' in verbs:
		reject()
		loop = False
	elif 'extravagantly' in advs:
		skimpy()
		loop = False
	elif 'over-exuberance' in adjs:
		skimpy()
		loop = False
	elif 'abduct' in nouns:
		wrongguy()
		loop = False
	if 'secret' in adjs:
		search_for.append(['unfaithful', 'suspicious'])
	if "forgiveness" in nouns:
		search_for.append(['forgive', 'apologize'])
	if "knight" in nouns:
		search_for.append(["charming"])
	if "execution" in nouns:
		search_for.append(["off the market"])
	if "united" in nouns:
		search_for.append(["wedding", "marriage", "married"])
	if "rich" in nouns:
		search_for.append(["rich"])
	if 'envy' in nouns:
		search_for.append(['jealous', 'envy'])
	if 'jealous' in adjs:
		search_for.append(['envy', 'jealous'])
	if 'watch' in nouns:
		search_for.append(["looks at"])
	if 'kiss' in nouns:
		search_for.append ["lips"]
	if 'die' in nouns:
		search_for.append(['drama'])
	if 'tragic' in adjs:
		search_for.append(['drama'])
	if 'tragedy' in nouns:
		search_for.append(['drama'])
	if 'dying' in verbs:
		search_for.append(['drama'])
	if 'die' in nouns:
		search_for.append(['drama'])
	if 'alone' in advs:
		search_for.append(['lonely', 'loneliness'])
	if 'himself' in nouns:
		search_for.append(['alone', 'lonely', 'loneliness'])
	if 'suspicion' in nouns:
		search_for.append(['unfaithful', 'suspicious'])
	if 'difficulty' in nouns:
		search_for.append(['hard'])
	if 'evil' in adjs:
		search_for.append(['nemesis', 'rival'])
	if "carabosse" in nouns:
		search_for.append(['nemesis', 'rival'])
	if "rothbart" in nouns:
		search_for.append(['nemesis', 'rival'])
	if "rival" in adjs:
		search_for.append(['nemesis'])
	if not search_for:
		if "lover" in nouns:
			lover()
			loop = False
			break
	search_terms = list(itertools.chain.from_iterable(search_for))
	search_terms2 = list(itertools.chain(nouns, verbs, adjs, advs))

	#print search_terms
	possible_lines = []

	found = False
	if loop:
		for article in guys_lines:
			for line in article[1:]:
				if any(word in line for word in search_terms):
					possible_lines.append(line)
					found = True
			if found:
				print article[0]
				print possible_lines[randint(0,len(possible_lines)-1)]
				break

# if not found and loop:
# 	for article in guys_lines:
# 		for line in article[1:]:
# 			for word in search_terms2:
# 				print word
# 				if word in line:
# 					print
# 			# if any(word in line for word in search_terms2):
# 			# 	possible_lines.append(line)
# 			# 	found = True
# 		if found:
# 			print article[0]
# 			print possible_lines[randint(0,len(possible_lines)-1)]
# 			break
