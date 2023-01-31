import json
import random

db = json.load(open("wordwdif.json", "r"))
Z = sorted(db, key=lambda x: x[1])

difficulty = 14  # n for select only 0-n hardest words
output_size = 5

Q = [random.choice(Z[0:difficulty]) for _ in range(output_size)]
f = ' '.join(''.join(Q)).split(" ")
random.shuffle(f)

print("Question:", ''.join(f), f"({len(f)} )")
print("Answer:", ' '.join(Q))
