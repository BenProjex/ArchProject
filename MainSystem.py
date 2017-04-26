class MainSystem:

    # Array of registers

    # Array of stage one chips

    # Array of stage two chips

    # Array of stage three chips

    # Array of stage four chips

    @classmethod
    def construct_register_chips(self):

        # Type: Register
        # ID: U_0_010
        # Name: Register_0
        # Input: TBD
        # Control: {  }
        # Output: W_0_010_0

        # Type: Register
        # ID: U_0_011
        # Name: Register_1
        # Input: TBD
        # Control: {  }
        # Output: W_0_011_0

        # Type: Register
        # ID: U_0_012
        # Name: Register_2
        # Input: TBD
        # Control: {  }
        # Output: W_0_012_0

        #Type: Register
        # ID: U_0_013
        # Name: Register_3
        # Input: TBD
        # Control: {  }
        # Output:  { W_0_013_0 }

        # Type: Register
        # ID: U_0_014
        # Name: Stack_Pointer
        # Input:   { W_2_117_0 }
        # Control: {  }
        # Output:  { W_0_014_0 }

        # Type: Register
        # ID: U_0_015
        # Name: Instruction_Pointer
        # Input:
        # Control: {  }
        # Output:  { W_0_015_0 }

        # Type: Register
        # ID: U_0_500
        # Name: Instruction_Register_Decoder
        # Input:   { MEM_1_4 }
        # Control: {  }
        # Output:  { W_0_500_0, W_0_500_1, W_0_500_2, CONTROL } // W_0_500_2 is INSTR

        # Type: Register
        # ID: U_0_110
        # Name: Flags_Register
        # Inputs:  { W_2_100_0, W_2_100_1, W_2_100_2 }
        # Control: {  }
        # Outputs: { W_0_110_0 }

        return

    @classmethod
    def construct_stage_1_chips(self):

        # Type: Multiplexer
        # ID: U_1_112
        # Name: Select_Register_A_MUX
        # Inputs: { W_0_010_0, W_0_011_0, W_0_012_0, W_0_013_0, W_3_100_0, W_0_110_0, W_0_500_2 }
        # Control: { W_1_112_9 }
        # Outputs: { W_1_112_0 }

        # Type: Multiplexer
        # ID: U_1_113
        # Name: Select_Register_B_MUX
        # Inputs: { W_0_010_0, W_0_011_0, W_0_012_0, W_0_013_0, W_3_100_0, W_0_110_0, W_0_500_2 }
        # Control: { W_1_113_9 }
        # Outputs: { W_1_113_0 } // This and W_1_112_0 make up the DATA line

        # Type: Adder / Subtractor
        # ID: U_1_107
        # Name: Stack_Adder_Subtractor
        # Inputs: { W_0_014_0, (LITERAL VALUE 2) }
        # Control: { W_1_107_9 }
        # Outputs: { W_1_107_0 }

        # Type: Adder
        # ID: U_1_105
        # Name: Instruction_Length_Adder
        # Inputs:  { W_0_500_0, W_0_015_0 }
        # Control: {  }
        # Outputs: { W_1_105_0 }

        return

    @classmethod
    def construct_stage_2_chips(self):


        # Type: Adder-Subtractor
        # ID: U_2_100
        # Name: ALU_Adder_Subtractor
        # Inputs:  { W_1_112_0, W_1_113_0 }
        # Control: { U_2_100_9 }
        # Outputs: { W_2_100_0, W_2_100_1 }

        # Type: AND
        # ID: U_2_101
        # Name: ALU_AND
        # Inputs:  { W_1_112_0, W_1_113_0 }
        # Control: {  }
        # Outputs: { W_2_101_0 }

        # Type: OR
        # ID: U_2_102
        # Name: ALU_OR
        # Inputs:  { W_1_112_0, W_1_113_0 }
        # Control: {  }
        # Outputs: { W_2_102_0 }

        # Type: XOR
        # ID: U_2_103
        # Name: ALU_OR
        # Inputs:  { W_1_112_0, W_1_113_0}
        # Control: {  }
        # Outputs: { W_2_103_0 }

        # Type: NOT
        # ID: U_2_104
        # Name: ALU_NOT
        # Inputs:  { W_1_113_0 }
        # Control: {  }
        # Outputs: { W_2_104_0 }

        # Type: Adder
        # ID: U_2_106
        # Name: Instruction_Offset_Adder
        # Inputs:  { W_1_105_0, W_0_500_1 }
        # Control: {  }
        # Outputs: { W_2_106_0 }

        # Type: Multiplexer
        # ID: U_2_116
        # Name: Memory_Addr_MUX
        # Inputs:  { W_0_015_0, W_0_014_0, W_0_500_2, DATA }
        # Control: { W_2_116_9 }
        # Outputs: { W_2_116_0 }  // MEM ADDR LINE

        # Type: Multiplexer
        # ID: U_2_117
        # Name: Stack_Ptr_MUX
        # Inputs:  { W_1_107_0, DATA }
        # Control: { W_2_117_9 }
        # Outputs: { W_2_117_0 }  AT THIS POINT WE CAN PROVIDE INPUT TO STK POINTER

        return

    @classmethod
    def construct_stage_3_chips(self):

        # Type: Multiplexer
        # ID: U_3_111
        # Name: Select_ALU_MUX
        # Inputs:  { W_2_100_0, W_2_101_0, W_2_102_0, W_2_103_0, W_2_104_0 }
        # Control: { W_3_111_9 }
        # Outputs: { W_3_111_0 } // This is the ALU line

        # Type: Multiplexer
        # ID: U_3_115
        # Name: Select_ALU_MUX
        # Inputs:  { DATA, W_3_500_2, W_1_105_0, W_2_106_0 }
        # Control: { W_3_115_9 }
        # Outputs: { W_3_115_0 } // INPUT FOR U_015

        return

    @classmethod
    def construct_stage_4_chips(self):

        # Type: Multiplexer
        # ID: U_3_119
        # Name: Select_MEM_MUX
        # Inputs:  { W_3_111_0, W_1_112_0, W_0_500_2 } // Fill these out later
        # Control: { W_3_115_9 }
        # Outputs: { W_3_119_0 } input to RAM

        # Type: RAM
        # ID: U_4_100
        # Name: RAM_Chip                    // This and the Select_MEM_MUX are technically different stages but we treat them the same
        # Inputs:  { W_2_116_0, W_3_119_0 }
        # Control: { W_4_100_9 }            // Read/Write
        # Outputs: { W_3_100_0 }            // This is the MEM line

        # Type: Multiplexer
        # ID: U_4_120
        # Name: Select_FLAGS_MUX
        # Inputs:  { W_2_100_1, W_3_111_0 }
        # Control: { W_4_111_9 }
        # Outputs: { W_4_120_0 }

        return

    @classmethod
    def construct_stage_5_chips(self):

        # Type: Multiplexer
        # ID: U_4_118A
        # Name: Select_Register_A_Input_MUX
        # Inputs:  { W_1_112_0, W_0_014_0, W_0_500_2, W_3_111_0, RES, W_3_100_0, RES, RES }
        # Control: { W_4_118A_9, W_0_014_1 }
        # Outputs: { W_4_118A_0 }

        # Type: Multiplexer
        # ID: U_4_118B
        # Name: Select_Register_B_Input_MUX
        # Inputs:  { W_1_113_0, W_0_014_0, W_0_500_2, W_3_111_0, RES, W_3_100_0, RES, RES }
        # Control: { W_4_118B_9 }
        # Outputs: { W_4_118B_0 }

        return

    @classmethod
    def construct_stage_6_chips(self):

        # Type: Demultiplexer
        # ID: U_4_114A
        # Name: Select_Register_A_Input_MUX
        # Inputs:  { W_5_118A_0 }
        # Control: { W_6_114A_9, OE_A }
        # Outputs: { W_6_114A_0 } // These outputs go into the registers

        # Type: Demultiplexer
        # ID: U_4_114B
        # Name: Select_Register_B_Input_MUX
        # Inputs:  { W_5_118B_0 }
        # Control: { W_6_114B_9, OE_B }
        # Outputs: { W_6_114B_0 } // These outputs go into the registers

        return

    @classmethod
    def final_stage(self):

        # Hook up all register inputs


        return

    def __init__(self):

        self.construct_register_chips()

        self.construct_stage_1_chips()

        self.construct_stage_2_chips()

        self.construct_stage_3_chips()

        self.construct_stage_4_chips()

        self.construct_stage_5_chips()

        self.construct_stage_6_chips()

        self.final_stage()