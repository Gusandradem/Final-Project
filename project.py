import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_return_on_investment(initial_investment, final_value):
    """Calculates Return on Investment (ROI) as a percentage."""
    if initial_investment == 0:
        return None  
    roi = ((final_value - initial_investment) / initial_investment) * 100
    return round(roi, 2)

def analyze_stock_performance(historical_prices, period):
    """Analyzes stock performance by calculating average return over a period."""
    if len(historical_prices) < period:
        return None 
    returns = np.diff(historical_prices) / historical_prices[:-1] * 100
    avg_return = np.mean(returns[-period:])
    return round(avg_return, 2)

def estimate_future_value(current_value, growth_rate, years):
    """Estimates future stock value based on constant annual growth rate."""
    future_value = current_value * ((1 + (growth_rate / 100)) ** years)
    return round(future_value, 2)

def main():
    """Streamlit main function to interact with the user."""
    st.title("Stock Market ROI Calculator 📈")
    
    st.header("Calculate ROI")
    initial_investment = st.number_input("Initial Investment ($)", min_value=0.0, format="%.2f")
    final_value = st.number_input("Final Value ($)", min_value=0.0, format="%.2f")
    if st.button("Calculate ROI"):
        roi = calculate_return_on_investment(initial_investment, final_value)
        if roi is not None:
            st.success(f"Return on Investment: {roi}%")
        else:
            st.error("Initial investment cannot be zero.")
    
    st.header("Analyze Stock Performance")
    historical_prices = st.text_area("Enter historical prices (comma-separated)")
    period = st.number_input("Period (days)", min_value=1, step=1)
    if st.button("Analyze Performance"):
        try:
            prices = list(map(float, historical_prices.split(',')))
            avg_return = analyze_stock_performance(prices, period)
            if avg_return is not None:
                st.success(f"Average Return over {period} days: {avg_return}%")
                
                plt.figure(figsize=(10, 5))
                plt.plot(prices, marker='o', linestyle='-', color='b', label='Stock Prices')
                plt.xlabel("Time (Days)")
                plt.ylabel("Price ($)")
                plt.title("Stock Price Trend")
                plt.legend()
                st.pyplot(plt)
            else:
                st.error("Not enough data points for the selected period.")
        except ValueError:
            st.error("Please enter valid numerical prices separated by commas.")
    
    st.header("Estimate Future Stock Value")
    current_value = st.number_input("Current Stock Price ($)", min_value=0.0, format="%.2f")
    growth_rate = st.number_input("Expected Annual Growth Rate (%)", format="%.2f")
    years = st.number_input("Years into Future", min_value=1, step=1)
    if st.button("Estimate Future Value"):
        future_value = estimate_future_value(current_value, growth_rate, years)
        st.success(f"Estimated Future Value: ${future_value}")
        
        years_range = np.arange(0, years + 1, 1)
        future_values = [estimate_future_value(current_value, growth_rate, y) for y in years_range]
        
        plt.figure(figsize=(10, 5))
        plt.plot(years_range, future_values, marker='o', linestyle='-', color='g', label='Projected Growth')
        plt.xlabel("Years")
        plt.ylabel("Estimated Value ($)")
        plt.title("Future Stock Value Projection")
        plt.legend()
        st.pyplot(plt)

if __name__ == "__main__":
    main()