
#WAP to print below pattern:


def pattern(n):
    for i in range(n,0,-1):
        for j in range(0,i):
            print("*",end="")
        print("\t")
    for i in range(0, n):
        for j in range(0, i+1):
            print("*",end="")
        print("\t")
n=5
pattern(n)
    
