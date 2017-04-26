from abc import ABCMeta, abstractmethod, abstractproperty
import Wire


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

###############################################################
#
###############################################################


class REGISTERChip(Chip):

    def __init__(self, wire_1, cs_wire, clock_wire, chip_id):
        self.wire_1 = wire_1
        self.cs_wire = cs_wire
        self.clock_wire= clock_wire
        self.output_wire = Wire.Wire(self.chip_id + "_OUT_WIRE")
        self.chip_id = chip_id

    def Action(self):
        self.output_wire.set_value()

    def name(self):
        print(self.chip_id)

###############################################################
#
###############################################################


class XORChip(Chip):

    def __init__(self, wire_1, wire_2, chip_id):
        self.wire_1 = wire_1
        self.wire_2 = wire_2
        self.output_wire = Wire.Wire(self.chip_id + "_OUT_WIRE")
        self.chip_id = chip_id

    def Action(self):
        self.output_wire.set_value((self.wire_1.get_value() ^ self.wire_2.get_value()))

    def name(self):
        print(self.chip_id)

###############################################################
#
###############################################################


class ANDChip(Chip):

    def __init__(self, wire_1, wire_2, chip_id):
        self.in_wire_1=wire_1
        self.in_wire_2=wire_2
        self.out_wire= Wire.Wire(chip_id+"_out_wire")
        self.chip_id = chip_id

    def Action(self):
        val_1 = self.in_wire_1.get_value()
        val_2 = self.in_wire_2.get_value()
        self.out_wire.set_value(val_1 & val_2)

    def name(self):
        print("Chip ID: "+self.chip_id)

###############################################################
#
###############################################################


class NOTChip(Chip):

    def __init__(self, wire_1, chip_id):
        self.wire_1 = wire_1
        self.output_wire = Wire.Wire(self.chip_id + "_OUT_WIRE")
        self.chip_id = chip_id

    def Action(self):
        self.output_wire.set_value(~ self.wire_1.get_value())

    def name(self):
        print(self.chip_id)

###############################################################
#
###############################################################


class ORChip(Chip):

    def __init__(self, wire_1, wire_2, chip_id):
        self.wire_1 = wire_1
        self.wire_2 = wire_2
        self.output_wire = Wire.Wire(self.chip_id + "_OUT_WIRE")
        self.chip_id = chip_id

    def Action(self):
        self.output_wire.set_value((self.wire_1.get_value() | self.wire_2.get_value()))

    def name(self):
        print(self.chip_id)

###############################################################
#
###############################################################


class MUX2to1Chip(Chip):

    def __init__(self, wire_1, wire_2, select_wire_1, chip_id):
        self.wire_1 = wire_1
        self.wire_2 = wire_2
        self.select = select_wire_1.get_value()
        self.output_wire = Wire.Wire(self.chip_id + "_OUT_WIRE")
        self.chip_id = chip_id

    def Action(self):
        self.output_wire.set_value()
        if self.select == 0:
            self.output_wire.set_value(self.wire_1.get_value())
        else:
            self.output_wire.set_value(self.wire_2.get_value())

    def name(self):
        print(self.chip_id)

###############################################################
#
###############################################################


class MUX4to1Chip(Chip):

    def __init__(self, wire_1, wire_2, wire_3, wire_4, select_wire_1, chip_id):
        self.wire_1 = wire_1
        self.wire_2 = wire_2
        self.wire_3 = wire_3
        self.wire_4 = wire_4
        self.select = select_wire_1.get_value()
        self.output_wire = Wire.Wire(self.chip_id + "_OUT_WIRE")
        self.chip_id = chip_id

    def Action(self):
        if self.select == 0:
            self.output_wire.set_value(self.wire_1.get_value())
        elif self.select == 1:
            self.output_wire.set_value(self.wire_2.get_value())
        elif self.select == 2:
            self.output_wire.set_value(self.wire_3.get_value())
        else:
            self.output_wire.set_value(self.wire_4.get_value())

    def name(self):
        print(self.chip_id)

###############################################################
#
###############################################################


class MUX8to1Chip(Chip):

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

    def name(self):
        print(self.chip_id)

###############################################################
#DEMUX2to4 Chip accepts 2 input wires, 2 enable wires, 2 Select Wires, and has 4 output wires that correspond to Registers 0-4
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


    def name(self):
        print(self.chip_id)

###############################################################
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

    def name(self):
        print(self.chip_id)
        
###############################################################
#
###############################################################


class DECODERChip(Chip):

    def __init__(self, wire_1, wire_2, chip_id):
        self.wire_1 = wire_1
        self.wire_2 = wire_2
        self.chip_id = chip_id
        self.output_wire = Wire.Wire(self.chip_id + "_OUT_WIRE")

    def Action(self):
        self.output_wire.set_value()

    def name(self):
        print(self.chip_id)

###############################################################
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

    def name(self):
        print(self.chip_id)


