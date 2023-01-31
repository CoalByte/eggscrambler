import json

db = open("words.txt", "r").read().lower().split("\n")


def similarity(x, y):
    a = [int(a == b) for (a, b) in zip(x, y)]
    return sum(a)/len(a)


length_map = [(i, len(i)) for i in db]
unique_lengths = {i: len([0 for _, v in length_map if v == i]) for i in set([i for _, i in length_map])}
# unique_lengths = {1: 27, 2: 637, 3: 4711, 4: 11171, 5: 22950, 6: 39518, 7: 52093, 8: 61019, 9: 61754, 10: 54321, 11: 46411, 12: 37524, 13: 27924, 14: 19258, 15: 12148, 16: 7115, 17: 3982, 18: 2003, 19: 1053, 20: 506, 21: 238, 22: 102, 23: 49, 24: 18, 25: 7, 26: 2, 27: 3, 28: 2, 29: 2, 31: 1, 45: 1}

difficulty_map = [
    (i, 2 * unique_lengths[len(i)]/61754 + len(i)/45) for i in db
]

Z = sorted(difficulty_map, key=lambda x: x[1])[-3000:-1:-1]  # first 3k only

output = {
    k: sum([similarity(k, i) for i, _ in Z])/len(Z) + v for k, v in Z
}

open("wordwdif.json", "w").write(json.dumps(output))
