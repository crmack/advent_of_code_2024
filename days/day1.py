import pandas as pd

def calc_distances(left, right):
    left.sort()
    right.sort()
    distances = [abs(a-b) for a,b in zip(left,right)]
    return distances


def calc_counts(left, right):
    count_prods = [l * right.count(l) for l in left]
    return sum(count_prods)


def run(file_name):
    f = open(file_name, "r")
    left_side = []
    right_side = []
    for line in f:
        parts = line.split(None)
        left_side.append(int(parts[0]))
        right_side.append(int(parts[1]))

    distances = calc_distances(left_side, right_side)
    count_prod_result = calc_counts(left_side, right_side)

    print("Day 1 - Part 1: " + str(sum(distances)))
    print("Day 1 - Part 2: " + str(count_prod_result))
    f.close()


def run_pd(file_name):
    df = pd.read_csv(file_name, sep='   ', header=None, engine='python')
    df['diff'] = abs(df[0].sort_values(ignore_index=True) - df[1].sort_values(ignore_index=True))
    print(f"Day 1 - Part 1: {df['diff'].abs().sum()}")

    df['count'] = df[0].map(df[1].value_counts()).fillna(0)
    df['count_prod'] = df[0] * df['count']
    print(f"Day 1 - Part 2: {df['count_prod'].sum().astype(int)}")
