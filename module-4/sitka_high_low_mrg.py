import csv
import sys
from datetime import datetime
import matplotlib.pyplot as plt

'''Create a function to read the weather data from the CSV file and return the dates and temperatures.'''
def get_weather_data(filename, temp_type):
    """Extracts dates and selected temperature data from the CSV file."""
    dates, temps = [], []
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        
        # Index 5 is High (TMAX), Index 6 is Low (TMIN)
        column_index = 5 if temp_type == 'highs' else 6
        
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            temp = int(row[column_index])
            dates.append(current_date)
            temps.append(temp)
    return dates, temps

'''Create a function to plot the data with appropriate titles and colors.'''
def plot_data(dates, temps, temp_type):
    """Plots the temperature data with appropriate titles and colors."""
    color = 'red' if temp_type == 'highs' else 'blue'
    title_label = "High" if temp_type == 'highs' else "Low"
    
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)

    # Format plot
    plt.title(f"Daily {title_label} Temperatures - 2018", fontsize=20)
    plt.xlabel('', fontsize=12)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.show()

def main():
    filename = 'sitka_weather_2018_simple.csv'
    # Display welcome message and instructions
    print("--- Sitka Weather Data Viewer ---")
    print("Instructions: Enter 'highs' to see daily highs, 'lows' for daily lows, or 'exit' to quit.")
    # Loop to allow user to select which data to view until they choose to exit
    while True:
        choice = input("\nSelect an option (Highs/Lows/Exit): ").lower().strip()
        
        if choice == 'exit':
            print("Thank you for using the Sitka Weather Data Viewer. Goodbye!")
            # Exit the program
            sys.exit()
        elif choice == 'highs' or choice == 'lows':
            # Get the weather data based on user choice and plot it
            dates, temps = get_weather_data(filename, choice)
            plot_data(dates, temps, choice)
        else:
            # Handle invalid input
            print("Invalid selection. Please enter 'highs', 'lows', or 'exit'.")

if __name__ == '__main__':
    main()