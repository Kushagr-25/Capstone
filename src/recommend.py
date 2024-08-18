def recommend_products(rules, product, top_n=5):
    print("Generating recommendations for product:", product)
    recommendations = rules[rules['antecedents'].apply(lambda x: product in x)]
    if recommendations.empty:
        print(f"No recommendations found for product: {product}")
        return None

    recommendations = recommendations.sort_values(by='lift', ascending=False)
    top_recommendations = recommendations.head(top_n)

    print("Recommendations generated")
    for index, row in top_recommendations.iterrows():
        print(f"Recommended products for '{product}': {', '.join(list(row['consequents']))} with lift: {row['lift']:.2f}")

    return top_recommendations
