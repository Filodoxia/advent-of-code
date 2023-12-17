from pathlib import Path
import re

IN_FILE = Path(__file__).joinpath("../in/day3").resolve()

rx = re.compile(r"")


def is_part(char: str):
    return (not ((char == '.') or char.isdigit()))


def star1():
    input = IN_FILE.open().readlines()

    max_row = len(input) - 1
    max_col = len(input[0].strip()) - 1

    print(max_row, max_col)

    parts = []

    # .LAAAR.
    # .LnnnR.
    # .LBBBR.
    for r in range(max_row+1):
        cur_num = ''
        is_part = False

        for c in range(max_col+1):
            if input[r][c].isdigit():
                # for the first digit of a number we check the left side for symbols
                if (cur_num == '') and (c > 0):
                    # check left
                    is_part = not (
                        (input[r][c-1] == '.') or (input[r][c-1].isdigit())
                    )

                    # check left above (diagonally)
                    if r > 0:
                        # if r == max_row:
                        #     print(input[r][c])
                        #     print(input[r-1][c-1])

                        is_part = is_part or (not (
                            (input[r-1][c-1] == '.') or (input[r-1][c-1].isdigit())
                        ))

                    # check left below (diagonally)
                    if r < max_row:
                        is_part = is_part or (not (
                            (input[r+1][c-1] == '.') or (input[r+1][c-1].isdigit())
                        ))

                # add digit to current nubmer
                cur_num += input[r][c]

                # check above
                if r > 0:
                    is_part = is_part or (not (
                        (input[r-1][c] == '.') or (input[r-1][c].isdigit())
                    ))

                # check below
                if r < max_row:
                    is_part = is_part or (not (
                        (input[r+1][c] == '.') or (input[r+1][c].isdigit())
                    ))
            else:
                # if there is a cur_num, we now have reached the end of the number => check right side for symbols
                if cur_num:
                    # check right
                    is_part = is_part or (not (input[r][c] == '.'))

                    # check right above (diagonally)
                    if r > 0:
                        is_part = is_part or (not (
                            (input[r-1][c] == '.') or (input[r-1][c].isdigit())
                        ))

                    # check right below (diagonally)
                    if r < max_row:
                        is_part = is_part or (not (
                            (input[r+1][c] == '.') or (input[r+1][c].isdigit())
                        ))

                    if is_part:
                        parts.append(int(cur_num))
                        is_part = False
                    cur_num = ''

        # if a number 'touches' the end of a line we have to manually handle it at the EOL
        if is_part:
            parts.append(int(cur_num))

    print(parts)
    print(sum(parts))


def star2():
    pass


if __name__ == "__main__":
    star1()
    star2()
