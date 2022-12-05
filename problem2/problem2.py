p1_choices = {'A': 1, 'B': 2, 'C': 3}
p2_choices = {'X': 3, 'Y': 2, 'Z': 1}
outcome_pts = {'loss': 0, 'draw': 3, 'win': 6}


def calculate_score_p1(line: str):
    """I use modular arithmetic to condense comparisons."""
    pick_pts = {'X': 1, 'Y': 2, 'Z': 3}
    p1, p2 = line.rstrip().split(" ")
    if (p1_choices[p1] + p2_choices[p2]) % 3 == 0:
        return outcome_pts['win'] + pick_pts[p2]
    if (p1_choices[p1] + p2_choices[p2]) % 3 == 1:
        return outcome_pts['draw'] + pick_pts[p2]
    if (p1_choices[p1] + p2_choices[p2]) % 3 == 2:
        return outcome_pts['loss'] + pick_pts[p2]


def problem2p1():
    """problem 2 part 1"""
    with open('problem2.txt', 'r') as f:
        total = 0
        for line in f:
            total += calculate_score_p1(line)
    return total


def calculate_score_p2(line: str):
    """I use modular arithmetic with shifts to condense comparisons."""
    shift = {'A': 1, 'B': 0, 'C': -1}
    pick_shift_pts = {'A': {'X': 3, 'Y': 1, 'Z': 2},
                      'B': {'X': 1, 'Y': 2, 'Z': 3},
                      'C': {'X': 2, 'Y': 3, 'Z': 1}}
    p1, p2 = line.rstrip().split(" ")
    if (p1_choices[p1] + p2_choices[p2] + shift[p1]) % 3 == 0:
        return outcome_pts['win'] + pick_shift_pts[p1][p2]
    if (p1_choices[p1] + p2_choices[p2] + shift[p1]) % 3 == 1:
        return outcome_pts['draw'] + pick_shift_pts[p1][p2]
    if (p1_choices[p1] + p2_choices[p2] + shift[p1]) % 3 == 2:
        return outcome_pts['loss'] + pick_shift_pts[p1][p2]


def problem2p2():
    """problem 2 part 2"""
    with open('problem2.txt', 'r') as f:
        total = 0
        for line in f:
            total += calculate_score_p2(line)
    return total


if __name__ == '__main__':
    print(problem2p1())
    print(problem2p2())
