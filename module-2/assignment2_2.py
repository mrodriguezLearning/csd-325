"""
Marco Rodriguez
03/27/2026
Module 2
Assignment 2.2
This python program converts miles driven to kilometers with input validation.
"""
def miles_to_km(miles):
    """
    Accepts a number of miles and returns the equivalent in kilometers.
    Conversion factor: 1 mile = 1.60934 kilometers
    """
    return miles * 1.60934

def main():
    # Initialize a flag to control the input loop
    valid_input = False
    
    while not valid_input:
        try:
            # Get user input
            user_input = input("Enter the number of miles driven: ")
            
            # Attempt to convert string input to a float
            miles = float(user_input)
            
            # Validate that the number is positive
            if miles < 0:
                print("Error: Please enter a non-negative number.")
            else:
                # If we pass the checks, input is valid
                valid_input = True
                
                # Call the conversion function [cite: 624]
                kilometers = miles_to_km(miles)
                
                # Display results formatted to 2 decimal places
                print(f"\nTotal Miles:      {miles:,.2f}")
                print(f"Total Kilometers: {kilometers:,.2f}")
                
        except ValueError:
            # This block executes if float() fails (e.g., user enters "ten")
            print("Error: Invalid input. Please enter a numeric value.")

# Standard boilerplate to call the main function
if __name__ == '__main__':
    main()