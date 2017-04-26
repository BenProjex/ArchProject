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

    wire_1 = Wire()
    cs_wire = Wire()
    clock_wire = Wire()
    output_wire = Wire()
    chip_id = ""

    def __init__(self, wire_1, cs_wire, clock_wire, chip_id):
        self.wire_1 = wire_1
        self.cs_wire = cs_wire
        self.clock_wire= clock_wire
        self.output_wire = Wire(self.chip_id + "_OUT_WIRE")
        self.chip_id = chip_id


    def Action(self):
        self.output_wire.set_value()

    def name(self):
        print(self.chip_id)

###############################################################
#
###############################################################


class XORChip(Chip):

    wire_1 = Wire()
    wire_2 = Wire()
    output_wire = Wire()
    chip_id = ""

    def __init__(self, wire_1, wire_2, chip_id):
        self.wire_1 = wire_1
        self.wire_2 = wire_2
        self.output_wire = Wire(self.chip_id + "_OUT_WIRE")
        self.chip_id = chip_id

    def Action(self):
        self.output_wire.set_value((self.wire_1.get_value() ^ self.wire_2.get_value()))

    def name(self):
        print(self.chip_id)

###############################################################
#
###############################################################


class ANDChip(Chip):

    in_wire_1= Wire()
    in_wire_2= Wire()
    out_wire= Wire()
    chip_id= ""

    def __init__(self, wire_1, wire_2, chip_id):
        self.in_wire_1=wire_1
        self.in_wire_2=wire_2
        self.out_wire= Wire(chip_id+"_out_wire")
        self.chip_id

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

    wire_1 = Wire()
    output_wire = Wire()
    chip_id = ""

    def __init__(self, wire_1, chip_id):
        self.wire_1 = wire_1
        self.output_wire = Wire(self.chip_id + "_OUT_WIRE")
        self.chip_id = chip_id

    def Action(self):
        self.output_wire.set_value(~ self.wire_1.get_value())

    def name(self):
        print(self.chip_id)

###############################################################
#
###############################################################


class ORChip(Chip):

    wire_1 = Wire()
    wire_2 = Wire()
    output_wire = Wire()
    chip_id = ""

    def __init__(self, wire_1, wire_2, chip_id):
        self.wire_1 = wire_1
        self.wire_2 = wire_2
        self.output_wire = Wire(self.chip_id + "_OUT_WIRE")
        self.chip_id = chip_id

    def Action(self):
        self.output_wire.set_value((self.wire_1.get_value() | self.wire_2.get_value()))

    def name(self):
        print(self.chip_id)

###############################################################
#
###############################################################


class MUXChip(Chip):

    wire_1 = Wire()
    wire_2 = Wire()
    chip_id = ""
    output_wire = Wire()

    def __init__(self, wire_1, wire_2, chip_id):
        self.wire_1 = wire_1
        self.wire_2 = wire_2
        self.chip_id = chip_id
        self.output_wire = Wire(self.chip_id + "_OUT_WIRE")

    def Action(self):
        self.output_wire.set_value()

    def name(self):
        print(self.chip_id)

###############################################################
#
###############################################################


class DEMUXChip(Chip):

    wire_1 = Wire()
    wire_2 = Wire()
    chip_id = ""
    output_wire = Wire()

    def __init__(self, wire_1, wire_2, chip_id):
        self.wire_1 = wire_1
        self.wire_2 = wire_2
        self.chip_id = chip_id
        self.output_wire = Wire(self.chip_id + "_OUT_WIRE")

    def Action(self):
        self.output_wire.set_value()

    def name(self):
        print(self.chip_id)

###############################################################
#
###############################################################


class ADDSUBChip(Chip):

    wire_1 = Wire()
    wire_2 = Wire()
    cin_wire_1=Wire()
    v_output_wire = Wire()
    c_output_wire = Wire()
    chip_id = ""

    def __init__(self, wire_1, wire_2, cin_wire_1, chip_id):
        self.wire_1 = wire_1
        self.wire_2 = wire_2
        self.cin_wire_1=cin_wire_1;
        self.v_output_wire = Wire(self.chip_id + "_V_OUT_WIRE")
        self.c_output_wire = Wire(self.chip_id + "_C_OUT_WIRE")
        self.chip_id = chip_id

    def Action(self):
        self.output_wire.set_value()

    def name(self):
        print(self.chip_id)
        
###############################################################
#
###############################################################


class DECODERChip(Chip):

    wire_1 = Wire()
    wire_2 = Wire()
    chip_id = ""
    output_wire = Wire()

    def __init__(self, wire_1, wire_2, chip_id):
        self.wire_1 = wire_1
        self.wire_2 = wire_2
        self.chip_id = chip_id
        self.output_wire = Wire(self.chip_id + "_OUT_WIRE")

    def Action(self):
        self.output_wire.set_value()

    def name(self):
        print(self.chip_id)

###############################################################
#
###############################################################


class FLAGSChip(Chip):

    wire_1 = Wire()
    cs_wire = Wire()
    clock_wire = Wire()
    z_output_wire = Wire()
    v_output_wire = Wire()
    n_output_wire = Wire()
    c_output_wire = Wire()
    chip_id = ""

    def __init__(self, wire_1, cs_wire, clock_wire,  chip_id):
        self.wire_1 = wire_1
        self.cs_wire=cs_wire
        self.clock_wire=clock_wire
        self.z_output_wire = Wire(self.chip_id + "_Z_OUT_WIRE")
        self.v_output_wire = Wire(self.chip_id + "_V_OUT_WIRE")
        self.n_output_wire = Wire(self.chip_id + "_N_OUT_WIRE")
        self.c_output_wire = Wire(self.chip_id + "_C_OUT_WIRE")
        self.chip_id = chip_id

    def Action(self):
        self.output_wire.set_value()

    def name(self):
        print(self.chip_id)


