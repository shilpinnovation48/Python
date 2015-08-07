a=eval(input("a:"))
b=eval(input("b:"))
c=eval(input("c:"))
d=eval(input("d:"))

if a>1 and a<14:
    ad=a+b+c+d
    print("aa",ad)
    if a==13:
        print("invalid")
elif a>15:
    ss = a-b-c-d
    print("ss",ss)
else:
    dd =(a+b)/(c+d)
    print("dd",dd)
