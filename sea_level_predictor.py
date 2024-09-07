import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Step 1: Read the data from the CSV file
    df = pd.read_csv('epa-sea-level.csv')

    # Step 2: Create a scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Step 3: Perform linear regression on all data
    slope_all, intercept_all, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Step 4: Create a line of best fit from the year 1880 to 2050
    years_extended = pd.Series(range(1880, 2051))
    sea_level_pred_all = slope_all * years_extended + intercept_all
    plt.plot(years_extended, sea_level_pred_all, color='red', label='Fit Line (1880-2050)')
    
    # Step 5: Perform linear regression on data from year 2000 to the most recent year
    recent_data = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])

    # Step 6: Create another line of best fit from the year 2000 to 2050
    years_recent = pd.Series(range(2000, 2051))
    sea_level_pred_recent = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent, sea_level_pred_recent, color='green', label='Fit Line (2000-2050)')

    # Step 7: Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Step 8: Add a legend
    plt.legend()

    # Step 9: Save plot and return the plot object
    plt.savefig('sea_level_plot.png')
    return plt.gca()
  
