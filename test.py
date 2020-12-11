num = input()

num={0:'零',1:'一',2:'二',3:'三',4:'四',5:'五',6:'六',7:'七',8:'八',9:'九',"+":"加","-":"減","*":"乘以","/":"除以"}
k = "十"


try :
    for i in num :
        if i in num :
            print(num[i], end = "")

except :
    print(0)
