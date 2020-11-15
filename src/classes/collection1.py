#
# class
# 객체 지향: 변수와 함수를 묶어서 하나의 새로운 "객체(데이터) 타입"을 만드는 것.
#
class BusinessCard:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.address = ""

    def set_info(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        print("{} - {} - {}".format(name, email, address))


member1 = BusinessCard()

member1.set_info("saeinlee1", "saeinin@kakao.com", "address_saeinlee")
member1.set_info("saeinlee2", "saeinin@kakao.com", "address_saeinlee")
member1.set_info("saeinlee3", "saeinin@kakao.com", "address_saeinlee")
