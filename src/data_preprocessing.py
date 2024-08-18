import pandas as pd
import os


def load_and_preprocess_data(file_path, cache_path='data/preprocessed_basket.pkl'):
    if os.path.exists(cache_path):
        print(f"Loading preprocessed data from cache: {cache_path}")
        basket = pd.read_pickle(cache_path)
        print("Preprocessed data loaded successfully from cache")
    else:
        print("Loading dataset from:", file_path)
        data = pd.read_excel(file_path)
        print("Dataset loaded successfully")

        print("Grouping and aggregating data by InvoiceNo and Description")
        basket = data.groupby(['InvoiceNo', 'Description'])['Quantity'].sum().unstack().reset_index().fillna(0).set_index('InvoiceNo')

        print("Converting quantities to boolean values")
        basket = basket > 0

        print("Saving preprocessed data to cache")
        basket.to_pickle(cache_path)
        print("Preprocessed data saved to cache")

    print("Data preprocessing complete")
    return basket
