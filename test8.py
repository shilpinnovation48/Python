def con():
    s=eval(input("enter s:-"))
    f=eval(input("enter f:-"))
    if s>3 and s<15 :
        add=s+f
        print('Ans:',add)

    elif s<3:
        sub=f-s
        print('Ans',sub)
    else:
        mul=s*f
        print('Ans:',mul)
        
        
        
