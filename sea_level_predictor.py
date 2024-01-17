import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']

    fig , ax = plt.subplots(figsize=(14,6))
    plt.scatter(x,y)

    # Create first line of best fit
    res = linregress(x,y)
    x_first= pd.Series([i for i in range(1880,2051)])
    y_first= res.slope*x_first + res.intercept
    plt.plot(x_first,y_first , 'g')

    # Create second line of best fit
    x=df.loc[df['Year']>=2000]['Year']
    y=df.loc[df['Year']>=2000]['CSIRO Adjusted Sea Level']
  
    res_second = linregress(x,y)
    x_second= pd.Series([i for i in range(2000,2051)])
    y_second= res_second.slope*x_second + res_second.intercept
    plt.plot(x_second,y_second , 'r')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()