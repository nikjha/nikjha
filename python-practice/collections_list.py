#Initiating Lists with Interger and String data.
int_list = [1,2,3,4]
string_list =['abc','niraj']



print(string_list.append("Sita"))


string_list.insert(1, "Niiki")
print(string_list)
remove_value=input("Enter the value you want to remove")
string_list.remove(remove_value)
print(string_list)
finds=input("Enter the value to find POS")
string_list.index(finds)
print("find the total lenght of list", len(string_list))
print("Reverse order of List", int_list.reverse())
print("Remove and Return last value", string_list, string_list.pop())
print('\n','\n')
for element in string_list:
   print(element)
