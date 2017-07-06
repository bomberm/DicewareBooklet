import sys
#print formatting
def formating(matrix, output):
	firstsection = matrix[0][0][:3]
	lastsection = matrix[26][3][:3]
	output.write("\\begin{table}\n\t\\centering\n\t\\section*{"+firstsection+"** - "+lastsection+"**}\n\t\\begin{tabular}{l l l l}\n")
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
	output.write("\t\\end{tabular}\n \\end{table}\n\\clearpage\n\n")
	sys.stdout.flush()
		

# Creates a list containing 4 lists, each of 27 items, all set to blank strings
w, h = 4, 27;
Matrix = [["" for x in range(w)] for y in range(h)] 

o = open("ModifiedOutput", 'w+')
l = []

with open("ModifiedWordlist.csv", 'r') as f:
	for line in f:	
		l.append(line)


while 1:
	for i in range(0,4):
		line = ""
		for j in range(0, 27):		
			if not l: break			
			line = l.pop(0) #Get front of list
			line = line.replace(",", " ")
			Matrix[j][i] = line
	formating(Matrix, o)
	if not l: break

o.close()


