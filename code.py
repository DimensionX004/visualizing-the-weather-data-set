# --------------
# Import the required Libraries
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import calendar
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# Generate a line chart that visualizes the readings in the months
def line_chart(df,period,col):
    df[col].plot()    
    plt.title('Temperature Trend, 2012')
    plt.ylabel('Temp (C)')

# Function to perform univariate analysis of categorical columns
def plot_categorical_columns(df):
    pass

# Function to plot continous plots
def plot_cont(df,plt_typ):
    if(plt_typ == 'distplot'):
        fig, ((ax_1, ax_2), (ax_3, ax_4), (ax_5, ax_6)) = plt.subplots(3,2, figsize = (15, 10))
        sns.distplot(df['Temp (C)'], color = 'b', ax = ax_1)
        sns.distplot(df['Dew Point Temp (C)'], color = 'b', ax = ax_2)
        sns.distplot(df['Rel Hum (%)'], color = 'b', ax = ax_3)
        sns.distplot(df['Wind Spd (km/h)'], color = 'b', ax = ax_4)
        sns.distplot(df['Visibility (km)'], color = 'b', ax = ax_5)
        sns.distplot(df['Stn Press (kPa)'], color = 'b', ax = ax_6)
        plt.tight_layout()
    else:
        fig, ((ax_1, ax_2), (ax_3, ax_4), (ax_5, ax_6)) = plt.subplots(3,2, figsize = (15, 10))
        ax_1.boxplot(df['Temp (C)'])
        ax_2.boxplot(df['Dew Point Temp (C)'])
        ax_3.boxplot(df['Rel Hum (%)'])
        ax_4.boxplot(df['Wind Spd (km/h)'])
        ax_5.boxplot(df['Visibility (km)'])
        ax_6.boxplot(df['Stn Press (kPa)'])
        plt.tight_layout()
# Function to plot grouped values based on the feature
def group_values(df,col1,agg1,col2):
    grouping = df.groupby(col1)[col2].mean()
    return grouping

# Read the Data and pass the parameter as parse_dates=True, index_col='Date/Time'
weather_df = pd.read_csv(path, index_col = 'Date/Time', parse_dates = True)
#print(weather_df.head(5))

# Lets try to generate a line chart that visualizes the temperature readings in the months.
# Call the function line_chart() with the appropriate parameters.
line_chart(weather_df, 12, 'Temp (C)')
df_temp = pd.read_csv(path)
df_temp['Date/Time'] = pd.to_datetime(df_temp['Date/Time'])
df_temp['Month'] = df_temp['Date/Time'].dt.month
df_tempMonth = df_temp.groupby('Month')['Temp (C)'].mean()
plt.plot(df_tempMonth)

# Now let's perform the univariate analysis of categorical features.
# Call the "function plot_categorical_columns()" with appropriate parameters.
plot_categorical_columns(weather_df)

# Let's plot the Univariate analysis of Numerical columns.
# Call the function "plot_cont()" with the appropriate parameters to plot distplot
plot_cont(weather_df, "distplot")

# Call the function "plot_cont()" with the appropriate parameters to plot boxplot
plot_cont(weather_df, "boxplot")

# Groupby the data by Weather and plot the graph of the mean visibility during different weathers. Call the function group_values to plot the graph.
# Feel free to try on diffrent features and aggregated functions like max, min.
group1 = group_values(weather_df, 'Weather', np.mean, 'Visibility (km)')
plt.figure(figsize = (12, 18))
group1.plot(kind = 'bar')



