

def primo():
    n=0
    while True:
        n=n+1
        c=0
        for d in range(2,n):
            if n%d==0:
                c=c+1
        if c==0:
            c=c+1
        if c==0:
            print (n)    
        