class Itemset:
    def __init__(self, items):
        # ensures the immutability of itemset
        self.items = frozenset(items)

    def __hash__(self):
        return hash(self.items)

    def __eq__(self, other):
        return self.items == other.items

    def __repr__(self):
        return f"{self.items}"

    def combine(cls, itemset1, itemset2):
        return cls(itemset1.items.union(itemset2.items))

    def is_subset_of(self, basket):
        return self.items.issubset(basket)
