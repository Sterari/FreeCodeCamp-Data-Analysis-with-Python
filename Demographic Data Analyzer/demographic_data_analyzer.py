import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This is a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = df[df["sex"] == "Male"]
    average_age_men = round(average_age_men["age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(100 * df.education.value_counts().Bachelors / df.shape[0], 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?

    # dfs for people with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[
        (df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate")]
    lower_education = df[
        (df["education"] != "Bachelors") & (df["education"] != "Masters") & (df["education"] != "Doctorate")]

    higher_education_rich = round(
        100 * higher_education[higher_education["salary"] == ">50K"].shape[0] / higher_education.shape[0], 1)

    # What percentage of people without advanced education make more than 50K?
    lower_education_rich = round(
        100 * lower_education[lower_education["salary"] == ">50K"].shape[0] / lower_education.shape[0], 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round(
        100 * num_min_workers[num_min_workers["salary"] == ">50K"].shape[0] / num_min_workers.shape[0], 1)

    # What country has the highest percentage of people that earn >50K?
    df_clean = df[df["native-country"] != "?"]
    country_values = df_clean["native-country"].value_counts()
    countries_list = country_values.index
    country_rich = []
    for country in countries_list:
        country_df = df[df["native-country"] == country]
        country_percentage = country_df[country_df["salary"] == ">50K"].shape[0] / country_df.shape[0]
        country_rich.append(country_percentage)

    # series containing countries and their respective percentages of people who earn more than 50k
    country_series = pd.Series(country_rich, index=countries_list)

    highest_earning_country = country_series[country_series == country_series.max()].index[0]
    highest_earning_country_percentage = round(100 * country_series.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_df = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
    india_occupations = india_df.occupation.value_counts()
    top_IN_occupation = india_occupations[india_occupations == india_df.occupation.value_counts().max()].index[0]

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
            highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }