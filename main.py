from src.data_preprocessing import load_and_preprocess_data
from src.build_rules import generate_rules
from src.recommend import recommend_products
import pandas as pd

def main():
    file_path = 'data/PreprocessedData.xlsx'
    image_file_path = 'data/unique_items_with_images.csv'
    base_image_path = 'content/images'  # Set this to the directory containing your images

    print("Starting the recommendation system pipeline")

    # Load and preprocess data
    basket = load_and_preprocess_data(file_path)

    # Load product images data
    product_images_df = pd.read_csv(image_file_path)
    product_images = dict(zip(product_images_df['Description'], product_images_df['Image_File']))

    # Generate association rules
    rules = generate_rules(basket)

    # Example usage: Get recommendations for a specific product
    product_to_check = 'WOODEN FRAME ANTIQUE WHITE '
    recommendations = recommend_products(rules, product_to_check, product_images, base_image_path)

    if recommendations is not None:
        print("Recommendation system pipeline completed")
    else:
        print("No recommendations were generated for the specified product.")


if __name__ == "__main__":
    main()
