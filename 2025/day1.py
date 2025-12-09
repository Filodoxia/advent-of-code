def star1():
    zero_count = 0
    dial = 50

    with open("./2025/input/day1") as f:
        for l in f:
            if l[0] == "L":
                sign = -1
            else:
                sign = 1

            clicks = int(l[1:])
            dial = (dial + (sign * clicks)) % 100

            if dial == 0:
                zero_count += 1

    print(zero_count)


def star2():
    zero_count = 0
    dial = 50

    with open("./2025/input/day1") as f:
        for l in f:
            if l[0] == "L":
                sign = -1
            else:
                sign = 1

            clicks = int(l[1:])
            dial_new = (dial + (sign * clicks)) % 100

            intermediate_zeroes = clicks // 100
            end_on_zero = 1 if dial_new == 0 else 0

            if dial != 0 and dial_new != 0:
                if sign == 1 and dial_new < dial:
                    intermediate_zeroes += 1
                elif sign == -1 and dial_new > dial:
                    intermediate_zeroes += 1

            zero_count += intermediate_zeroes + end_on_zero

            if dial == 0 and dial_new == 0 and clicks > 0:
                zero_count -= 1

            dial = dial_new
            # print(l.rstrip())
            # print("  ", dial, "  ", intermediate_zeroes, end_on_zero, zero_count)

    print(zero_count)


if __name__ == "__main__":
    star1()
    star2()
