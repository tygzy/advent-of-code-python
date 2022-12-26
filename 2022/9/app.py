import numpy as np


def solution(length):
    input = open('data.in', 'r').read().splitlines()
    knots = []

    for k in range(length):
        knots.append((0, 0))

    visited = set()
    visited.add(knots[-1])

    for motion in input:
        direction, steps = motion.split()
        for _ in range(int(steps)):
            match direction:
                case 'U':
                    knots[0] = (knots[0][0], knots[0][1] + 1)
                case 'D':
                    knots[0] = (knots[0][0], knots[0][1] - 1)
                case 'R':
                    knots[0] = (knots[0][0] + 1, knots[0][1])
                case 'L':
                    knots[0] = (knots[0][0] - 1, knots[0][1])
            for k in range(length-1):
                diff_x = knots[k][0] - knots[k+1][0]
                diff_y = knots[k][1] - knots[k+1][1]
                if abs(diff_x) > 1 or abs(diff_y) > 1:
                    knots[k+1] = (knots[k+1][0] + np.sign(diff_x), knots[k+1][1] + np.sign(diff_y))
                visited.add(knots[-1])
    return len(visited)


def main():
    print(solution(2))
    print(solution(10))


if __name__ == '__main__':
    main()