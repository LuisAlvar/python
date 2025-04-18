import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Function to calculate amortization schedule
def calculate_amortization(principal, apr, monthly_payment, months):
    schedule = []
    remaining_balance = principal
    monthly_interest_rate = apr / 12 / 100
    
    # Standard amoritzation
    for month in range(1, months + 1):
        interest = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest
        remaining_balance -= principal_payment
        schedule.append({
            'Month': month,
            'Interest Paid ($)': round(interest, 2),
            'Principal Paid ($)': round(principal_payment, 2),
            'Remaining Balance ($)': round(remaining_balance, 2)
        })
        
        # Stop if balance is paid off
        if remaining_balance <= 0:
            break
    
    return schedule

# Parameters
loan_amount = 25680.77  # Principal amount
apr = 3.90              # Annual Percentage Rate
monthly_payment = 402.21
loan_term = 72          # Total months

# Calculate amortization schedule
amortization_schedule = calculate_amortization(loan_amount, apr, monthly_payment, loan_term)

# Convert to DataFrame for tabular representation
df_schedule = pd.DataFrame(amortization_schedule)

# Add timestamp to the Excel file
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Save the amortization schedule to an Excel file
file_name = f"Amortization_Schedule_{timestamp.replace(':', '-')}.xlsx"
df_schedule.to_excel(file_name, index=False)

print(f"Excel file '{file_name}' has been successfully generated!")

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df_schedule['Month'], df_schedule['Interest Paid ($)'], label='Interest Paid ($)', color='red')
plt.plot(df_schedule['Month'], df_schedule['Principal Paid ($)'], label='Principal Paid ($)', color='green')
plt.plot(df_schedule['Month'], df_schedule['Remaining Balance ($)'], label='Remaining Balance ($)', color='blue')
plt.title("Loan Amortization Schedule")
plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.legend()
plt.grid(True)
plt.show()