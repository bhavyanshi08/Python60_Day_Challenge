n =int(input("Enter number of elements: "))
data=[0]*n
for i in range(n):
    value=input("Enter element " + str(i+1) + ": ")
    if value.isdigit():
        data[i]=int(value)
    else:
        data[i]=value
number_list=[0]*n
string_list=[""]*n
num_index=0
str_index=0
number_count=0
string_count=0
for i in range(n):
    element=data[i]
    if type(element)==int:
        number_list[num_index]=element
        num_index=num_index+1
        number_count=number_count+1
    elif type(element)==str:
        if element!="":
            string_list[str_index]=element
            str_index=str_index+1
            string_count=string_count+1

section = input("Enter your section (A/B/C): ")
print("---- FINAL OUTPUT ----")
if section=="A" or section=="a":
    print("Numbers List:", number_list[:num_index])
elif section=="B" or section=="b":
    print("Strings List:", string_list[:str_index])
elif section=="C" or section=="c":
    print("Numbers List:", number_list[:num_index])
    print("Strings List:", string_list[:str_index])
else:
    print("Invalid section entered")
print("Total Numbers:", number_count)
print("Total Strings:", string_count)