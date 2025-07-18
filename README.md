# Predictive Analysis with Machine Learning – Supplier Reliability

Hi there!  
In this project, I built a machine learning model that predicts **supplier reliability** based on real-world procurement KPIs. The idea is simple: if we can use past supplier performance data, we should be able to predict whether a supplier is reliable or not—and make smarter business decisions.

---

# Problem Statement

In procurement and supply chain management, selecting the right supplier is crucial. Late deliveries, defective products, or poor responsiveness can have major business impacts.

**This project aims to predict whether a supplier is reliable** based on their performance KPIs. The goal is to classify suppliers as:

- `1` → Reliable  
- `0` → Not Reliable

If a company can predict this in advance, they can avoid risk, reduce returns, and make data-driven sourcing decisions.

---

#  Dataset Description

I used a dataset titled **"Procurement KPI Analysis Dataset"** which includes 11 columns representing performance metrics for suppliers. The key features used in the prediction model include:

| Feature                  |                          Description               |
|--------------------------|----------------------------------------------------|
| `On-Time Delivery Rate`  | How often the supplier delivers on time |
| `Quality Defect Rate`    | Frequency of defective items |
| `Order Accuracy Rate`    | Match between order placed and order delivered |
| `Fulfillment Lead Time`  | Time taken to complete and deliver an order |
| `Compliance Rate`        | Adherence to policies and contracts |
| `Return Rate`            | Proportion of goods returned |
| `Responsiveness Score`   | How quickly issues or queries are handled |
| `Sustainability Score`   | Supplier’s eco-friendly practices |
| `Innovation Capability`  | Supplier’s ability to bring new ideas/processes |
| `Supplier ID`            | Unique ID (not used in training) |
| `Reliability Score`      | Target variable (0 = Not reliable, 1 = Reliable)

---

#  My Approach

Here’s how I tackled this project step by step:

# 1. Data Cleaning & Exploration
- Removed any nulls or inconsistent entries
- Dropped `Supplier ID` since it doesn’t help with prediction
- Visualized distributions using Seaborn and Matplotlib
- Checked class imbalance for `Reliability Score`

# 2. Preprocessing
- Scaled numerical features using `StandardScaler`
- Ensured all features were numeric and ready for modeling

# 3. Train-Test Split
- Used `train_test_split` to divide the data (80% training, 20% testing)
  
# 4. Model Training
I used a Random Forest Classifier for this task because it:
-Handles tabular data well
-Captures non-linear relationships
-Provides built-in feature importance

# 5. Model Evaluation
Evaluated using:
-Accuracy Score
-Confusion Matrix
-Precision, Recall, F1-score (via classification_report)

# 6. Feature Importance
I also visualized which supplier KPIs had the biggest impact on the reliability prediction. This is great for explaining the model to business stakeholders.

Results:
Here’s how the model performed on the test set:

Metric	        Score (example)
Accuracy	      91%
Precision	      90%
Recall	        89%
F1-score	      89.5%

These numbers may vary depending on the dataset split and hyperparameters. You can update them after each experiment.

🔮 Future Improvements
Here’s what I plan to do next:

Hyperparameter tuning with GridSearchCV

Try other models like XGBoost or Logistic Regression

Handle class imbalance using SMOTE

Deploy as a Streamlit web app

Save and reuse the model using joblib

License:
This project is licensed under the MIT License.
Feel free to fork, modify, or use it for your own projects.

About Me:
I’m currently pursuing an MSc in Data Science and I love applying machine learning to solve real-world problems.
This project gave me hands-on experience in both data preprocessing and predictive modeling in the procurement domain.

Let’s connect!
📧 rajshreya8271@gmail.com
🔗 https://www.linkedin.com/in/shreya-05a53a1b7/
