import re


def parse_monkey(monkey: str) -> list:
    info = monkey.split('\n')
    monkey_name = [int(x) for x in re.findall(r'\d+', info[0])][0]
    items = [int(x) for x in re.findall(r'\d+', info[1])]
    operation = [x for x in re.findall(r'[+*]', info[2])][0]
    scalar = [int(x) for x in re.findall(r'\d+', info[2])]
    divisible = [int(x) for x in re.findall(r'\d+', info[3])][0]
    true_target = [int(x) for x in re.findall(r'\d+', info[4])][0]
    false_target = [int(x) for x in re.findall(r'\d+', info[5])][0]
    return {'monkey': monkey_name,
            'items': items,
            'operation': operation if len(scalar) > 0 else '^',
            'scalar': scalar[0] if len(scalar) > 0 else None,
            'divisible': divisible,
            'true_target': true_target,
            'false_target': false_target,
            'inspection_count': 0}


def mod_shifting(value: int, monkeys: list) -> int:
    """I'd like to preface and state this code is not elegant at all.
    It's a raw expanded solution to reducing the modular values from expanding
    into uncomprehensibly big numbers by using the chinese reamainder theorem
    algorithm to find the smallest common divisor that maintains the same
    modularity among all of the possible divisors. I'm certain there is a more
    elegant and smart solution, but I'm proud to have figured out a solution on
    my own, even if it is very inelegant."""

    # divisors
    mod_0 = monkeys[0]['divisible']
    mod_1 = monkeys[1]['divisible']
    mod_2 = monkeys[2]['divisible']
    mod_3 = monkeys[3]['divisible']
    mod_4 = monkeys[4]['divisible']
    mod_5 = monkeys[5]['divisible']
    mod_6 = monkeys[6]['divisible']
    mod_7 = monkeys[7]['divisible']

    mod_total = mod_0 * mod_1 * mod_2 * mod_3 * mod_4 * mod_5 * mod_6 * mod_7

    # remainders
    r0 = value % mod_0
    r1 = value % mod_1
    r2 = value % mod_2
    r3 = value % mod_3
    r4 = value % mod_4
    r5 = value % mod_5
    r6 = value % mod_6
    r7 = value % mod_7

    # shifters
    shift_0 = 1
    shift_1 = 1
    shift_2 = 1
    shift_3 = 1
    shift_4 = 1
    shift_5 = 1
    shift_6 = 1
    shift_7 = 1

    while (mod_1 * mod_2 * mod_3 * mod_4 * mod_5 * mod_6 * mod_7 * shift_0) % mod_0 != r0:
        shift_0 += 1
    while (mod_0 * mod_2 * mod_3 * mod_4 * mod_5 * mod_6 * mod_7 * shift_1) % mod_1 != r1:
        shift_1 += 1
    while (mod_0 * mod_1 * mod_3 * mod_4 * mod_5 * mod_6 * mod_7 * shift_2) % mod_2 != r2:
        shift_2 += 1
    while (mod_0 * mod_1 * mod_2 * mod_4 * mod_5 * mod_6 * mod_7 * shift_3) % mod_3 != r3:
        shift_3 += 1
    while (mod_0 * mod_1 * mod_2 * mod_3 * mod_5 * mod_6 * mod_7 * shift_4) % mod_4 != r4:
        shift_4 += 1
    while (mod_0 * mod_1 * mod_2 * mod_3 * mod_4 * mod_6 * mod_7 * shift_5) % mod_5 != r5:
        shift_5 += 1
    while (mod_0 * mod_1 * mod_2 * mod_3 * mod_4 * mod_5 * mod_7 * shift_6) % mod_6 != r6:
        shift_6 += 1
    while (mod_0 * mod_1 * mod_2 * mod_3 * mod_4 * mod_5 * mod_6 * shift_7) % mod_7 != r7:
        shift_7 += 1

    new_value = ((mod_1 * mod_2 * mod_3 * mod_4 * mod_5 * mod_6 * mod_7 * shift_0) +
                 (mod_0 * mod_2 * mod_3 * mod_4 * mod_5 * mod_6 * mod_7 * shift_1) +
                 (mod_0 * mod_1 * mod_3 * mod_4 * mod_5 * mod_6 * mod_7 * shift_2) +
                 (mod_0 * mod_1 * mod_2 * mod_4 * mod_5 * mod_6 * mod_7 * shift_3) +
                 (mod_0 * mod_1 * mod_2 * mod_3 * mod_5 * mod_6 * mod_7 * shift_4) +
                 (mod_0 * mod_1 * mod_2 * mod_3 * mod_4 * mod_6 * mod_7 * shift_5) +
                 (mod_0 * mod_1 * mod_2 * mod_3 * mod_4 * mod_5 * mod_7 * shift_6) +
                 (mod_0 * mod_1 * mod_2 * mod_3 * mod_4 * mod_5 * mod_6 * shift_7))

    while new_value > mod_total:
        new_value -= mod_total

    return new_value


def monkey_action(monkey: dict, monkeys: list, worry: bool) -> None:
    for item in monkey['items']:
        monkey['inspection_count'] = monkey['inspection_count'] + 1
        if monkey['operation'] == '*':
            update = item * monkey['scalar']
        elif monkey['operation'] == '+':
            update = item + monkey['scalar']
        else:
            update = item * item

        if worry:
            update //= 3
        else:
            update = mod_shifting(update, monkeys)

        if update % monkey['divisible'] == 0:
            monkeys[monkey['true_target']]['items'].append(update)
        else:
            monkeys[monkey['false_target']]['items'].append(update)

    monkey['items'] = []


def problem11p1():
    """problem 11 part 1"""
    with open('problem11.txt', 'r') as f:
        monkeys = [parse_monkey(monkey) for monkey in f.read().split('\n\n')]
        total_rounds = 20
        for _ in range(total_rounds):
            for monkey in monkeys:
                monkey_action(monkey, monkeys, True)

    inspections = []
    for monkey in monkeys:
        inspections.append(monkey['inspection_count'])
    inspections.sort()

    return inspections[-1] * inspections[-2]


def problem11p2():
    """problem 11 part 2"""
    with open('problem11.txt', 'r') as f:
        monkeys = [parse_monkey(monkey) for monkey in f.read().split('\n\n')]
        total_rounds = 10000
        for i in range(total_rounds):
            for monkey in monkeys:
                monkey_action(monkey, monkeys, False)

    inspections = []
    for monkey in monkeys:
        inspections.append(monkey['inspection_count'])
    inspections.sort()

    return inspections[-1] * inspections[-2]


if __name__ == '__main__':
    print(problem11p1())
    print(problem11p2())
