# ==========================================
# نموذج أشجار القرار (Decision Tree Classifier)
# ==========================================

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. تحميل بيانات تجريبية مشهورة (بيانات الزهور Iris)
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# 2. تقسيم البيانات إلى بيانات تدريب (Train) وبيانات اختبار (Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. إنشاء نموذج شجرة القرار
model = DecisionTreeClassifier(random_state=42)

# 4. تدريب النموذج على البيانات
model.fit(X_train, y_train)

# 5. التنبؤ واختبار دقة النموذج
y_pred = model.predict(X_test)

# 6. طباعة النتائج ودقة النموذج
print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))