# Scanner for CPU Project

class Scanner:
   # Initialize variables and open files
   def __init__(self, fileName):
      self.instList = []
      self.inFile = fileName
      self.fin = open(self.inFile, "r")

   def fetchInstructions(self):
      for line in self.fin:
         hexInstructions = line.split()
      self.fin.close()
