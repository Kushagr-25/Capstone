from src.data_preprocessing import load_and_preprocess_data
from src.build_rules import generate_rules
from src.recommend import recommend_products


def main():
    file_path = 'data/PreprocessedData.xlsx'

    print("Starting the recommendation system pipeline")

    # Load and preprocess data
    basket = load_and_preprocess_data(file_path)

    # Generate association rules
    rules = generate_rules(basket)

    # Example usage: Get recommendations for a specific product
    product_to_check = 'WHITE HANGING HEART T-LIGHT HOLDER'
    recommendations = recommend_products(rules, product_to_check)

    if recommendations is not None:
        print("Recommendation system pipeline completed")
    else:
        print("No recommendations were generated for the specified product.")


if __name__ == "__main__":
    main()
