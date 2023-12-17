from pathlib import Path
from functools import reduce

IN_FILE = Path(__file__).joinpath("../in/day3").resolve()


def is_symbol(char: str):
    return (not ((char == '.') or char.isdigit()))


def star1():
    input = IN_FILE.open().readlines()

    max_row = len(input) - 1
    max_col = len(input[0].strip()) - 1

    parts = []

    # .LAAAR.
    # .LnnnR.
    # .LBBBR.
    for r in range(max_row + 1):
        cur_num = ''
        is_part = False

        for c in range(max_col + 1):
            if input[r][c].isdigit():
                # for the first digit of a number we check the left side for symbols
                if (cur_num == '') and (c > 0):
                    # check left
                    is_part = is_symbol(input[r][c-1])

                    # check left above (diagonally)
                    if r > 0:
                        is_part = is_part or is_symbol(input[r-1][c-1])

                    # check left below (diagonally)
                    if r < max_row:
                        is_part = is_part or is_symbol(input[r+1][c-1])

                # add digit to current nubmer
                cur_num += input[r][c]

                # check above
                if r > 0:
                    is_part = is_part or is_symbol(input[r-1][c])

                # check below
                if r < max_row:
                    is_part = is_part or is_symbol(input[r+1][c])
            else:
                # if there is a cur_num, we now have reached the end of the number => check right side for symbols
                if cur_num:
                    # check right
                    is_part = is_part or (not (input[r][c] == '.'))

                    # check right above (diagonally)
                    if r > 0:
                        is_part = is_part or is_symbol(input[r-1][c])

                    # check right below (diagonally)
                    if r < max_row:
                        is_part = is_part or is_symbol(input[r+1][c])

                    if is_part:
                        parts.append(int(cur_num))
                        is_part = False
                    cur_num = ''

        # if a number 'touches' the end of a line we have to manually handle it at the EOL
        if is_part:
            parts.append(int(cur_num))

    # print(parts)
    print(sum(parts))


def star2():
    input = IN_FILE.open().readlines()

    max_row = len(input) - 1
    max_col = len(input[0].strip()) - 1

    gear_rations = []

    for r in range(max_row + 1):
        for c in range(max_col + 1):
            if input[r][c] == "*":
                # search around the * for numbers
                numbers = []

                is_row_0 = (r == 0)
                is_row_max = (r == max_row)
                is_col_0 = (c == 0)
                is_col_max = (c == max_col)

                def find_left(r, c):
                    c_temp = c

                    while (c_temp >= 0) and input[r][c_temp].isdigit():
                        c_temp -= 1

                    return (c_temp + 1)

                def search_right(r, c):
                    c_temp = c
                    n = ''

                    while (c_temp <= max_col) and input[r][c_temp].isdigit():
                        n += input[r][c_temp]
                        c_temp += 1

                    return int(n)

                def get_number(r, c):
                    if not input[r][c].isdigit():
                        return
                    return search_right(r, find_left(r, c))

                # above
                if not is_row_0:
                    n = get_number(r-1, c)
                    if n:
                        numbers.append(n)

                # above left (diagonally)
                if not (is_row_0 or is_col_0 or input[r-1][c].isdigit()):
                    n = get_number(r-1, c-1)
                    if n:
                        numbers.append(n)

                # above right (diagonally)
                if not (is_row_0 or is_col_max or input[r-1][c].isdigit()):
                    n = get_number(r-1, c+1)
                    if n:
                        numbers.append(n)

                # right
                if not is_col_max:
                    n = get_number(r, c+1)
                    if n:
                        numbers.append(n)

                # below
                if not is_row_max:
                    n = get_number(r+1, c)
                    if n:
                        numbers.append(n)

                # below left (diagonally)
                if not (is_row_max or is_col_0 or input[r+1][c].isdigit()):
                    n = get_number(r+1, c-1)
                    if n:
                        numbers.append(n)

                # below right (diagonally)
                if not (is_row_max or is_col_max or input[r+1][c].isdigit()):
                    n = get_number(r+1, c+1)
                    if n:
                        numbers.append(n)

                # left
                if not is_col_0:
                    n = get_number(r, c-1)
                    if n:
                        numbers.append(n)

                if len(numbers) == 2:
                    gear_rations.append(reduce(lambda x, y: x*y, numbers))

    print(sum(gear_rations))


if __name__ == "__main__":
    star1()
    star2()
