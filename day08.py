import sys

lines = [line.strip() for line in open(sys.argv[1]).readlines()]

unique = [2,3,4,7]

total = 0
for line in lines:
    fields = line.split(' | ')
    for w in fields[1].split():
        if len(w) in unique:
            total += 1

print(total)

chars = 'abcdefg'
total = 0
for line in lines:

    tm = ''
    tl = ''
    tr = ''
    m = ''
    bl = ''
    br = ''
    bm = ''

    fields = line.split(' | ')
    input = fields[0].split()
    output = fields[1].split()

    l2 = ''
    l3 = ''
    l4 = ''
    l5 = []
    l6 = []
    l7 = ''
    for w in input:
        if len(w) == 2:
            l2 = w
        elif len(w) == 3:
            l3 = w
        elif len(w) == 4:
            l4 = w
        elif len(w) == 5:
            l5.append(w)
        elif len(w) == 6:
            l6.append(w)
        else:
            l7 = w

    for c in l3:
        if c not in l2:
            tm = c

    for c in chars:
        if all(c in w for w in l5) and c in l4:
            m = c

    for w in l6:
        for c in chars:
            if c not in w and c in l2:
                tr = c

    for c in l2:
        if c != tr:
            br = c

    for w in l5:
        if tm in w and tr in w and m in w and br in w:
            for c in w:
                if c not in [tm,tr,m,br]:
                    bm = c

    for c in l4:
        if c not in [tr,m,br]:
            tl = c

    for c in chars:
        if c not in [tm,tl,tr,m,br,bm]:
            bl = c

    n0 = ''.join(sorted([tm, tl, tr, bl, br, bm]))
    n1 = ''.join(sorted([tr,br]))
    n2 = ''.join(sorted([tm, tr, m, bl, bm]))
    n3 = ''.join(sorted([tm, tr, m, br, bm]))
    n4 = ''.join(sorted([tl, tr, m, br]))
    n5 = ''.join(sorted([tm, tl, m, br, bm]))
    n6 = ''.join(sorted([tm, tl, m, bl, br, bm]))
    n7 = ''.join(sorted([tm, tr, br]))
    n8 = ''.join(sorted([tm, tl, tr, m, bl, br, bm]))
    n9 = ''.join(sorted([tm, tl, tr, m, br, bm]))

    nums = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]

    final = ''
    for word in output:
        s = ''.join(sorted(word))
        for i in range(len(nums)):
            if nums[i] == s:
                final += str(i)

    total += int(final)

print(total)
