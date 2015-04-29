lines = []

file_name = open("wrongguy.txt")
lines = file_name.readlines()
file_name.close()

new_story = ""

for line in lines:
	line.rstrip()
	line = line.replace('\n',' ')
	new_story += line.replace('.', '.\n')
	#print line

print new_story
