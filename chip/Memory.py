
#!/usr/bin/python
from ArchProject.Wire import Wire

WRITE = 1
READ = 0
###########################################################
#Don't worry about class Chip cuz Memory class use it only#
###########################################################
class Block:


  def __init__(self,name):
      self.data = [0]*(2**12)
      self.name =name;
#rdOrwr: 0 for read and 1 for write
  def read8bit(self,address,data):
    print("read data at chip: ",self.name," address [$", address,"] = $", self.data[address],".");
    return self.data[address]

  def write8bit(self,address,data):
    print("Write $",data," to chip: ",self.name," address [$", address,"].");
    self.data[address] =  data

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
class MEMChip:

  def __init__(self, address_wire, value_input, read_write, chip_id):
    self.chip = [Block("U" + str(200 + i)) for i in range(15)]
    self.value_output = Wire("MEM_LINE")
    self.address_wire = address_wire
    self.value_input = value_input
    self.read_write = read_write
    self.chip_id = chip_id


  def Action(self):
      self.memoryOp(self.address_wire.get_value(), self.value_input.get_value(), self.read_write.get_value)


  def memoryOp(self,address,data,rdOrwr):
    if(address<=65535):
      chipselect = address >> 12
      chipaddr = address & 4095 
      if rdOrwr == WRITE:
        self.chip[chipselect].write8bit(chipaddr,data)
      elif rdOrwr == READ:
        return self.chip[chipselect].read8bit(chipaddr,data)
      else:
        return None
    else:
      raise Exception('the address is overflow')
#temp = Memory();
#temp.memoryOp(5000,300,WRITE);
#print(temp.memoryOp(5000,300,READ));