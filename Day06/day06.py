# Part 1
adds = []
muls = []
total = 0
with open('Day06/day06input.txt', 'r') as lines:
    for line in lines:
        nums = line.strip().split()
        for n_index, n in enumerate(nums):
            adds.append(0)
            muls.append(1)

            if n == '*':
                total += muls[n_index]
            elif n == '+':
                total += adds[n_index]
            else:
                adds[n_index] += int(n)
                muls[n_index] *= int(n)

print(f'Part 1: {total}')