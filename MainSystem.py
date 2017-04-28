from ArchProject.Chip import *
from ArchProject.Wire import Wire
from ArchProject.chip.Memory import MEMChip
from ArchProject.InstRegister import InstRegister
from ArchProject.Scanner import Scanner


class MainSystem:

    stk_wire = Wire("Stack Wire")
    clock_wire = Wire("Clock")
    stk_wire.set_value(2)

    def construct_register_chips(self):


        # Type: Register
        # ID: U_0_500
        # Name: Instruction_Register_Decoder
        # Input:   { MEM_1_4 }
        # Control: {  }
        # Output:  { W_0_500_0, W_0_500_1, W_0_500_2, CONTROL } // W_0_500_2 is INSTR
        self.U_0_500 = InstRegister()

        # Type: Register
        # ID: U_0_010
        # Name: Register_0
        # Input: TBD
        # Control: {  }
        # Output: W_0_010_0
        self.U_0_010 = REGISTERChip(None, None, self.clock_wire, "U_0_010")
        self.register_chip_list.append(self.U_0_010)
        # Type: Register
        # ID: U_0_011
        # Name: Register_1
        # Input: TBD
        # Control: {  }
        # Output: W_0_011_0
        self.U_0_011 = REGISTERChip(None, None, self.clock_wire, "U_0_011")
        self.register_chip_list.append(self.U_0_011)

        # Type: Register
        # ID: U_0_012
        # Name: Register_2
        # Input: TBD
        # Control: {  }
        # Output: W_0_012_0
        self.U_0_012 = REGISTERChip(None, None, self.clock_wire, "U_0_012")
        self.register_chip_list.append(self.U_0_012)

        #Type: Register
        # ID: U_0_013
        # Name: Register_3
        # Input: TBD
        # Control: {  }
        # Output:  { W_0_013_0 }
        self.U_0_013 = REGISTERChip(None, None, self.clock_wire, "U_0_013")
        self.register_chip_list.append(self.U_0_013)

        # Type: Register
        # ID: U_0_014
        # Name: Stack_Pointer
        # Input:   { W_2_117_0 }
        # Control: {  }
        # Output:  { W_0_014_0 }
        self.U_0_014 = REGISTERChip(None, self.U_0_500.u14CS, self.clock_wire, "U_0_014")
        self.register_chip_list.append(self.U_0_014)

        # Type: Register
        # ID: U_0_015
        # Name: Instruction_Pointer
        # Input:
        # Control: {  }
        # Output:  { W_0_015_0 }
        self.U_0_015 = REGISTERChip(None, self.U_0_500.u15CS, self.clock_wire, "U_0_015")
        self.register_chip_list.append(self.U_0_015)

        # Type: Register
        # ID: U_0_110
        # Name: Flags_Register
        # Inputs:  { W_2_100_0, W_2_100_1, W_2_100_2 }
        # Control: {  }
        # Outputs: { W_0_110_0 }
        self.U_0_110 = REGISTERChip(None, self.U_0_500.u110CS, self.clock_wire, "U_0_110")
        self.register_chip_list.append(self.U_0_110)
        return

    def construct_stage_1_chips(self):

        # Type: Multiplexer
        # ID: U_1_112
        # Name: Select_Register_A_MUX
        # Inputs: { W_0_010_0, W_0_011_0, W_0_012_0, W_0_013_0, W_3_100_0, W_0_110_0, W_0_500_2 }
        # Control: { W_1_112_9 }
        # Outputs: { W_1_112_0 }
        self.U_1_112 = MUX8to1Chip(self.U_0_010.output_wire, self.U_0_011.output_wire, self.U_0_012.output_wire, self.U_0_013.output_wire, None, self.U_0_110.output_wire, self.U_0_500.Inst, None,
                                   self.U_0_500.u112Sel, "U_1_112")
        self.stage_1_chip_list.append(self.U_1_112)

        # Type: Multiplexer
        # ID: U_1_113
        # Name: Select_Register_B_MUX
        # Inputs: { W_0_010_0, W_0_011_0, W_0_012_0, W_0_013_0, W_3_100_0, W_0_110_0, W_0_500_2 }
        # Control: { W_1_113_9 }
        # Outputs: { W_1_113_0 } // This and W_1_112_0 make up the DATA line
        self.U_1_113 = MUX8to1Chip(self.U_0_010.output_wire, self.U_0_011.output_wire, self.U_0_012.output_wire, self.U_0_013.output_wire, None, self.U_0_110.output_wire, self.U_0_500.Inst, None,
                                   self.U_0_500.u113Sel, "U_1_113")
        self.stage_1_chip_list.append(self.U_1_113)

        # Type: Adder / Subtractor
        # ID: U_1_107
        # Name: Stack_Adder_Subtractor
        # Inputs: { W_0_014_0, (LITERAL VALUE 2) }
        # Control: { W_1_107_9 }
        # Outputs: { W_1_107_0 }
        self.U_1_107 = ADDSUBChip(self.U_0_014.output_wire, self.stk_wire
                                  , self.U_0_500.u107Sign, "U_1_107")
        self.stage_1_chip_list.append(self.U_1_107)

        # Type: Adder
        # ID: U_1_105
        # Name: Instruction_Length_Adder
        # Inputs:  { W_0_500_0, W_0_015_0 }
        # Control: {  }
        # Outputs: { W_1_105_0 }
        self.U_1_105 = ADDSUBChip(self.U_0_500.instLen, self.U_0_015.output_wire, Wire("FAKE"), "U_1_105")
        self.stage_1_chip_list.append(self.U_1_105)

        return

    def construct_stage_2_chips(self):


        # Type: Adder-Subtractor
        # ID: U_2_100
        # Name: ALU_Adder_Subtractor
        # Inputs:  { W_1_112_0, W_1_113_0 }
        # Control: { U_2_100_9 }
        # Outputs: { W_2_100_0, W_2_100_1 }
        self.U_2_100 = ADDSUBChip(self.U_1_112.output_wire, self.U_1_113.output_wire, Wire("Fake"), "U_2_100")
        self.stage_2_chip_list.append(self.U_2_100)

        # Type: AND
        # ID: U_2_101
        # Name: ALU_AND
        # Inputs:  { W_1_112_0, W_1_113_0 }
        # Control: {  }
        # Outputs: { W_2_101_0 }
        self.U_2_101 = ANDChip(self.U_1_112.output_wire, self.U_1_113.output_wire, "U_2_101")
        self.stage_2_chip_list.append(self.U_2_101)

        # Type: OR
        # ID: U_2_102
        # Name: ALU_OR
        # Inputs:  { W_1_112_0, W_1_113_0 }
        # Control: {  }
        # Outputs: { W_2_102_0 }
        self.U_2_102 = ORChip(self.U_1_112.output_wire, self.U_1_113.output_wire, "U_2_102")
        self.stage_2_chip_list.append(self.U_2_102)

        # Type: XOR
        # ID: U_2_103
        # Name: ALU_OR
        # Inputs:  { W_1_112_0, W_1_113_0}
        # Control: {  }
        # Outputs: { W_2_103_0 }
        self.U_2_103 = XORChip(self.U_1_112.output_wire, self.U_1_113.output_wire, "U_2_103")
        self.stage_2_chip_list.append(self.U_2_103)

        # Type: NOT
        # ID: U_2_104
        # Name: ALU_NOT
        # Inputs:  { W_1_113_0 }
        # Control: {  }
        # Outputs: { W_2_104_0 }
        self.U_2_104 = NOTChip(self.U_1_113.output_wire, "U_2_104")
        self.stage_2_chip_list.append(self.U_2_104)

        # Type: Adder
        # ID: U_2_106
        # Name: Instruction_Offset_Adder
        # Inputs:  { W_1_105_0, W_0_500_1 }
        # Control: {  }
        # Outputs: { W_2_106_0 }
        self.U_2_106 = ADDSUBChip(self.U_1_105.v_output_wire, self.U_0_500.Offset, Wire("FAKE"), "U_2_106")
        self.stage_2_chip_list.append(self.U_2_106)

        # Type: Multiplexer
        # ID: U_2_116
        # Name: Memory_Addr_MUX
        # Inputs:  { W_0_015_0, W_0_014_0, W_0_500_2, DATA } //W_1_112_0
        # Control: { W_2_116_9 }
        # Outputs: { W_2_116_0 }  // MEM ADDR LINE
        self.U_2_116 = MUX4to1Chip(self.U_0_015.output_wire, self.U_0_014.output_wire, self.U_0_500.Inst, self.U_1_112.output_wire,
                                   self.U_0_500.u116Sel, "U_2_116")
        self.stage_2_chip_list.append(self.U_2_116)

        # Type: Multiplexer
        # ID: U_2_117
        # Name: Stack_Ptr_MUX
        # Inputs:  { W_1_107_0, DATA }
        # Control: { W_2_117_9 }
        # Outputs: { W_2_117_0 }  AT THIS POINT WE CAN PROVIDE INPUT TO STK POINTER
        self.U_2_117 = MUX2to1Chip(self.U_1_107.v_output_wire, self.U_1_112.output_wire,
                                   self.U_0_500.u117Sel, "U_2_117")
        self.stage_2_chip_list.append(self.U_2_117)

        return

    def construct_stage_3_chips(self):

        # Type: Multiplexer
        # ID: U_3_111
        # Name: Select_ALU_MUX
        # Inputs:  { W_2_100_0, W_2_101_0, W_2_102_0, W_2_103_0, W_2_104_0 }
        # Control: { W_3_111_9 }
        # Outputs: { W_3_111_0 } // This is the ALU line
        self.U_3_111 = MUX8to1Chip(self.U_2_100.v_output_wire, self.U_2_101.out_wire, self.U_2_102.output_wire, self.U_2_103.output_wire, self.U_2_104.output_wire, None, None, None,
                                   self.U_0_500.u111Sel, "U_3_111")
        self.stage_3_chip_list.append(self.U_3_111)

        # Type: Multiplexer
        # ID: U_3_115
        # Name: Select_ALU_MUX
        # Inputs:  { DATA, W_3_500_2, W_1_105_0, W_2_106_0 }
        # Control: { W_3_115_9 }
        # Outputs: { W_3_115_0 } // INPUT FOR U_015
        self.U_3_115 = MUX4to1Chip(self.U_1_112.output_wire, self.U_0_500.Inst, self.U_1_105.v_output_wire, self.U_2_106.v_output_wire,
                                   self.U_0_500.u115Sel, "U_3_115")
        self.stage_3_chip_list.append(self.U_3_115)

        return

    def construct_stage_4_chips(self):

        # Type: Multiplexer
        # ID: U_4_119
        # Name: Select_MEM_MUX
        # Inputs:  { W_3_111_0, W_1_112_0, W_0_500_2 } // Fill these out later
        # Control: { W_3_115_9 }
        # Outputs: { W_3_119_0 } input to RAM
        self.U_4_119 = MUX4to1Chip(self.U_3_111.output_wire, self.U_1_112.output_wire, None, None,
                                   self.U_0_500.u119Sel, "U_4_119")
        self.stage_4_chip_list.append(self.U_4_119)

        # Type: RAM
        # ID: U_4_100
        # Name: RAM_Chip                    // This and the Select_MEM_MUX are technically different stages but we treat them the same
        # Inputs:  { W_2_116_0, W_3_119_0 }
        # Control: { W_4_100_9 }            // Read/Write
        # Outputs: { W_4_100_0 }            // This is the MEM line
        self.U_4_100 = MEMChip(self.U_2_116.output_wire, self.U_4_119.output_wire, self.U_0_500.RW, "U_4_100")
        self.stage_4_chip_list.append(self.U_4_100)

        # Type: Multiplexer
        # ID: U_4_120
        # Name: Select_FLAGS_MUX
        # Inputs:  { W_2_100_1, W_3_111_0 }
        # Control: { W_4_111_9 }
        # Outputs: { W_4_120_0 }
        self.U_4_120 = MUX2to1Chip(self.U_2_100.c_output_wire, self.U_3_111.output_wire,
                                   self.U_0_500.u120Sel, "U_4_120")
        self.stage_4_chip_list.append(self.U_4_120)

        return

    def construct_stage_5_chips(self):

        # Type: Multiplexer
        # ID: U_5_118A
        # Name: Select_Register_A_Input_MUX
        # Inputs:  { W_1_112_0, W_0_014_0, W_0_500_2, W_3_111_0, RES, W_3_100_0, RES, RES }
        # Control: { W_4_118A_9, W_0_014_1 }
        # Outputs: { W_4_118A_0 }
        self.U_5_118A = MUX8to1Chip(self.U_1_112.output_wire, self.U_0_014.output_wire, self.U_0_500.Inst, self.U_3_111.output_wire, None, self.U_2_100.v_output_wire, None, None,
                                    self.U_0_500.u118ASel, "U_5_118A")
        self.stage_5_chip_list.append(self.U_5_118A)

        # Type: Multiplexer
        # ID: U_5_118B
        # Name: Select_Register_B_Input_MUX
        # Inputs:  { W_1_113_0, W_0_014_0, W_0_500_2, W_3_111_0, RES, W_3_100_0, RES, RES }
        # Control: { W_4_118B_9 }
        # Outputs: { W_4_118B_0 }
        self.U_5_118B = MUX8to1Chip(self.U_1_113.output_wire, self.U_0_014.output_wire, self.U_0_500.Inst, self.U_3_111.output_wire, None, self.U_2_100.v_output_wire, None, None,
                                    self.U_0_500.u118BSel, "U_5_118B")

        self.stage_5_chip_list.append(self.U_5_118B)

        return


    def construct_stage_6_chips(self):

        # Type: Demultiplexer
        # ID: U_4_114A
        # Name: Select_Register_A_Input_MUX
        # Inputs:  { W_5_118A_0 }
        # Control: { W_6_114A_9, OE_A }
        # Outputs: { W_6_114A_0 } // These outputs go into the registers
        self.U_6_114 = DEMUX2to4Chip(self.U_5_118A.output_wire, self.U_5_118B.output_wire,
                                     self.U_0_500.u114OEA, self.U_0_500.u114OEB, self.U_0_500.u114SelA, self.U_0_500.u114SelB, "U_6_114")
        self.stage_6_chip_list.append(self.U_6_114)

        # Type: Demultiplexer
        # ID: U_4_114B
        # Name: Select_Register_B_Input_MUX
        # Inputs:  { W_5_118B_0 }
        # Control: { W_6_114B_9, OE_B }
        # Outputs: { W_6_114B_0 } // These outputs go into the registers

        return

    def final_stage(self):

        # Register chip selects
        self.U_0_010.cs_wire = self.U_6_114.cs_wire_0
        self.U_0_011.cs_wire = self.U_6_114.cs_wire_1
        self.U_0_012.cs_wire = self.U_6_114.cs_wire_2
        self.U_0_013.cs_wire = self.U_6_114.cs_wire_3

        # Special register chip selects
        self.U_0_014.cs_wire = self.U_0_500.u14CS
        self.U_0_015.cs_wire = self.U_0_500.u15CS
        self.U_0_110.cs_wire = self.U_0_500.u110CS

        # Register inputs
        self.U_0_010.wire_1 = self.U_6_114.output_wire_0
        self.U_0_011.wire_1 = self.U_6_114.output_wire_1
        self.U_0_012.wire_1 = self.U_6_114.output_wire_2
        self.U_0_013.wire_1 = self.U_6_114.output_wire_3

        # Special register inputs
        self.U_0_014.wire_1 = self.U_2_117.output_wire
        self.U_0_015.wire_1 = self.U_3_115.output_wire
        self.U_0_110.wire_1 = self.U_4_120.output_wire

        # Hook up memory into the ALU MUX B
        self.U_1_113.wire_6 = self.U_4_100.value_output
        self.U_0_500.ram = self.U_4_100.chip[0]


        return

    def __init__(self):

        # Array of registers
        self.register_chip_list = []

        # Array of stage one chips
        self.stage_1_chip_list = []

        # Array of stage two chips
        self.stage_2_chip_list = []

        # Array of stage three chips
        self.stage_3_chip_list = []

        # Array of stage four chips
        self.stage_4_chip_list = []

        # Array of stage five chips
        self.stage_5_chip_list = []

        # Array of stage six chips
        self.stage_6_chip_list = []

        self.stk_wire.set_value(2)   # Stack grows or shrinks by 2 every time
        self.clock_wire.set_value(0) # Clock starts low

        self.construct_register_chips()

        self.construct_stage_1_chips()

        self.construct_stage_2_chips()

        self.construct_stage_3_chips()

        self.construct_stage_4_chips()

        self.construct_stage_5_chips()

        self.construct_stage_6_chips()

        self.final_stage()

        scanner = Scanner("Logical.txt")

        scanner.fetchInstructions()

        scanner.writeEPROM(self.U_4_100.chip[0])

        i = 0

        while i < 7:
            i += 1
            # LOW CLOCK
            self.clock_wire.set_value(0)
            self.U_0_500.Action(self.U_4_100.chip[0])
            for chip in self.register_chip_list:
                chip.Action()
            for chip in self.stage_1_chip_list:
                chip.Action()
            for chip in self.stage_2_chip_list:
                chip.Action()
            for chip in self.stage_3_chip_list:
                chip.Action()
            for chip in self.stage_4_chip_list:
                chip.Action()
            for chip in self.stage_5_chip_list:
                chip.Action()
            for chip in self.stage_6_chip_list:
                chip.Action()

            # HIGH CLOCK
            self.clock_wire.set_value(1)
            for chip in self.register_chip_list:
                chip.Action()
            for chip in self.stage_1_chip_list:
                chip.Action()
            for chip in self.stage_2_chip_list:
                chip.Action()
            for chip in self.stage_3_chip_list:
                chip.Action()
            for chip in self.stage_4_chip_list:
                chip.Action()
            for chip in self.stage_5_chip_list:
                chip.Action()
            for chip in self.stage_6_chip_list:
                chip.Action()

MainSystem()