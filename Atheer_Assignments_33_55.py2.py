# ==========================================
#  Boolean Operators (033 - 037)
# ==========================================

# --- التكليف 01 ---
print("=== التكليف 01 ===")
# True Values
print(bool("Atheer Alqahtani"))
print(bool(100))
print(bool([1, 2, 3]))
print(bool(True))

# False Values
print(bool(""))
print(bool(0))
print(bool([]))
print(bool(False))


# --- التكليف 02 ---
print("\n=== التكليف 02 ===")
html = 80
css = 60
javascript = 70

print(html > 50 and css > 50 and javascript > 50)


# --- التكليف 03 ---
print("\n=== التكليف 03 ===")
num_one = 10
num_two = 20
num = 20

print(num > num_one or num > num_two)
print(num > num_one and num > num_two)


# --- التكليف 04 ---
print("\n=== التكليف 04 ===")
num_one = 10
num_two = 20

result = num_one + num_two
print(result)

exponent = result ** 3
print(exponent)

remainder = exponent % 26000
print(remainder)

division = remainder / 5
print(division)

print(str(type(str(division))))