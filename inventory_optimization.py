import pandas as pd
import numpy as np

def calculate_safety_stock(std_dev, lead_time, service_factor=1.65):
    return service_factor * std_dev * np.sqrt(lead_time)

def calculate_optimal_inventory_levels(data, lead_time=2):
    data['Safety_Stock'] = calculate_safety_stock(data['demand'].std(), lead_time)
    data['Reorder_Point'] = data['demand'].mean() * lead_time + data['Safety_Stock']
    data['Optimal_Inventory'] = data['Reorder_Point'] + data['Safety_Stock']
    return data

if __name__ == "__main__":
    data = pd.read_csv('../data/historical_inventory_data.csv')
    data = calculate_optimal_inventory_levels(data)
    data.to_csv('../data/optimized_inventory_data.csv', index=False)
