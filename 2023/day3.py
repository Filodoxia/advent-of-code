from pathlib import Path

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
    for r in range(max_row+1):
        cur_num = ''
        is_part = False

        for c in range(max_col+1):
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
    pass


if __name__ == "__main__":
    star1()
    star2()
