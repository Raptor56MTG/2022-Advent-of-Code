def generate_elves():
    with open('example.txt', 'r') as f:
        elf_calories = []
        total = 0
        for line in f:
            if line.strip():
                total += int(line)
            else:
                elf_calories.append(total)
                total = 0
        elf_calories.append(total)
        return elf_calories


def problem1p1():
    """problem 1 part 1"""
    return max(generate_elves())


def problem1p2():
    """problem 1 part 2"""
    elf_calories = generate_elves()
    elf_calories.sort()
    return sum(elf_calories[-3:])


if __name__ == '__main__':
    print(problem1p1())
    print(problem1p2())
