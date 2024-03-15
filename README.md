# Discovery of Frequent Itemsets in Ta-feng transactions for Recommendations
## Problem
The problem of discovering frequent itemsets in transaction data involves finding set of items that appear in 'many' baskets/transactions. Formally, we assume there is a number s, called the support threshold. If
I is a set of items, the support for I is the number of baskets/transactions for which I is a
subset. We say I is frequent if its support is s or more. The complexity of discovering frequent itemsets arises from the fact that the number of baskets is very large, bigger than what can fit in main memory. Also, it is regarded as a computationally expensive problem. 
 
## Terminologies:
### Market-Basket model of data
It is a many-many relationship between items and baskets (representing items bought by a customer in a single transaction).

## Savasere, Omiecinski, and Navathe (SON) algorithm
Since the number of transactions is usually astronomical, it is safe to assume that the transactions are stored in a distributed file system like HDFS. Hence, distributed computing or distributed algorithms (divide the work among many processors, each processor processes a subset of transactions) seem a natural fit to solve the problem. Dividing the work among the processors in the clusters seems very natural and intuitive but combining the work of multiple processors to get the exact collection of itemsets that meet a global support threshold is difficult. SON algorithm propose a solution to this problem. Unlike many approximation algorithms that yield false positives and false negative, SON algorithm yields the exact collection of frequent itemsets at the cost of 2 passes over the data. The idea of the algorithm is to process each chunk of data on a processor to find the local frequent itemsets using some in-memory algorithms like Apriori, PCY, Multistage, Multihash using a scaled-down support threshold to account for the fact that these algorithms run on sample/subset of original data. Once all frequent itemsets have been found for the samples/subsets, take a union of these (which we call candidate frequent itemsets) and make a second pass over the transactions in same distributed fashion to accumulate the support of each candidate frequent itemset and then prune the itemsets that don't meet the global support threshold. We have utilized PySpark framework for distributed computing and implementation of the SON algorithm. 

### Options for in-memory frequent itemset discovery algorithms
#### Apriori
It relies on the idea of monotonicity of itemsets: If a set I of items is frequent, then so is every subset of I. It starts by finding frequent itemsets of size 1 (which is trivial) and builds frequent itemsets of size 2, 3, 4 and so on at each iteration of algorithms. It makes a pass over the entire data in every iteration. If frequent itemsets of a certain size, say k,  are not found, we stop the algorithm as idea of monotonicity tells that frequent itemsets of size k+1 cannot exist. The pattern of moving from frequent itemsets of size k to size k+1 is described by this pattern:
1. C<sub>k</sub> is the set of candidate itemsets of size k - frequency of each candidate must be counted  to determine if they are truly frequent.
2. L<sub>k</sub> is the set of true frequent itemsets of size k.

The pattern of moving from itemsets of size k to the next is suggested in below figure:

The pattern involves generating the candidate set C<sub>k+1</sub> from the set L<sub>k</sub> using the idea of monotonicity and then pruning/filtering items from C<sub>k+1</sub> based on support threshold to generate the L<sub>k+1</sub> set. 

## Future directions
1. Substitute apriori algorithm with other more efficient in-memory algorithms like PCY (Park, Chen, and Yu
), Multistage, Multihash algorithm to improve the runtime of the job.
2. Improve the code structure to enhance modularity, readability and maintainability of the codebase.
3. Incorporate coding best practices.
4. Explore and implement various approximate algorithms to solve the problem at hand.
5. Explore and Toivenen's algorithm (a randomized algorithm) to solve the problem at hand.
6. Benchmark and compare performance and resource utilization of various algorithms (listed above).
7. Improve logging and monitoring to enhance observability.
8. Apply the solution for other problems/applications (discussed in next section).
9. Instead of a file of transactions, deal with a stream of transactions to mine the frequent itemsets. This problem is more realistic.

## Other applications:
1. Finding related concepts in a set of documents/blogs/tweets.
2. Detecting plagarism
3. Detecting biomarkers

## References:
1. [Mining of Massive Datasets - Jure Leskovec, Anand Rajaraman, Jeff Ullman](http://www.mmds.org/#ver21)
2. [An Efficient Algorithm for Mining Association Rules in Large Databases](https://www.vldb.org/conf/1995/P432.PDF)
3. [Fast Algorithms for Mining Association Rules](https://www.vldb.org/conf/1994/P487.PDF)