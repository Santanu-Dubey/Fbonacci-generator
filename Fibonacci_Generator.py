def generate_fibonacci(n):

    if n <= 0:
        return []

    if n == 1:
        return [0]

    fibonacci_series = [0, 1]

    for _ in range(2, n):
        fibonacci_series.append(
            fibonacci_series[-1] + fibonacci_series[-2]
        )

    return fibonacci_series


def main():
    print("=" * 40)
    print("      FIBONACCI GENERATOR")
    print("=" * 40)

    try:
        n = int(input("Enter number of terms: "))

        if n <= 0:
            print("Please enter a positive integer.")
            return

        result = generate_fibonacci(n)

        print("\nFibonacci Series:")
        print(*result)

    except ValueError:
        print("Invalid input! Please enter an integer.")


if __name__ == "__main__":
    main()