
class Wire:


    value = 0
    wire_id = ""

    def __init__(self, wire_id):
        self.wire_id = wire_id


    def set_value(self, value):
        self.value = value
        if value > 255 or value < 0:
            self.value = 0
            print("Wire overflow value: ", str(value))

    def get_value(self):
        return self.value

    def debug_print(self):
        print("Wire: ", str(self.wire_id), " Has value: ", str(self.value))