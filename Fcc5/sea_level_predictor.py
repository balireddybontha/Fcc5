import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Function to draw scatter plot and regression lines
def draw_plot():
    # Read data from the CSV file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Observed')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))  # Extend to 2050
    plt.plot(years_extended, intercept + slope * years_extended, color='red', label='Best Fit (1880 - 2050)')

    # Filter data from year 2000 onwards for the second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    plt.plot(years_extended, intercept_recent + slope_recent * years_extended, color='green', label='Best Fit (2000 - 2050)')

    # Labeling the plot
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    # Save the figure
    plt.savefig('sea_level_plot.png')
    plt.show()

# Call the function to draw the plot
draw_plot()
