# =========================================================
# نادي الذكاء الاصطناعي - جامعة نجران (الأسبوع السادس)
# التصنيف الثنائي باستخدام الانحدار اللوجستي (Logistic Regression)
# =========================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

# ---------------------------------------------------------
# 1. تحميل واستكشاف البيانات (Breast Cancer Dataset)
# ---------------------------------------------------------
data = load_breast_cancer(as_frame=True)
features = ["mean radius", "mean texture"]

X = data.data[features].copy()
# تحويل الهدف: 1 للورم الخبيث (Malignant) و 0 للورم الحميد (Benign)
y = (data.target == 0).astype(int)

class_names = {0: "Benign", 1: "Malignant"}

print("=== 1. المعاينة الأولى للبيانات ===")
df = X.copy()
df["target"] = y
df["class_name"] = y.map(class_names)
print(df.head().to_string(index=False))

print("\nحجم البيانات الأصلي:", data.data.shape)
counts = y.value_counts().sort_index()
counts.index = ["Benign (0)", "Malignant (1)"]
print("\nتوزيع الفئات:\n", counts)

# ---------------------------------------------------------
# 2. تقسيم البيانات (Data Splitting)
# ---------------------------------------------------------
X_dev, X_test, y_dev, y_test = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=42
)
X_train, X_val, y_train, y_val = train_test_split(
    X_dev, y_dev, test_size=0.25, stratify=y_dev, random_state=42
)

print("\n=== 2. تقسيم البيانات ===")
print("بيانات التدريب (Training):", len(X_train))
print("بيانات التحقق (Validation):", len(X_val))
print("بيانات الاختبار (Test):", len(X_test))

# ---------------------------------------------------------
# 3. بناء وتدريب النموذج الأساسي (Pipeline)
# ---------------------------------------------------------
model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000)
)
model.fit(X_train, y_train)
print("\n=== 3. تم تدريب النموذج بنجاح ===")

# ---------------------------------------------------------
# 4. التنبؤ وتطبيق عتبة التصنيف (Threshold)
# ---------------------------------------------------------
sample = X_val.iloc[[0]]
probabilities = model.predict_proba(sample)[0]

print("\n=== 4. نتائج التنبؤ لعينة من بيانات التحقق ===")
print(f"احتمالية الورم الحميد (Benign): {probabilities[0]:.2%}")
print(f"احتمالية الورم الخبيث (Malignant): {probabilities[1]:.2%}")

threshold = 0.5
predicted_class = int(probabilities[1] >= threshold)
print("عتبة التصنيف (Threshold):", threshold)
print("الفئة المتوقعة (Predicted Class):", class_names[predicted_class])

# ---------------------------------------------------------
# 5. تقييم الدقة وفحص فرط التعلم (Overfitting Check)
# ---------------------------------------------------------
train_predictions = model.predict(X_train)
val_predictions = model.predict(X_val)

train_accuracy = accuracy_score(y_train, train_predictions)
val_accuracy = accuracy_score(y_val, val_predictions)

print("\n=== 5. تقييم الدقة وفحص الفجوة ===")
print(f"دقة التدريب (Training Accuracy): {train_accuracy:.2%}")
print(f"دقة التحقق (Validation Accuracy): {val_accuracy:.2%}")

accuracy_gap = train_accuracy - val_accuracy
print(f"الفجوة بين الدقتين: {accuracy_gap * 100:.2f} نقطة مئوية")

# ---------------------------------------------------------
# 6. مثال توضيحي لمحدودية مقياس الدقة (Limitations of Accuracy)
# ---------------------------------------------------------
example_true = np.array([0] * 95 + [1] * 5)
example_predictions = np.zeros_like(example_true)
example_accuracy = accuracy_score(example_true, example_predictions)

print("\n=== 6. مثال محدودية الدقة مع الفئات غير المتوازنة ===")
print(f"الدقة المحسوبة: {example_accuracy:.2%}")
print("تنبيه: النموذج توقع أن جميع الحالات سليمة وتم تفويت جميع الحالات الخبيثة الـ 5!")

