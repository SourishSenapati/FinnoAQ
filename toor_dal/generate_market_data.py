"""
Generates synthetic market data for Toor Dal Analysis.
"""
import pandas as pd
import numpy as np


def generate_indian_market_data():
    """
    Creates a CSV file with weekly price data for 2024-2025.
    Models seasonality, shocks, and regional variance.
    """
    # Date range: Jan 2024 to Dec 2025 (Weekly data)
    dates = pd.date_range(start='2024-01-01', end='2025-12-31', freq='W-MON')
    n = len(dates)

    # Base Price for Tur Khanda (Brokens) - usually 60-70% of whole dal price
    base_price = 65.0  # INR/kg

    # Seasonality: Harvest in Dec-Jan (Low Price), Peak in Oct (High Price)
    # Sine wave peaking in October (Month 10)
    # 2*pi * (month - 1) / 12
    dates_series = pd.Series(dates)
    months = dates_series.dt.month.values
    seasonality = np.sin(2 * np.pi * (months - 1) / 12 -
                         np.pi/2) * 5.0  # +/- 5 INR swing

    # Regional Variance (Maharashtra is hub, Karnataka slightly different, Delhi consumer market)
    price_maha = base_price + seasonality + np.random.normal(0, 2.0, n)
    price_karnataka = base_price + seasonality + \
        np.random.normal(0, 2.5, n) - 2.0  # Slightly cheaper
    price_delhi = base_price + seasonality + \
        np.random.normal(0, 3.0, n) + 5.0  # Transport cost

    # Supply Shocks (Random spikes due to rain/drought)
    # Let's add a random shock in mid 2024
    shock_index = np.random.choice(range(20, n-20), 1)[0]
    shock_magnitude = np.random.uniform(5, 15)
    # Decay the shock over 10 weeks
    shock_profile = np.exp(-np.arange(0, 10)) * shock_magnitude

    # Apply shock
    if shock_index + 10 < n:
        price_maha[shock_index:shock_index+10] += shock_profile
        price_karnataka[shock_index:shock_index+10] += shock_profile
        price_delhi[shock_index:shock_index+10] += shock_profile

    df = pd.DataFrame({
        'Date': dates,
        'Price_Maharashtra_Akola': price_maha,
        'Price_Karnataka_Gulbarga': price_karnataka,
        'Price_Delhi_Mandi': price_delhi
    })

    output_path = "d:/PROJECT/FINNO PROJECTS/toor_dal/indian_market_data_2024_2025.csv"
    df.to_csv(output_path, index=False)
    print(f"Market Data Generated at: {output_path}")


if __name__ == "__main__":
    generate_indian_market_data()
