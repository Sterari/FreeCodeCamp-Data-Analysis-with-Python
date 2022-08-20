import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Reading data from file
    df = pd.read_csv("epa-sea-level.csv")
    df.head()

    # Creating scatter plot (year vs CSIRO adjusted sea level)
    fig, ax = plt.subplots(figsize=(16, 6))
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    plt.scatter(x, y)

    # Creating first line of best fit
    line1_info = linregress(x, y)
    x_fit = np.linspace(np.min(x), 2050, 171)
    y_fit = line1_info[0] * x_fit + line1_info[1]
    ax.plot(x_fit, y_fit, color="red", label="line of best fit using years from 1880 onwards")

    # Creating second line of best fit
    df2 = df[df["Year"] >= 2000]
    x2 = df2["Year"]
    y2 = df2["CSIRO Adjusted Sea Level"]
    line2_info = linregress(x2, y2)
    x2_fit = np.linspace(np.min(x2), 2050, 51)
    y2_fit = line2_info[0] * x2_fit + line2_info[1]
    ax.plot(x2_fit, y2_fit, color="green", label="line of best fit using years from 2000 onwards")
    plt.legend(loc="upper left")

    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()