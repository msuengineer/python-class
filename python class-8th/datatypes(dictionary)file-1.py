d={1:"PAK",2:"AUS",3:"GER"}
inp=int(input("Enter the key"))
if inp in d:
    print("the value is ","('",d[inp],"')"," in this data")
else:
    print("The value is not exist","This is present in our data",d)
