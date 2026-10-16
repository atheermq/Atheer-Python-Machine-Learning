import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

# ==========================================
# 1. تحميل وتجهيز البيانات
# ==========================================
data = load_breast_cancer(as_frame=True)
features = ["mean radius", "mean texture"]
X = data.data[features].copy()
y = (data.target == 0).astype(int)

X_dev, X_test, y_dev, y_test = train_test_split(X, y, test_size=0.20, stratify=y, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_dev, y_dev, test_size=0.25, stratify=y_dev, random_state=42)

# ==========================================
# 2. بناء النموذج وحساب الدقة وفجوة الأداء
# ==========================================
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)

train_acc = accuracy_score(y_train, model.predict(X_train))
val_acc = accuracy_score(y_val, model.predict(X_val))

print("==========================================")
print("=== 1. نتائج نموذج التصنيف اللوجستي ===")
print("==========================================")
print(f"دقة التدريب (Train Accuracy): {train_acc:.2%}")
print(f"دقة التحقق (Validation Accuracy): {val_acc:.2%}")
print(f"فجوة الدقة (Accuracy Gap): {(train_acc - val_acc)*100:.2f}%")

# ==========================================
# 3. تجربة مقارنة قوة التنظيم (Regularization Strength C)
# ==========================================
print("\n==========================================")
print("=== 2. تجربة تغيير قيم C للتنظيم ===")
print("==========================================")
print(f"{'C':>8} | {'Train Accuracy':>16} | {'Val Accuracy':>16}")
print("-" * 48)

for c_val in [0.01, 1.0, 100.0]:
    pipe = make_pipeline(StandardScaler(), LogisticRegression(C=c_val, max_iter=1000))
    pipe.fit(X_train, y_train)
    tr_acc = accuracy_score(y_train, pipe.predict(X_train))
    va_acc = accuracy_score(y_val, pipe.predict(X_val))
    print(f"{c_val:>8.2f} | {tr_acc:>16.2%} | {va_acc:>16.2%}")