##def sum(a,b,c):
##    print("Addition of",a,b,c,"is","=",a+b+c)
##    print("Substraction of",a,b,c,"is","=",a-b-c)
##    print("Multiplication of",a,b,c,"is","=",a*b*c)
#sum(45,4,45)# this is posional argument
#sum(b=45,c=45,a=45)# this is key word argument
"------------------------------------------------------------------------------------------------"
##def arb(*arg):
##    print(arg)
##    for x in arg:
##        print(x)
"------------------------------------------------------------------------------------------------"
def arb(*arg):
    sum=0
    print(arg)
    for x in arg:
        print(x)
        sum+=x
    print("sum=",sum)    


"------------------------------------------------------------------------------------------------"
##
##a=str(input("What is your Name :"))
##print(a,"Welcome to the world of Sum")
##sum(int(a=input("Give value of a"),b=input("Give value of b"),c=input("Give value of c")))
