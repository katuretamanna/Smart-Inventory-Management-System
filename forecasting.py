import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def train_forecasting_model(data):
    train, test = train_test_split(data, test_size=0.2, shuffle=False)
    model = ExponentialSmoothing(train['demand'], trend='add', seasonal='add', seasonal_periods=12).fit()
    forecast = model.forecast(len(test))
    mae = mean_absolute_error(test['demand'], forecast)
    print(f'Mean Absolute Error: {mae}')
    return model, forecast

if __name__ == "__main__":
    data = pd.read_csv('../data/historical_inventory_data.csv')
    data['Date'] = pd.to_datetime(data['Date'])
    model, forecast = train_forecasting_model(data)
