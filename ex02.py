import itertools as it
import timeit

def main():
    ids = range(1, 46)
    with open('d:\\list2.txt','w') as f:
        for i, v in enumerate(it.combinations(ids, 7), 1):
            if i % 1000000 == 0:
                print(i)
            else:
                f.write('{}\n'.format(v))

print(timeit.timeit(main, number=1))
# 80 초