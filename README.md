# 📊 Statistical Analysis of Student Academic Performance

**Course:** Statistical Methods and Data Analysis (BMA62001)  
**Author:** Rahul (MCA – Cloud Computing)  
**Institution:** Hindustan Institute of Technology and Science, Chennai  

🌐 **Live Interactive Dashboard:** [View Live App on Streamlit](https://stats-mini-project-dl7p97pbbur6anvesdvx9w.streamlit.app/)

---

## 📌 Project Overview
This mini-project investigates the key factors influencing student academic performance using descriptive and inferential statistical methods in Python. A structured dataset of 100 students (`student_data.csv`) containing variables such as Gender, Daily Study Hours, Attendance Percentage, Marks, and Final Result was analyzed, visualized, and deployed as an interactive web dashboard.

---

## 🛠️ Statistical Techniques Applied
1. **Measures of Central Tendency:** Mean (`76.63`), Median (`75.95`), and Mode (`100.00`)
2. **Measures of Dispersion:** Variance (`215.93`), Standard Deviation (`14.69`), and Coefficient of Variation (`19.17%`)
3. **Pearson Correlation ($r$):** Strong positive correlation (`r = 0.9261`, `p = 2.89e-43`) between daily study hours and marks
4. **Simple Linear Regression:** Predictive model $\text{Marks} = 45.37 + 6.52 \times \text{Study\_Hours}$ ($R^2 = 0.8576$)
5. **Hypothesis Testing (One-Sample t-test):** Verified that class average (`76.63`) is significantly higher than the benchmark mean of `65` (`t = 7.9173`, `p = 3.61e-12`)
6. **Chi-Square Test of Independence:** Confirmed that pass/fail outcomes are independent of gender ($\chi^2 = 0.0000$, `p = 1.0000`)

---

## 📈 Visualizations Included
* **Histogram (`1_histogram.png`):** Frequency and KDE distribution of student marks
* **Box Plot (`2_boxplot.png`):** Comparison of marks distribution across gender
* **Scatter Plot (`3_scatterplot.png`):** Linear regression trend line showing Study Hours vs. Marks

---

## 📂 Repository Structure
```text
├── project.py          # Core script for data generation, statistical tests & graph generation
├── app.py              # Streamlit web application for the live interactive dashboard
├── student_data.csv    # Preprocessed dataset of 100 student records
├── 1_histogram.png     # Histogram of student marks
├── 2_boxplot.png       # Box plot of marks by gender
├── 3_scatterplot.png   # Scatter plot with linear regression line
├── requirements.txt    # Python dependencies for deployment
└── README.md           # Project documentation
