import sys

lines = [int(i.strip()) for i in open(sys.argv[1]).readlines()]

curr = 0
inc = 0

for num in lines:
    if curr and num > curr:
        inc += 1
    curr = num

print(inc)

curr = 0
inc = 0
for i in range(len(lines) - 2):
    total = sum(lines[i:i+3])
    if curr and total > curr:
        inc += 1
    curr = total

print(inc)
