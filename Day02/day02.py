def isValidID(id):
    l = 0
    r = 1
    s = 1
    repeated = False
    curSequence = id[l:r]
    while (s < len(id)):
        candidate = id[s:s+len(curSequence)]
        if curSequence == candidate:
            s += len(curSequence)
            repeated = True
        else:
            r += 1
            curSequence = id[l:r]
            s = r
            repeated = False
    
    return repeated


totalIds = 0
with open('Day02/day02input.txt', 'r') as lines:
    for line in lines:
        ids = line.strip().split(',')

        for pair in ids:
            first, second = pair.split('-')
            for id in range(int(first), int(second)+1):
                if isValidID(str(id)):
                    totalIds += id

print(totalIds)