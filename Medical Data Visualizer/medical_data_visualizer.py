import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Importing data
df = pd.read_csv("medical_examination.csv", index_col="id")

# Adding 'overweight' column, if BMI > 25 -> person is overweight -> value = 1,
# otherwise -> person is not overweight -> value = 0
df["overweight"] = np.where((df["weight"] / ((df["height"] / 100) ** 2)) > 25, 1, 0)

# Normalising data. making 0 always good and 1 always bad.
# if cholesterol or gluc = 1, make value 0. if value > 1. make value 1
df["cholesterol"] = np.where(df["cholesterol"] > 1, 1, 0)
df["gluc"] = np.where(df["gluc"] > 1, 1, 0)

# Creating catplot

# Reformatting df to plot bar chart in seaborn,
# data grouped by cardio showing the number of counts for each value (0,1) of each variable
def draw_cat_plot():
    df_cat = df.drop(columns=["sex", "age", "height", "weight", "ap_hi", "ap_lo"])
    df_cat_cardio_0 = df_cat[df_cat["cardio"] == 0]
    df_cat_cardio_1 = df_cat[df_cat["cardio"] == 1]
    df_cat_cardio_0 = df_cat_cardio_0.set_index("cardio")
    df_cat_cardio_1 = df_cat_cardio_1.set_index("cardio")

    df_cat_cardio_0 = pd.melt(df_cat_cardio_0).value_counts().to_frame()
    df_cat_cardio_0["cardio"] = 0
    df_cat_cardio_0.rename(columns={0: "total"}, inplace=True)

    df_cat_cardio_1 = pd.melt(df_cat_cardio_1).value_counts().to_frame()
    df_cat_cardio_1["cardio"] = 1
    df_cat_cardio_1.rename(columns={0: "total"}, inplace=True)

    df_cat = pd.concat([df_cat_cardio_0, df_cat_cardio_1], axis=0)
    df_cat = df_cat.reset_index()

    # ordering variables
    df_cat["variable"] = pd.Categorical(df_cat["variable"],
                                        categories=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"],
                                        ordered=True)

    # Plotting the arranged df in seaborn
    fig = sns.catplot(x="variable", y="total", data=df_cat, kind="bar", hue="value", col="cardio").fig

    # Saving plot as image
    fig.savefig('catplot.png')
    return fig


# Creating heatmap

def draw_heat_map():
    # Cleaning data to filter out incorrect values
    df_clean = df[(df["ap_lo"] <= df["ap_hi"]) & (df["height"] >= df["height"].quantile(0.025)) & (
                df["height"] <= df["height"].quantile(0.975)) & (df["weight"] >= df["weight"].quantile(0.025)) & (
                              df["weight"] <= df["weight"].quantile(0.975))]

    df_clean = df_clean.reset_index()
    # Creating correlation matrix
    corr = df_clean.corr()

    # Generating a mask for the upper triangle
    upper_tri = np.triu(corr)

    fig, ax = plt.subplots()

    # Plotting heatmap
    sns.heatmap(corr, mask=upper_tri, annot=True, fmt=".1f").get_figure()

    # Saving plot as image
    fig.savefig('heatmap.png')
    return fig
