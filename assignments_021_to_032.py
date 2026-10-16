# ==========================================
# المجموعة الأولى: Lists (021 - 023)
# ==========================================

# --- التكليف 01 ---
friends = ["Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani"]

print(friends[0])   # Method One
print(friends[-5])  # Method Two
print(friends[4])   # Method One
print(friends[-1])  # Method Two


# --- التكليف 02 ---
friends_02 = ["Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani"]

print(friends_02[0::2]) # العناصر الفردية
print(friends_02[1::2]) # العناصر الزوجية


# --- التكليف 03 ---
friends_03 = ["Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani"]

print(friends_03[1:4])
print(friends_03[-2:])


# --- التكليف 04 ---
friends_04 = ["Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani"]

friends_04[-2:] = ["Atheer Alqahtani", "Atheer Alqahtani"]
print(friends_04)


# --- التكليف 05 ---
friends_05 = ["Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani"]

friends_05.insert(0, "Atheer Alqahtani")
print(friends_05)

friends_05.append("Atheer Alqahtani")
print(friends_05)


# --- التكليف 06 ---
friends_06 = ["Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani"]

friends_06.pop(0)
friends_06.pop(0)
print(friends_06)

friends_06.pop(-1)
print(friends_06)


# --- التكليف 07 ---
friends_07 = ["Atheer Alqahtani", "Atheer Alqahtani"]
employees = ["Atheer Alqahtani", "Atheer Alqahtani"]
school = ["Atheer Alqahtani", "Atheer Alqahtani"]

friends_07.extend(employees)
friends_07.extend(school)
print(friends_07)


# --- التكليف 08 ---
friends_08 = ["Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani"]

friends_08.sort()
print(friends_08)

friends_08.sort(reverse=True)
print(friends_08)


# --- التكليف 09 ---
friends_09 = ["Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani"]

print(len(friends_09))


# --- التكليف 10 ---
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[-1][0])  # أول إطار عمل
print(technologies[-1][-1]) # آخر إطار عمل
# ==========================================
# المجموعة الثانية: Tuples (024 - 025)
# ==========================================

# --- التكليف 01 ---
my_tuple = "Atheer Alqahtani",

print(my_tuple[0])
print(type(my_tuple))


# --- التكليف 02 ---
friends_tuple = ("Atheer Alqahtani", "Atheer Alqahtani", "Atheer Alqahtani")

friends_list = list(friends_tuple)
friends_list[0] = "Atheer Alqahtani"
friends_tuple = tuple(friends_list)

print(friends_tuple)
print(type(friends_tuple))
print(f"{len(friends_tuple)} Elements")


# --- التكليف 03 ---
nums = (1, 2, 3)
letters = ("A", "B", "C")

nums_and_letters_one = nums + letters

print(nums_and_letters_one)
print(f"{len(nums_and_letters_one)} Elements")


# --- التكليف 04 ---
my_tuple_04 = (1, 2, 3, 4)

a, b, _, c = my_tuple_04

print(a)
print(b)
print(c)
# ==========================================
# المجموعة الثالثة: Set & Dictionary (026 - 032)
# ==========================================

# --- التكليف 01 ---
my_list = [1, 2, 3, 3, 4, 5]

unique_list = list(set(my_list))

print(unique_list)
print(type(unique_list))
print(unique_list[:-1])


# --- التكليف 02 ---
nums_set = {1, 2, 3}
letters_set = {"A", "B", "C"}

# الطريقة الأولى
print(nums_set.union(letters_set))

# الطريقة الثانية
print(nums_set | letters_set)

# الطريقة الثالثة
nums_set_copy = nums_set.copy()
nums_set_copy.update(letters_set)
print(nums_set_copy)


# --- التكليف 03 ---
my_set = {1, 2, 3}
print(my_set)

my_set.clear()
print(my_set)

my_set.add("A")
my_set.add("B")
print(my_set)

my_set.discard("C") # إزالة العنصر بدون إخراج خطأ إذا كان غير موجود


# --- التكليف 04 ---
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two))


# --- التكليف 05 (Dictionary) ---
skills = {
    "HTML": "90%",
    "CSS": "80%",
    "Python": "30%"
}

print(f"HTML Progress Is {skills['HTML']}")
print(f"CSS Progress Is {skills['CSS']}")
print(f"Python Progress Is {skills['Python']}")

skills["AI"] = "20%"

print(f"AI Progress Is {skills['AI']}")