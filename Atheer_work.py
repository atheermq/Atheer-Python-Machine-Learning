import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. أكواد قراءة البيانات وفحص الجودة (تجريبي وأساسي)
# ==========================================
try:
    df = pd.read_csv('sales_dirty.csv')
except Exception:
    try:
        df = pd.read_csv('sales.csv')
    except Exception:
        df = pd.read_excel('sales.csv.xlsx')

print("=== 1. فحص الجودة والنظرة الأولى ===")
print("حجم البيانات (صفوف، أعمدة):", df.shape)
print("\nمعلومات البيانات:")
print(df.info())
print("\nعدد القيم المفقودة لكل عمود:\n", df.isna().sum())
print("\nنسبة المفقود %:\n", (df.isna().mean() * 100).round(2))
print("\nعدد الصفوف المكررة:", df.duplicated().sum())

# ==========================================
# 2. أكواد التنظيف وتوحيد التنسيق
# ==========================================
# أ) حذف التكرار
df = df.drop_duplicates()

# ب) تنظيف السعر وتحويله إلى رقم
if 'UnitPrice' in df.columns:
    df['UnitPrice'] = df['UnitPrice'].astype(str).str.replace(' SAR', '', regex=False)
    df['UnitPrice'] = pd.to_numeric(df['UnitPrice'], errors='coerce')

# ج) تحويل التاريخ إلى Datetime
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# د) توحيد الفروع لتبقى 4 فروع فقط
if 'Branch' in df.columns:
    df['Branch'] = df['Branch'].astype(str).str.strip().str.title()
    valid_branches = ['Olaya', 'Malqa', 'Yasmeen', 'Narjis', 'Jeddah', 'Riyadh', 'Dammam', 'Najran']
    df['Branch'] = df['Branch'].apply(lambda x: x if x in valid_branches else 'Unknown')

# هـ) تعويض المفقود بالوسيط (Median) لكل منتج
if 'UnitPrice' in df.columns and 'Product' in df.columns:
    df['UnitPrice'] = df['UnitPrice'].fillna(df.groupby('Product')['UnitPrice'].transform('median'))
    df['UnitPrice'] = df['UnitPrice'].fillna(df['UnitPrice'].median())

if 'Quantity' in df.columns:
    df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())

# و) إضافة عمود Total وحفظ الملف النظيف
if 'Quantity' in df.columns and 'UnitPrice' in df.columns:
    df['Total'] = df['Quantity'] * df['UnitPrice']

df.to_csv('sales_clean.csv', index=False)
print("\nتم حفظ الملف النظيف بنجاح باسم: sales_clean.csv")

# ==========================================
# 3. الأكواد التحليلية والتجميعات (GroupBy)
# ==========================================
print("\n=== 2. نتائج التحليل ===")
if 'Total' in df.columns:
    print("الملخص الإحصائي المكتمل (Describe):\n", df['Total'].describe())

if 'Branch' in df.columns and 'Total' in df.columns:
    print("\nإجمالي المبيعات لكل فرع:\n", df.groupby('Branch')['Total'].sum().sort_values(ascending=False))

if 'Product' in df.columns and 'Total' in df.columns:
    print("\nأعلى 5 منتجات مبيعاً:\n", df.groupby('Product')['Total'].sum().nlargest(5))

# ==========================================
# 4. الرسوم البيانية الاستكشافية (EDA Plots)
# ==========================================
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

# رسم المبيعات حسب الفرع
if 'Branch' in df.columns and 'Total' in df.columns:
    plt.figure(figsize=(8, 4))
    branch_sales = df.groupby('Branch')['Total'].sum().sort_values(ascending=False)
    sns.barplot(x=branch_sales.index, y=branch_sales.values, palette='Blues_d')
    plt.title('Total Sales by Branch (SAR)')
    plt.xlabel('Branch')
    plt.ylabel('Sales')
    plt.tight_layout()
    plt.savefig('branch_sales.png', dpi=150)
    plt.show()

# رسم مصفوفة الارتباط (Heatmap)
numeric_cols = df.select_dtypes(include=[np.number]).columns
if len(numeric_cols) > 1:
    plt.figure(figsize=(6, 4))
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.savefig('correlation_matrix.png', dpi=150)
    plt.show()
    