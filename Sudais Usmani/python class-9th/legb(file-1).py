##import math
##x=100 #global
##def outer():
##    x=90 #enclosed
##    def inner():
##        x=80 #local
##        print(x)
##        print(math.pi)
##        print(math.cos(8))
##        print(math.sin(8))
##        print(math.tan(8))
##    inner()

"------------------------------------------------------------------------------------------------"
##def h():
##    global x
##    x+=1
##    print(x)
##    x=5
##    h()
##    print(x)
"------------------------------------------------------------------------------------------------"

##def g(x): #step3
##    x=5   #step4
##a=3       #step1
##g(a)      #step2
##print(a)  #step5
"------------------------------------------------------------------------------------------------"
def lst_input():
    my_str=input('Enter integer values separated by commas:')
    my_str=my_str.split(',')
    int_lst=[]
    for i in my_str:
        int_lst.append(int(i))
    return int_lst
print('Tou entered:',lst_input,())
"------------------------------------------------------------------------------------------------"

"------------------------------------------------------------------------------------------------"

"------------------------------------------------------------------------------------------------"
