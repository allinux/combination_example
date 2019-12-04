import itertools as it
import timeit

def main():
    ids = range(1, 46)
    with open('d:\\list.txt','w',encoding='euc-kr') as f:
        temp = []
        for i, v in enumerate(it.combinations(ids, 7), 1):
            if i % 100000 == 0:
                f.write("\n".join(temp))
                temp.clear()
            if i % 1000000 == 0:
                print(i)
            else:
                temp.append('{}'.format(v))

print(timeit.timeit(main, number=1))
# 56초
