def recur1(n):
    if n>=1:
       recur1(n-1)
       print(n,end=" ")
       return
x=int(input("Enter a number"))
recur1(x)
