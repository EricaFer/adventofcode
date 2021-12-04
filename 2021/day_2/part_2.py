# --- Day 2: Dive! (Part 2) ---

with open('2021/input/input_day2.txt','r') as f:
    direction_list = [x for x in f.read().split("\n")]


depth = 0
horizontal = 0
aim = 0

for x in direction_list:

    direction, value = x.split(' ')

    value = int(value)

    if direction == 'forward':

        horizontal += value
        depth += aim * value

    elif direction == 'down':

        aim += value

    elif direction == 'up':

        aim -= value

print(depth * horizontal)