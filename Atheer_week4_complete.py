import pandas as pd
import numpy as np

# ==========================================
# الجزء الأول: أساسيات NumPy و Pandas (الجلسة الأولى)
# ==========================================
print("=== 1. تجربة مصفوفات NumPy ===")
# إنشاء مصفوفة أحادية للكميات والأسعار كمثال من الشرائح
qty_arr = np.array([2, 4, 3, 1])
price_arr = np.array([1500, 180, 350, 3200])
revenue = qty_arr * price_arr
print("مصفوفة المبيعات لكل طلب (Quantity * Price):", revenue)
print("المجموع الكلي للمبيعات:", revenue.sum())
print("متوسط قيمة الطلب:", revenue.mean())

# ==========================================
# الجزء الثاني: قراءة الملف وفحص الجودة (EDA)
# ==========================================
print("\n=== 2. قراءة الملف وفحص الجودة (sales_dirty.csv) ===")
try:
    df = pd.read_csv('sales_dirty.csv')
except FileNotFoundError:
    print("⚠️ تنبيه: ملف 'sales_dirty.csv' غير موجود في نفس المجلد، يرجى التأكد من وضعه بجانب الكود.")
    # بيانات افتراضية للتوضيح في حال لم يتوفر الملف حالياً
    df = pd.DataFrame({
        'OrderID': [1001, 1002, 1003, 1002, 1035],
        'Branch': ['riyadh', 'Jeddah', 'Najran ', 'riyadh', 'Najran'],
        'Product': ['Laptop', 'Tablet', 'Mouse', 'Laptop', 'Smartwatch'],
        'Quantity': [2, 1, 5, 2, np.nan],
        'UnitPrice': ['3200 SAR', '1500', '90', '3200 SAR', '750']
    })

print("حجم البيانات قبل التنظيف (صفوف، أعمدة):", df.shape)
print("عدد الصفوف المكررة:", df.duplicated().sum())
print("\nالقيم المفقودة لكل عمود:\n", df.isna().sum())

# ==========================================
# الجزء الثالث: تنظيف البيانات وتوحيد التنسيق (الجلسة الثانية)
# ==========================================
print("\n=== 3. تنفيذ خطوات التنظيف وحفظ الملف ===")
df_clean = df.copy()

# 1. حذف الصفوف المكررة
df_clean = df_clean.drop_duplicates()

# 2. تنظيف وتحويل عمود السعر (UnitPrice) إلى رقم
if 'UnitPrice' in df_clean.columns:
    df_clean['UnitPrice'] = df_clean['UnitPrice'].astype(str).str.replace(' SAR', '', regex=False)
    df_clean['UnitPrice'] = pd.to_numeric(df_clean['UnitPrice'], errors='coerce')

# 3. معالجة القيم المفقودة بالوسيط (Median)
if 'UnitPrice' in df_clean.columns:
    df_clean['UnitPrice'] = df_clean['UnitPrice'].fillna(df_clean['UnitPrice'].median())
if 'Quantity' in df_clean.columns:
    df_clean['Quantity'] = df_clean['Quantity'].fillna(df_clean['Quantity'].median())

# 4. توحيد أسماء الفروع لتصبح 4 فروع رئيسية + Unknown
if 'Branch' in df_clean.columns:
    df_clean['Branch'] = df_clean['Branch'].astype(str).str.strip().str.title()
    valid_branches = ['Jeddah', 'Dammam', 'Najran', 'Riyadh', 'Olaya', 'Malqa', 'Yasmeen', 'Narjis']
    df_clean['Branch'] = df_clean['Branch'].apply(lambda x: x if x in valid_branches else 'Unknown')

# 5. إنشاء عمود إجمالي المبيعات (Total)
df_clean['Total'] = df_clean['Quantity'] * df_clean['UnitPrice']

# 6. تصدير وحفظ الملف النظيف المطلوبة في التسليم
df_clean.to_csv('sales_clean.csv', index=False)
print("✅ تم بنجاح إنشاء وتصدير ملف البيانات النظيفة باسم: sales_clean.csv")

# ==========================================
# الجزء الرابع: الإجابة على الأسئلة التحليلية المطلوبة
# ==========================================
print("\n==========================================")
print("=== 4. نتائج التحليل والإجابة على الأسئلة ===")
print("==========================================")
print(f"1. إجمالي عدد الطلبات بعد التنظيف: {len(df_clean)}")
print(f"2. متوسط قيمة الطلب: {df_clean['Total'].mean():,.2f} ريال")
print("\n3. إجمالي المبيعات لكل فرع:")
print(df_clean.groupby('Branch')['Total'].sum())
print("\n4. أعلى 5 منتجات مبيعاً:")
print(df_clean.groupby('Product')['Total'].sum().nlargest(5))
