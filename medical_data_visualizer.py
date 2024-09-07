import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Import data
df = pd.read_csv("medical_examination.csv")

# Step 2: Add 'overweight' column. BMI = weight(kg) / height(m)^2.
# Overweight is BMI > 25 (1 for overweight, 0 for not)
df['overweight'] = ((df['weight'] / ((df['height'] / 100) ** 2)) > 25).astype(int)

# Step 3: Normalize data by making 0 always good and 1 always bad
# For cholesterol and gluc, if the value is 1, make it 0, otherwise make it 1
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Step 4: Categorical Plot (draw_cat_plot function)
def draw_cat_plot():
    # Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # Group and reformat the data to split by 'cardio' and show counts of each feature
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # Create the catplot with Seaborn
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', kind='bar', data=df_cat).fig
    
    # Return the figure for testing
    return fig

# Step 5: Heatmap (draw_heat_map function)
def draw_heat_map():
    # Clean the data: filter incorrect data based on specified criteria
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 8))

    # Draw the heatmap using seaborn
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0, cmap='coolwarm', ax=ax)

    # Return the figure for testing
    return fig
  
