# Stock Market ROI Calculator 📈
## Video: https://youtu.be/Vw2OsOA3Ul8

The **Stock Market ROI Calculator** is a web-based financial tool built using **Streamlit** that helps investors analyze stock investments and make data-driven decisions. The tool allows users to:
- Calculate **Return on Investment (ROI)** based on initial and final investment values.
- Analyze stock performance over a given period using historical stock prices.
- Estimate **future stock value** based on projected growth rates and years of investment.
- Visualize stock price trends and future projections using interactive graphs powered by **Matplotlib**.

This project serves as a useful tool for traders, investors, and financial analysts looking to assess stock market performance and estimate potential gains.


## Project Structure
The project consists of the following key files:

### 1️⃣ `project.py`
This is the **main file** that contains the Streamlit application logic and core functionalities. It includes:
- **User Interface (UI)**: Built with Streamlit, allowing users to input stock data and view analysis.
- **ROI Calculation**: Computes the percentage gain or loss of an investment.
- **Stock Performance Analysis**: Calculates the average return over a given period based on historical prices.
- **Future Value Estimation**: Uses compound interest formulas to predict stock value growth.
- **Graphical Representation**: Utilizes Matplotlib to generate real-time **stock trend and future projection graphs**.

### 2️⃣ `test_project.py`
This file contains **unit tests** for core functions, ensuring the correctness of the calculations. Using **pytest**, it verifies:
- ROI calculations are accurate.
- Stock performance analysis correctly computes average returns.
- Future stock value estimates are mathematically sound.
- Edge cases, such as zero investment values, are handled correctly.

### 3️⃣ `requirements.txt`
This file lists all required dependencies to run the project, including:
- **Streamlit** – For the interactive web interface.
- **NumPy & Pandas** – For financial calculations and data handling.
- **Matplotlib** – For graphical visualization of stock data.
- **Pytest** – For testing the integrity of the financial computations.

### 4️⃣ `README.md` (This file)
A comprehensive guide explaining the purpose, functionality, and design choices of the project.


## Design Decisions
### ✅ **Streamlit for UI**
We chose **Streamlit** for the user interface due to its simplicity in creating web apps for data science and financial modeling. It allows easy deployment and interactive input fields for users to enter stock data.

### ✅ **NumPy for Calculations**
For stock performance analysis, we rely on **NumPy** to compute **daily returns** and extract meaningful insights from historical stock prices.

### ✅ **Matplotlib for Visualization**
Financial data is best understood visually. We implemented **line charts** to display stock price trends and projected growth, making data interpretation intuitive.

### ✅ **Pytest for Testing**
To ensure **accuracy and reliability**, we implemented unit tests covering various scenarios, including:
- **Valid and invalid stock data.**
- **Edge cases such as zero investment values.**
- **Extreme growth rates and time periods.**

This approach guarantees that the tool provides **reliable financial insights** without errors.


## How to Use the Stock Market ROI Calculator 🏦

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application:**
   ```bash
   streamlit run project.py
   ```

3. **Use the Features:**
   - Enter **initial and final investment** values to calculate ROI.
   - Input **historical stock prices** (comma-separated) to analyze stock performance.
   - Provide a **growth rate and time period** to estimate future stock value.
   - View **graphs** representing stock price trends and projections.

4. **Run Tests:**
   ```bash
   pytest test_project.py
   ```


## Academic Integrity & AI Use Policy 📝
For this final project, the use of AI-based tools such as **ChatGPT, GitHub Copilot, Bing Chat and  CS50 duck**, and other similar tools is allowed. However, the essence of the work must still be **our own**. and we used this tools as **helpers** to amplify productivity, not as a complete replacement for our work.


## Future Improvements 🚀
We plan to enhance this tool with:
- **Live Stock Data Integration**: Fetch real-time stock prices using an API.
- **Portfolio Analysis**: Allow users to track multiple stocks and view aggregated performance.
- **Risk Assessment**: Implement financial risk calculations to provide insights into market volatility.


## Conclusion 🎯
The **Stock Market ROI Calculator** is a simple yet powerful tool for stock investors. It provides crucial insights into **investment returns, stock trends, and future value projections** while ensuring accuracy through rigorous testing.

By leveraging **Streamlit, NumPy, Pandas, and Matplotlib**, this project offers a streamlined solution for both novice and experienced investors looking to evaluate stock performance efficiently.

This project represents a strong foundation for further expansion, and we welcome feedback and suggestions for improvement. Happy investing! 🚀📊