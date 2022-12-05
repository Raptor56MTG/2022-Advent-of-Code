import re


def problem5p1():
    """problem 5 part 1"""
    with open('problem5.txt', 'r') as f:
        file = f.read().splitlines()

        # parse file and grab steps, number of towers, and text layout of tower.
        tower_text = []
        steps = []
        switch = False
        for line in file:
            if not line:
                switch = True
                num_towers = max([int(i) for i in tower_text.pop() if i.isdigit()])
                towers = [[] for i in range(num_towers)]
            elif not switch:
                tower_text.append(line)
            else:
                steps.append([int(i) for i in re.split(r'\D+', line) if i.isdigit()])

        # generate stacks from tower text
        for layer in tower_text:
            count = 0
            layer_list = list(layer)
            for i in range(1, num_towers * 4 - 1, 4):
                if layer_list[i].isalpha():
                    towers[count].insert(0, layer_list[i])
                count += 1

        # execute steps
        for step in steps:
            start = towers[step[1] - 1]
            target = towers[step[2] - 1]
            amount = step[0]
            for _ in range(amount):
                target.append(start.pop())

        # get output
        tops = ''
        for tower in towers:
            if len(tower) > 0:
                tops += tower[-1]
        return tops


def problem5p2():
    """problem 5 part 2"""
    with open('problem5.txt', 'r') as f:
        file = f.read().splitlines()

        # parse file and grab steps, number of towers, and text layout of tower.
        tower_text = []
        steps = []
        switch = False
        for line in file:
            if not line:
                switch = True
                num_towers = max([int(i) for i in tower_text.pop() if i.isdigit()])
                towers = [[] for i in range(num_towers)]
            elif not switch:
                tower_text.append(line)
            else:
                steps.append([int(i) for i in re.split(r'\D+', line) if i.isdigit()])

        # generate stacks from tower text
        for layer in tower_text:
            count = 0
            layer_list = list(layer)
            for i in range(1, num_towers * 4 - 1, 4):
                if layer_list[i].isalpha():
                    towers[count].insert(0, layer_list[i])
                count += 1

        # execute steps
        for step in steps:
            start = towers[step[1] - 1]
            target = towers[step[2] - 1]
            amount = step[0]
            crates = []
            for _ in range(amount):
                crates.append(start.pop())
            for _ in reversed(crates):  # reverse double pop cause I'm lazy
                target.append(crates.pop())

        # get output
        tops = ''
        for tower in towers:
            if len(tower) > 0:
                tops += tower[-1]
        return tops


if __name__ == '__main__':
    print(problem5p1())
    print(problem5p2())
