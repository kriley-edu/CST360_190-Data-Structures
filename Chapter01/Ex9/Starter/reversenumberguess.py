def main():
    print("Think of a number, and I will try to guess it.")

    low = int(input("Enter the smaller number: "))
    high = int(input("Enter the larger number: "))

    guesses = 0

    # Maximum guesses needed using binary search
    maxGuesses = round((high - low) + 1)

    while True:
        guesses += 1

        # Computer makes a guess
        guess = (low + high) // 2
        print("Your number is", guess)

        # User gives a hint
        hint = input("Enter =, <, or >: ")

        if hint == "=":
            print("Hooray, I've got it in", guesses, "tries!")
            break

        elif hint == "<":
            high = guess - 1

        elif hint == ">":
            low = guess + 1

        else:
            print("Invalid input. Please enter =, <, or >.")

        # Detect cheating or impossible answers
        if guesses >= maxGuesses or low > high:
            print("You're cheating!")
            break


if __name__ == "__main__":
    main()
