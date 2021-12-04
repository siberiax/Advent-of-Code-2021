import sys

lines = open(sys.argv[1]).readlines()

hor = 0
vert = 0
aim = 0

for line in lines:
    fields = line.strip().split()
    if fields[0] == "forward":
        hor += int(fields[1])
        vert += int(fields[1]) * aim
    elif fields[0] == "up":
        # vert -= int(fields[1])
        aim -= int(fields[1])
    else:
        # vert += int(fields[1])
        aim += int(fields[1])

print(hor*vert)
