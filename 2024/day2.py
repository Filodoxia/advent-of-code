import re
from pathlib import Path
from typing import List

DAY = int(re.search(r"day(\d+).py", __file__)[1])
IN_PATH = Path(__file__).parent.joinpath(f"in/day{DAY}").resolve()
INPUT = open(IN_PATH, mode="r").readlines()


def star1():
    safe_count = 0

    for report in INPUT:
        if _is_report_safe([int(x) for x in report.split(" ")]) == -1:
            safe_count += 1

    print(f"Safe reports: {safe_count}")


def star2():
    safe_count = 0

    for r in INPUT:
        report = [int(x) for x in r.split(" ")]
        result = _is_report_safe(report)

        if result == -1:
            safe_count += 1
        else:
            report_without_i = report[0:result] + report[result + 1 :]
            if _is_report_safe(report_without_i) == -1:
                safe_count += 1
                continue

            report_without_i_plus_1 = report[0 : result + 1] + report[result + 2 :]
            if _is_report_safe(report_without_i_plus_1) == -1:
                safe_count += 1
                continue

            if result == 0:
                continue

            report_without_i_minus_1 = report[0 : result - 1] + report[result:]
            if _is_report_safe(report_without_i_minus_1) == -1:
                safe_count += 1

    print(f"Safe reports: {safe_count}")


def _is_report_safe(report: List[int]) -> int:
    if report[0] == report[1]:
        return 0

    is_increase = report[0] < report[1]

    for i in range(0, len(report) - 1):
        difference = report[i + 1] - report[i]

        if not _is_distance_safe(is_increase, difference):
            return i

    return -1


def _is_distance_safe(is_increase: bool, difference: int) -> bool:
    if is_increase and (difference < 1 or difference > 3):
        return False
    elif (not is_increase) and (difference < -3 or difference > -1):
        return False
    return True


if __name__ == "__main__":
    star1()
    star2()
