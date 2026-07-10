print("Welcome to the WACC Calculator!")

def calculate_wacc(equity_value, debt_value, cost_of_equity, cost_of_debt, tax_rate):
    total_capital = equity_value + debt_value
    wacc = (equity_value / total_capital) * cost_of_equity + (debt_value / total_capital) * cost_of_debt * (1 - tax_rate)
    return wacc

print("\nPlease enter the following values:")

equity_value = float(input("Market value of equity ($): "))
debt_value = float(input("Market value of debt ($): "))
cost_of_equity = float(input("Cost of equity (as decimal, e.g., 0.10 for 10%): "))
cost_of_debt = float(input("Cost of debt (as decimal, e.g., 0.05 for 5%): "))
tax_rate = float(input("Corporate tax rate (as decimal, e.g., 0.30 for 30%): "))

wacc = calculate_wacc(equity_value, debt_value, cost_of_equity, cost_of_debt, tax_rate)

print(f"\nYour WACC is: {wacc:.2%}")
input("Press Enter to exit...")