#funcion primo
def primo(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
        if c>2:
            return False
        else:
            return True