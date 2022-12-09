def problem8p1():
    """problem 8 part 1"""
    with open('problem8.txt', 'r') as f:
        grid = [[int(i) for i in line] for line in f.read().splitlines()]
        visible = 0
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                tree = grid[i][j]
                north = [row[j] for k, row in enumerate(grid) if k < i]
                south = [row[j] for k, row in enumerate(grid) if k > i]
                east = row[j + 1:]
                west = row[:j]
                if (tree > max(north, default=-1) or tree > max(south, default=-1) or
                   tree > max(east, default=-1) or tree > max(west, default=-1)):
                    visible += 1
        return visible


def problem8p2():
    """problem 8 part 2"""
    with open('problem8.txt', 'r') as f:
        grid = [[int(i) for i in line] for line in f.read().splitlines()]
        scores = []
        for level, row in enumerate(grid):
            for width, _ in enumerate(row):
                current_tree = grid[level][width]
                north = [row[width] for i, row in enumerate(grid) if i < level]
                north.reverse()  # reverse for proper ordering
                south = [row[width] for i, row in enumerate(grid) if i > level]
                east = row[width + 1:]
                west = row[:width]
                west.reverse()  # reverse for proper ordering

                north_score = 0
                for tree in north:
                    north_score += 1
                    if current_tree <= tree:
                        break
                south_score = 0
                for tree in south:
                    south_score += 1
                    if current_tree <= tree:
                        break
                west_score = 0
                for tree in west:
                    west_score += 1
                    if current_tree <= tree:
                        break
                east_score = 0
                for tree in east:
                    east_score += 1
                    if current_tree <= tree:
                        break

                score = north_score * south_score * west_score * east_score
                scores.append(score)
        return max(scores)


if __name__ == '__main__':
    print(problem8p2())
