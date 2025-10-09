import math
#this is square root function
def square_root(x):
    """Calculates the square root of a number."""
    if x < 0:
        return "Error: Cannot calculate square root of a negative number."
    return math.sqrt(x)

def factorial(x):
    """Calculates the factorial of a number."""
    if x < 0:
        return "Error: Factorial is not defined for negative numbers."
    if not isinstance(x, int):
        return "Error: Factorial is only defined for integers."
    return math.factorial(x)

def natural_log(x):
    """Calculates the natural logarithm of a number."""
    if x <= 0:
        return "Error: Natural logarithm is only defined for positive numbers."
    return math.log(x)

def power(base, exponent):
    """Calculates the power of a number."""
    return math.pow(base, exponent)

def main():
    """Main function to run the calculator menu."""
    while True:
        print("\n--- Scientific Calculator Menu ---")
        print("1. Square Root (√x)")
        print("2. Factorial (!x)")
        print("3. Natural Logarithm (ln(x))")
        print("4. Power Function (x^b)")
        print("5. Exit")

        try:
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                # Square root function - √x [cite: 5]
                num = float(input("Enter a number: "))
                print(f"Result: {square_root(num)}")
            
            elif choice == '2':
                # Factorial function - !x [cite: 6]
                num = int(input("Enter an integer: "))
                print(f"Result: {factorial(num)}")

            elif choice == '3':
                # Natural logarithm (base - e) In(x) [cite: 7]
                num = float(input("Enter a number: "))
                print(f"Result: {natural_log(num)}")

            elif choice == '4':
                # Power function - x^b [cite: 7]
                base = float(input("Enter the base (x): "))
                exponent = float(input("Enter the exponent (b): "))
                print(f"Result: {power(base, exponent)}")

            elif choice == '5':
                print("Exiting calculator. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
