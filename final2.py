from random import randint
import nltk

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

#trigger_words = ['prince', 'run', 'wedding']
trigger_words = ['prince']

last_word = ""
thing = ""
for word in trigger_words:
	for story in story_ballets:
		for line in story:
			if line.find(word) != -1:
				line_split = line.split('.')
				curr_line = line_split[-1]
				print curr_line
				last_word = curr_line.split(' ')[-1]
				# print last_word
				for line in guys_lines:
					thing = line
					guy_words = line.split(' ')
					for guy_word in guy_words:
						if guy_word == last_word:
							# print 'HERE'
							print last_word
							print thing[thing.index(guy_word):]
							break
				# if 'Odile' in curr_line:
				# 	for line in guys_lines:
				# 		if ' ex' in line:
				# 			print line
				# 			break

			