# ---------------------------------------------------------
# 7. مقارنة تأثير قوة التنظيم (Regularization C Values)
# ---------------------------------------------------------
print("\n=== 7. مقارنة أثر تغيير معامل التنظيم C ===")
print(f"{'C Value':>10} | {'Train Accuracy':>18} | {'Val Accuracy':>18}")
print("-" * 55)

for c_value in [0.01, 1.0, 100.0]:
    comp_model = make_pipeline(
        StandardScaler(),
        LogisticRegression(C=c_value, max_iter=1000)
    )
    comp_model.fit(X_train, y_train)
    
    comp_train_acc = accuracy_score(y_train, comp_model.predict(X_train))
    comp_val_acc = accuracy_score(y_val, comp_model.predict(X_val))
    
    print(f"{c_value:>10.2f} | {comp_train_acc:>18.2%} | {comp_val_acc:>18.2%}")
    # =========================================================
# الواجب الشامل للأسبوع السادس - نادي الذكاء الاصطناعي
# التصنيف الثنائي باستخدام الانحدار اللوجستي والرسوم البيانية
# =========================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

# ---------------------------------------------------------
# 1. تحميل واستكشاف البيانات (Breast Cancer Dataset)
# ---------------------------------------------------------
data = load_breast_cancer(as_frame=True)
features = ["mean radius", "mean texture"]

X = data.data[features].copy()
y = (data.target == 0).astype(int)  # 1 للخبيث، 0 للحميد

class_names = {0: "Benign", 1: "Malignant"}

print("=== 1. المعاينة الأولى للبيانات ===")
df = X.copy()
df["target"] = y
df["class_name"] = y.map(class_names)
print(df.head().to_string(index=False))

print("\nحجم البيانات الأصلي:", data.data.shape)
counts = y.value_counts().sort_index()
counts.index = ["Benign (0)", "Malignant (1)"]
print("\nتوزيع الفئات:\n", counts)

# ---------------------------------------------------------
# 2. تقسيم البيانات (Data Splitting)
# ---------------------------------------------------------
X_dev, X_test, y_dev, y_test = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=42
)
X_train, X_val, y_train, y_val = train_test_split(
    X_dev, y_dev, test_size=0.25, stratify=y_dev, random_state=42
)

print("\n=== 2. تقسيم البيانات ===")
print("بيانات التدريب (Training):", len(X_train))
print("بيانات التحقق (Validation):", len(X_val))
print("بيانات الاختبار (Test):", len(X_test))

# ---------------------------------------------------------
# 3. إعدادات الألوان والخطوط للرسومات البيانية
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

# ---------------------------------------------------------
# 4. رسم بيانات التدريب (Training Data Scatter Plot)
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5), constrained_layout=True)
for label, color in [(0, BLUE), (1, PURPLE)]:
    mask = y_train == label
    ax.scatter(
        X_train.loc[mask, "mean radius"],
        X_train.loc[mask, "mean texture"],
        color=color,
        label=class_names[label],
        s=40,
        alpha=0.75,
        edgecolors="white",
        linewidths=0.4
    )
ax.set_title("Training Data: Benign vs Malignant")
ax.set_xlabel("Mean radius")
ax.set_ylabel("Mean texture")
ax.grid(alpha=0.15)
ax.legend(frameon=False)
plt.show()

# ---------------------------------------------------------
# 5. رسم دالة السيغمويد (Sigmoid Function Curve)
# ---------------------------------------------------------
z_curve = np.linspace(-6, 6, 400)
p_curve = 1 / (1 + np.exp(-z_curve))

fig, ax = plt.subplots(figsize=(8, 5), constrained_layout=True)
ax.plot(z_curve, p_curve, color=PURPLE, linewidth=3, label=r"$\sigma(z)$")
ax.axhline(0.5, color="#9CA3AF", linestyle="--", linewidth=1.5)
ax.axvline(0, color="#9CA3AF", linestyle="--", linewidth=1.5)

for value in [-2, 0, 2]:
    probability = 1 / (1 + np.exp(-value))
    ax.scatter(value, probability, color="#16151f", s=75, zorder=3)
    ax.annotate(
        f"({value}, {probability:.2f})",
        (value, probability),
        xytext=(10, 12),
        textcoords="offset points",
        fontsize=11
    )

