# Empty List
[]

#List of Integers
[1,2,3]

#List of Numbers(Floating and Integers)
[1,2,1.1,5]

#List of characters 
['a','b','c']

#List of mixed data types 
['a','bc','xero',0,1,2.2]

#List of Strings 
["One","Two","Three"]

#Creating List
list1 = []

#Nested List 
list1 = [1,2,3,[1,2.2],'Hello']


#Accessing Elements in a List
li = ['Mother','Dad','Daughter','Son',1,2,3.3]
print(li[2]) # Accessing the third element in list it will be present at 2 index because list has 0 based indexing  
print(li[10]) # This will give list index out of range error
# Negative Indexing

li = ['Mother','Dad','Daughter','Son',1, 2, 3.3]
#li = [  -7      -6      -5       -4  -3 -2  -1] negative indexing
print(li[-2]) #This will print 2
print(li[-10]) # This will give list index out of range error

#Changing the element of the list
li = ['Mother','Dad','Daughter','Son',1, 2, 3.3]
li[-1] = 'Satyam'

#Now li will be
['Mother','Dad','Daughter','Son',1, 2, 'Satyam']

#Concatenation of List
li = [1,2,3]
l2 = [4,5,6]
l3 = li+l2 

#l3 will be
[1,2,3,4,5,6]

#Repeating/ Replication List
li = [1,2,3,5]
print(li*3)

#This will print
[1,2,3,5,1,2,3,5,1,2,3,5]

#List Slicing list_name[start_index:stop_index:steps]
L = ['a','b','c','d','e','f','g','h','i']
print(L[2:7])

#This will print
['c','d','e','f','g']

#Slicing using negative indexing
L = ['a','b','c','d','e','f','g','h','i']
print(L[-7:-2])
['c','d','e','f','g']

#Slicing with steps
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[2:7:2])
['c','e','g']

#Slicing with steps using negative indexing
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[-2:-7:-2])
['h','f','d']

L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[6:1:-2])
['g','e','c']

#Slicing at the beginning and end
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[0:3]) #Beginning
['a','b','c','d']

L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[5:]) #Ending
['f','g','h','i']


#Reversing a List
L = ['a','b','c','d','e']
print(L[::-1])


#Methods in List
#1.Append
li = [1,2,3,4]
li.append(5)
[1,2,3,4,5]

#2.Extend
l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
[1,2,3,4,5,6]

"""
Append simply adds the element at the end of the list
Extends adds the content of the other list into the first list it basically merges the two list
"""


