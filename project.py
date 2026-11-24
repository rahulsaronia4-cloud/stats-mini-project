import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# ==========================================
# 1. AUTOMATIC DATASET GENERATION & CLEANING
# ==========================================
np.random.seed(42)
n = 100

study_hours = np.round(np.random.uniform(1.5, 8.5, n), 1)
attendance = np.random.randint(60, 100, n)
gender = np.random.choice(['Male', 'Female'], n)

# Realistic Marks formula (Study hours + Attendance + slight random noise)
noise = np.random.normal(0, 5, n)
marks = np.clip(np.round(25 + (6.5 * study_hours) + (0.25 * attendance) + noise, 1), 30, 100)
result = np.where(marks >= 50, 'Pass', 'Fail')

df = pd.DataFrame({
    'Student_ID': range(1, n + 1),
    'Gender': gender,
    'Study_Hours': study_hours,
    'Attendance_Pct': attendance,
    'Marks': marks,
    'Result': result
})

# Save dataset to CSV (Appendix ke liye kaam aayega)
df.to_csv('student_data.csv', index=False)
print("✅ Dataset 'student_data.csv' successfully generated (100 rows, 0 missing values).\n")

# ==========================================
# 2. STATISTICAL TECHNIQUES (6 SYLLABUS TOPICS)
# ==========================================
print("="*55)
print("STATISTICAL ANALYSIS RESULTS")
print("="*55)

# Technique 1: Central Tendency (Mean, Median, Mode)
mean_m = df['Marks'].mean()
median_m = df['Marks'].median()
mode_m = df['Marks'].mode()[0]
print(f"1. CENTRAL TENDENCY (Marks):")
print(f"   - Mean   : {mean_m:.2f}")
print(f"   - Median : {median_m:.2f}")
print(f"   - Mode   : {mode_m:.2f}\n")

# Technique 2: Measures of Dispersion (Variance, SD, CV)
var_m = df['Marks'].var()
std_m = df['Marks'].std()
cv_m = (std_m / mean_m) * 100
print(f"2. DISPERSION (Marks):")
print(f"   - Variance           : {var_m:.2f}")
print(f"   - Standard Deviation : {std_m:.2f}")
print(f"   - Coeff of Variation : {cv_m:.2f}%\n")

# Technique 3: Correlation (Study Hours vs Marks)
corr, p_corr = stats.pearsonr(df['Study_Hours'], df['Marks'])
print(f"3. CORRELATION (Study Hours vs Marks):")
print(f"   - Pearson r : {corr:.4f} (Strong Positive Correlation)")
print(f"   - p-value   : {p_corr:.4e}\n")

# Technique 4: Simple Linear Regression (Predicting Marks from Study Hours)
slope, intercept, r_val, p_val, std_err = stats.linregress(df['Study_Hours'], df['Marks'])
pred_6hrs = intercept + slope * 6.0
print(f"4. LINEAR REGRESSION (Marks = {intercept:.2f} + {slope:.2f} * Study_Hours):")
print(f"   - R-squared : {r_val**2:.4f}")
print(f"   - Predicted Marks for 6 Study Hours : {pred_6hrs:.2f}\n")

# Technique 5: Hypothesis Testing (One-Sample t-test: Is avg marks significantly > 65?)
t_stat, p_ttest = stats.ttest_1samp(df['Marks'], 65)
print(f"5. HYPOTHESIS TESTING (One-Sample t-test vs Population Mean = 65):")
print(f"   - t-statistic : {t_stat:.4f}")
print(f"   - p-value     : {p_ttest:.4e}")
print(f"   - Decision    : {'Reject H0 (Significant difference)' if p_ttest < 0.05 else 'Fail to Reject H0'}\n")

# Technique 6: Chi-Square Test (Gender vs Pass/Fail Result)
contingency_table = pd.crosstab(df['Gender'], df['Result'])
chi2, p_chi2, dof, ex = stats.chi2_contingency(contingency_table)
print(f"6. CHI-SQUARE TEST (Gender vs Result):")
print(f"   - Chi2 Statistic : {chi2:.4f}, df = {dof}")
print(f"   - p-value        : {p_chi2:.4e}")
print(f"   - Decision       : {'Dependent' if p_chi2 < 0.05 else 'Independent (No gender bias)'}")
print("="*55 + "\n")

# ==========================================
# 3. AUTOMATIC DATA VISUALIZATION (3 GRAPHS)
# ==========================================
sns.set_theme(style="whitegrid")

# Graph 1: Histogram
plt.figure(figsize=(7, 4))
sns.histplot(df['Marks'], bins=12, kde=True, color='royalblue')
plt.title('Distribution of Student Marks (Histogram)')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('1_histogram.png', dpi=300)
plt.close()

# Graph 2: Box Plot
plt.figure(figsize=(7, 4))
sns.boxplot(x='Gender', y='Marks', data=df, palette='Set2')
plt.title('Marks Distribution by Gender (Box Plot)')
plt.tight_layout()
plt.savefig('2_boxplot.png', dpi=300)
plt.close()

# Graph 3: Scatter Plot with Regression Line
plt.figure(figsize=(7, 4))
sns.regplot(x='Study_Hours', y='Marks', data=df, scatter_kws={'alpha':0.7}, line_kws={'color':'red'})
plt.title('Study Hours vs Marks (Scatter Plot & Regression Line)')
plt.xlabel('Daily Study Hours')
plt.ylabel('Marks')
plt.tight_layout()
plt.savefig('3_scatterplot.png', dpi=300)
plt.close()

print("✅ All 3 graphs saved: '1_histogram.png', '2_boxplot.png', '3_scatterplot.png'")