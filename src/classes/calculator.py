class FourCal:
    def __init__(self):
        self.first_num = 0
        self.second_num = 0

    def set_data(self, first, second):
        self.first_num = first
        self.second_num = second

    def add(self):
        result = self.first_num + self.second_num
        return result


cal = FourCal()
cal.set_data(1, 2)
print("add {}: {}".format(id(cal.second_num), cal.add()))
