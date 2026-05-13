# Write your code below:
filename = input("Enter the file name: ")

print("\n{:<15} {:>5} {:>12}".format("Name",
            "Hours",
            "Total Pay"))

with open(filename, "r") as file:
    for line in file:
        data = line.split()

        last = data[0]
        hours = float(data[1])
        hourly = float(data[2])


        total_pay = hourly * hours

        print("{:<15} {:>5.0f} {:>12.2f}".format( last,
            hours,
            total_pay))
