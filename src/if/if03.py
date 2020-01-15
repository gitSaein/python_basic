number = input("정수입력 > ")
last_caracter = number[-1]

if last_caracter in '02468':
    print("{} 짝수입니다. ".format(number))
if last_caracter in '13579':
    print("{} 홀수입니다.".format(number))
