import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import and clean data
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Step 2: Clean the data by removing the top 2.5% and bottom 2.5%
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

# Step 3: Line Plot
def draw_line_plot():
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 5))

    # Plot the data
    ax.plot(df.index, df['value'], color='red', linewidth=1)

    # Set title and labels
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save and return the figure
    fig.savefig('line_plot.png')
    return fig

# Step 4: Bar Plot
def draw_bar_plot():
    # Copy and modify data for bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    # Group data by year and month, then calculate the mean
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Create the bar plot
    fig = df_bar.plot(kind='bar', figsize=(10, 5), legend=True).figure

    # Set the labels and title
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    # Save and return the figure
    fig.savefig('bar_plot.png')
    return fig

# Step 5: Box Plot
def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box['date']]
    df_box['month'] = [d.strftime('%b') for d in df_box['date']]
    df_box['month_num'] = df_box['date'].dt.month  # to sort month correctly
    df_box = df_box.sort_values('month_num')

    # Create box plots
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Year-wise box plot (Trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise box plot (Seasonality)
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save and return the figure
    fig.savefig('box_plot.png')
    return fig
  
