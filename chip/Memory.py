#!/usr/bin/python
WRITE = 1
READ = 0
###########################################################
#Don't worry about class Chip cuz Memory class use it only#
###########################################################
class Chip:
  
  def __init__(self):
      self.data = [0]*(2**12)
#rdOrwr: 0 for read and 1 for write
  def read8bit(seft,address,data):
    return seft.data[address]

  def write8bit(seft,address,data):
    seft.data[address] =  data
###############################################################
#Memory class will work as a real memory that will store      #
#instruction pointer and data.                                #
#we can call memoryOp function to read or write data to memory
#
#exmple:
#m = Memory()
#m.memoryOp(4096,34,1) #memoryOp(address,data,rdOrwr)
#now rdOrwr(1bit) = 1 mean write to memory
#this call will write data(8bit) = 34 to address(16bit)=4096
#
#m.memoryOp(4096,34,0) #memoryOp(address,data,rdOrwr)
#now rdOrwr(1bit) = 0 mean read from memory
#notice: we won't use parameter data in this call.
#this call will read from memory address(16bit)=4096 and return#
#data(8bit)                                                    #
################################################################
class Memory:

  def __init__(seft):
    seft.chip = [Chip() for i in range(15)]
  def memoryOp(seft,address,data,rdOrwr):
    if(address<=65535):
      chipselect = address >> 12
      chipaddr = address & 4095 
      if rdOrwr == WRITE:
        seft.chip[chipselect].write8bit(chipaddr,data)
      elif rdOrwr == READ:
        return seft.chip[chipselect].read8bit(chipaddr,data)
      else:
        return None
    else:
      raise Exception('the address is overflow')