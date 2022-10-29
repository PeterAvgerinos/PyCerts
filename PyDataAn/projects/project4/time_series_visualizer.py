import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates = ['date'], index_col = 'date')
# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    df['month'] = df.index.month
    df['year'] = df.index.year
    list_month_cut = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
       'Nov', 'Dec']
    list_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
       'November', 'December']
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(df.index, df['value'], 'r', linewidth=1)
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set(title = 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df['month'] = df.index.month
    df['year'] = df.index.year
    list_month_cut = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
       'Nov', 'Dec']
    list_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
       'November', 'December']
    
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby(['year','month'])[['value']].mean()
    #df_bar = df_bar.sort_values('month')
    #df_bar = df_bar.pivot_table(values='value', index='year', columns='month')
    #df_bar = df_bar.unstack()
    df_bar = df_bar.reset_index()
    df_bar = df_bar.sort_values(['year', 'month'])
    df_bar['month'] = pd.to_datetime(df_bar['month'], format='%m').dt.month_name()

    # Draw bar plot
    df_bar = df_bar.pivot_table(values='value', index='year', columns='month')
    df_bar = df_bar[list_month]
    fig = df_bar.plot.bar();




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15,5))
    sns.boxplot(data=df, x='year', y='value',ax=axes[0])
    sns.boxplot(data=df,x='month_str_sliced', y='value',             order=list_month_cut,ax=axes[1])
    axes[1].set_xlabel('month')
    axes[1].axvline('Jan', color='black', linestyle='--');





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

