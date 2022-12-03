def ascii_shift_value(shared: set):
    """calculates the shifted ascii values.
    a-z (1-26), A-Z (27-52)"""
    if list(shared)[0].islower():
        ascii_offset = 96
        return ord(list(shared)[0]) - ascii_offset
    else:
        ascii_offset = 38
        return ord(list(shared)[0]) - ascii_offset


def problem3p1():
    """problem 3 part 1"""
    with open('problem3.txt', 'r') as f:
        total = 0
        for line in f:
            shared = set(line[: len(line) // 2]) & set(line[len(line) // 2:])
            total += ascii_shift_value(shared)
    return total


def problem3p2():
    """problem 3 part 2"""
    with open('problem3.txt', 'r') as f:
        total = 0
        lines = f.read().splitlines()
        a, b, c = 0, 1, 2
        while c < len(lines):
            shared = set(lines[a]) & set(lines[b]) & set(lines[c])
            total += ascii_shift_value(shared)
            a += 3
            b += 3
            c += 3
        return total


if __name__ == '__main__':
    print(problem3p2())
