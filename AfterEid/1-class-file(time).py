import time
def calcTime(func):
    def wrapper(): 
        begin=time.time() 
        func() 
        end=time.time()
        print('Run-time:',end-begin,'seconds')
    return wrapper
@calcTime
def long_loop():
    print('Take your time\nHit any alphanumeric key to exit!') 
    input()
long_loop()
