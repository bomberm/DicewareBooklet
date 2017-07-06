import itertools

digits = '123456'
shortfile = open("ShortWordlist.csv", 'r')
longfile = open("CleanedLongWordlist.csv", 'r')
newfile = open("ModifiedWordlist.csv", 'w+')

l = []
for line in shortfile:
	templine = line.split(',')
	l.append(templine[1].rstrip())


for line in longfile:
	templine = line.split(',')
	l.append(templine[1].rstrip())


for num in itertools.product(digits, repeat=5):
	s = ''.join(num)
	newfile.write(s+","+l.pop(0)+"\n")

shortfile.close()
longfile.close()
newfile.close()
	
