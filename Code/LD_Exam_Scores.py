import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load Excel file
df = pd.read_csv(r"C:\Users\Jacks\OneDrive\Desktop\archive\StudentPerformanceFactors (1).csv")

# Group data by Learning_Disabilities
grouped = df.groupby("Learning_Disabilities")["Exam_Score"]

# Print average scores for each group
print("Average scores:")
print(grouped.mean())

# Print standard deviations for each group
print("\nStandard deviations:")
print(grouped.std())

# Perform independent t-test
yes_scores = df[df["Learning_Disabilities"] == "Yes"]["Exam_Score"]
no_scores = df[df["Learning_Disabilities"] == "No"]["Exam_Score"]
t_stat, p_value = stats.ttest_ind(yes_scores, no_scores, equal_var=False)

print(f"\nT-test result: t={t_stat:.3f}, p={p_value:.3f}")

# Create boxplot
df.boxplot(column="Exam_Score", by="Learning_Disabilities")
plt.title("Exam Scores by Learning Disability")
plt.suptitle("")
plt.xlabel("Learning Disability")
plt.ylabel("Exam Score")
plt.show()
