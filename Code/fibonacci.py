def F(n):
    a=0
    b=1
    if n<0:
        return "Invalid Input"
    elif n==0:
        return a
    elif n==1:
        return b
    else:
        for i in range(2, n+1):
            c=a+b
            a=b
            b=c
        return b
    
print(F(0))
print(F(1))
print(F(-2))
print(F(10))