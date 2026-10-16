import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. إنشاء جدول البيانات
data = pd.DataFrame({
    'hours': [1, 2, 3, 4, 5],
    'score': [45, 50, 60, 68, 75]
})

# 2. تحديد المدخل X والهدف y
X = data[['hours']]
y = data['score']

# 3. تدريب النموذج وتوقع درجة طالب يذاكر 4.5 ساعات
model = LinearRegression()
model.fit(X, y)

pred = model.predict(pd.DataFrame({'hours': [4.5]}))

print(f"الدرجة المتوقعة (عند 4.5 ساعات): {pred[0]:.1f}")
print(f"الميل (w): {model.coef_[0]:.2f}, الثابت (b): {model.intercept_:.2f}")
import numpy as np

# بيانات الطالب
hours = np.array([1., 2., 3., 4., 5.])
scores = np.array([45., 50., 60., 68., 75.])

print("=== تجربة معدلات التعلم (Gradient Descent) ===")

# تجربة معدلات التعلم المطلوبة (0.1 و 0.01، ومقارنتها مع 0.05)
for lr in [0.1, 0.01, 0.05]:
    w, b = 0.0, 0.0
    epochs = 1000
    
    for i in range(epochs):
        y_pred = w * hours + b
        error = y_pred - scores
        dw = 2 * np.mean(error * hours)
        db = 2 * np.mean(error)
        w -= lr * dw
        b -= lr * db
    
    pred_3_5 = w * 3.5 + b
    print(f"معدل التعلم (lr = {lr:<4}): w = {w:.2f}, b = {b:.2f} | التوقع عند 3.5 ساعات = {pred_3_5:.2f}")