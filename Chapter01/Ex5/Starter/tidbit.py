# Write your code below:
purchase_price = float(input("Enter the purchase price: "))

down_payment = purchase_price * 0.10
annual_interest_rate = 0.12
monthly_payment = (purchase_price - down_payment) * 0.05
monthly_interest_rate = annual_interest_rate / 12
balance = purchase_price - down_payment

print("\nPayment Schedule")
print(f"Purchase Price: ${purchase_price:,.2f}")
print(f"Down Payment:   ${down_payment:,.2f}")
print(f"Monthly Payment: ${monthly_payment:,.2f}\n")

print("{:<8} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
    "Month", "Balance", "Interest", "Principal", "Payment", "New Balance"
))

month = 1

while balance > 0:
    interest = balance * monthly_interest_rate
    principal = monthly_payment - interest

    # Prevent overpayment in the final month
    if principal > balance:
        principal = balance
        monthly_payment = interest + principal

    new_balance = balance - principal

    print("{:<8} ${:<14.2f} ${:<14.2f} ${:<14.2f} ${:<14.2f} ${:<14.2f}".format(
        month, balance, interest, principal, monthly_payment, new_balance
    ))

    balance = new_balance
    month += 1
