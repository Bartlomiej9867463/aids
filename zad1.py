def numbers(n):
    print(n)
    n=n-1
    if n>=0:
        numbers(n)
def fibbonaci(n):
    if n<=1:
        return (n)
    return fibbonaci(n-1)+ fibbonaci(-2)
#numbers(4)
print(fibbonaci(9))
