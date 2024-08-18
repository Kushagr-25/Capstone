from mlxtend.frequent_patterns import fpgrowth, association_rules


def generate_rules(basket, min_support=0.01, min_threshold=1):
    print("Generating frequent itemsets using the FP-Growth algorithm")
    frequent_itemsets = fpgrowth(basket, min_support=min_support, use_colnames=True)
    print("Frequent itemsets generated")

    print("Generating association rules from frequent itemsets")
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=min_threshold)
    print("Association rules generated")

    return rules
