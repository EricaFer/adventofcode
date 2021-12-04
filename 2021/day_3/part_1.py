#--- Day 3: Binary Diagnostic ---

from collections import Counter

with open('2021/input/input_day3.txt','r') as f:
    binary_list = [x for x in f.read().split("\n")]

gamma_rate = ''
episilon_rate = ''

# Getting number of digits
num_digits = len(binary_list[0])

for i in range(0,num_digits):

    most_common = list(Counter([x[i] for x in binary_list]).most_common())[0][0]

    least_common = '0' if most_common == '1' else '1'

    gamma_rate += str(most_common)

    episilon_rate += str(least_common) 

power_consuption = int(gamma_rate, 2) * int(episilon_rate, 2)

print(power_consuption)
