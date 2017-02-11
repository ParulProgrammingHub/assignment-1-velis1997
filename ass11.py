def compound(p,t,i):
    A=p(1+(i/100))**t
    return A
p=raw_input("please enter the principal amount")
p=float(p)
t=raw_input("please enter the time per year")
i=raw_input("please enter the interest in percantage")
i=float(i)
print compound(p,t,i)
