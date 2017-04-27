from abc import ABCMeta, abstractmethod, abstractproperty
import Wire

###############################################################
#                  Abstract Chip Class
#AbstractMethod Action: What function the chip performs
#AbstractProperty Name: Debugging tool retrieving the name of the chip
###############################################################

class Chip:

    __metaclass__ = ABCMeta

    @abstractmethod
    def Action(self): pass

    @property
    @abstractmethod
    def name(self):
        # Name property will be provided by the inheriting class
        # This will mostly be used for debugging
        pass

#####################REGISTERChip##############################
#Input: 1 Input wire, 1 Chip Select Wire, 1 Clock Wire
#
#Function:
###############################################################

class REGISTERChip(Chip):

    def __init__(self, wire_1, cs_wire, clock_wire, chip_id):
        self.wire_1 = wire_1
        self.cs_wire = cs_wire
        self.clock_wire= clock_wire
        self.output_wire = Wire.Wire(self.chip_id + "_OUT_WIRE")
        self.chip_id = chip_id
        self.register_value=None

    #At the moment, Registers simply set their input to their output
    def Action(self):
        if self.cs_wire.get_value()==0: #If the chip is not selected, do nothing
            return
        if self.clock_wire.get_value() == 1: #If the chip is selected and the clock is high, update value from input and update output
            self.register_value=self.wire_1.get_value()
            self.output_wire.set_value(self.register_value)
        else:                                #Regardless of the chip being selected, if the clock is low, do nothing.
            return
    def name(self):
        print(self.chip_id)

    def get_value(self):
        return self.register_value
##########################XORChip##############################
#  Inputs: two input wires and a chip id
#
#  Function: XORs the values of the two wires and
#  sets the value of the output wire to
#  to that value.
###############################################################

class XORChip(Chip):

    #sets the values of the wires to the input and names the output wire

    def __init__(self, wire_1, wire_2, chip_id):
        self.wire_1 = wire_1
        self.wire_2 = wire_2
        self.output_wire = Wire.Wire(self.chip_id + "_OUT_WIRE")
        self.chip_id = chip_id

    #xors values using '^' and sets output wires value
    def Action(self):
        self.output_wire.set_value((self.wire_1.get_value() ^ self.wire_2.get_value()))

    #prints the name of the chip id for testing
    def name(self):
        print(self.chip_id)

###########################ANDChip#############################
#  Inputs: two input wires and a chip id
#
#  Function: ANDs the values of the two wires and
#  sets the value of the output wire to
#  to that value.
###############################################################

class ANDChip(Chip):

    # sets the values of the wires to the input and names the output wire

    def __init__(self, wire_1, wire_2, chip_id):
        self.in_wire_1=wire_1
        self.in_wire_2=wire_2
        self.out_wire= Wire.Wire(chip_id+"_out_wire")
        self.chip_id = chip_id

    # ands values using '&' and sets output wires value
    def Action(self):
        val_1 = self.in_wire_1.get_value()
        val_2 = self.in_wire_2.get_value()
        self.out_wire.set_value(val_1 & val_2)

    # prints the name of the chip id for testing
    def name(self):
        print("Chip ID: "+self.chip_id)

#########################NOTChip###############################
#  Inputs: one input wires and a chip id
#
#  Function: NOTs the value of the wire and
#  sets the value of the output wire to
#  to that value.
###############################################################

class NOTChip(Chip):

    # sets the values of the wires to the input and names the output wire

    def __init__(self, wire_1, chip_id):
        self.wire_1 = wire_1
        self.output_wire = Wire.Wire(self.chip_id + "_OUT_WIRE")
        self.chip_id = chip_id

    # nots value using '~' and sets output wires value
    def Action(self):
        if self.wire_1.get_value()==0:
            self.output_wire.set_value(255)
        else:
            self.output_wire.set_value(~ self.wire_1.get_value())

    # prints the name of the chip id for testing
    def name(self):
        print(self.chip_id)

##########################ORChip###############################
#  Inputs: two input wires and a chip id
#
#  Function: ORs the values of the two wires and
#  sets the value of the output wire to
#  to that value.
###############################################################

class ORChip(Chip):


    # sets the values of the wires to the input and names the output wire

    def __init__(self, wire_1, wire_2, chip_id):
        self.wire_1 = wire_1
        self.wire_2 = wire_2
        self.output_wire = Wire.Wire(self.chip_id + "_OUT_WIRE")
        self.chip_id = chip_id

    # ors values using '|' and sets output wires value
    def Action(self):
        self.output_wire.set_value((self.wire_1.get_value() | self.wire_2.get_value()))

    # prints the name of the chip id for testing
    def name(self):
        print(self.chip_id)

#####################MUX2to1Chip###############################
#  Inputs: two input wires, select wire and a chip id
#
#  Function: set the value of the output wire to the
#  correct input wire determined by the select wire
###############################################################

