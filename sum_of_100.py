num_array = list()
num = raw_input("Enter how many elements you want:")
print 'Enter numbers in array: '
for i in range(int(num)):
    n = raw_input("num :")
    num_array.append(int(n))
print 'ARRAY: ', num_array


for i in range(0, len(num_array)):
    value = 100 - num_array[i]
    if value in num_array:
        print " found the pair" , value, 100 - value
    else:
        None 

        