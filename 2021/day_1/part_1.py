# --- --- Day 1: Sonar Sweep ------ 

with open('2021/input/input_day1.txt','r') as f:
    measure_list = [int(x) for x in f.read().split("\n")]

increase_count = 0

for i in range(1, len(measure_list)):

    if measure_list[i] > measure_list[i-1]:

        increase_count += 1

print(f'There are {increase_count} measurements that are larger than the previous measurement.')
