inp=input('how many numbers do u want: ')
i=int(inp)
fib=[]
x=1

if i == 0:
    fib=[1]

elif i==1:
    fib=[1]

elif i==2:
    fib=[1,1]

elif i>2:
    fib=[1,1]
    while x<i-1:

        fib.append(fib[x]+fib[x-1])
        x=x+1


print(' fibonacci series with',i,'numbers is\n',fib)
