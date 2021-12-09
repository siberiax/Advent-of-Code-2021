import sys

lines = [line.strip() for line in open(sys.argv[1]).readlines()]
nums = [int(i) for i in lines[0].split(',')]

low = min(nums)
high = max(nums)

lowest_fuel1 = 99999999999999
lowest_fuel2 = 99999999999999
for i in range(low, high+1):
    curr_fuel1 = 0
    curr_fuel2 = 0
    for el in nums:
        curr_fuel1 += abs(el-i)
        curr_fuel2 += (abs(el-i)*(abs(el-i)+1))//2
    if curr_fuel1 < lowest_fuel1:
        lowest_fuel1 = curr_fuel1
    if curr_fuel2 < lowest_fuel2:
        lowest_fuel2 = curr_fuel2

print(lowest_fuel1)
print(lowest_fuel2)
