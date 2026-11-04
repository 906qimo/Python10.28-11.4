def tem(num):
    print("Hello World! 请出示你的健康码好72小时内核酸码")
    if num<=37.2:
        print(f"您的体温{num}正常，请进入")
    else:
        print(f"您的体温{num}异常，请离开")
num=float(input("请输入你的体温:"))
tem(num)