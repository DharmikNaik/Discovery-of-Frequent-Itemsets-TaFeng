
import unittest
from src.apriori import generateSingletonItemsets, generateCandidateItemsets, getItemsetsFrequency, pruneInfrequentItemsets, getFrequentItemsets
from src.itemset import Itemset


class TestAprioriImplementation(unittest.TestCase):

    def setUp(self):
        self.baskets = [['apple', 'banana'], ['banana', 'orange'], ['apple', 'orange'], ['apple', 'banana', 'orange']]
        self.support = 2

    def test_generate_singleton_itemsets(self):
        expected_counts = {Itemset(['apple']): 3, Itemset(['banana']): 3, Itemset(['orange']): 3}
        singleton_itemsets = generateSingletonItemsets(self.baskets)
        self.assertEqual(singleton_itemsets, expected_counts)

    def test_generate_candidate_itemsets(self):
        frequent_itemsets = [Itemset(['apple']), Itemset(['banana']), Itemset(['orange'])]
        candidate_itemsets = generateCandidateItemsets(self.baskets, 2, frequent_itemsets)
        expected_candidates = {Itemset(['apple', 'banana']): 2, Itemset(['apple', 'orange']): 2, Itemset(['banana', 'orange']): 2}
        self.assertEqual(candidate_itemsets, expected_candidates)

    def test_get_itemsets_frequency(self):
        itemsets = [Itemset(['apple', 'banana']), Itemset(['apple', 'orange']), Itemset(['banana', 'orange'])]
        frequencies = getItemsetsFrequency(itemsets, self.baskets)
        expected_frequencies = {Itemset(['apple', 'banana']): 2, Itemset(['apple', 'orange']): 2, Itemset(['banana', 'orange']): 2}
        self.assertEqual(frequencies, expected_frequencies)

    def test_prune_infrequent_itemsets(self):
        candidate_itemsets = {Itemset(['apple', 'banana']): 2, Itemset(['apple', 'orange']): 1, Itemset(['banana', 'orange']): 3}
        frequent_itemsets = pruneInfrequentItemsets(candidate_itemsets, self.support)
        expected_frequent_itemsets = [Itemset(['apple', 'banana']), Itemset(['banana', 'orange'])]
        self.assertEqual(frequent_itemsets, expected_frequent_itemsets)

if __name__ == '__main__':
    unittest.main()
