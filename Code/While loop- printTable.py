# function to calculate table in reverse order
def table(n):
    i=10
    while i>0:
        a=i*n
        i=i-1
        print(a, end=" ")

print(table(5))