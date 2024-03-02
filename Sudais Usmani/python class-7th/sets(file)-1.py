'''thisset={"apple","apple","banana","cherry"}#set does not have indexes 
thisset.add("orange")
print(thisset)'''

'''
thisset={"apple","apple","banana","cherry"}#set does not have indexes 
newset={"google","microsoft","apple"}
thisset.update(newset)
print(thisset)
'''

'''
thisset={"apple","apple","banana","cherry"}#set does not have indexes 
newset={"google","microsoft","apple"}
set1= thisset.difference(newset)
print(set1)
'''

fruits={"apple","orange","banana"}
fruits.remove("banana")
fruits.add("banana")
fruits.remove("banana")
fruits.discard("banana")
'''fruits.pop()
print(fruits)'''
fruits={"apple","orange","banana"}
new_fruit={"cherry","banana","lemon"}
name_of_fruit=fruits.union(new_fruit)
print(name_of_fruit)
name_of_fruit=fruits.intersection(new_fruit)
print(name_of_fruit)
