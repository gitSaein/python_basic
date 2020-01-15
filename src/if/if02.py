number = input("정수입력> ")

last_character = number[-1]

last_number = int(last_character)

if last_number == 0 \
   or last_number == 2 \
   or last_number == 4 \
   or last_number == 6 \
   or last_number == 8:
    print("{} 는 짝수입니다.".format(number))
if last_number == 1\
        or last_number == 3\
        or last_number == 5\
        or last_number == 7\
        or last_number == 9:
    print("{} 는 홀수입니다.".format(number))
else:
    print("없어욥.")
