import pandas as pd


def calculate_demographic_data(print_data=True):
    # Reading data from file
    df = pd.read_csv('/Users/samir/Desktop/Machine_Learning/demographic_data_analyzation/adult.data.csv')

    #number of each race
    race_count = df['race'].value_counts()

    #the average age of men
    average_age_men = float("{:.1F}".format(df[df['sex'] == 'Male']['age'].mean()))

    #the percentage of people who have a Bachelor's degree
    percentage_bachelors = float("{:.1f}".format((df[df['education'] == 'Bachelors'])['education'].count() / (len(df)) * 100))

    #the percentage of people who have a high school diploma
    percentage_high_school = float("{:.1f}".format((df[df['education'] == 'HS-grad'])['education'].count() / (len(df)) * 100))

    #the percentage of people who have been married at least 10 years
    percentage_married_10 = float("{:.1f}".format((df[df['marital-status'] == 'Married-civ-spouse'])['marital-status'].count() / (len(df)) * 100))

    #the percentage of people who have been married at least 15 years
    percentage_married_15 = float("{:.1f}".format((df[df['marital-status'] == 'Married-civ-spouse'])['marital-status'].count() / (len(df)) * 100))

    # percentage of people with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = float("{:.1f}".format((df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])])['education'].count() / (len(df)) * 100))
    lower_education =float("{:.1f}".format((df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])])['education'].count() / (len(df)) * 100))

    # percentage with salary >50K
    higher_education_rich = float("{:.1f}".format(df[(df['salary'] == '>50K') & (df['education'].isin(['Bachelors', 'Masters', 'Doctorate', '?']))]['education'].count() / (df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate', '?']))])['education'].count() * 100))
    lower_education_rich = float("{:.1f}".format(df[(df['salary'] == '>50K') & (~df['education'].isin(['Bachelors', 'Masters', 'Doctorate', '?']))]['education'].count() / (df[(~df['education'].isin(['Bachelors', 'Masters', 'Doctorate', '?']))])['education'].count() * 100))

    #minimum number of hours a person works per week (hours-per-week feature)
    min_work_hours = df['hours-per-week'].min()

    #percentage of the people who work the minimum number of hours per week have a salary of >50K
    num_min_workers = (df[df['salary'] == '>50K']['native-country'].count())

    rich_percentage = (df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')])['salary'].count() / (df[df['hours-per-week'] == min_work_hours]['hours-per-week'].count()) * 100

    # country having the highest percentage of people that earn >50K?
    highest_earning_country_percentage = float("{:.1f}".format(max(df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts() * 100)))
    highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts() * 100).idxmax()


    #the most popular occupation for those who earn >50K in India.
    top_IN_occupation = (df[(df['salary'] == '>50K') & (df['native-country'] == 'India')])['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with high school degrees: {percentage_high_school}%")
        print(f"Percentage married at least 15 years: {percentage_married_15}%")
        print(f"Percentage married at least 10 years: {percentage_married_10}%")
        print(f"Percentage with higher education: {higher_education}%")
        print(f"Percentage without higher education: {lower_education}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'percentage_high_school': percentage_high_school,
        'percentage_married_10': percentage_married_10,
        'percentage_married_15': percentage_married_15,
        'higher_education': higher_education,
        'lower_education': lower_education,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'num_min_workers': num_min_workers,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
