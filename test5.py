def triangel():
    n=10
    b=[]
    for i in range(n-1):                                                            
        col=n-1                                                              
        a=' '*col + '*'*i + '*'*i  
        b.append(a)
        print a
        
    b.pop()
    b.reverse()
     
    for ele in b:
        print ele
triangel()
