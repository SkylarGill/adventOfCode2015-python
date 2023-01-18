import json
import re
import sys


def get_cases(filename):
    f = open(filename)
    data = json.load(f)
    return data["Cases"]


def calc_floor(input):
    open_matches = re.findall(r"[(]{1}", input)
    close_matches = re.findall(r"[)]{1}", input)

    return len(open_matches) - len(close_matches)


filename = sys.argv[1]

cases = get_cases(filename)

for case in cases:
    result = calc_floor(case["Input"])
    print(case["Input"])
    print(result)
