from Chip import *
from Wire import *

import sys

class InstRegister():
   
   def __init__(self):
      self.cursor = 0
      self.wire = Wire()
   
   def action(self, eprom):
      if cursor >= 2**12:
         print("Reached end of EPROM")
         return 0
      else:
         currentByte = eprom.data[cursor]
         #left off here
