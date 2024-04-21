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

##try:
##    amount=int(input('Enter amount to be shared: '))
##    sharers=int(input('Enter number of sharers: '))
##    print('Each one will get Rs. ',amount/sharers)
##except ValueError:
##    print('Enter inputs in digits!')
##except ZeroDivisionError:
##    print('Number of sharers must be >=1')
##except:
##    print('Something went wrong!')
##    print('Have a blessed day')



##try:
##    amount=int(input('Enter amount to be shared: '))
##    sharers=int(input('Enter number of sharers: '))
##    print('Each one will get Rs. ',amount/sharers)
##except ValueError as e:
##    print('Problem with value:',type(e),e)
##    
##except ZeroDivisionError as e:
##    print('Problem with value:',type(e),e)
##    
##except:
##    print('Cannot identify the problem')
##    print('Have a blessed day')
##


##def divide(x,y):
##    try:
##        result=x//y
##    except ZeroDivisionError:
##        print("Sorry ! You Are Dividing by zero")
##    else:
##        print("Yeah ! Your Answer is : ", result)
##    finally:
##        print('This is always executed')
##divide(24,78)


##class InvalidWithdrawal(Exception):
##    pass
##try:
##    raise InvalidWithdrawal
##except InvalidWithdrawal:
##    print('I am sorry, but do not have enough balance')
##


class InvalidWithdrawal(Exception):
    def __init__ (self, balance, amount):
        super(). __init__(f'Account doesn\'t have ${amount}')
        self.amount = amount
        self.balance = balance
    def overage(self):
        return self.amount - self.balance
try:
    raise InvalidWithdrawal(25,50)
except InvalidWithdrawal as e:
    print('I am sorry, but your withdrawal is more than your balance by', e.overage())
