def move_head(direction, head):
    """move the head knot."""
    if direction == 'R':
        head[0] += 1
    if direction == 'L':
        head[0] -= 1
    if direction == 'U':
        head[1] += 1
    if direction == 'D':
        head[1] -= 1


def move_knots(knot1, knot2):
    """move following knots."""
    while abs(knot1[0] - knot2[0]) > 1 or abs(knot1[1] - knot2[1]) > 1:
        if knot1[0] - knot2[0] > 0:
            knot2[0] += 1
        if knot1[0] - knot2[0] < 0:
            knot2[0] -= 1
        if knot1[1] - knot2[1] > 0:
            knot2[1] += 1
        if knot1[1] - knot2[1] < 0:
            knot2[1] -= 1


def problem9p1():
    """problem 9 part 1"""
    with open('problem9.txt', 'r') as f:
        steps = [(s.split()[0], int(s.split()[1])) for s in f.read().splitlines()]
        places = {(0, 0)}
        knots = [[0, 0] for _ in range(2)]
        for step in steps:
            direction = step[0]
            moves = step[1]
            for _ in range(moves):
                move_head(direction, knots[0])
                for i in range(1, len(knots)):
                    move_knots(knots[i - 1], knots[i])
                places.add(tuple(knots[-1]))
        return len(places)


def problem9p2():
    """problem 9 part 2"""
    with open('problem9.txt', 'r') as f:
        steps = [(s.split()[0], int(s.split()[1])) for s in f.read().splitlines()]
        places = {(0, 0)}
        knots = [[0, 0] for _ in range(10)]
        for step in steps:
            direction = step[0]
            moves = step[1]
            for _ in range(moves):
                move_head(direction, knots[0])
                for i in range(1, len(knots)):
                    move_knots(knots[i - 1], knots[i])
                places.add(tuple(knots[-1]))
        return len(places)


if __name__ == '__main__':
    print(problem9p1())
    print(problem9p2())
