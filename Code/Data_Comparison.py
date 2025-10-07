import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = 'browser'
import warnings 
warnings.filterwarnings('ignore')

df = pd.read_csv(r"C:\Users\Jacks\OneDrive\Desktop\Senior Project\StudentPerformanceFactors.csv")


# Region 1 (9/29/25)
## Create a scatter plot to visualize the relationship between study hours vs. learning disabilities, and the resulting exam scores
fig = px.scatter(df, 
                 x="Hours_Studied", 
                 y="Exam_Score", 
                 color="Learning_Disabilities",
                 color_continuous_scale="Viridis", 
                 title="Study Hours and Learning Disabilities on Exam")
# Update layout for better visualization
fig.update_layout(width=600, height=500,template='plotly_white',title_x=0.5)
#Display the plot
fig.show()
# Calculate the average exam score for students with and without learning disabilities
atg = df.groupby("Learning_Disabilities")["Exam_Score"].mean()
# End Region 1


# Region 2 (10/1/25)
## Create a box plot to show the distribution of exam scores based on parental education level and learning disabilities
fig = px.box(df, 
             x="Parental_Education_Level", 
             y="Exam_Score", 
             color="Learning_Disabilities", 
             color_discrete_sequence=px.colors.qualitative.D3,
             category_orders = {"Parental_Education_Level": sorted(df["Parental_Education_Level"].dropna().astype(str).unique())},
             title="Parental Education Level & Learning Disabilities on Exam")
            # Make sure categories are sorted as strings, drop NaNs

# Update layout settings for box plot
fig.update_layout(
    height=600, 
    width=800, 
    template='plotly_white', 
    title_x=0.5
)
fig.update_layout(width=700, height=600,template='plotly_white',title_x=0.5)
# Display box plot
fig.show()
# End Region 2

#Region 3 (10/7/25)
## This section visualizes the distribution of all categorical columns in the dataset
cat_cols = df.select_dtypes(include='O')
cols = 2
rows = (len(cat_cols.columns) + 1) // cols 

colors = ['#404546', '#4C6B73', '#7492C1', '#8A7D4C', '#A7B7A7', '#A69585', '#6D7F8C', 
          '#4F7D9E', '#82A1B2', '#A19B8F', '#B59A6A', '#9A7A48', '#706E4C']

# Create a subplot figure with titles for each categorical feature
fig = sp.make_subplots(rows=rows, cols=cols, subplot_titles=[col for col in cat_cols.columns])
# Loop through each categorical column to create a bar chart
for i, column in enumerate(cat_cols.columns):
    row = (i // cols) + 1  
    col = (i % cols) + 1   
    # Count occurrences of each unique category in the column
    count_df = df[column].value_counts().reset_index()
    count_df.columns = [column, 'count']
    
    fig.add_trace(
        go.Bar(x=count_df[column], y=count_df['count'], name=column, marker_color=colors[i],text=count_df['count'],textposition='auto'),
        row=row, col=col
    )
# Update layout settings
fig.update_layout(
    title_text="Distribution of Each Categorical Features",
    height=2500, width=800,  
    showlegend=True,
    template='plotly_white'
)
# Display bar charts
fig.show()