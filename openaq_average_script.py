import pandas as pd

# values can be 'hourly', 'daily', 'weekly', 'monthly', 'half year', 'yearly'
# preferrable that the df is a time series
def openaq_averages(df, time, parameter):

    # Filter data by the parameter
    df_param = df[df['parameter'] == parameter]

    # Check the value of the time parameter in the function
    if (time == 'hourly'):
        # resample the data by 1 hour
        resample = df_param.resample('1H')['value'].mean()

    elif (time == 'daily'):
        # resample the data by 1 day
        resample = df_param.resample('1D')['value'].mean()

    elif (time == 'weekly'):
        # resample the data by 1 week
        resample = df_param.resample('1W')['value'].mean()

    elif (time == 'monthly'):
        # resample the data by 1 month
        resample = df_param.resample('1M')['value'].mean()

    elif (time == 'half year'):
        # resample the data by 6 months
        resample = df_param.resample('6M')['value'].mean()

    elif (time == 'yearly'):
        # resample the data by 1 year
        resample = df_param.resample('1Y')['value'].mean()

    # a valid value is not submitted. return a message letting the user know what the value can be
    else:
        return "Not an accepted time value. Accepted values are hourly, daily, monthly, half year, or yearly."

    return resample