ax.set_title("Sigmoid: From Score to Probability")
ax.set_xlabel("Model score (z)")
ax.set_ylabel("Probability of class 1")
ax.set_ylim(-0.05, 1.12)
ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
ax.grid(alpha=0.15)
plt.show()

# ---------------------------------------------------------
# 6. تدريب نموذج الانحدار اللوجستي وتقييمه
# ---------------------------------------------------------
model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000)
)
model.fit(X_train, y_train)
print("\n=== 3. تم تدريب النموذج بنجاح ===")

# ---------------------------------------------------------
# 7. التنبؤ وتطبيق عتبة التصنيف (Threshold)
# ---------------------------------------------------------
sample = X_val.iloc[[0]]
probabilities = model.predict_proba(sample)[0]

print("\n=== 4. نتائج التنبؤ لعينة من بيانات التحقق ===")
print(f"احتمالية الورم الحميد (Benign): {probabilities[0]:.2%}")
print(f"احتمالية الورم الخبيث (Malignant): {probabilities[1]:.2%}")

threshold = 0.5
predicted_class = int(probabilities[1] >= threshold)
print("عتبة التصنيف (Threshold):", threshold)
print("الفئة المتوقعة (Predicted Class):", class_names[predicted_class])

# ---------------------------------------------------------
# 8. تقييم الدقة وفحص فرط التعلم (Overfitting Check)
# ---------------------------------------------------------
train_predictions = model.predict(X_train)
val_predictions = model.predict(X_val)

train_accuracy = accuracy_score(y_train, train_predictions)
val_accuracy = accuracy_score(y_val, val_predictions)

print("\n=== 5. تقييم الدقة وفحص الفجوة ===")
print(f"دقة التدريب (Training Accuracy): {train_accuracy:.2%}")
print(f"دقة التحقق (Validation Accuracy): {val_accuracy:.2%}")

accuracy_gap = train_accuracy - val_accuracy
print(f"الفجوة بين الدقتين: {accuracy_gap * 100:.2f} نقطة مئوية")

# ---------------------------------------------------------
# 9. مثال توضيحي لمحدودية مقياس الدقة
# ---------------------------------------------------------
example_true = np.array([0] * 95 + [1] * 5)
example_predictions = np.zeros_like(example_true)
example_accuracy = accuracy_score(example_true, example_predictions)

print("\n=== 6. مثال محدودية الدقة مع الفئات غير المتوازنة ===")
print(f"الدقة المحسوبة: {example_accuracy:.2%}")
print("تنبيه: النموذج توقع أن جميع الحالات سليمة وتم تفويت جميع الحالات الخبيثة الـ 5!")

# ---------------------------------------------------------
# 10. مقارنة تأثير قوة التنظيم (Regularization C Values)
# ---------------------------------------------------------
print("\n=== 7. مقارنة أثر تغيير معامل التنظيم C ===")
print(f"{'C Value':>10} | {'Train Accuracy':>18} | {'Val Accuracy':>18}")
print("-" * 55)

for c_value in [0.01, 1.0, 100.0]:
    comp_model = make_pipeline(
        StandardScaler(),
        LogisticRegression(C=c_value, max_iter=1000)
    )
    comp_model.fit(X_train, y_train)
    
    comp_train_acc = accuracy_score(y_train, comp_model.predict(X_train))
    comp_val_acc = accuracy_score(y_val, comp_model.predict(X_val))
    
    print(f"{c_value:>10.2f} | {comp_train_acc:>18.2%} | {comp_val_acc:>18.2%}")
    # =========================================================
# الواجب الشامل والنهائي للأسبوع السادس - نادي الذكاء الاصطناعي
# التصنيف الثنائي باستخدام الانحدار اللوجستي (مع كافة الرسوم البيانية)
# =========================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

# ---------------------------------------------------------
# 1. تحميل واستكشاف البيانات
# ---------------------------------------------------------
data = load_breast_cancer(as_frame=True)
features = ["mean radius", "mean texture"]

X = data.data[features].copy()
y = (data.target == 0).astype(int)  # 1 للخبيث، 0 للحميد

class_names = {0: "Benign", 1: "Malignant"}

print("=== 1. المعاينة الأولى للبيانات ===")
df = X.copy()
df["target"] = y
df["class_name"] = y.map(class_names)
print(df.head().to_string(index=False))

