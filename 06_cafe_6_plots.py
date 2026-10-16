import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. قراءة وتنظيف البيانات المباشر
# ==========================================
file_path = 'cafe_sales.csv.xlsx'
df = pd.read_excel(file_path)

df_clean = df.drop_duplicates(subset=['OrderID']).copy()
df_clean['Category'] = df_clean['Category'].astype(str).str.strip().str.capitalize()
df_clean.loc[df_clean['UnitPrice'] == 160, 'UnitPrice'] = 16
df_clean['Quantity'] = df_clean['Quantity'].fillna(df_clean['Quantity'].median())
df_clean['Payment'] = df_clean['Payment'].fillna('Unknown')
df_clean['Size'] = df_clean['Size'].fillna('N/A')
df_clean['Total'] = df_clean['Quantity'] * df_clean['UnitPrice']
df_clean['DayOfWeek'] = pd.to_datetime(df_clean['Date']).dt.day_name()

# ==========================================
# 2. إعداد شبكة الرسومات الستة (3x2 Grid)
# ==========================================
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
fig, axes = plt.subplots(3, 2, figsize=(14, 15))
fig.suptitle('Cafe Sales Analysis - Complete 6 Plots Package', fontsize=16, fontweight='bold', y=0.98)

# Drawing 1: Total Sales by Branch
branch_sales = df_clean.groupby('Branch')['Total'].sum().reset_index()
sns.barplot(data=branch_sales, x='Branch', y='Total', ax=axes[0, 0], palette='Blues_d', hue='Branch')
axes[0, 0].set_title('1. Total Sales by Branch (SAR)', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Branch')
axes[0, 0].set_ylabel('Total Revenue')
for p in axes[0, 0].patches:
    axes[0, 0].annotate(f'{p.get_height():,.0f} SAR', (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='bottom', fontsize=9, xytext=(0, 3), textcoords='offset points')

# Drawing 2: Sales Revenue Share by Category
cat_sales = df_clean.groupby('Category')['Total'].sum()
axes[0, 1].pie(cat_sales, labels=cat_sales.index, autopct='%1.1f%%', startangle=140, 
               colors=['#3b82f6', '#ec4899', '#f59e0b'], explode=(0.04, 0.04, 0.04))
axes[0, 1].set_title('2. Sales Revenue Share by Category', fontsize=12, fontweight='bold')

# Drawing 3: Hourly Sales Trend
hourly_sales = df_clean.groupby('Hour')['Total'].sum().reset_index()
axes[1, 0].plot(hourly_sales['Hour'], hourly_sales['Total'], marker='o', linewidth=2, color='#2563eb')
axes[1, 0].fill_between(hourly_sales['Hour'], hourly_sales['Total'], alpha=0.2, color='#2563eb')
axes[1, 0].set_title('3. Hourly Sales Pattern (Peak Hours)', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Hour of Day (24h)')
axes[1, 0].set_ylabel('Total Revenue')

# Drawing 4: Top 5 Best Selling Items
item_sales = df_clean.groupby('Item')['Total'].sum().sort_values(ascending=False).head(5).reset_index()
sns.barplot(data=item_sales, y='Item', x='Total', ax=axes[1, 1], palette='Purples_r', hue='Item')
axes[1, 1].set_title('4. Top 5 Best Selling Items (Revenue)', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Total Revenue (SAR)')
axes[1, 1].set_ylabel('Item')

# Drawing 5: Sales by Day of Week
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_sales = df_clean.groupby('DayOfWeek')['Total'].sum().reindex(day_order).reset_index()
sns.barplot(data=day_sales, x='DayOfWeek', y='Total', ax=axes[2, 0], palette='crest', hue='DayOfWeek')
axes[2, 0].set_title('5. Total Sales by Day of Week', fontsize=12, fontweight='bold')
axes[2, 0].set_xlabel('Day')
axes[2, 0].set_ylabel('Total Revenue')
axes[2, 0].tick_params(axis='x', rotation=30)

# Drawing 6: Correlation Heatmap
corr_matrix = df_clean[['Quantity', 'UnitPrice', 'Total', 'Hour']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='Blues', fmt='.2f', ax=axes[2, 1], cbar=False, linewidths=0.5)
axes[2, 1].set_title('6. Correlation Heatmap (Numerical Features)', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('cafe_project_6_visuals.png', dpi=200)
plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. قراءة وتنظيف البيانات
# ==========================================
file_path = 'cafe_sales.csv.xlsx'
df = pd.read_excel(file_path)

df_clean = df.drop_duplicates(subset=['OrderID']).copy()
df_clean['Category'] = df_clean['Category'].astype(str).str.strip().str.capitalize()
df_clean.loc[df_clean['UnitPrice'] == 160, 'UnitPrice'] = 16
df_clean['Quantity'] = df_clean['Quantity'].fillna(df_clean['Quantity'].median())
df_clean['Payment'] = df_clean['Payment'].fillna('Unknown')
df_clean['Size'] = df_clean['Size'].fillna('N/A')
df_clean['Total'] = df_clean['Quantity'] * df_clean['UnitPrice']
df_clean['DayOfWeek'] = pd.to_datetime(df_clean['Date']).dt.day_name()

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'

# ==========================================
# 1. الرسم الأول: إجمالي المبيعات لكل فرع
# ==========================================
plt.figure(figsize=(8, 5))
branch_sales = df_clean.groupby('Branch')['Total'].sum().reset_index()
ax1 = sns.barplot(data=branch_sales, x='Branch', y='Total', palette='Blues_d', hue='Branch')
plt.title('1. Total Sales by Branch (SAR)', fontsize=14, fontweight='bold')
plt.xlabel('Branch', fontsize=11)
plt.ylabel('Total Revenue (SAR)', fontsize=11)

for p in ax1.patches:
    ax1.annotate(f'{p.get_height():,.0f} SAR', (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha='center', va='bottom', fontsize=10, xytext=(0, 5), textcoords='offset points')

plt.tight_layout()
plt.savefig('plot1_sales_by_branch.png', dpi=200)
plt.show()

# ==========================================
# 2. الرسم الثاني: نسبة المبيعات حسب الفئة
# ==========================================
plt.figure(figsize=(7, 6))
cat_sales = df_clean.groupby('Category')['Total'].sum()
plt.pie(cat_sales, labels=cat_sales.index, autopct='%1.1f%%', startangle=140, 
        colors=['#3b82f6', '#ec4899', '#f59e0b'], explode=(0.04, 0.04, 0.04),
        textprops={'fontsize': 11, 'weight': 'bold'})
plt.title('2. Sales Revenue Share by Category', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('plot2_category_share.png', dpi=200)
plt.show()

# ==========================================
# 3. الرسم الثالث: نمط المبيعات حسب الساعات
# ==========================================
plt.figure(figsize=(9, 5))
hourly_sales = df_clean.groupby('Hour')['Total'].sum().reset_index()
plt.plot(hourly_sales['Hour'], hourly_sales['Total'], marker='o', linewidth=2.5, color='#2563eb')
plt.fill_between(hourly_sales['Hour'], hourly_sales['Total'], alpha=0.2, color='#2563eb')
plt.title('3. Hourly Sales Pattern (Peak Hours)', fontsize=14, fontweight='bold')
plt.xlabel('Hour of Day (24h)', fontsize=11)
plt.ylabel('Total Revenue (SAR)', fontsize=11)
plt.xticks(range(6, 24))
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('plot3_hourly_sales.png', dpi=200)
plt.show()

# ==========================================
# 4. الرسم الرابع: أعلى 5 منتجات مبيعاً
# ==========================================
plt.figure(figsize=(9, 5))
item_sales = df_clean.groupby('Item')['Total'].sum().sort_values(ascending=False).head(5).reset_index()
sns.barplot(data=item_sales, y='Item', x='Total', palette='Purples_r', hue='Item')
plt.title('4. Top 5 Best Selling Items (Revenue)', fontsize=14, fontweight='bold')
plt.xlabel('Total Revenue (SAR)', fontsize=11)
plt.ylabel('Item', fontsize=11)

plt.tight_layout()
plt.savefig('plot4_top_items.png', dpi=200)
plt.show()

# ==========================================
# 5. الرسم الخامس: المبيعات حسب أيام الأسبوع
# ==========================================
plt.figure(figsize=(9, 5))
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_sales = df_clean.groupby('DayOfWeek')['Total'].sum().reindex(day_order).reset_index()
sns.barplot(data=day_sales, x='DayOfWeek', y='Total', palette='crest', hue='DayOfWeek')
plt.title('5. Total Sales by Day of Week', fontsize=14, fontweight='bold')
plt.xlabel('Day of Week', fontsize=11)
plt.ylabel('Total Revenue (SAR)', fontsize=11)
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig('plot5_sales_by_day.png', dpi=200)
plt.show()

# ==========================================
# 6. الرسم السادس: الخريطة الحرارية للارتباط (Heatmap)
# ==========================================
plt.figure(figsize=(7, 6))
corr_matrix = df_clean[['Quantity', 'UnitPrice', 'Total', 'Hour']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='Blues', fmt='.2f', cbar=True, linewidths=0.5)
plt.title('6. Correlation Heatmap (Numerical Features)', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('plot6_correlation_heatmap.png', dpi=200)
plt.show()

print("تم عرض وحفظ كافة الرسومات البيانية الستة بنجاح كملفات مستقلة!")
import pandas as pd
import numpy as np

# ==========================================
# 1. قراءة وتنظيف البيانات
# ==========================================
file_path = 'cafe_sales.csv.xlsx'
df = pd.read_excel(file_path)

df_clean = df.drop_duplicates(subset=['OrderID']).copy()
df_clean['Category'] = df_clean['Category'].astype(str).str.strip().str.capitalize()
df_clean.loc[df_clean['UnitPrice'] == 160, 'UnitPrice'] = 16
df_clean['Quantity'] = df_clean['Quantity'].fillna(df_clean['Quantity'].median())
df_clean['Payment'] = df_clean['Payment'].fillna('Unknown')
df_clean['Size'] = df_clean['Size'].fillna('N/A')
df_clean['Total'] = df_clean['Quantity'] * df_clean['UnitPrice']
df_clean['DayOfWeek'] = pd.to_datetime(df_clean['Date']).dt.day_name()

# ==========================================
# 2. التحليلات الإحصائية التفصيلية (مثل الملف الأول)
# ==========================================
print("==========================================")
print("=== 1. الملخص الإحصائي الكامل (Describe) ===")
print("==========================================")
print(df_clean[['Quantity', 'UnitPrice', 'Total']].describe().round(2))

print("\n==========================================")
print("=== 2. تفاصيل أداء المنتجات (Product Performance) ===")
print("==========================================")
product_summary = df_clean.groupby('Item').agg(
    إجمالي_المبيعات=('Total', 'sum'),
    الكمية_المباعة=('Quantity', 'sum'),
    عدد_الطلبات=('OrderID', 'count'),
    متوسط_سعر_الوحدة=('UnitPrice', 'mean')
).sort_values(by='إجمالي_المبيعات', ascending=False)
print(product_summary)

print("\n==========================================")
print("=== 3. توزيع الطلبات حسب الأحجام (Size Distribution) ===")
print("==========================================")
print(df_clean['Size'].value_counts())

print("\n==========================================")
print("=== 4. المبيعات حسب الفرع والفئة (Branch x Category) ===")
print("==========================================")
branch_cat = pd.crosstab(df_clean['Branch'], df_clean['Category'], values=df_clean['Total'], aggfunc='sum')
print(branch_cat)

print("\n==========================================")
print("=== 5. خلاصة نتائج المشروع بالأرقام ===")
print("==========================================")
print(f"إجمالي مبيعات المقهى الكلية: {df_clean['Total'].sum():,.2f} ريال")
print(f"إجمالي عدد الطلبات بعد التنظيف: {len(df_clean)} طلب")
print(f"متوسط قيمة الطلب الواحد: {df_clean['Total'].mean():,.2f} ريال")