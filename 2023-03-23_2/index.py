import random
import string

persons = ["吉总", "胡总", "张三", "李四", "王二"]

num = 0
while True:
    if (num >=3):
        break
    name = input("请输入一个名字")
    if (name == 'q'):
        break
    if (name in persons):
        str = random.choices(string.digits, k=4)
        print(name, "".join(str))
    else:
        print("对不起，您输入的名字不存在")
    num += 1
