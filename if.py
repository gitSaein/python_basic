print(ord('p'))
print(ord('P'))
c1 = ([1, 2] == [1, 2])
print(c1)
c2 = True and False
print(c2)
c3 = not True
print(c3)
money = 5
if money > 9:
    print('A')
elif money > 6:
    print('B')
elif money > 4:
    print('C')
else:
    print('F')

is_true_live = True
while is_true_live:
    print("me")
    break

wweight = 70
while wweight < 90:
    print(wweight)
    wweight += 10
for n in range(20):
    if '3' in str(n):
        print('!')
    elif '6' in str(n):
        print('?')
    elif '9' in str(n):
        print('+')
    else:
        print(n)
print('------------------')
for n in range(20):
    if '3' in str(n) or '6' in str(n) or '9' in str(n):
        print('!')
    else:
        print(n)
