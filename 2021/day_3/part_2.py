#--- Day 3: Binary Diagnostic (Part 2) ---

from collections import Counter

with open('2021/input/input_day3.txt','r') as f:
    binary_list = [x for x in f.read().split("\n")]

oxygen_list = binary_list
carbon_list = binary_list

# Getting number of digits
num_digits = len(binary_list[0])

for i in range(0,num_digits):

    #Oxygen
    most_common = list(Counter([x[i] for x in oxygen_list]).most_common())

    if len(most_common) > 1:

        # if number of occurences are equal
        if most_common[0][1] == most_common[1][1]:
            most_common = '1'
        
        else:
            most_common = most_common[0][0]

    else:
        most_common = most_common[0][0]

    if len(oxygen_list) > 1:
        oxygen_list = [x for x in oxygen_list if x[i] == most_common]

    #Carbon
    most_common = list(Counter([x[i] for x in carbon_list]).most_common())

    if len(most_common) > 1:

        # if number of occurences are equal
        if most_common[0][1] == most_common[1][1]:
            least_common = '0'
        
        else:
            least_common = most_common[-1][0]

    else:
        least_common = most_common[-1][0]


    #Carbon
    if len(carbon_list) > 1:
        carbon_list = [x for x in carbon_list if x[i] == least_common]

life_support = int(oxygen_list[0], 2) * int(carbon_list[0], 2)

print(life_support)