print("\nحجم البيانات الأصلي:", data.data.shape)
counts = y.value_counts().sort_index()
counts.index = ["Benign (0)", "Malignant (1)"]
print("\nتوزيع الفئات:\n", counts)

# ---------------------------------------------------------
# 2. تقسيم البيانات
# ---------------------------------------------------------
X_dev, X_test, y_dev, y_test = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=42
)
X_train, X_val, y_train, y_val = train_test_split(
    X_dev, y_dev, test_size=0.25, stratify=y_dev, random_state=42
)

# ---------------------------------------------------------
# 3. إعدادات الألوان والخطوط الموحدة للرسومات
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

# ---------------------------------------------------------
# الرسمة الأولى: توزيع بيانات التدريب (Training Data Scatter Plot)
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5), constrained_layout=True)
for label, color in [(0, BLUE), (1, PURPLE)]:
    mask = y_train == label
    ax.scatter(
        X_train.loc[mask, "mean radius"],
        X_train.loc[mask, "mean texture"],
        color=color,
        label=class_names[label],
        s=40, alpha=0.75, edgecolors="white", linewidths=0.4
    )
ax.set_title("Training Data: Benign vs Malignant")
ax.set_xlabel("Mean radius")
ax.set_ylabel("Mean texture")
ax.grid(alpha=0.15)
ax.legend(frameon=False)
plt.show()

# ---------------------------------------------------------
# الرسمة الثانية: دالة السيغمويد (Sigmoid Function Curve)
# ---------------------------------------------------------
z_curve = np.linspace(-6, 6, 400)
p_curve = 1 / (1 + np.exp(-z_curve))

fig, ax = plt.subplots(figsize=(8, 5), constrained_layout=True)
ax.plot(z_curve, p_curve, color=PURPLE, linewidth=3, label=r"$\sigma(z)$")
ax.axhline(0.5, color="#9CA3AF", linestyle="--", linewidth=1.5)
ax.axvline(0, color="#9CA3AF", linestyle="--", linewidth=1.5)

for value in [-2, 0, 2]:
    probability = 1 / (1 + np.exp(-value))
    ax.scatter(value, probability, color="#16151f", s=75, zorder=3)
    ax.annotate(
        f"({value}, {probability:.2f})",
        (value, probability),
        xytext=(10, 12), textcoords="offset points", fontsize=11
    )

ax.set_title("Sigmoid: From Score to Probability")
ax.set_xlabel("Model score (z)")
ax.set_ylabel("Probability of class 1")
ax.set_ylim(-0.05, 1.12)
ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
ax.grid(alpha=0.15)
plt.show()

# ---------------------------------------------------------
# تدريب نموذج الانحدار اللوجستي
# ---------------------------------------------------------
model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000)
)
model.fit(X_train, y_train)

# ---------------------------------------------------------
# الرسمة الثالثة: حدود القرار (Decision Boundary Plot)
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5), constrained_layout=True)

# رسم نقاط البيانات الحقيقية
for label, color in [(0, BLUE), (1, PURPLE)]:
    mask = y_train == label
    ax.scatter(
        X_train.loc[mask, "mean radius"],
        X_train.loc[mask, "mean texture"],
        color=color, label=class_names[label], s=35, alpha=0.7
    )

# شبكة لرسم حدود القرار
scaler = model.named_steps['standardscaler']
log_reg = model.named_steps['logisticregression']

x_min, x_max = X_train["mean radius"].min() - 1, X_train["mean radius"].max() + 1
y_min, y_max = X_train["mean texture"].min() - 1, X_train["mean texture"].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200), np.linspace(y_min, y_max, 200))
grid_points = np.c_[xx.ravel(), yy.ravel()]
probs = log_reg.predict_proba(scaler.transform(grid_points))[:, 1].reshape(xx.shape)

# رسم خلفية الاحتمالات وحدود القرار عند العتبة 0.5 و 0.7
ax.contourf(xx, yy, probs, levels=20, cmap="coolwarm", alpha=0.2)
decision_boundary = ax.contour(xx, yy, probs, levels=[0.5], colors="black", linewidths=2)
decision_boundary_07 = ax.contour(xx, yy, probs, levels=[0.7], colors="black", linestyles="dashed", linewidths=1.5)

