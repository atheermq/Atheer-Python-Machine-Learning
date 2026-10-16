import pandas as pd
import numpy as np

# ==========================================
# 1. قراءة واستكشاف البيانات
# ==========================================
file_path = 'cafe_sales.csv.xlsx'
df = pd.read_excel(file_path)

print("=== 1. فحص الجودة والنظرة الأولى ===")
print("حجم البيانات (صفوف، أعمدة):", df.shape)
print("عدد الصفوف المكررة:", df.duplicated(subset=['OrderID']).sum())
print("\nالقيم المفقودة لكل عمود:")
print(df.isnull().sum())

# ==========================================
# 2. تنظيف البيانات وتوثيق القرارات
# ==========================================
df_clean = df.copy()

# قرار 1: حذف الصفوف المكررة
df_clean = df_clean.drop_duplicates(subset=['OrderID']).copy()

# قرار 2: توحيد صياغة الفئات (Category)
df_clean['Category'] = df_clean['Category'].astype(str).str.strip().str.capitalize()

# قرار 3: تصحيح سعر الوحدة الشاذ (160 -> 16)
df_clean.loc[df_clean['UnitPrice'] == 160, 'UnitPrice'] = 16

# قرار 4: معالجة الكميات المفقودة (استبدال بالوسيط 1.0)
df_clean['Quantity'] = df_clean['Quantity'].fillna(df_clean['Quantity'].median())

# قرار 5: معالجة وسيلة الدفع المفقودة (استبدال بـ Unknown)
df_clean['Payment'] = df_clean['Payment'].fillna('Unknown')

# قرار 6: معالجة الأحجام المفقودة للحلويات (استبدال بـ N/A)
df_clean['Size'] = df_clean['Size'].fillna('N/A')

# قرار 7: إنشاء عمود إجمالي المبيعات (Total = Quantity * UnitPrice)
df_clean['Total'] = df_clean['Quantity'] * df_clean['UnitPrice']

# حفظ الملف النظيف
df_clean.to_csv('cafe_sales_clean.csv', index=False)
print("\nتم حفظ البيانات المنظفة بنجاح باسم: cafe_sales_clean.csv")

# ==========================================
# 3. نتائج التحليل والإجابة على الأسئلة
# ==========================================
print("\n==========================================")
print("=== 3. نتائج الإجابة على الأسئلة التحليلية ===")
print("==========================================")

# س1: أكثر ساعات اليوم مبيعاً؟
hourly = df_clean.groupby('Hour')['Total'].sum().sort_values(ascending=False)
print("\n1. أعلى 3 ساعات مبيعاً في اليوم:")
print(hourly.head(3))

# س2: أعلى فئة في المبيعات؟
cat_sales = df_clean.groupby('Category')['Total'].sum().sort_values(ascending=False)
print("\n2. إجمالي المبيعات حسب الفئة (Cold / Dessert / Hot):")
print(cat_sales)

# س3: الفرع صاحب أعلى متوسط طلب؟
branch_avg = df_clean.groupby('Branch')['Total'].mean().sort_values(ascending=False)
print("\n3. متوسط قيمة الطلب لكل فرع (ريال):")
print(branch_avg.round(2))

# س4: تفضيلات طرق الدفع بين الفروع؟
payment_dist = pd.crosstab(df_clean['Branch'], df_clean['Payment'], normalize='index') * 100
print("\n4. نسبة استخدام طرق الدفع لكل فرع (%):")
print(payment_dist.round(2))

# س5: أفضل يوم في الأسبوع؟
df_clean['DayOfWeek'] = df_clean['Date'].dt.day_name()
day_sales = df_clean.groupby('DayOfWeek')['Total'].sum().sort_values(ascending=False)
print("\n5. إجمالي المبيعات حسب أيام الأسبوع:")
print(day_sales)
import pandas as pd
import numpy as np

# ==========================================
# 1. قراءة البيانات بأمان
# ==========================================
file_path = 'cafe_sales.csv.xlsx'

