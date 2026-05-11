# Write your code below:
filename = input("Enter the file name: ")

print("\nPayroll Report")
print("{:<12} {:<12} {:<12}".format("Last Name:",
            "Hours Worked:",
            "Wages Paid:"))

with open(filename, "r") as file:
    for line in file:
        data = line.split()

        last_name = data[0]
        hourly_wage = float(data[1])
        hours_worked = float(data[2])

        wages_paid = hourly_wage * hours_worked

        print("{:<12} {:<12.2f} ${:<11.2f}".format( last_name,
            hours_worked,
            wages_paid))
