# --- Day 2: Dive! ---

with open('2021/input/input_day2.txt','r') as f:
    direction_list = [x for x in f.read().split("\n")]


depth = 0
horizontal = 0

for x in direction_list:

    direction, value = x.split(' ')

    value = int(value)

    if direction == 'forward':

        horizontal += value

    elif direction == 'down':

        depth += value

    elif direction == 'up':

        depth -= value

print(depth * horizontal)