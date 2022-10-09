import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df.sex == 'Male'].age.mean()
    average_age_men = round(average_age_men, 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = len(df[df.education == 'Bachelors'])*100/len(df)
    percentage_bachelors = round(percentage_bachelors, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advnced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = len(df[(df.education == 'Bachelors') |
                        (df.education == 'Masters') |
                        (df.education == 'Doctorate')])
    lower_education = len(df) - higher_education

    # percentage with salary >50K
    higher_education_rich = len(df[((df.education == 'Bachelors') |
                                (df.education == 'Masters') |
                                (df.education == 'Doctorate')) &
                                (df.salary == '>50K')])*100/higher_education
    lower_education_rich = len(df[((df.education != 'Bachelors') &
                                (df.education != 'Masters') &
                                (df.education != 'Doctorate')) &
                                (df.salary == '>50K')])*100/lower_education
    higher_education_rich = round(higher_education_rich, 1)
    lower_education_rich = round(lower_education_rich, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[df['hours-per-week'] == min_work_hours])

    rich_percentage = len(df[(df['hours-per-week'] == min_work_hours) &
                            (df['salary'] == '>50K')])*100/num_min_workers

    # What country has the highest percentage of people that earn >50K?
    salaries_by_country = df.groupby(['native-country', 'salary']).agg({'salary' : 'count'})
    percentage_by_country = salaries_by_country.groupby(level=0, group_keys=False).apply(lambda x: x*100/x.sum())
    percentage_by_country = percentage_by_country.rename(columns = {'salary' : 'percentage'})
    percentage_by_country = percentage_by_country.reset_index()
    highest_earning_country = percentage_by_country[percentage_by_country['salary'] == '>50K'].sort_values(by=['percentage'], ascending=False).iloc[0][0]
    highest_earning_country_percentage = percentage_by_country[percentage_by_country['salary'] == '>50K'].sort_values(by=['percentage'], ascending=False).iloc[0][2]
    highest_earning_country_percentage = round(highest_earning_country_percentage, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    popular_occupation = df.groupby(['native-country', 'salary', 'occupation']).agg({'salary' : 'count'})
    popular_occupation = popular_occupation.rename(columns = {'salary' : 'count'})
    popular_occupation = popular_occupation.reset_index()
    popular_occupation_india = popular_occupation[(popular_occupation['native-country'] == 'India') &
                                                  (popular_occupation['salary'] == '>50K')]
    popular_occupation_india = popular_occupation_india.sort_values(by='count', ascending=False)
    top_IN_occupation = popular_occupation_india.iloc[0][2]

    # DO NOT MODIFY BELOW THIS LINE

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

