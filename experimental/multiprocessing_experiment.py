import multiprocessing as mp
import random


def obscene_overcalculation(x):
    blast = [random.randint(0, 1E6) for element in range(x)]
    blorst = sum(blast[0::2]) - sum(blast[1::2])
    return blorst


if __name__ == '__main__':
    pool = mp.Pool(processes=4)
    results = pool.map(obscene_overcalculation, range(0, 10))

    print(results)

    pool.close()
    pool.join()
