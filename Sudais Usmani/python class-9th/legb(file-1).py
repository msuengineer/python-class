import math
x=100 #global
def outer():
    x=90 #enclosed
    def inner():
        x=80 #local
        print(x)
        print(math.pi)
        print(math.cos(8))
        print(math.sin(8))
        print(math.tan(8))
    inner()

"------------------------------------------------------------------------------------------------"
def h():
    global x
    x+=1
    print(x)
    x=5
    h()
    print(x)
"------------------------------------------------------------------------------------------------"

"------------------------------------------------------------------------------------------------"

"------------------------------------------------------------------------------------------------"

"------------------------------------------------------------------------------------------------"

"------------------------------------------------------------------------------------------------"
