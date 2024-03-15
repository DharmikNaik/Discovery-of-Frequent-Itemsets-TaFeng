from src.data_loader import loadTestDataInList
from src.apriori import getFrequentItemsets
import time


def main():
    baskets = loadTestDataInList()
    start_time = time.time()
    frequentItemsets = getFrequentItemsets(baskets, support=50)
    end_time = time.time()
    print(frequentItemsets)
    jobDuration = end_time - start_time
    print(jobDuration)


if __name__ == '__main__':
    main()