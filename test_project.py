import pytest
from project import calculate_return_on_investment, analyze_stock_performance, estimate_future_value

def test_calculate_return_on_investment():
    assert calculate_return_on_investment(1000, 1200) == 20.0
    assert calculate_return_on_investment(500, 750) == 50.0
    assert calculate_return_on_investment(0, 1000) is None  

def test_analyze_stock_performance():
    historical_prices = [100, 105, 110, 120, 130]
    assert analyze_stock_performance(historical_prices, 3) is not None
    assert analyze_stock_performance(historical_prices, 10) is None  
    prices = [50, 52, 54, 58, 60, 65, 70]
    assert analyze_stock_performance(prices, 5) > 0  # Expected positive growth

def test_estimate_future_value():
    assert estimate_future_value(100, 10, 3) == pytest.approx(133.1, rel=1e-2)  
    assert estimate_future_value(50, 5, 2) == pytest.approx(55.13, rel=1e-2) 
    assert estimate_future_value(200, 0, 10) == 200  