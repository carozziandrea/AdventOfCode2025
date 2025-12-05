def merge_ranges(ranges):
    if not ranges:
        return []

    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged = [sorted_ranges[0]]

    for current in sorted_ranges[1:]:
        last = merged[-1]
        if current[0] <= last[1] + 1:
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            merged.append(current)

    return merged

ranges = []
rules = True
fresh = 0
total_fresh = 0
with open('Day05/day05input.txt', 'r') as lines:
    for line in lines:
        line = line.strip()

        if not line:
            rules = False
            continue

        if rules:
            start, end = map(int, line.split('-'))
            ranges.append([start, end])
            ranges = merge_ranges(ranges)
        else:
            num = int(line)
            for r in ranges:
                if r[0] <= num <= r[1]:
                    fresh += 1
                    break

for r in ranges:
    total_fresh += (r[1] - r[0] + 1)

print(f'Part 1: {fresh}')
print(f'Part 2: {total_fresh}')