ax.set_title("Logistic Regression: Decision Boundary")
ax.set_xlabel("Mean radius")
ax.set_ylabel("Mean texture")
ax.legend(frameon=False)
plt.show()

# ---------------------------------------------------------
# طباعة النتائج والتقييم في التيرمينال
# ---------------------------------------------------------
train_predictions = model.predict(X_train)
val_predictions = model.predict(X_val)

train_accuracy = accuracy_score(y_train, train_predictions)
val_accuracy = accuracy_score(y_val, val_predictions)

print("\n=== تقييم الدقة وفحص الفجوة ===")
print(f"دقة التدريب (Training Accuracy): {train_accuracy:.2%}")
print(f"دقة التحقق (Validation Accuracy): {val_accuracy:.2%}")
print(f"الفجوة بين الدقتين: {(train_accuracy - val_accuracy) * 100:.2f} نقطة مئوية")

print("\n=== مقارنة أثر تغيير معامل التنظيم C ===")
for c_value in [0.01, 1.0, 100.0]:
    comp_model = make_pipeline(StandardScaler(), LogisticRegression(C=c_value, max_iter=1000))
    comp_model.fit(X_train, y_train)
    c_train_acc = accuracy_score(y_train, comp_model.predict(X_train))
    c_val_acc = accuracy_score(y_val, comp_model.predict(X_val))
    print(f"C = {c_value:<5} | Train Acc: {c_train_acc:.2%} | Val Acc: {c_val_acc:.2%}")
    # =========================================================
# الواجب الشامل والنهائي للأسبوع السادس - نادي الذكاء الاصطناعي
# التصنيف الثنائي باستخدام الانحدار اللوجستي (مع كافة الرسوم البيانية الـ 4)
# =========================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

# ---------------------------------------------------------
# 1. تحميل واستكشاف البيانات
# ---------------------------------------------------------
data = load_breast_cancer(as_frame=True)
features = ["mean radius", "mean texture"]

X = data.data[features].copy()
y = (data.target == 0).astype(int)  # 1 للخبيث، 0 للحميد

class_names = {0: "Benign", 1: "Malignant"}

print("=== 1. المعاينة الأولى للبيانات ===")
df = X.copy()
df["target"] = y
df["class_name"] = y.map(class_names)
print(df.head().to_string(index=False))

print("\nحجم البيانات الأصلي:", data.data.shape)
counts = y.value_counts().sort_index()
counts.index = ["Benign (0)", "Malignant (1)"]
print("\nتوزيع الفئات:\n", counts)

# ---------------------------------------------------------
# 2. تقسيم البيانات
# ---------------------------------------------------------
X_dev, X_test, y_dev, y_test = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=42
)
X_train, X_val, y_train, y_val = train_test_split(
    X_dev, y_dev, test_size=0.25, stratify=y_dev, random_state=42
)

# ---------------------------------------------------------
# 3. إعدادات الألوان والخطوط الموحدة للرسومات
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

# ---------------------------------------------------------
# الرسمة الأولى: توزيع بيانات التدريب (Training Data Scatter Plot)
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5), constrained_layout=True)
for label, color in [(0, BLUE), (1, PURPLE)]:
    mask = y_train == label
    ax.scatter(
        X_train.loc[mask, "mean radius"],
        X_train.loc[mask, "mean texture"],
        color=color,
        label=class_names[label],
        s=40, alpha=0.75, edgecolors="white", linewidths=0.4
    )
ax.set_title("Training Data: Benign vs Malignant")
ax.set_xlabel("Mean radius")
ax.set_ylabel("Mean texture")
ax.grid(alpha=0.15)
ax.legend(frameon=False)
plt.show()

# ---------------------------------------------------------
# الرسمة الثانية: دالة السيغمويد (Sigmoid Function Curve)
# ---------------------------------------------------------
z_curve = np.linspace(-6, 6, 400)
p_curve = 1 / (1 + np.exp(-z_curve))

fig, ax = plt.subplots(figsize=(8, 5), constrained_layout=True)
ax.plot(z_curve, p_curve, color=PURPLE, linewidth=3, label=r"$\sigma(z)$")
ax.axhline(0.5, color="#9CA3AF", linestyle="--", linewidth=1.5)
ax.axvline(0, color="#9CA3AF", linestyle="--", linewidth=1.5)

