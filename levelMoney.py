import numpy as np
import pandas as pd


monthly_activities = pd.read_csv(
    '/Users/blakevanfleteren/Documents/Coding_Projects/monthly_activities.csv')
monthly_activities_types = monthly_activities.groupby(
    'Type').sum('Amount').reset_index()

for activity in monthly_activities['Amount']:

    if activity >= 0:

        monthly_activities['lm_type'] = 'income'

    else:

        monthly_activities['lm_type'] = 'expense'

print(monthly_activities)


# estimating monthly income from monthly payment
monthly_income = monthly_activities_types[
    monthly_activities_types['Type'] == 'Payment'].Amount

# annual income calculated from 12 months of monthly income
annual_income = monthly_income * 12

# daily income based on annual income divided by number of days in a year
daily_income = annual_income/365


def income_expense(df, col_name='Amount'):

    df['lm_type'] = ''

    # for every instance in the amount column
    for activity in df[col_name]:

        if activity in df[col_name] >= 0:
            df['lm_type'] = 'income'

        else:
            df['lm_type'] = 'expense'

    return df


monthly_acts = income_expense(monthly_activities, 'Amount')
