#Create an empty list
my_list = []

#Appending to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#Inserting 15 at second position
my_list.insert(1, 15)
print(my_list)

#Extending my_list with additional_list
additional_list = [50,60,70]
my_list.extend(additional_list)
print(my_list)

#Removing last element from my_list
my_list.remove(70)
print(my_list)

#Sorting my_list in ascending order
my_list.sort()
print(my_list)

#Finding and printing the index of the value of 30
index_of_30 = my_list.index(30)
print("Index of 30 is: ", index_of_30)
