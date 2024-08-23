from PIL import Image
import matplotlib.pyplot as plt
import os


def calculate_similarity_score(lift):
    # Example calculation, you can customize this to suit your needs
    return min(100, round(lift * 20))  # Convert lift to a percentage


def display_image(image_path, title, ax):
    try:
        img = Image.open(image_path)
        ax.imshow(img)
        ax.axis('off')
        ax.set_title(title, fontsize=10, pad=3)
    except Exception as e:
        print(f"Error displaying image: {e}")


def recommend_products(rules, product, product_images, base_image_path, top_n=5):
    print("Generating recommendations for product:", product)

    # Generate recommendations
    recommendations = rules[rules['antecedents'].apply(lambda x: product in x)]
    if recommendations.empty:
        print(f"No recommendations found for product: {product}")
        return None

    recommendations = recommendations.sort_values(by='lift', ascending=False)

    # Collect unique consequents and their best lift scores
    unique_recommendations = {}
    for _, row in recommendations.iterrows():
        for item in row['consequents']:
            if item not in unique_recommendations or row['lift'] > unique_recommendations[item]:
                unique_recommendations[item] = row['lift']

    # Limit to top_n recommendations
    top_recommendations = list(unique_recommendations.items())[:top_n]

    print("Recommendations generated")

    # Determine the number of rows needed
    num_recommendations = len(top_recommendations)
    num_columns = 2
    num_rows = (num_recommendations + num_columns - 1) // num_columns  # Ceiling division to fit all images

    # Set up a plot for displaying all images in two columns
    fig, axes = plt.subplots(num_rows, num_columns, figsize=(8, 4 * num_rows))
    axes = axes.flatten()  # Flatten the array of axes for easy iteration

    # Hide any extra axes
    for ax in axes[num_recommendations:]:
        ax.axis('off')

    for i, (item, lift) in enumerate(top_recommendations):
        image_filename = product_images.get(item, None)
        if image_filename:
            full_image_path = os.path.join(base_image_path, image_filename)
            similarity_score = calculate_similarity_score(lift)
            title = f"{item} - Similarity: {similarity_score}%"
            display_image(full_image_path, title, axes[i])
        else:
            print(f"- {item}: Image not found")

    plt.tight_layout()
    plt.show()

    return top_recommendations
