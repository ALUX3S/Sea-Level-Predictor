import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    df2 = df[df['Year']>=2000]
    res2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    added_years = pd.DataFrame(np.arange(2014, 2051, 1), columns=['Year'])
    df1 = pd.concat([df, added_years])
    df2 = pd.concat([df2, added_years])

    # Create scatter plot
    fig = plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], marker='.')

    # Create first line of best fit
    plt.plot(df1['Year'], res1.intercept + res1.slope*df1['Year'], 'r', label='fitted line since 1880')

    # Create second line of best fit
    plt.plot(df2['Year'], res2.intercept + res2.slope*df2['Year'], '--b', label='fitted line since 2000')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()