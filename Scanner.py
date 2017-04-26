# Scanner for CPU Project

class Scanner:
   # Initialize variables and open files
   def __init__(self, fileName, fOutName):
      self.instList = []
      self.inFile = fileName
      self.fin = open(self.inFile, "r")
      self.outFile = fOutName
      self.fout = open(self.outFile, "w")

   def fetchInstructions(self):
      for line in self.fin:
         hexInstructions = line.split()
         self.out.write(hexInstructions)
      self.fin.close()