for value in [-2, 0, 2]:
    probability = 1 / (1 + np.exp(-value))
    ax.scatter(value, probability, color="#16151f", s=75, zorder=3)
    ax.annotate(
        f"({value}, {probability:.2f})",
        (value, probability),
        xytext=(10, 12), textcoords="offset points", fontsize=11
    )

ax.set_title("Sigmoid: From Score to Probability")
ax.set_xlabel("Model score (z)")
ax.set_ylabel("Probability of class 1")
ax.set_ylim(-0.05, 1.12)
ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
ax.grid(alpha=0.15)
plt.show()

# ---------------------------------------------------------
# تدريب نموذج الانحدار اللوجستي الأساسي
# ---------------------------------------------------------
model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000)
)
model.fit(X_train, y_train)

# ---------------------------------------------------------
# الرسمة الثالثة: حدود القرار (Decision Boundary Plot)
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5), constrained_layout=True)

for label, color in [(0, BLUE), (1, PURPLE)]:
    mask = y_train == label
    ax.scatter(
        X_train.loc[mask, "mean radius"],
        X_train.loc[mask, "mean texture"],
        color=color, label=class_names[label], s=35, alpha=0.7
    )

scaler = model.named_steps['standardscaler']
log_reg = model.named_steps['logisticregression']

x_min, x_max = X_train["mean radius"].min() - 1, X_train["mean radius"].max() + 1
y_min, y_max = X_train["mean texture"].min() - 1, X_train["mean texture"].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200), np.linspace(y_min, y_max, 200))
grid_points = np.c_[xx.ravel(), yy.ravel()]
probs = log_reg.predict_proba(scaler.transform(grid_points))[:, 1].reshape(xx.shape)

ax.contourf(xx, yy, probs, levels=20, cmap="coolwarm", alpha=0.2)
ax.contour(xx, yy, probs, levels=[0.5], colors="black", linewidths=2)
ax.contour(xx, yy, probs, levels=[0.7], colors="black", linestyles="dashed", linewidths=1.5)

ax.set_title("Logistic Regression: Decision Boundary")
ax.set_xlabel("Mean radius")
ax.set_ylabel("Mean texture")
ax.legend(frameon=False)
plt.show()

# ---------------------------------------------------------
# الرسمة الرابعة: تأثير قيم معامل التنظيم C على دقة التدريب والتحقق
# ---------------------------------------------------------
c_range = [0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
train_accuracies = []
val_accuracies = []

for c_val in c_range:
    comp_model = make_pipeline(
        StandardScaler(),
        LogisticRegression(C=c_val, max_iter=1000)
    )
    comp_model.fit(X_train, y_train)
    train_accuracies.append(accuracy_score(y_train, comp_model.predict(X_train)))
    val_accuracies.append(accuracy_score(y_val, comp_model.predict(X_val)))

fig, ax = plt.subplots(figsize=(8, 5), constrained_layout=True)
ax.plot(np.log10(c_range), train_accuracies, marker='o', label='Training Accuracy', color=BLUE, linewidth=2)
ax.plot(np.log10(c_range), val_accuracies, marker='s', label='Validation Accuracy', color=PURPLE, linewidth=2)

ax.set_title("Regularization Strength (C) vs Accuracy")
ax.set_xlabel("log10(C) (Higher C = Weaker Regularization)")
ax.set_ylabel("Accuracy")
ax.grid(alpha=0.15)
ax.legend(frameon=False)
plt.show()

# ---------------------------------------------------------
# طباعة النتائج النهائية في التيرمينال
# ---------------------------------------------------------
train_predictions = model.predict(X_train)
val_predictions = model.predict(X_val)
train_accuracy = accuracy_score(y_train, train_predictions)
val_accuracy = accuracy_score(y_val, val_predictions)

print("\n=== تقييم الدقة وفحص الفجوة ===")
print(f"دقة التدريب (Training Accuracy): {train_accuracy:.2%}")
print(f"دقة التحقق (Validation Accuracy): {val_accuracy:.2%}")
print(f"الفجوة بين الدقتين: {(train_accuracy - val_accuracy) * 100:.2f} نقطة مئوية")