class MUX2to1Chip(Chip):

    # sets the values of the wires to the input and names the output wire


    def __init__(self, wire_1, wire_2, select_wire_1, chip_id):
        self.wire_1 = wire_1
        self.wire_2 = wire_2
        self.select = select_wire_1.get_value()
        self.output_wire = Wire.Wire(self.chip_id + "_OUT_WIRE")
        self.chip_id = chip_id

    # use the select variable to determine the output value from the input wires
    def Action(self):
        if self.select == 0:
            self.output_wire.set_value(self.wire_1.get_value())
        else:
            self.output_wire.set_value(self.wire_2.get_value())

    # prints the name of the chip id for testing
    def name(self):
        print(self.chip_id)

###################MUX4to1Chip##################################
#  Inputs: four input wires, select wire and a chip id
#
#  Function: set the value of the output wire to the
#  correct input wire determined by the select wire
###############################################################

class MUX4to1Chip(Chip):


    # sets the values of the wires to the input and names the output wire

    def __init__(self, wire_1, wire_2, wire_3, wire_4, select_wire_1, chip_id):
        self.wire_1 = wire_1
        self.wire_2 = wire_2
        self.wire_3 = wire_3
        self.wire_4 = wire_4
        self.select = select_wire_1.get_value()
        self.output_wire = Wire.Wire(self.chip_id + "_OUT_WIRE")
        self.chip_id = chip_id

    # use the select variable to determine the output value from the input wires
    def Action(self):
        if self.select == 0:
            self.output_wire.set_value(self.wire_1.get_value())
        elif self.select == 1:
            self.output_wire.set_value(self.wire_2.get_value())
        elif self.select == 2:
            self.output_wire.set_value(self.wire_3.get_value())
        else:
            self.output_wire.set_value(self.wire_4.get_value())

    # prints the name of the chip id for testing
    def name(self):
        print(self.chip_id)

###########################MUX8to1Chip#########################
#  Inputs: eight input wires, select wire and a chip id
#
#  Function: set the value of the output wire to the
#  correct input wire determined by the select wire
###############################################################

class MUX8to1Chip(Chip):

    # sets the values of the wires to the input and names the output wire
    def __init__(self, wire_1, wire_2, wire_3, wire_4, wire_5, wire_6, wire_7, wire_8, select_wire_1, chip_id):
        self.wire_1 = wire_1
        self.wire_2 = wire_2
        self.wire_3 = wire_3
        self.wire_4 = wire_4
        self.wire_5 = wire_5
        self.wire_6 = wire_6
        self.wire_7 = wire_7
        self.wire_8 = wire_8
        self.select = select_wire_1.get_value()
        self.output_wire = Wire.Wire(self.chip_id + "_OUT_WIRE")
        self.chip_id = chip_id


    # use the select variable to determine the output value from the input wires
    def Action(self):
        if self.select == 0:
            self.output_wire.set_value(self.wire_1.get_value())
        elif self.select == 1:
            self.output_wire.set_value(self.wire_2.get_value())
        elif self.select == 2:
            self.output_wire.set_value(self.wire_3.get_value())
        elif self.select == 3:
            self.output_wire.set_value(self.wire_4.get_value())
        elif self.select == 4:
            self.output_wire.set_value(self.wire_5.get_value())
        elif self.select == 5:
            self.output_wire.set_value(self.wire_6.get_value())
        elif self.select == 6:
            self.output_wire.set_value(self.wire_7.get_value())
        else:
            self.output_wire.set_value(self.wire_8.get_value())

    # prints the name of the chip id for testing
    def name(self):
        print(self.chip_id)

##########################DEMUX2to4Chip#########################
#Inputs: 2 input wires, 2 enable wires, 2 Select wires

#Function: Sets input wire's value to output wires value based on Select wires.
#Assumptions: Select Wires must be a value between 0 and 3
#As it stands, Select_2 can be enabled when select_1 isnt, and it will work
#as intended. I dont think this is how it works in Ortiz's system but it shouldnt cause any problems
#Since we are using short's and not bits, it is possible for the two select wires
#to choose the same register, this will error out if attempted.
###############################################################

