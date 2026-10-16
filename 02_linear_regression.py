import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# ==========================================
# 1. تطبيق الانحدار الخطي (Scikit-Learn)
# ==========================================
# بيانات تدريبية بسيطة (المساحة مقابل السعر)
data = pd.DataFrame({
    'area': [80, 100, 120, 140, 160],
    'price': [300, 360, 420, 480, 540]
})

X = data[['area']]
y = data['price']

# إنشاء وتدريب النموذج
model = LinearRegression()
model.fit(X, y)

# التنبؤ بأسعار المساحات المحددة (150 و 180 متر)
pred_150 = model.predict(pd.DataFrame({'area': [150]}))[0]
pred_180 = model.predict(pd.DataFrame({'area': [180]}))[0]

print("==========================================")
print("=== 1. نتائج الانحدار الخطي (أسعار المنازل) ===")
print("==========================================")
print(f"الميل / الوزن (w): {model.coef_[0]:.2f}")
print(f"الثابت / القطع الصادي (b): {model.intercept_:.2f}")
print(f"توقع سعر منزل مساحته 150م: {pred_150:.2f} ألف ريال")
print(f"توقع سعر منزل مساحته 180م (استقراء): {pred_180:.2f} ألف ريال")

# ==========================================
# 2. النزول التدريجي اليدوي (Gradient Descent)
# ==========================================
x_vals = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y_vals = np.array([45.0, 50.0, 60.0, 68.0, 75.0])

print("\n==========================================")
print("=== 2. تجربة معدلات التعلم (Gradient Descent) ===")
print("==========================================")

for lr in [0.01, 0.05, 0.1]:
    w, b = 0.0, 0.0
    epochs = 1000
    for i in range(epochs):
        y_pred = w * x_vals + b
        error = y_pred - y_vals
        dw = 2 * np.mean(error * x_vals)
        db = 2 * np.mean(error)
        w -= lr * dw
        b -= lr * db
    
    pred_3_5 = w * 3.5 + b
    print(f"معدل التعلم (lr={lr:<4}): w={w:.2f}, b={b:.2f} | التوقع عند 3.5 ساعات = {pred_3_5:.2f}")