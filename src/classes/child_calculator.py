from src.classes.calculator import FourCal


class MoreForCal(FourCal):
    def pow(self):
        result = self.first_num ** self.second_num
        return result


a = MoreForCal()
a.set_data(2, 2)
print("2의 2승 {}: {}".format(id(a.second_num), a.pow()))
