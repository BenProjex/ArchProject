# Scanner for CPU Project

class Scanner:
   # Initialize variables and open files
   def __init__(self, fileName):
      self.instList = []
      self.inFile = fileName
      self.fin = open(self.inFile, "r")

   def fetchInstructions(self):
      for line in self.fin:
         if line[0] == '/':
            continue;
         hexInstructions = line.split()
         for byte in hexInstructions:
            self.instList.append(int(byte, 16))
      self.fin.close()
   
   def writeEPROM(self, epromChip):
      for i in range(len(epromChip.data)):
         epromChip.data[i] = self.instList
