import sys
from src.apriori import Itemset
from src.apriori import getFrequentItemsets


def main():
    baskets = [
        ['coke', 'milk', 'beer'],
        ['milk', 'pepsi', 'juice'],
        ['milk', 'beer'],
        ['coke', 'juice'],
        ['milk', 'pepsi', 'beer'],
        ['coke', 'milk', 'juice', 'beer'],
        ['coke', 'beer', 'juice'],
        ['coke', 'beer'],
    ]
    itemsets = set(getFrequentItemsets(baskets, 3))
    expectedFreqeuntItemsets = {Itemset(['beer']), Itemset(['milk']), Itemset(['coke']), Itemset(['juice']), Itemset(['beer', 'milk']), Itemset(['beer', 'coke']), Itemset(['coke', 'juice'])}
    assert itemsets == expectedFreqeuntItemsets, f"Expected {expectedFreqeuntItemsets}, got {itemsets}"


if __name__ == '__main__':
    sys.path.append('E:\spark-apps\MarketBasketAnalysis\src')
    main()