try:
    df = pd.read_excel(file_path)
except PermissionError:
    print("⚠️ تنبيه: ملف الإكسل مفتوح حالياً في برنامج آخر، جاري المحاولة مرة أخرى...")
    import shutil
    shutil.copyfile(file_path, 'temp_cafe_sales.xlsx')
    df = pd.read_excel('temp_cafe_sales.xlsx')

print("=== 1. فحص الجودة والنظرة الأولى ===")
print("حجم البيانات (صفوف، أعمدة):", df.shape)
print("عدد الصفوف المكررة:", df.duplicated(subset=['OrderID']).sum())
print("\nالقيم المفقودة لكل عمود:")
print(df.isnull().sum())

# ==========================================
# 2. تنظيف البيانات وتوثيق القرارات
# ==========================================
df_clean = df.copy()

# قرار 1: حذف الصفوف المكررة
df_clean = df_clean.drop_duplicates(subset=['OrderID']).copy()

# قرار 2: توحيد صياغة الفئات (Category)
df_clean['Category'] = df_clean['Category'].astype(str).str.strip().str.capitalize()

# قرار 3: تصحيح سعر الوحدة الشاذ (160 -> 16)
df_clean.loc[df_clean['UnitPrice'] == 160, 'UnitPrice'] = 16

# قرار 4: معالجة الكميات المفقودة (استبدال بالوسيط 1.0)
df_clean['Quantity'] = df_clean['Quantity'].fillna(df_clean['Quantity'].median())

# قرار 5: معالجة وسيلة الدفع المفقودة (استبدال بـ Unknown)
df_clean['Payment'] = df_clean['Payment'].fillna('Unknown')

# قرار 6: معالجة الأحجام المفقودة للحلويات (استبدال بـ N/A)
df_clean['Size'] = df_clean['Size'].fillna('N/A')

# قرار 7: إنشاء عمود إجمالي المبيعات (Total = Quantity * UnitPrice)
df_clean['Total'] = df_clean['Quantity'] * df_clean['UnitPrice']

# حفظ الملف النظيف
df_clean.to_csv('cafe_sales_clean.csv', index=False)
print("\nتم حفظ البيانات المنظفة بنجاح باسم: cafe_sales_clean.csv")

# ==========================================
# 3. نتائج التحليل والإجابة على الأسئلة
# ==========================================
print("\n==========================================")
print("=== 3. نتائج الإجابة على الأسئلة التحليلية ===")
print("==========================================")

# س1: أكثر ساعات اليوم مبيعاً؟
hourly = df_clean.groupby('Hour')['Total'].sum().sort_values(ascending=False)
print("\n1. أعلى 3 ساعات مبيعاً في اليوم:")
print(hourly.head(3))

# س2: أعلى فئة في المبيعات؟
cat_sales = df_clean.groupby('Category')['Total'].sum().sort_values(ascending=False)
print("\n2. إجمالي المبيعات حسب الفئة (Cold / Dessert / Hot):")
print(cat_sales)

# س3: الفرع صاحب أعلى متوسط طلب؟
branch_avg = df_clean.groupby('Branch')['Total'].mean().sort_values(ascending=False)
print("\n3. متوسط قيمة الطلب لكل فرع (ريال):")
print(branch_avg.round(2))

# س4: تفضيلات طرق الدفع بين الفروع؟
payment_dist = pd.crosstab(df_clean['Branch'], df_clean['Payment'], normalize='index') * 100
print("\n4. نسبة استخدام طرق الدفع لكل فرع (%):")
print(payment_dist.round(2))

# س5: أفضل يوم في الأسبوع؟
df_clean['DayOfWeek'] = df_clean['Date'].dt.day_name()
day_sales = df_clean.groupby('DayOfWeek')['Total'].sum().sort_values(ascending=False)
print("\n5. إجمالي المبيعات حسب أيام الأسبوع:")
print(day_sales)