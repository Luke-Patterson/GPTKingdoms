import random
from templates.region import region_symbols

def gen_random_terrain_probs():
    # Invert the dictionary (swap keys and values)
    inverted_region_symbols = {symbol: region_name for region_name, symbol in region_symbols.items()}

    # Generate random numbers that sum to 1
    random_weights = [random.uniform(0, 1) for _ in range(len(inverted_region_symbols))]
    sum_weights = sum(random_weights)
    normalized_weights = [weight / sum_weights for weight in random_weights]
    # Replace the values with the random weights
    weighted_region_symbols = {symbol: weight for symbol, weight in
                               zip(inverted_region_symbols.keys(), normalized_weights)}

    return weighted_region_symbols