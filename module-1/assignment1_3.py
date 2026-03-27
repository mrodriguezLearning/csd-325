'''
Marco Rodriguez
03/27/2026
Assignment 1.3
This program prompts the user for a number of bottles of beer and then counts down to zero, and provides a final message when the countdown is complete.
'''
# Function to the countdown of bottles of beer
def countdown(count):
    # Loop until the count reaches zero
    while count > 0:
        # Handling pluralization for the first line of the verse
        current_unit = "bottles" if count > 1 else "bottle"
        
        print(f"{count} {current_unit} of beer on the wall, {count} {current_unit} of beer.")
        
        # Decrement the count
        count -= 1
        
        print(f"Take one down and pass it around, {count} bottle(s) of beer on the wall.\n")

def main():
    # Prompt the user for the number of bottles
    try:
        user_input = int(input("Enter number of bottles:"))
        
        # Manage the countdown via function call
        countdown(user_input)
        
        # Final reminder in the main program
        print("Time to buy more bottles of beer.")
        
    except ValueError:
        # Handle the case where the input is not a valid integer
        print("Please enter a valid whole number.")

if __name__ == "__main__":
    main()