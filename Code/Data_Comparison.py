import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'browser'
import warnings 
warnings.filterwarnings('ignore')

df = pd.read_csv(r"C:\Users\Jacks\OneDrive\Desktop\Senior Project\StudentPerformanceFactors.csv")

# Region 1
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


# Region 2
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