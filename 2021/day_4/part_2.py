#--- Day 4: Giant Squid ---

from collections import defaultdict


with open('../input/input_day4.txt','r') as f:

    # contains matrix and called numbers
    raw_file = [[num for num in line.split('\n')] for line in f]


# just contains called numbers
called_numbers = [int(num) for num in raw_file[0][0].split(',')]


# Creating dictionary of matrix
blocks = defaultdict(list)

i = 0

for line in raw_file[2:]:

    if line != ['', '']:

        blocks[i].append([int(num) for num in line[0].split(' ') if num != ''])

    else:
        #line counter
        i += 1

class BreakIt(Exception):pass

winners = []

boards = list(blocks.keys())

try:

    for called_number in called_numbers:

        if len(winners) > 0:

            for winner in set(winners):

                boards.remove(winner)

        winners = []

        for key in boards:

            # checks for number by line in dict
            for line in blocks[key]:

                if called_number in line:

                    blocks[key][blocks[key].index(line)][line.index(called_number)] = 0

                # checks if a line is complete
                if sum(line) == 0:

                    winners.append(key)

                    if len(boards) == 1:
                        raise BreakIt
                    

                # checks if column is complete
                for col in range(0,5):

                    if sum([blocks[key][line_num][col] for line_num in range(0,5)]) == 0:

                        winners.append(key)

                        if len(boards) == 1:
                            raise BreakIt

except BreakIt:

    block_sum = 0

    for line in blocks[key]:

        block_sum += sum(line)

    print(f'The result is {block_sum * called_number}')