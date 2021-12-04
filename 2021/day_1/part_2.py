# --- --- Day 1: Sonar Sweep (Part 2) ------ 

with open('2021/input/input_day1.txt','r') as f:
    measure_list = [int(x) for x in f.read().split("\n")]

increase_count = 0

for i in range(1, len(measure_list)):

    if sum(measure_list[i:(i+3)]) > sum(measure_list[i-1:i+2]):

        increase_count += 1

print(f'There are {increase_count} measurements that are larger than the previous measurement.')