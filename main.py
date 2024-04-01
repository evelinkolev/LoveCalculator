print("Love Calculator is calculating your score...")
name1 = input()
name2 = input()

names = name1 + name2
print(names)

names_lower = names.lower()
print(names_lower)

t = names_lower.count("t")
r = names_lower.count("r")
u = names_lower.count("u")
e = names_lower.count("e")

first_letter = t + r + u + e
print(first_letter)

l = names_lower.count("l")
o = names_lower.count("o")
v = names_lower.count("v")
e = names_lower.count("e")

second_letter = l + o + v + e
print(second_letter)

score = int(str(first_letter) + str(second_letter))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")