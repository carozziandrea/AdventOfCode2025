total_jolts = 0
with open('Day03/day03input.txt', 'r') as lines:
    for line in lines:
        bank = [int(x) for x in list(line.strip())]
        #print(bank)
        battery1 = max(bank[:len(bank)-1])
        battery1pos = bank.index(battery1)
        battery2 = max(bank[battery1pos+1:])

        jolts = str(battery1) + str(battery2)
        #print(jolts)
        total_jolts += int(jolts)

print(f'Part 1: {total_jolts}')

def get_largest_subsequence(digits_list, k):
    stack = []
    drop_count = len(digits_list) - k
    
    for digit in digits_list:
        while stack and digit > stack[-1] and drop_count > 0:
            stack.pop()
            drop_count -= 1
        stack.append(digit)
        
    return stack[:k]

total_sum = 0
with open('Day03/day03input.txt', 'r') as lines:
    for line in lines:
        line = line.strip()
        if not line: continue
        
        bank = [int(x) for x in list(line)]
        
        result_list = get_largest_subsequence(bank, 12)
        
        result_string = "".join(map(str, result_list))
        result_num = int(result_string)
        
        total_sum += result_num

print(f"Part 2: {total_sum}")