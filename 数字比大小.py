def get_max(a, b):
    if a>=b:
        return a
    else:
        return b
a=int(input("请输入数字a："))
b=int(input("请输入数字b："))
print(get_max(a,b))