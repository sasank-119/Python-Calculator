# ==========================================
#         PYTHON CLI CALCULATOR
# ==========================================

# Initialize 'again' to enter the loop
again = "yes"

# Keep running until user types 'no'
while again != "no":

    # ---------- Take User Inputs ----------
    A = int(input("Enter A value: "))       # First number
    B = int(input("Enter B value: "))       # Second number

    # ---------- Show Available Operations ----------
    operations = ['add', 'subtract', 'multiply', 'division', 'modulus', 'floor']
    print(f"Available operations: {operations}")

    # Take operation input and convert to lowercase
    # so it works for ADD / Add / add all the same
    operation = input("Enter an operation: ").lower()

    # ---------- Validate & Perform Operation ----------

    # Check if entered operation is valid
    if operation not in operations:
        print("Invalid operation. Please enter a valid operation.")

    # Addition
    elif operation == 'add':
        print(f"Sum of numbers is: {A + B}")

    # Subtraction
    elif operation == 'subtract':
        print(f"Subtraction of numbers is: {A - B}")

    # Multiplication
    elif operation == 'multiply':
        print(f"Multiplication of numbers is: {A * B}")

    # Division — includes divide by zero check
    elif operation == 'division':              
        if B == 0:
            print("Division by 0 is not possible.")  # Guard clause
        else:
            print(f"Division of numbers is: {round(A / B, 2)}")  # Rounded to 2 decimal

    # Modulus — gives remainder
    elif operation == 'modulus':
        print(f"Modulus(%) of numbers is: {A % B}")

    # Floor division — removes decimal part
    elif operation == 'floor':
        print(f"Floor(//) of numbers is: {A // B}")

    # ---------- Ask to Continue ----------
    # .lower() handles YES / Yes / yes all the same
    again = input("Do you want to continue? (yes/no): ").lower()

# End of program
print("Thank you for using the calculator. Goodbye! 👋")








