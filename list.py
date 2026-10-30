#list of mcu characters
c=["cap", "Iron man","Thor","Hulk","Gamora","Star lord","Nebula","Nat","Loki","Doom",]
print (c) 

#counting begins at 0 begining from left to right, going backwards right to left is negative
#indexing 
#begin with the smaller number 
print(c[2])
print(c[4])

#negative indexing
print(c[-2])
print(c[-5])

#range of indexes/slicing
print(c[1:6])
print(c[0:4]) # prints 0-3

#negative slicing
print(c[-4:-1]) # all numbers excluding -1
print(c[-3:]) #leave the other number empty to have the last name in list apear 
print(c[-10:])
print(c[0:])

#change list items
#change item value 
print("changing items in list")
c[2]="dan"
print(c)
c[-4]="drax"
print(c)

#Change a range of items
c[0:4]= ["mantice","yondu","groot"]
print(c)
#negative range change
c[-4:]=["wanda","vision","peter","MJ"]
print(c)