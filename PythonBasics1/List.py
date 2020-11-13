values = [1, 2, "Sai", 4, 5]
print(values[0]) # prints 1
print(values[3]) # prints 4
print(values[-1]) # -1 refers to the last element in the list, prints 5
print(values[1:3])#[1:3] is used to get substring.it will fetch 2 values leaving the 3rd index, prints 2, Sai
values.insert(3, "Ramana") # will insert Ramana at 3rd index
print(values) # prints [1, 2, 'Sai', 'Ramana', 4, 5]
values.append("End") # append will insert value at last
print(values) # prints [1, 2, 'Sai', 'Ramana', 4, 5, 'End']
values[2] ="SAI" # will Update the old value with new one
print(values) # prints [1, 2, 'Sai', 'Ramana', 4, 5, 'End']
del values[0] # will delete the 0th index value
print(values) # prints [2, 'SAI', 'Ramana', 4, 5, 'End']
#Tuple
val= (1, 2, "Sai")
print(val) # prints (1, 2, 'Sai')
#val[2] ="SAI" #TypeError: 'tuple' object does not support item assignment

# Dictionary
dic = {"a":2, 4:"bcd","c":"Hello World"}
print(dic[4]) # prints bcd
print(dic["c"]) # prints Hello World
print(dic["a"]) # prints 2
#
dict = {}
dict["firstname"] = "Madhavi"
dict["lastname"] = "Latha"
dict["gender"] = "Male"
print(dict)# prints {'firstname': 'Madhavi', 'lastname': 'Latha', 'gender': 'Male'}
print(dict["lastname"]) # prints Latha
