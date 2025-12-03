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