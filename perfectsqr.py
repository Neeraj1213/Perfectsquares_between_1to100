import math

def perfectornot(x):
    s= int(math.sqrt(x))
    return (s*s==x)

for n in range (1,100):
    if perfectornot(n)== True:
        print(n, "is a perfect square.")
