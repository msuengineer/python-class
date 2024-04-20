class myClass:
    classAttribute='ClassAttribute'
    def __init__ (self):
        self.instanceAttribute='InstanceAttribute'
    def instanceMethod(self): 
        print(myClass.classAttribute) 
        print(self.instanceAttribute) 
        print('This is an instance method')
    @classmethod
    def classMethod(cls):
        print(cls.classAttribute)
##        print(self.instanceAttribute)#error 
##        print(cls.instanceAttribute) #error
        print('This is a class method')
    @staticmethod
    def staticMethod(): 
        print(myClass.classAttribute) 
##        print(self.instanceAttribute) #error
##        print(cls.instanceAttribute)#error
        print('This is a static method')
        #new code

    def anotherMethod(self):
        self.instanceMethod()
        myClass.classMethod()
        myClass.staticMethod()

a=myClass() 
a.instanceMethod() 
#myClass.instanceMethod()#error
myClass.classMethod() 
a.classMethod()
myClass.staticMethod() 
a.staticMethod()
