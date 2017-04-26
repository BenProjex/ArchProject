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


class XORChip(Chip):

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
        self.output_wire.set_value((self.wire_1.get_value() ^ self.wire_2.get_value()))

    def name(self):
        print(self.chip_id)


class ANDChip(Chip):
    in_wire_1= Wire()
    in_wire_2= Wire()
    chip_id= ""
    out_wire= Wire()

    def __init__(self, wire_1, wire_2, chip_id):
        self.in_wire_1=wire_1
        self.in_wire_2=wire_2
        self.chip_id
        self.out_wire= Wire(chip_id+"_out_wire")

    def Action(self):
        val_1 = self.in_wire_1.get_value()
        val_2 = self.in_wire_2.get_value()
        self.out_wire.set_value(val_1 & val_2)

    def name(self):
        print("Chip ID: "+self.chip_id)


class NOTChip(Chip):

    wire_1 = Wire()
    chip_id = ""
    output_wire = Wire()

    def __init__(self, wire_1, chip_id):
        self.wire_1 = wire_1
        self.chip_id = chip_id
        self.output_wire = Wire(self.chip_id + "_OUT_WIRE")

    def Action(self):
        self.output_wire.set_value(~ self.wire_1.get_value())

    def name(self):
        print(self.chip_id)


class ORChip(Chip):

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
        self.output_wire.set_value((self.wire_1.get_value() | self.wire_2.get_value()))

    def name(self):
        print(self.chip_id)

