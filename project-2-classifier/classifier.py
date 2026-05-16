"""
Project 2: Data Classification Using AI (Iris dataset, KNN classifier)
DecodeLabs Industrial Training Kit | Batch 2026
Author: Toheeb
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ---------- INPUT PHASE ----------
iris = load_iris()
X = iris.data
y = iris.target

print("=" * 55)
print("🌸 IRIS FLOWER CLASSIFICATION — KNN MODEL")
print("=" * 55)
print(f"Total samples : {len(X)}")
print(f"Features      : {iris.feature_names}")
print(f"Classes       : {list(iris.target_names)}")

# ---------- SPLIT PHASE ----------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\nTraining set : {len(X_train)} flowers")
print(f"Testing set  : {len(X_test)} flowers")

# ---------- PROCESS PHASE (TRAIN) ----------
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# ---------- OUTPUT PHASE (VALIDATE) ----------
accuracy = accuracy_score(y_test, predictions)
print("\n" + "=" * 55)
print(f"🎯 ACCURACY: {accuracy * 100:.2f}%")
print("=" * 55)

print("\n📊 CONFUSION MATRIX")
print("(rows = actual, columns = predicted)")
print("            setosa  versicolor  virginica")
matrix = confusion_matrix(y_test, predictions)
for label, row in zip(iris.target_names, matrix):
    print(f"{label:<12}{row[0]:^8}{row[1]:^12}{row[2]:^10}")

print("\n📈 DETAILED REPORT (Precision, Recall, F1-Score)")
print(classification_report(y_test, predictions, target_names=iris.target_names))

# ---------- BONUS: Try predicting a brand new flower ----------
new_flower = [[5.1, 3.5, 1.4, 0.2]]   # measurements of a mystery flower
prediction = model.predict(new_flower)
predicted_name = iris.target_names[prediction[0]]
print(f"🔮 New flower {new_flower[0]} → predicted: {predicted_name}")