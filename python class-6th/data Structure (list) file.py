l=[1,2,0.5,"A","@",[3,4]]
l.append(56) #the append is use to add int add the end of list

# output
'''l
[1, 2, 0.5, 'A', '@', [3, 4], 56]''' #[3,4] is nested list



#l.index('@') this is use for cheak the location of number store in the list or the data
#l.count('@') this is use for cheak the number the variable int or string is stored in the list or the data


#[1, 2, 0.5, 'A', '@', [3, 4], 56] 
#l[2]=3 we use this to to change the number const or variable list in list or data
# 2 define the address and 3 tell replace the value with 3



'''
l=[1,2,0.5,"A","@",[3,4]]
user=input("input the value to search ")
if user in l:
    print("this is exist")
else:
    print("error")
'''



'''l=[1,2,0.5,"A","@",[3,4]]
user=input("input the value to search ")
if user in l or user.upper() in l: #this make user easier if user input capital or small it show the result
    print("this is exist")
else:
    print("error")
 
'''



'''l=[1,2,0.5,"hello","A","@",[3,4]]
user=input("input the value to search ")
if user in l or user.upper() in l: #this make user easier if user input capital or small it show the result
    print("this is exist")
else:
    print("error")'''


#l*2 this is repeatation
#l+l1 this is all both list
#2 in l1   in << is membership
