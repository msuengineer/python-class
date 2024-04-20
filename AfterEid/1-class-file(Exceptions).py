##amount=int(input('Enter amount to be shared: '))
##sharers=int(input('Enter number of sharers: '))
##print('Each one will get Rs. ',amount/sharers)
##print('Have a blessed day')


##try:
##    amount=int(input('Enter amount to be shared: '))
##    sharers=int(input('Enter number of sharers: '))
##    print('Each one will get Rs. ',amount/sharers)
##except:
##    print('Enter inputs in digits!')
##    print('Have a blessed day')

##try:
##    amount=int(input('Enter amount to be shared: '))
##    sharers=int(input('Enter number of sharers: '))
##    print('Each one will get Rs. ',amount/sharers)
##except ValueError:
##    print('Enter inputs in digits!')
##except ZeroDivisionError:
##    print('Number of sharers must be >=1')
##    print('Have a blessed day')
##

try:
    amount=int(input('Enter amount to be shared: '))
    sharers=int(input('Enter number of sharers: '))
    print('Each one will get Rs. ',amount/sharers)
except ValueError:
    print('Enter inputs in digits!')
except ZeroDivisionError:
    print('Number of sharers must be >=1')
except:
    print('Something went wrong!')
    print('Have a blessed day')
