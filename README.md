# ❤️ Heart Disease Prediction System (Using XGBoost)

An end-to-end **Machine Learning Web Application** that predicts the risk of heart disease using **XGBoost**, integrated with **MySQL** and deployed using **Flask**.

---

## 🚀 Why XGBoost?

We selected **XGBoost (Extreme Gradient Boosting)** as the final model because:

* It handles **non-linear relationships** effectively
* Built-in **regularization** reduces overfitting
* Works well on **tabular medical datasets**
* Provides **high accuracy and stability** compared to basic models

---

## 🧠 Algorithm Used: XGBoost

XGBoost is an **ensemble learning algorithm** based on boosting:

* Builds trees **sequentially**
* Each new tree corrects errors of previous trees
* Uses **gradient descent optimization**
* Applies **regularization (L1 & L2)** to prevent overfitting

---

## ⚙️ Model Performance

### 🔹 Before Hyperparameter Tuning

* Train Accuracy: 1.0 (Overfitting ❌)
* Test Accuracy: ~0.73

---

### 🔹 After Hyperparameter Tuning

* Train Accuracy: ~0.86
* Test Accuracy: ~0.78

---

## 🏆 Final Model: XGBoost (Tuned)

### Why this model?

* Reduced overfitting compared to initial training
* Improved generalization
* Better balance between bias and variance

---

## ⚠️ Important (Medical Context)

In healthcare prediction:

* **Recall is more important than accuracy**
* Missing a patient (false negative) is critical

So model evaluation includes:

* Accuracy
* Recall
* F1-score

---

## 🔄 Project Workflow

```text
Raw Data (Excel)
        ↓
Data Cleaning (remove '?' and null values)
        ↓
Store in MySQL Database
        ↓
Data Extraction using pymysql
        ↓
Feature Engineering
        ↓
Train-Test Split
        ↓
Standard Scaling
        ↓
Model Training (XGBoost)
        ↓
Hyperparameter Tuning (GridSearchCV)
        ↓
Model Evaluation
        ↓
Save Model (model.pkl)
        ↓
Flask Web App Deployment
        ↓
User Input → Prediction → Result Page
```

---

## 🛠️ Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* Flask
* MySQL
* HTML, CSS (3D UI)

---
## 📌 Conclusion

This project demonstrates:

* End-to-end ML pipeline
* Database integration (MySQL)
* Model optimization using XGBoost
* Deployment using Flask

XGBoost provided a **strong balance between accuracy and generalization**, making it suitable for this prediction task.

---
## 📁 Project Structure

```text
project/
│
├── app.py
├── requirements.txt
│
├── src/
│   ├── components/
│   ├── utils.py
│   ├── logger.py
│   ├── exception.py
│
├── templates/
│   ├── index.html
│   ├── result.html
│
├── static/
│   ├── style.css
│   ├── result.css
│
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
```

---





