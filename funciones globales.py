def fun(x):
    global t
    t=2*x
    y=t+5
    return y

#programa que usa fun

x=3
r=fun(x)
print(r)
print(t)
