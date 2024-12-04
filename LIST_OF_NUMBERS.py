#Reverse_array_of_numbers

from operator import indexOf

numbers = (12, 34, 55, 15, 78, 22, 67, 88, 93, 39)

def reverse(list):
    reversed_array = []
    for y in list:
        reversed_array.append(list[len(list) - 1 - list.index(y)])
    return reversed_array



#sum_of_numbers

def sum(list):
    total = 0
    for y in list:
        total = total + y
    return total


print('Reverse:  ' + str(reverse(numbers)))
print('Total Sum: ' + str(sum(numbers)))
