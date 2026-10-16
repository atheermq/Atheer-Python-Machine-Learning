import pandas as pd

# 1. قراءة الملف وفحصه
df = pd.read_csv('sales_dirty.csv')
print("عدد الصفوف والأعمدة:", df.shape)
print("القيم المفقودة:\n", df.isna().sum())
print("عدد الصفوف المكررة:", df.duplicated().sum())

# 2. تنظيف التكرار والأنواع
df = df.drop_duplicates()  # حذف المكرر

# تنظيف السعر وتحويله إلى رقم
df['UnitPrice'] = pd.to_numeric(
    df['UnitPrice'].astype(str).str.replace(' SAR', ''), 
    errors='coerce'
)

# تحويل التاريخ إلى Datetime
df['Date'] = pd.to_datetime(df['Date'])

# 3. توحيد أسماء الفروع (لتصبح 4 فروع فقط)
df['Branch'] = df['Branch'].str.strip().str.title()

# 4. معالجة القيم المفقودة (تعويض سعر الوحدة بالوسيط لكل منتج)
df['UnitPrice'] = df['UnitPrice'].fillna(
    df.groupby('Product')['UnitPrice'].transform('median')
)
df['Branch'] = df['Branch'].fillna('Unknown')
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())

# 5. معالجة المتطرف وإعادة حساب Total وحفظ الملف
df['Total'] = df['Quantity'] * df['UnitPrice']
df.to_csv('sales_clean.csv', index=False)
print("تم حفظ الملف النظيف بنجاح باسم sales_clean.csv")
import pandas as pd

# 1. القراءة والحجم
df = pd.read_csv('sales.csv')
print("حجم البيانات:", df.shape)

# 2. إنشاء عمود قيمة البيع Total
df['Total'] = df['Quantity'] * df['UnitPrice']

# 3. عرض الطلبات الكبيرة (التي تتجاوز 500 ريال)
large_orders = df[df['Total'] > 500]
print("عدد الطلبات الكبيرة:", len(large_orders))

# 4. إجمالي المبيعات لكل فرع
branch_sales = df.groupby('Branch')['Total'].sum()
print("المبيعات لكل فرع:\n", branch_sales)

# 5. أعلى 5 منتجات مبيعاً
top_5_products = df.groupby('Product')['Total'].sum().sort_values(ascending=False).head(5)
print("أعلى 5 منتجات:\n", top_5_products)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# قراءة وفهم البيانات
df_cafe = pd.read_csv('cafe_sales.csv')

# تنظيف أساسي
df_cafe = df_cafe.drop_duplicates()
df_cafe['Total'] = df_cafe['Quantity'] * df_cafe['UnitPrice']

# 1. إجابة أسئلة تحليلية (مثال: أعلى ساعات اليوم مبيعاً)
hourly_sales = df_cafe.groupby('Hour')['Total'].sum()

# 2. رسم بياني 1: المبيعات حسب الساعة (Line Chart)
plt.figure(figsize=(8, 4))
plt.plot(hourly_sales.index, hourly_sales.values, marker='o')
plt.title('Hourly Sales')
plt.xlabel('Hour')
plt.ylabel('Sales (SAR)')
plt.tight_layout()
plt.savefig('hourly_sales.png', dpi=150)
plt.show()

# 3. رسم بياني 2: المبيعات حسب الفئة (Bar Chart)
plt.figure(figsize=(8, 4))
sns.barplot(data=df_cafe, x='Category', y='Total', estimator=sum, ci=None)
plt.title('Sales by Category')
plt.tight_layout()
plt.savefig('category_sales.png', dpi=150)
plt.show()

# 4. مصفوفة الارتباط (Heatmap)
plt.figure(figsize=(6, 4))
sns.heatmap(df_cafe[['Quantity', 'UnitPrice', 'Total']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig('correlation.png', dpi=150)
plt.show()


import pandas as pd
import numpy as np

# 1. قراءة البيانات وفحصها
df = pd.read_csv('cafe_sales.csv') # أو sales.csv

print("=== حجم البيانات ===")
print(f"عدد الصفوف: {df.shape[0]}، عدد الأعمدة: {df.shape[1]}")

print("\n=== القيم المفقودة ===")
print(df.isnull().sum())

# 2. تنظيف التكرار والأنواع
df = df.drop_duplicates()

if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

if 'ItemPrice' in df.columns:
    df['ItemPrice'] = pd.to_numeric(df['ItemPrice'], errors='coerce')

# 3. توحيد الفروع (التركيز على 4 فروع رئيسية)
# مثال لتوحيد الأسماء المتشابهة:
if 'Branch' in df.columns:
    df['Branch'] = df['Branch'].fillna('Unknown')
    # يمكنك تعديل التجميع حسب الأسماء الموجودة لديك في الملف

# 4. حساب عمود Total
if 'Quantity' in df.columns and 'ItemPrice' in df.columns:
    df['Total'] = df['Quantity'] * df['ItemPrice']

# 5. الطلبات الكبيرة (أكبر من 500 ريال)
large_orders = df[df['Total'] > 500]
print(f"\nعدد الطلبات الكبيرة (> 500 ريال): {len(large_orders)}")

# 6. المبيعات لكل فرع
sales_per_branch = df.groupby('Branch')['Total'].sum()
print("\n=== إجمالي المبيعات لكل فرع ===")
print(sales_per_branch)

# 7. أعلى 5 منتجات مبيعاً
top_5_items = df.groupby('Item')['Total'].sum().nlargest(5)
print("\n=== أعلى 5 منتجات من حيث المبيعات ===")
print(top_5_items)

# 8. حفظ الملف النظيف النهائي
df.to_csv('sales_clean.csv', index=False)
print("\nتم حفظ الملف النظيف باسم sales_clean.csv بنجاح.")