import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, log_loss
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

# ==========================================
# 1. تحميل وتجهيز البيانات
# ==========================================
data = load_breast_cancer(as_frame=True)
features = ["mean radius", "mean texture"]
X = data.data[features].copy()
y = (data.target == 0).astype(int)

class_names = {0: "Benign", 1: "Malignant"}

X_dev, X_test, y_dev, y_test = train_test_split(X, y, test_size=0.20, stratify=y, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_dev, y_dev, test_size=0.25, stratify=y_dev, random_state=42)

print("=== 1. تقسيم البيانات ===")
print(f"التدريب (Training): {len(X_train)}")
print(f"التحقق (Validation): {len(X_val)}")
print(f"الاختبار (Test): {len(X_test)}")

# ==========================================
# 2. رسم توزيع بيانات التدريب
# ==========================================
BLUE, PURPLE, TEXT = "#2563EB", "#8b5cf6", "#1F2937"
plt.rcParams.update({"font.size": 12, "text.color": TEXT, "axes.labelcolor": TEXT})

fig, ax = plt.subplots(figsize=(8, 5))
for label, color in [(0, BLUE), (1, PURPLE)]:
    mask = y_train == label
    ax.scatter(X_train.loc[mask, "mean radius"], X_train.loc[mask, "mean texture"],
               color=color, label=class_names[label], s=40, alpha=0.75)
ax.set_title("Training Data: Benign vs Malignant")
ax.set_xlabel("Mean radius")
ax.set_ylabel("Mean texture")
ax.legend()
plt.show()

# ==========================================
# 3. رسم دالة السجمويد (Sigmoid Function)
# ==========================================
z_curve = np.linspace(-6, 6, 400)
p_curve = 1 / (1 + np.exp(-z_curve))

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(z_curve, p_curve, color=PURPLE, linewidth=3)
ax.axhline(0.5, color="#9CA3AF", linestyle="--")
ax.axvline(0, color="#9CA3AF", linestyle="--")

for val in [-2, 0, 2]:
    prob = 1 / (1 + np.exp(-val))
    ax.scatter(val, prob, color="#16151f", s=75, zorder=3)
    ax.annotate(f"({val}, {prob:.2f})", (val, prob), xytext=(10, 12), textcoords="offset points")

ax.set_title("Sigmoid: From Score to Probability")
ax.set_xlabel("Model score (z)")
ax.set_ylabel("Probability")
plt.show()

# ==========================================
# 4. تدريب النموذج وتجربة عتبات القرار (Thresholds)
# ==========================================
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)

sample = X_val.iloc[[0]]
probs = model.predict_proba(sample)[0]
malignant_prob = probs[1]

print("\n=== 2. تجربة الاحتمالات وتغيير العتبة (Threshold) ===")
print(f"احتمال الورم الخبيث للعيّنة: {malignant_prob:.2%}")

for th in [0.3, 0.5, 0.7]:
    pred = int(malignant_prob >= th)
    print(f"عند العتبة {th:.1f}: التصنيف هو -> {class_names[pred]}")

# ==========================================
# 5. رسم حد القرار (Decision Boundary)
# ==========================================
x_min, x_max = X_train["mean radius"].min() - 1, X_train["mean radius"].max() + 1
y_min, y_max = X_train["mean texture"].min() - 1, X_train["mean texture"].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200), np.linspace(y_min, y_max, 200))
grid = pd.DataFrame({"mean radius": xx.ravel(), "mean texture": yy.ravel()})

Z = model.predict_proba(grid)[:, 1].reshape(xx.shape)

fig, ax = plt.subplots(figsize=(8, 5))
ax.contourf(xx, yy, Z, levels=[0, 0.5, 1], colors=[BLUE, PURPLE], alpha=0.15)
ax.contour(xx, yy, Z, levels=[0.5], colors=[TEXT], linewidths=2)

for label, color in [(0, BLUE), (1, PURPLE)]:
    mask = y_train == label
    ax.scatter(X_train.loc[mask, "mean radius"], X_train.loc[mask, "mean texture"],
               color=color, label=class_names[label], s=30, alpha=0.7)
ax.set_title("Logistic Regression: Decision Boundary")
ax.legend()
plt.show()

# ==========================================
# 6. رسم دالة الخسارة Log Loss للتنظيم
# ==========================================
c_values = np.logspace(-4, 4, 30)
train_losses, val_losses = [], []

for c in c_values:
    m = make_pipeline(StandardScaler(), LogisticRegression(C=c, max_iter=1000))
    m.fit(X_train, y_train)
    train_losses.append(log_loss(y_train, m.predict_proba(X_train)))
    val_losses.append(log_loss(y_val, m.predict_proba(X_val)))

plt.figure(figsize=(8, 5))
plt.plot(c_values, train_losses, label="Training Loss", color=BLUE)
plt.plot(c_values, val_losses, label="Validation Loss", color="#cb6ce6")
plt.xscale("log")
plt.xlabel("C (Higher C = Weaker Regularization)")
plt.ylabel("Log Loss")
plt.title("Training vs. Validation Loss")
plt.legend()
plt.grid(alpha=0.3)
plt.show()