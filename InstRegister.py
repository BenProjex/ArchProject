from ArchProject.Chip import Chip
from ArchProject.Wire import Wire
from ArchProject.chip.Memory import Block

class InstRegister():


   def __init__(self):
      self.eprom = Block("TEMP")
      self.cursor = 0
      self.instLen = Wire("InstLen")
      self.Offset = Wire("Offset")
      self.Offset.set_value(0)
      self.Inst = Wire("Inst")
      self.RW = Wire("RW")
      self.opCodes = []
      self.u14CS = Wire("u14_CS")
      self.u15CS = Wire("u15_CS")
      self.u100Cin = Wire("u100_Cin")
      self.u100CS = Wire("u100_CS")
      self.u107Sign = Wire("u107_Sign")
      self.u110CS = Wire("u110_CS")
      self.u111Sel = Wire("u111_Sel")
      self.u112Sel = Wire("u112_Sel")
      self.u113Sel = Wire("u113_Sel")
      self.u114SelA = Wire("u114_SelA")
      self.u114SelB = Wire("u114_SelB")
      self.u114OEA = Wire("u114_OEA")
      self.u114OEB = Wire("u114_OEB")
      self.u115Sel = Wire("u115_Sel")
      self.u116Sel = Wire("u116_Sel")
      self.u117Sel = Wire("u117_Sel")
      self.u118ASel = Wire("u118A_Sel")
      self.u118BSel = Wire("u118B_Sel")
      self.u120Sel = Wire("u120_Sel")
      self.u220Sel = Wire("u220_Sel")
      self.u220OE1 = Wire("u220_OE1")
      self.u220OE2 = Wire("u220_OE2")

      self.u119Sel = Wire("u119_Sel")
   
   def Action(self, eprom):
      self.opCodes = []
      if self.cursor >= 2**12:
         print("Reached end of EPROM")
         return 0
      else:
         self.byte_list = eprom.data[0]
         self.currentByte = self.byte_list[self.cursor]
         self.opCodes.append(self.currentByte)
         print(self.currentByte)
         if(self.currentByte == 0x80):
            # Mov RX,RY
            self.fetchBytes(3)
            self.u113Sel.set_value(self.opCodes[2] // 0x10)
            self.u118BSel.set_value(0)
            self.u114SelB.set_value(self.opCodes[1] // 0x10)
            self.u114OEA.set_value(0)
            self.u114OEB.set_value(1)
         elif(self.currentByte == 0x81):
            # Mov RX,$HH
            self.fetchBytes(3)
            self.u113Sel.set_value(6)
            self.u118BSel.set_value(0)
            self.u114SelB.set_value(self.opCodes[1] // 0x10)
            self.u114OEA.set_value(0)
            self.u114OEB.set_value(1)
            self.Inst.set_value(self.opCodes[2])
         elif(self.currentByte == 0x82):
            # Mov RX,[$MMMM]
            self.fetchBytes(4)
            self.u113Sel.set_value(4)
            self.u118BSel.set_value(0)
            self.u114SelB.set_value(self.opCodes[1] // 0x10)
            self.u114OEA.set_value(0)
            self.u114OEB.set_value(1)
            self.RW.set_value(0)
            addr = ''.join(str(self.opCodes[2]) + str(self.opCodes[3]))
            self.Inst.set_value(int(addr, 16))
         elif(self.currentByte == 0x83):
            # Mov [$MMMM],RX
            self.fetchBytes(4)
            self.u113Sel.set_value(self.opCodes[1] // 0x10)
            self.RW.set_value(1)
            addr = ''.join(str(self.opCodes[1]) + str(self.opCodes[2]))
            self.Inst.set_value(int(addr, 16))
            # to RAM
         elif(self.currentByte == 0x10):
            # Addc RX,RY
            self.fetchBytes(3)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(self.opCodes[2] // 0x10)
            self.u100Cin.set_value(0)
            self.u120Sel.set_value(0)
            self.u100CS.set_value(1)
            self.u111Sel.set_value(0)
            self.u118ASel.set_value(3)
            self.u114SelA.set_value(self.opCodes[1] // 0x10)
            self.u114OEA.set_value(1)
            self.u114OEB.set_value(0)
         elif(self.currentByte == 0x11):
            # Addc RX,$HH
            self.fetchBytes(3)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(6)
            self.u100Cin.set_value(0)
            self.u120Sel.set_value(0)
            self.u100CS.set_value(1)
            self.u111Sel.set_value(0)
            self.u118ASel.set_value(3)
            self.u114SelA.set_value(self.opCodes[1] // 0x10)
            self.u114OEA.set_value(1)
            self.u114OEB.set_value(0)
            self.Inst.set_value(self.opCodes[2])
         elif(self.currentByte == 0x12):
            # Addc RX,[$MMMM]
            self.fetchBytes(4)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(4)
            self.u100Cin.set_value(0)
            self.u120Sel.set_value(0)
            self.u100CS.set_value(1)
            self.u111Sel.set_value(0)
            self.u118ASel.set_value(3)
            self.u114SelA.set_value(self.opCodes[1] // 0x10)
            self.u114OEA.set_value(1)
            self.u114OEB.set_value(0)
            self.RW.set_value(0)
            addr = ''.join(str(self.opCodes[2]) + str(self.opCodes[3]))
            self.Inst.set_value(int(addr, 16))
         elif(self.currentByte == 0x13):
            # Addc [$MMMM],RX
            self.fetchBytes(4)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(4)
            self.u100Cin.set_value(0)
            self.u120Sel.set_value(0)
            self.u100CS.set_value(1)
            self.u111Sel.set_value(0)
            self.RW.set_value(1)
            addr = ''.join(str(self.opCodes[1]) + str(self.opCodes[2]))
            self.Inst.set_value(int(addr, 16))
            # to RAM
         elif(self.currentByte == 0x20):
            # Subb RX,RY
            self.fetchBytes(3)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(self.opCodes[2] // 0x10)
            self.u100Cin.set_value(1)
            self.u120Sel.set_value(0)
            self.u100CS.set_value(1)
            self.u111Sel.set_value(0)
            self.u118ASel.set_value(3)
            self.u114SelA.set_value(self.opCodes[1] // 0x10)
            self.u114OEA.set_value(1)
            self.u114OEB.set_value(0)
         elif(self.currentByte == 0x21):
            # Subb RX,$HH
            self.fetchBytes(3)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(6)
            self.u100Cin.set_value(1)
            self.u120Sel.set_value(0)
            self.u100CS.set_value(1)
            self.u111Sel.set_value(0)
            self.u118ASel.set_value(3)
            self.u114SelA.set_value(self.opCodes[1] // 0x10)
            self.u114OEA.set_value(1)
            self.u114OEB.set_value(0)
            self.Inst.set_value(self.opCodes[2])
         elif(self.currentByte == 0x22):
            # Subb RX,[$MMMM]
            self.fetchBytes(4)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(4)
            self.u100Cin.set_value(1)
            self.u120Sel.set_value(0)
            self.u100CS.set_value(1)
            self.u111Sel.set_value(0)
            self.u118ASel.set_value(3)
            self.u114SelA.set_value(self.opCodes[1] // 0x10)
            self.u114OEA.set_value(1)
            self.u114OEB.set_value(0)
            self.RW.set_value(0)
            addr = ''.join(str(self.opCodes[2]) + str(self.opCodes[3]))
            self.Inst.set_value(int(addr, 16))
         elif(self.currentByte == 0x23):
            # Subb [$MMMM],RX
            self.fetchBytes(4)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(4)
            self.u100Cin.set_value(1)
            self.u120Sel.set_value(0)
            self.u100CS.set_value(1)
            self.u111Sel.set_value(0)
            self.RW.set_value(1)
            addr = ''.join(str(self.opCodes[1]) + str(self.opCodes[2]))
            self.Inst.set_value(int(addr, 16))
            # to RAM
         elif(self.currentByte == 0x30):
            # Cmp RX,RY
            self.fetchBytes(3)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(self.opCodes[2] // 0x10)
            self.u100Cin.set_value(1)
            self.u120Sel.set_value(0)
            self.u110CS.set_value(1)
         elif(self.currentByte == 0x31):
            # Cmp RX,$HH
            self.fetchBytes(3)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(6)
            self.u100Cin.set_value(1)
            self.u120Sel.set_value(0)
            self.u110CS.set_value(1)
            self.Inst.set_value(self.opCodes[2])
         elif(self.currentByte == 0x32):
            # Cmp RX,[$MMMM]
            self.fetchBytes(4)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(4)
            self.u100Cin.set_value(1)
            self.u120Sel.set_value(0)
            self.u110CS.set_value(1)
            self.RW.set_value(0)
            addr = ''.join(str(self.opCodes[2]) + str(self.opCodes[3]))
            self.Inst.set_value(int(addr, 16))
         elif(self.currentByte == 0x33):
            # Cmp [$MMMM],RX
            self.fetchBytes(4)
            self.u112Sel.set_value(4)
            self.u113Sel.set_value(self.opCodes[1] // 0x10)
            self.u100Cin.set_value(1)
            self.u120Sel.set_value(0)
            self.u110CS.set_value(1)
            self.RW.set_value(1)
            addr = ''.join(str(self.opCodes[1]) + str(self.opCodes[2]))
            self.Inst.set_value(int(addr, 16))
         elif(self.currentByte == 0x40):
            # Not RX
            self.fetchBytes(2)
            self.u113Sel.set_value(self.opCodes[1] // 0x10)
            self.u111Sel.set_value(4)
            self.u118ASel.set_value(3)
            self.u114SelA.set_value(self.opCodes[1] // 0x10)
            self.u114OEA.set_value(1)
            self.u114OEB.set_value(0)
         elif(self.currentByte == 0x43):
            # Not [$MMMM]
            self.fetchBytes(3)
            self.u113Sel.set_value(4)
            self.u111Sel.set_value(4)
            self.RW.set_value(0)
            addr = ''.join(str(self.opCodes[1]) + str(self.opCodes[2]))
            self.Inst.set_value(int(addr, 16))
            # to RAM
         elif(self.currentByte == 0x50):
            # And RX,RY
            self.fetchBytes(3)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(self.opCodes[2] // 0x10)
            self.u111Sel.set_value(1)
            self.u118ASel.set_value(3)
            self.u114SelA.set_value(self.opCodes[1] // 0x10)
            self.u114OEA.set_value(1)
            self.u114OEB.set_value(0)
         elif(self.currentByte == 0x51):
            # And RX,$HH
            self.fetchBytes(3)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(6)
            self.u111Sel.set_value(1)
            self.u118ASel.set_value(3)
            self.u114SelA.set_value(self.opCodes[1] // 0x10)
            self.u114OEA.set_value(1)
            self.u114OEB.set_value(0)
            self.Inst.set_value(self.opCodes[2])
         elif(self.currentByte == 0x52):
            # And RX,[$MMMM]
            self.fetchBytes(4)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(4)
            self.u111Sel.set_value(1)
            self.u118ASel.set_value(3)
            self.u114SelA.set_value(self.opCodes[1] // 0x10)
            self.u114OEA.set_value(1)
            self.u114OEB.set_value(0)
            self.u118ASel.set_value(3)
            self.u114SelA.set_value(self.opCodes[1] // 0x10)
            self.u114OEA.set_value(1)
            self.u114OEB.set_value(0)
            self.RW.set_value(0)
            addr = ''.join(str(self.opCodes[2]) + str(self.opCodes[3]))
            self.Inst.set_value(int(addr, 16))
         elif(self.currentByte == 0x53):
            # And [$MMMM],RX
            self.fetchBytes(4)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(4)
            self.u111Sel.set_value(1)
            self.RW.set_value(1)
            addr = ''.join(str(self.opCodes[1]) + str(self.opCodes[2]))
            self.Inst.set_value(int(addr, 16))
         elif(self.currentByte == 0x60):
            # Or RX,RY
            self.fetchBytes(3)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(self.opCodes[2] // 0x10)
            self.u111Sel.set_value(2)
            self.u118ASel.set_value(3)
            self.u114SelA.set_value(self.opCodes[1] // 0x10)
            self.u114OEA.set_value(1)
            self.u114OEB.set_value(0)
         elif(self.currentByte == 0x61):
            # Or RX,$HH
            self.fetchBytes(3)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(6)
            self.u111Sel.set_value(2)
            self.u118ASel.set_value(3)
            self.u114SelA.set_value(self.opCodes[1] // 0x10)
            self.u114OEA.set_value(1)
            self.u114OEB.set_value(0)
            self.Inst.set_value(self.opCodes[2])
         elif(self.currentByte == 0x62):
            # Or RX,[$MMMM]
            self.fetchBytes(4)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(4)
            self.u111Sel.set_value(2)
            self.u118ASel.set_value(3)
            self.u114SelA.set_value(self.opCodes[1] // 0x10)
            self.u114OEA.set_value(1)
            self.u114OEB.set_value(0)
            self.RW.set_value(0)
            addr = ''.join(str(self.opCodes[2]) + str(self.opCodes[3]))
            self.Inst.set_value(int(addr, 16))
         elif(self.currentByte == 0x63):
            # Or [$MMMM],RX
            self.fetchBytes(4)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(4)
            self.u111Sel.set_value(2)
            self.RW.set_value(1)
            addr = ''.join(str(self.opCodes[1]) + str(self.opCodes[2]))
            self.Inst.set_value(int(addr, 16))
            # to RAM
         elif(self.currentByte == 0x70):
            # Xor RX,RY
            self.fetchBytes(3)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(self.opCodes[2] // 0x10)
            self.u111Sel.set_value(3)
            self.u118ASel.set_value(3)
            self.u114SelA.set_value(self.opCodes[1] // 0x10)
            self.u114OEA.set_value(1)
            self.u114OEB.set_value(0)
         elif(self.currentByte == 0x71):
            # Xor RX,$HH
            self.fetchBytes(3)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(6)
            self.u111Sel.set_value(3)
            self.u118ASel.set_value(3)
            self.u114SelA.set_value(self.opCodes[1] // 0x10)
            self.u114OEA.set_value(1)
            self.u114OEB.set_value(0)
            self.Inst.set_value(self.opCodes[2])
         elif self.currentByte == 0x72:
            # Xor RX,[$MMMM]
            self.fetchBytes(4)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(4)
            self.u111Sel.set_value(3)
            self.u118ASel.set_value(3)
            self.u114SelA.set_value(self.opCodes[1] // 0x10)
            self.u114OEA.set_value(1)
            self.u114OEB.set_value(0)
            self.RW.set_value(0)
            addr = ''.join(str(self.opCodes[2]) + str(self.opCodes[3]))
            self.Inst.set_value(int(addr, 16))
         elif(self.currentByte == 0x73):
            # Xor [$MMMM],RX
            self.fetchBytes(4)
            self.u112Sel.set_value(self.opCodes[1] // 0x10)
            self.u113Sel.set_value(4)
            self.u111Sel.set_value(3)
            self.RW.set_value(1)
            addr = ''.join(str(self.opCodes[1]) + str(self.opCodes[2]))
            self.Inst.set_value(int(addr, 16))

      self.instLen.set_value(len(self.opCodes))
      self.cursor = self.cursor + 1

   def fetchBytes(self, count):
      for i in range(1, count):
         self.cursor = self.cursor + 1
         self.opCodes.append(self.byte_list[self.cursor])
