# Scanner for CPU Project

# Initialize variables and open files
instList = []
inFile = ""
fin = fopen(infile, "r")
for line in fin:
   strTokens = line.split()
   print(strTokens[1], strTokens[2])
