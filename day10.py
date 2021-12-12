import sys

lines = [line.strip() for line in open(sys.argv[1]).readlines()]

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

match = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

okay = []

score = 0
for line in lines:
    stack = []
    good = True
    for c in line:
        if c in '([{<':
            stack.append(c)
        else:
            if match[c] != stack.pop():
                score += points[c]
                good = False
                break
    if good:
        okay.append(stack)

print(score)

points = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

scores = []

for end in okay:
    end.reverse()
    score = 0
    for el in end:
        score *= 5
        score += points[el]
    scores.append(score)

scores.sort()

print(scores[len(scores)//2])
