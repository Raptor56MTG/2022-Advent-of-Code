def problem10p1():
    """problem 10 part 1"""
    with open('problem10.txt', 'r') as f:
        steps = f.read().splitlines()
        x_values = []
        x = 1
        for step in steps:
            if step == 'noop':
                x_values.append(x)
            else:
                add = int(step.split()[1])
                x_values.append(x)
                x += add
                x_values.append(x)
        return (x_values[18] * 20 + x_values[58] * 60 + x_values[98] * 100 +
                x_values[138] * 140 + x_values[178] * 180 + x_values[218] * 220)


def problem10p2():
    """problem 10 part 2"""
    with open('problem10.txt', 'r') as f:
        steps = f.read().splitlines()
        pixels = ['.' for _ in range(40)]
        counter = 0
        x = 1
        for step in steps:
            if step == 'noop':
                if x == counter or x - 1 == counter or x + 1 == counter:
                    pixels[counter] = '#'
                counter += 1
                if counter == 40:
                    print(''.join(pixels))
                    counter = 0
                    pixels = ['.' for _ in range(40)]
            else:
                add = int(step.split()[1])
                if x == counter or x - 1 == counter or x + 1 == counter:
                    pixels[counter] = '#'
                counter += 1
                if counter == 40:
                    print(''.join(pixels))
                    counter = 0
                    pixels = ['.' for _ in range(40)]
                if x == counter or x - 1 == counter or x + 1 == counter:
                    pixels[counter] = '#'
                counter += 1
                if counter == 40:
                    print(''.join(pixels))
                    counter = 0
                    pixels = ['.' for _ in range(40)]
                x += add


if __name__ == '__main__':
    print(problem10p1())
    problem10p2()

# ZKGRKGRK
#   ####.#..#..##..###..#..#..##..###..#..#.
#   ...#.#.#..#..#.#..#.#.#..#..#.#..#.#.#..
#   ..#..##...#....#..#.##...#....#..#.##...
#   .#...#.#..#.##.###..#.#..#.##.###..#.#..
#   #....#.#..#..#.#.#..#.#..#..#.#.#..#.#..
#   ####.#..#..###.#..#.#..#..###.#..#.#..#.
