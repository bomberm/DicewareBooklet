import sys
#print formatting
def formating(matrix, output):
	output.write("\\begin{table}\n\t\\centering\n\t\\section*{***** - *****}\n\t\\begin{tabular}{l l l l}\n")
	sys.stdout.flush()	
	newLine = ""
	for row in matrix:
		newLine = ""
		for line in row:
			newLine+= line.rstrip() + " & "
			newLine = newLine.rstrip()
		newLine = newLine.rstrip('&') #remove the last ampersand
		newLine = newLine.rstrip()		
		newLine += "\\\\\n"
		output.write(newLine)
	output.write("\t\\end{tabular}\n \\end{table}\n\n\n")
	sys.stdout.flush()
		

# Creates a list containing 4 lists, each of 27 items, all set to blank strings
w, h = 4, 27;
Matrix = [["" for x in range(w)] for y in range(h)] 

o = open("LongOutput", 'w+')
l = []

with open("LongWordlist.csv", 'r') as f:
	for line in f:	
		l.append(line)


while 1:
	for i in range(0,4):
		line = ""
		for j in range(0, 27):		
			line = l.pop(0) #Get front of list
			line = line.replace(",", " ")
			Matrix[j][i] = line
	formating(Matrix, o)
	if not l: break

o.close()


