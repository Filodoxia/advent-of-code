from typing import Dict
import input as inp


def star1():
    poly = buildPolymere_BF(START_STRING, RULES, 10, True)
    hist = list(createHist(poly).values())
    print(max(hist)-min(hist))


def star2():
    pairCounts = buildPolymere_smart(START_STRING, RULES, 40)
    hist = list(createHistFromPairCounts(pairCounts, START_STRING[0]).values())
    print(max(hist)-min(hist))


def buildPolymere_smart(initPolymere: str, rules: Dict[str, str], iterations: int):
    pairCounts = countPolymerePairs(initPolymere)

    pairRules = {}
    for rule in RULES.items():
        pairRules[rule[0]] = [rule[0][0]+rule[1], rule[1]+rule[0][1]]

    pairs = set()
    for k, v in pairRules.items():
        pairs.add(k)
        pairs.add(v[0])
        pairs.add(v[1])

    for _ in range(iterations):
        newPairCounts = dict(zip(
            pairs,
            [0 for _ in range(len(pairs))]
        ))

        for k, v in pairCounts.items():
            newPairCounts[pairRules[k][0]] += v
            newPairCounts[pairRules[k][1]] += v

        pairCounts = newPairCounts

    return pairCounts


def buildPolymere_BF(initPolymere: str, rules: Dict[str, str], iterations: int, log: bool = False):
    """Brute force approach to building the polymere"""
    poly = initPolymere

    for a in range(iterations):
        polyNew = poly[0]
        lastChar = poly[0]

        for i in range(1, len(poly)):
            if lastChar + poly[i] in rules:
                polyNew += rules[lastChar + poly[i]]
            polyNew += poly[i]
            lastChar = poly[i]

        poly = polyNew

        if log:
            print(f"""Finished step {a+1}. Polymere length: {len(poly)}""")

    return poly


def createHist(s: str):
    hist = {}

    for c in s:
        if c not in hist:
            hist[c] = 1
        else:
            hist[c] += 1

    return hist


def createHistFromPairCounts(pairCounts: Dict[str, int], firstPolymereElement: str):
    hist = {}

    for k in pairCounts.keys():
        hist[k[0]] = 0
        hist[k[1]] = 0

    for k, v in pairCounts.items():
        hist[k[1]] += v

    hist[firstPolymereElement] += 1

    return hist


def countPolymerePairs(polymere: str) -> Dict[str, int]:
    pairCounts = {}

    for i in range(len(polymere)-1):
        pair = polymere[i] + polymere[i+1]
        if pair in pairCounts:
            pairCounts[pair] += 1
        else:
            pairCounts[pair] = 1

    return pairCounts


def parse():
    global START_STRING, RULES
    RULES = {}
    START_STRING = ""

    lines = inp.read(14).readlines()
    START_STRING = lines[0].strip()

    for i in range(1, len(lines)):
        if lines[i] == "\n":
            continue

        a = lines[i][0:2]
        b = lines[i][6]
        RULES[a] = b


if __name__ == "__main__":
    parse()
    star1()
    star2()
