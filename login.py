from typing import TextIO


def account_login():
    password = input('请输入密码：')
    if password == '12345':
        print("登陆成功！")
    else:
        print("账户和密码不符！")
        account_login()


account_login()


def forString(msgs):
    for msg in msgs:
        print(msg)


forString(input('请输入字符串'))

for x in range(1, 10):
    for y in range(1, 10):
        print('{0} * {1} = {2}'.format(x, y, x * y))

print('------------------------------------------------')
i = 1
while i < 10:
    j = 1
    while j < 10:
        print('{0} * {1} == {2}'.format(i, j, i * j))
        j = j + 1;
    i = i + 1;

for i in range(1, 11):
    file = open(f'{i}.txt', 'w')
    file.writelines(str(i))
    print(file.name)


def invest(amount, rate, time):
    for t in range(1, time + 1):
        newAmount = amount + amount * rate;
        print(f'year{t}:${newAmount}')
        amount = newAmount;


invest(100, 0.05, 9);

for i in range(1,101):
    if i%2 == 0:
        print(str(i))
