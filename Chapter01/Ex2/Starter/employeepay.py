# Write your code below:

def main():

    # Get user input
    wage = float(input("Enter hourly wage: "))
    reg_hours = float(input("Enter regular hours worked: "))
    ot_hours = float(input("Enter overtime hours worked: "))

    # Calculate regular wages
    reg_pay = wage * reg_hours
    # Calculate OT wages
    ot_pay = ot_hours * wage * 1.5
    # Calculate total pay
    total_pay = reg_pay + ot_pay

    # Display total pay
    print(f"\nEmployee's total weekly pay: ${total_pay:.2f}")


if __name__ == "__main__":
    main()
