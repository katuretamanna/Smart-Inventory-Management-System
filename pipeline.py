import pandas as pd
from sqlalchemy import create_engine

def load_and_transform_data(filepath):
    # Load data
    data = pd.read_csv(filepath)
    # Data cleaning and transformation
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.sort_values('Date')
    return data

def store_data_to_db(data, db_url):
    # Connect to database and store data
    engine = create_engine(db_url)
    data.to_sql('inventory_data', con=engine, index=False, if_exists='replace')

if __name__ == "__main__":
    data = load_and_transform_data('../data/historical_inventory_data.csv')
    store_data_to_db(data, 'postgresql://user:password@localhost/inventory_db')
