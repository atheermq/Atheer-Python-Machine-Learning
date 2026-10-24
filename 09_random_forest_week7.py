# =========================================================
# الواجب النهائي للأسبوع السابع - نادي الذكاء الاصطناعي
# أشجار القرار والغابات العشوائية (Decision Trees & Random Forests)
# بيانات تيتانيك (Titanic Dataset) ودراسة أثر عدد الأشجار
# =========================================================

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ---------------------------------------------------------
# 1. تحميل وتجهيز البيانات (Data Preprocessing)
# ---------------------------------------------------------
df = sns.load_dataset('titanic')

# تحويل عمود الجنس (sex) إلى أرقام (0 و 1) وتعبئة الأعمار الناقصة بالوسيط
df['sex'] = (df['sex'] == 'female').astype(int)
df['age'] = df['age'].fillna(df['age'].median())
df['fare'] = df['fare'].fillna(df['fare'].median())

# اختيار المدخلات (Features) والهدف (Target)
X = df[['sex', 'pclass', 'age', 'fare']]
y = df['survived']

# ---------------------------------------------------------
# 2. تقسيم البيانات (Train, Validation, Test) بالشكل الصحيح
# ---------------------------------------------------------
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)
X_val, X_test_final, y_val, y_test_final = train_test_split(
    X_temp, y_temp, test_size=0.50, random_state=42, stratify=y_temp
)

print(f"حجم بيانات التدريب (Train): {len(X_train)}")
print(f"حجم بيانات التحقق (Validation): {len(X_val)}")
print(f"حجم بيانات الاختبار (Test): {len(X_test_final)}\n")

# ---------------------------------------------------------
# 3. تجربة أثر عدد الأشجار (n_estimators) على دقة التحقق
# ---------------------------------------------------------
tree_counts = [1, 5, 10, 25, 50, 100, 200, 300, 500]
val_accuracies = []
train_accuracies = []

print(f"{'n_estimators':<15} | {'Train Accuracy':<18} | {'Val Accuracy':<18}")
print("-" * 55)

for n in tree_counts:
    forest = RandomForestClassifier(n_estimators=n, random_state=42)
    forest.fit(X_train, y_train)
    
    train_acc = accuracy_score(y_train, forest.predict(X_train))
    val_acc = accuracy_score(y_val, forest.predict(X_val))
    
    train_accuracies.append(train_acc)
    val_accuracies.append(val_acc)
    
    print(f"{n:<15} | {train_acc:<18.2%} | {val_acc:<18.2%}")

# ---------------------------------------------------------
# 4. إعدادات الألوان ورسم العلاقة بيانياً (n_estimators vs Accuracy)
# ---------------------------------------------------------
BLUE = "#2563EB"
PURPLE = "#8b5cf6"
TEXT = "#1F2937"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12,
    "axes.titlesize": 16,
    "axes.labelsize": 13,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "text.color": TEXT,
    "axes.labelcolor": TEXT,
    "figure.facecolor": "white",
    "axes.facecolor": "white"
})

fig, ax = plt.subplots(figsize=(9, 5.5), constrained_layout=True)

ax.plot(tree_counts, train_accuracies, marker='o', label='Training Accuracy', color=BLUE, linewidth=2)
ax.plot(tree_counts, val_accuracies, marker='s', label='Validation Accuracy', color=PURPLE, linewidth=2)

ax.set_title("Random Forest: n_estimators vs. Accuracy")
ax.set_xlabel("Number of Trees (n_estimators)")
ax.set_ylabel("Accuracy")
ax.grid(alpha=0.15)
ax.legend(frameon=False)
plt.show()