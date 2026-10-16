"""
This is a multiple line comment
Describing the Python assignments from 01 to 05
Elzero Web School - Python Course
"""

# التكليف 02: إنشاء المتغيرات ببياناتك الخاصة
name = "Atheer Alqahtani"
age = "30"
country = "Saudi Arabia"

# التكليف 03: طباعة القيم في 3 أسطر
print(f'"Name: {name}"')
print(f'"Age: {age}"')
print(f'"Country: {country}"')

# التكليف 04: دمج المتغيرات (Concatenation) لطباعة الرسالة
print('"Hello, My Name Is ' + name + ' And My Age Is ' + age + ' And My Country Is ' + country + '"')

# التكليف 05: طباعة نوع كل متغير في سطر منفصل
print(type(name))
print(type(age))
print(type(country))
# ==========================================
# المجموعة الثانية: Strings And Methods
# ==========================================

# --- التكليف 01 ---
name = "Atheer Alqahtani"
age = "38"
country = "Egypt"

print('"Hello \'' + name + '\', How You Doing \\\n""" Your Age Is "' + age + '"" +\nAnd Your Country Is: ' + country)


# --- التكليف 02 ---
print(f""""Hello '{name}', How You Doing \\
""\" Your Age Is "{age}"" +
And Your Country Is: {country}""")


# --- التكليف 03 ---
name_03 = 'Atheer Alqahtani'
print(f'Second Letter Is "{name_03[1]}"')
print(f'Third Letter Is "{name_03[2]}"')
print(f'Last Letter Is "{name_03[-1]}"')


# --- التكليف 04 ---
name_04 = 'Atheer Alqahtani'
print('"' + name_04[1:4] + '"')
print('"' + name_04[0::2] + '"')
print('"' + name_04[-2::-2] + '"')


# --- التكليف 05 ---
name_05 = "#@#@Atheer Alqahtani#@#@"
print(name_05.strip("#@"))


# --- التكليف 06 ---
print("9".zfill(4))
print("15".zfill(4))
print("130".zfill(4))
print("950".zfill(4))
print("1500".zfill(4))


# --- التكليف 07 ---
name_one = "Atheer"
name_two = "Atheer_Alqahtani"
print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))


# --- التكليف 08 ---
name_one_08 = "ATheeR"
name_two_08 = "atHEEr"
print(name_one_08.swapcase())
print(name_two_08.swapcase())


# --- التكليف 09 ---
msg_09 = "I Love Python And Although Love Atheer Alqahtani Web School"
print(msg_09.count("Love"))


# --- التكليف 10 ---
name_10 = "Atheer Alqahtani"
print(name_10.index("h"))


# --- التكليف 11 ---
msg_11 = "I <3 Python And Although <3 Atheer Alqahtani Web School"
print(msg_11.replace("<3", "Love", 1))


# --- التكليف 12 ---
msg_12 = "I <3 Python And Although <3 Atheer Alqahtani Web School"
print(msg_12.replace("<3", "Love"))


# --- التكليف 13 ---
name_user = "Atheer Alqahtani"
age_user = 30
country_user = "Saudi Arabia"
print(f"My Name Is {name_user}, And My Age Is {age_user}, And My Country Is {country_user}")
# ==========================================
# المجموعة الثالثة: Numbers
# ==========================================

# --- التكليف 01 ---
print(type(100))    # Integer
print(type(100.5))  # Float
print(type(1+2j))   # Complex


# --- التكليف 02 ---
complex_num = 1+2j
print(complex_num.imag) # الجزء التخيلي
print(complex_num.real) # الجزء الحقيقي


# --- التكليف 03 ---
num_03 = 10
print(f"{float(num_03):.10f}")


# --- التكليف 04 ---
num_04 = 159.650
int_num = int(num_04)
print(int_num)
print(type(int_num))


# --- التكليف 05 ---
print(100 - 115)  # -15
print(50 * 30)    # 1500
print(21 % 4)     # 1
print(110 // 11)  # 10
print(97 // 20)   # 4