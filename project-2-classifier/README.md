# 🌸 Iris Flower Classifier — Supervised Learning

> Project 2 of the **DecodeLabs AI Industrial Training Kit (Batch 2026)**

A supervised machine learning model that classifies iris flowers into one of three species — *Setosa*, *Versicolor*, or *Virginica* — based on four physical measurements: sepal length, sepal width, petal length, and petal width.

This project marks the transition from **rule-based AI** (Project 1) to **machine learning**: instead of writing the logic myself, the model derives it from labeled training data.

## ✨ Features

- 🌸 Uses the classic **Iris benchmark dataset** (150 samples, 3 classes, 4 features)
- ✂️ **Train/test split** (80/20) for honest validation
- 🤖 **K-Nearest Neighbors (KNN)** classifier with K=5
- 📊 Full evaluation suite: accuracy, confusion matrix, precision, recall, F1-score
- 🔮 Live prediction on new, unseen flower measurements

## 🧠 Pipeline (IPO model)

1. **Input** — Load the Iris dataset from `sklearn.datasets`
2. **Process** — Split → Instantiate KNN → Fit → Predict
3. **Output** — Evaluate with confusion matrix and classification report

## 🚀 How to run

```bash
# Activate the virtual environment first
source ../venv/bin/activate

# Then run the classifier
python3 classifier.py
```

## 📈 Results

| Metric              | Score        |
|---------------------|--------------|
| **Accuracy**        | 100% (30/30) |
| **Precision (avg)** | 1.00         |
| **Recall (avg)**    | 1.00         |
| **F1-Score (avg)**  | 1.00         |

Confusion matrix is a perfect diagonal — zero misclassifications across all three classes.

## 🎓 What I learned

- Why we **never** test a model on data it was trained on (the "Accuracy Mirage")
- How `train_test_split` enforces structural integrity in ML pipelines
- The **KNN proximity principle**: *similar things exist in close proximity*
- How to read a confusion matrix and the precision/recall trade-off
- The full `instantiate → fit → predict` workflow of scikit-learn

## 📦 Dependencies

- Python 3
- scikit-learn
- pandas (optional, for data inspection)