import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Reading csv file
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Cleaning data (eliminating both top and bottom 2.5% of views
df = df[(df["value"] <= df["value"].quantile(0.975)) & (df["value"] >= df["value"].quantile(0.025))]


# Creating line plot of page views vs date
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(16, 6))
    plt.plot(df, color="red")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    # saving plot as image
    fig.savefig("line_plot.png")
    return fig


# Creating bar plot showing average monthly views per month
def draw_bar_plot():
    # Preparing data for bar plots
    df_bar = df.copy()
    df_bar = df_bar.reset_index()
    df_bar["day"] = df_bar.date.dt.day
    df_bar["month"] = df_bar.date.dt.month_name()
    df_bar["year"] = df_bar.date.dt.year
    df_bar = df_bar.drop(columns=["date"])

    # Grouping by year and month
    df_bar = df_bar.groupby([("year"), ("month")])["value"].mean().to_frame()

    df_bar = df_bar.reset_index()
    df_bar.columns = ["Years", "Months", "Average Page Views"]

    # Ordering months
    df_bar["Months"] = pd.Categorical(df_bar["Months"],
                                      categories=["January", "February", "March", "April", "May", "June",
                                                  "July", "August", "September", "October", "November", "December"],
                                      ordered=True)

    fig = sns.catplot(x="Years", y="Average Page Views", data=df_bar, kind="bar", hue="Months",
                      palette="Blues_d", height=6, aspect=2, legend=False).fig
    plt.legend(title="Months", loc="upper left")

    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Preparing data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = [d.year for d in df_box.date]
    df_box["month"] = [d.strftime('%b') for d in df_box.date]
    df_box["month"] = pd.Categorical(df_box['month'], categories=["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                                                                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                                     ordered=True)
    # Drawing data using seaborn
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[1].set_title("Month-wise Box Plot (Seasonality)")

    sns.boxplot(y="value", x="year", data=df_box, ax=axes[0])
    sns.boxplot(y="value", x="month", data=df_box, ax=axes[1])
    axes[0].set_ylabel("Page Views")
    axes[1].set_ylabel("Page Views")
    axes[0].set_xlabel("Year")
    axes[1].set_xlabel("Month")

    # Save image and return fig
    fig.savefig("box_plot.png")
    return fig
