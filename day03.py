import sys

lines = [line.strip() for line in open(sys.argv[1]).readlines()]

highest = 2**len(lines[0])-1

final = ""
co2 = ""
o2 = ""

for i in range(len(lines[0])) :
    one = 0
    zero = 0
    o2one = 0
    o2zero = 0
    co2one = 0
    co2zero = 0
    for line in lines:
        if line[i] == '1':
            one += 1
        else:
            zero += 1

        if line[:i] == o2:
            if line[i] == '1':
                o2one += 1
            else:
                o2zero += 1

        if line[:i] == co2:
            if line[i] == '1':
                co2one += 1
            else:
                co2zero += 1
    if one > zero:
        final += '1'
    else:
        final += '0'

    if o2one + o2zero > 1:
        if o2one >= o2zero:
            o2 += '1'
        else:
            o2 += '0'
    else:
        if o2one:
            o2 += '1'
        else:
            o2 += '0'

    if co2one + co2zero > 1:
        if co2one >= co2zero:
            co2 += '0'
        else:
            co2 += '1'
    else:
        if co2one:
            co2 += '1'
        else:
            co2 += '0'

n = int(final, 2)
o = int(o2, 2)
c = int(co2, 2)

print(n * (highest-n))
print(o*c)
