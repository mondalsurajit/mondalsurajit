def recur1(n):
    if n>=1:
       print(n,end=" ")
       recur1(n-1)
       return
x=int(input("Enter a number"))
recur1(x)
