from functools import cache

def run(file_name):
    towels = set()
    requests = []
    with open(file_name, 'r') as file:
        for idx, line in enumerate(file):
            if idx == 0:
                tmp = line.split(",")
                for t in tmp:
                    towels.add(t.strip())
            elif line != '\n':
                requests.append(line.replace('\n','').strip())

    
    @cache
    def find_match_in_towels(request, idx=0):
        if idx == len(request):
            return 1
    
        res = 0
        # check each towel rather than each character up to max_towel size (I think this is an overall win, computation-wise)
        for towel in towels:
            l = len(towel)
            # Does the currently being checked section of the request match the current towel
            if request[idx:idx+l] == towel:
                # If we have a match, increment the index by the size of the towel that matched and try the next section
                res += find_match_in_towels(request, idx+l)

        return res

    result1 = 0
    result2 = 0
    for request in requests:
        # Updated after P2, just count each request which had at least 1 result (P1) and also all combos (P2)
        res = find_match_in_towels(request)
        result2 += res
        if res:
            result1 += 1

    print(f"Day 19 - Part 1: {result1}")
    print(f"Day 19 - Part 2: {result2}")
