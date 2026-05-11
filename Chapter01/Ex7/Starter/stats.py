# Write your code below:

def mean(numbers):
    return sum(numbers) / len(numbers)


def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    midpoint = n // 2

    # Check if the list length is even
    if n % 2 == 0:
        return (sorted_numbers[midpoint - 1] + sorted_numbers[midpoint]) / 2
    else:
        return sorted_numbers[midpoint]


def mode(numbers):
    frequency = {}

    # Count how many times each number appears
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    # Find the highest frequency
    highest_count = max(frequency.values())

    # Return the first number with the highest frequency
    for number, count in frequency.items():
        if count == highest_count:
            return number


def main():
    """Tests the functions."""
    lyst = []
    
    for i in range(6):
        lyst.append(int(input('Enter a Value for the list: ')))

    print("List:", lyst)
    print("Mode:", mode(lyst))
    print("Median:", median(lyst))
    print("Mean:", mean(lyst))


if __name__ == "__main__":
    main()