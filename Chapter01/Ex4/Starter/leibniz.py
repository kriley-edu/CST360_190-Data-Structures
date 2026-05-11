# Write your code below:
def main():
    iterations = int(input("Enter number of iterations: "))

    pi_approx = 0.0

    for i in range(iterations):
        term = ((-1) ** i) / (2 * i + 1)
        pi_approx += term

    pi_approx *= 4

    print(f"\nApproximation of π: {pi_approx:.10f}")


if __name__ == "__main__":
    main()