class DEMUX2to4Chip(Chip):

    def __init__(self, wire_1, wire_2, enable_wire_1, enable_wire_2, select_wire_1, select_wire_2, chip_id):
        self.wire_1 = wire_1
        self.wire_2 = wire_2
        self.enable_wire_1 = enable_wire_1
        self.enable_wire_2 = enable_wire_2
        self.select_wire_1 = select_wire_1  #Select wires should be a number from 0 to 3, representing the 4 register options
        self.select_wire_2 = select_wire_2
        self.output_wire_0 = Wire.Wire(self.chip_id + "_OUT_WIRE_0")
        self.output_wire_1 = Wire.Wire(self.chip_id + "_OUT_WIRE_1")
        self.output_wire_2 = Wire.Wire(self.chip_id + "_OUT_WIRE_2")
        self.output_wire_3 = Wire.Wire(self.chip_id + "_OUT_WIRE_3")
        self.chip_id = chip_id

    #DEMUX2to4's action determines which input to read from based on the enable wires, then send the input to the corresponding
    #register.
    #Example: A demux with enable_wire_1 ON and enable_wire_2 ON will read from selects 1 and 2. Selects 1 and 2 should be selecting different
    #registers otherwise it will error out. Assuming Selects 1 and 2 are different registers between 0 and 3, inputs 1 and 2 are passed to the
    #respective registers
    def Action(self):
        if self.enable_wire_1.get_value() == 0 and self.enable_wire_2.get_value() == 0 :
            print("No Demux Action, both enable wires disabled")

        #If only enable wire 1 is enabled, pass the values to register 0-3 based on the select wire 1
        elif self.enable_wire_1.get_value() == 1 and self.enable_wire_2.get_value() == 0 :
            select= self.select_wire_1.get_value()
            if select == 0 :
                self.output_wire_0.set_value(self.wire_1.get_value())
            elif select == 1 :
                self.output_wire_1.set_value(self.wire_1.get_value())
            elif select == 2:
                self.output_wire_2.set_value(self.wire_1.get_value())
            elif select == 3:
                self.output_wire_3.set_value(self.wire_1.get_value())
            else:
                print("Error, select wire must hold a value between 0 and 3")
                return
        # I dont believe there should be a situation where sel_1 is off and sel_2 is on, but just in case
        #it will be supported, needs to be discussed.
        elif self.enable_wire_1.get_value() == 0 and self.enable_wire_2.get_value() == 1:
            select = self.select_wire_1.get_value()
            if select == 0:
                self.output_wire_0.set_value(self.wire_2.get_value())
            elif select == 1:
                self.output_wire_1.set_value(self.wire_2.get_value())
            elif select == 2:
                self.output_wire_2.set_value(self.wire_2.get_value())
            elif select == 3:
                self.output_wire_3.set_value(self.wire_2.get_value())
            else:
                print("Error, select wire must hold a value between 0 and 3")
                return
        #
        elif self.enable_wire_1.get_value() == 1 and self.enable_wire_2.get_value() == 1:
            select_1 = self.select_wire_1.get_value()
            select_2 = self.select_wire_2.get_value()
            if select_1 == select_2:
                print("Error in DEMUX, both select wires have selected the same register")
                return

            #Pass input 1 to the register chosen by select 1
            if select_1 == 0:
                self.output_wire_0.set_value(self.wire_1.get_value())
            elif select_1 == 1:
                self.output_wire_1.set_value(self.wire_1.get_value())
            elif select_1 == 2:
                self.output_wire_2.set_value(self.wire_1.get_value())
            elif select_1== 3:
                self.output_wire_3.set_value(self.wire_1.get_value())
            else:
                print("Error, select wire must hold a value between 0 and 3")
                return

            # Pass input 2 to the register chosen by select 2
            if select_2 == 0:
                self.output_wire_0.set_value(self.wire_2.get_value())
            elif select_2 == 1:
                self.output_wire_1.set_value(self.wire_2.get_value())
            elif select_2 == 2:
                self.output_wire_2.set_value(self.wire_2.get_value())
            elif select_2 == 3:
                self.output_wire_3.set_value(self.wire_2.get_value())
            else:
                print("Error, select wire must hold a value between 0 and 3")
                return


    # prints the name of the chip id for testing
    def name(self):
        print(self.chip_id)

##########################ADDSUBChip############################
#
###############################################################

class ADDSUBChip(Chip):

    def __init__(self, wire_1, wire_2, cin_wire_1, chip_id):
        self.wire_1 = wire_1
        self.wire_2 = wire_2
        self.cin_wire_1=cin_wire_1
        self.v_output_wire = Wire.Wire(self.chip_id + "_V_OUT_WIRE")
        self.c_output_wire = Wire.Wire(self.chip_id + "_C_OUT_WIRE")
        self.chip_id = chip_id

    def Action(self):
        self.v_output_wire.set_value()

    # prints the name of the chip id for testing
    def name(self):
        print(self.chip_id)


###########################FLAGSChip###########################
#
###############################################################

class FLAGSChip(Chip):

    def __init__(self, wire_1, cs_wire, clock_wire,  chip_id):
        self.wire_1 = wire_1
        self.cs_wire=cs_wire
        self.clock_wire=clock_wire
        self.z_output_wire = Wire.Wire(self.chip_id + "_Z_OUT_WIRE")
        self.v_output_wire = Wire.Wire(self.chip_id + "_V_OUT_WIRE")
        self.n_output_wire = Wire.Wire(self.chip_id + "_N_OUT_WIRE")
        self.c_output_wire = Wire.Wire(self.chip_id + "_C_OUT_WIRE")
        self.chip_id = chip_id

    def Action(self):
        self.z_output_wire.set_value()

    # prints the name of the chip id for testing
    def name(self):
        print(self.chip_id)


