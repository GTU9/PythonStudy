def add(n1,n2):
    return n1+n2

def cal(cal_func,n1,n2):
    num=cal_func(n1,n2)
    return num

print(cal(add,1,2))