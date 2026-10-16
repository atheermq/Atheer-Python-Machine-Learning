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
# ==========================================
#  User Input (038 - 040)
# ==========================================
# --- التكليف 01 ---
print("=== التكليف 01 ===")
name = input("Enter Name: ").strip().capitalize()
print(f'"Hello {name}, Happy To See You Here."')

# --- التكليف 02 ---
print("\n=== التكليف 02 ===")
age = int(input("Enter Age: "))

if age < 16:
    print('"Hello Your Age Is Under 16, Some Articles Is Not Suitable For You"')
else:
    print(f'"Hello Your Age Is {age}, All Articles Is Suitable For You"')


# --- التكليف 03 ---
print("\n=== التكليف 03 ===")
first_name = input("First Name: ").strip().capitalize()
second_name = input("Second Name: ").strip().capitalize()

print(f'"Hello {first_name} {second_name[0]}."')

# --- التكليف 04 ---
print("\n=== التكليف 04 ===")
email = input("Enter Email: ").strip().lower()

name = email[:email.index("@")].capitalize()
provider = email[email.index("@") + 1 : email.index(".")]
tld = email[email.index(".") + 1 :]

print(f'"Your Name Is {name}"')
print(f'"Email Service Provider Is {provider}"')
print(f'"Top Level Domain Is {tld}"')
# ==========================================
#Control Flow (041 - 046)
# ==========================================

# --- التكليف 01 ---
print("=== التكليف 01 ===")
num1 = int(input("Num1: ").strip())
num2 = int(input("Num2: ").strip())
operation = input("Operation (+, -, *, /, %): ").strip()

if operation == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
elif operation == "%":
    print(f"{num1} % {num2} = {num1 % num2}")


# --- التكليف 02 ---
print("\n=== التكليف 02 ===")
age = 17
print("App Is Suitable For You" if age > 16 else "App Is Not Suitable For You")

# --- التكليف 03 ---
print("\n=== التكليف 03 ===")
age = int(input("Enter Age: "))

if 10 < age < 100:
    months = age * 12
    weeks = months * 4
    days = age * 365
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    print(f'"Your Age In Months Is {months} Months"')
    print(f'"Your Age In Weeks Is {weeks} Weeks"')
    print(f'"Your Age In Days Is {days} Days"')
    print(f'"Your Age In Hours Is {hours} Hours"')
    print(f'"Your Age In Minutes Is {minutes} Minutes"')
    print(f'"Your Age In Seconds Is {seconds} Seconds"')
else:
    print("Age Is Out Of Range")

# --- التكليف 04 ---
print("\n=== التكليف 04 ===")
country = input("Input Your Country: ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "Ksa", "Saudi arabia"]
price = 100
discount = 30

if country in countries:
    print(f'"Your Country Eligible For Discount And The Price After Discount Is ${price - discount}"')
else:
    print(f'"Your Country Not Eligible For Discount And The Price Is ${price}"')

 # ==========================================
#  Loop While (047 - 050)
# ==========================================

# --- التكليف 01 ---
print("=== التكليف 01 ===")
num = int(input("Enter Number: "))

if num <= 0:
    print("Number Is Not Larger Than 0")
else:
    count = 0
    current = num - 1
    while current > 0:
        if current != 6:
            print(current)
            count += 1
        current -= 1
    print(f'"{count} Numbers Printed Successfully."')

# --- التكليف 02 ---
print("\n=== التكليف 02 ===")
friends = ["Atheer Alqahtani", "Shady", "ahmed", "eman", "Sherif"]

index = 0
ignored_count = 0

while index < len(friends):
    if friends[index][0].isupper():
        print(f'"{friends[index]}"')
    else:
        ignored_count += 1
    index += 1

print(f'"Friends Printed And Ignored Names Count Is {ignored_count}"')

# --- التكليف 03 ---
print("\n=== التكليف 03 ===")
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:
    print(f'"{skills.pop(0)}"')

# --- التكليف 04 ---
print("\n=== التكليف 04 ===")
my_friends = []
max_friends = 4

while len(my_friends) < max_friends:
    name = input("Enter Name: ").strip()
    
    if name.isupper():
        print("Invalid Name")
    elif name.islower():
        name_cap = name.capitalize()
        my_friends.append(name_cap)
        print(f'"Friend {name} Added => 1st Letter Become Capital"')
        print(f'"Names Left in List Is {max_friends - len(my_friends)}"')
    else:
        my_friends.append(name)
        print(f'"Friend {name} Added"')
        print(f'"Names Left in List Is {max_friends - len(my_friends)}"')

  # ==========================================
# Loop For (051 - 055)
# ==========================================

# --- التكليف 01 ---
print("=== التكليف 01 ===")
my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort(reverse=True)

count = 1
for num in my_nums:
    if num % 5 == 0:
        print(f'"{count} => {num}"')
        count += 1

print('"All Numbers Printed"')


# --- التكليف 02 ---
print("\n=== التكليف 02 ===")
for i in range(1, 21):
    if i in [6, 8, 12]:
        continue
    print(f'"{str(i).zfill(2)}"')

print('"All Numbers Printed"')


# --- التكليف 03 ---
print("\n=== التكليف 03 ===")
my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}

rank_points = {'A': 100, 'B': 80, 'C': 40}
total_points = 0

for subject, rank in my_ranks.items():
    points = rank_points[rank]
    total_points += points
    print(f'"My Rank in {subject} Is {rank} And This Equal {points} Points"')

print(f'"Total Points Is {total_points}"')


# --- التكليف 04 ---
print("\n=== التكليف 04 ===")
students = {
    "Atheer Alqahtani": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}

points_map = {"A": 100, "B": 80, "C": 40, "D": 20}

for student, subjects in students.items():
    print(f'"-- Student Name => {student}"')
    total = 0
    for subject, rank in subjects.items():
        pts = points_map[rank]
        total += pts
        print(f'"- {subject} => {pts} Points"')
    print(f'"Total Points For {student} Is {total}"')