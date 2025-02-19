#1: Write a function called count_vowels(input)
#Function
def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

#Example Usage
result = count_vowels("AMM Olympic College")
print(result)

#2: Palindrome
#Function
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

# Example usage
print(is_palindrome("Racecar"))
print(is_palindrome("Olympic"))

#3: Pokemon
#Function
def type_advantage(attacker, defender):
    effectiveness = {
        ("Water", "Fire"): "Super Effective",
        ("Fire", "Water"): "Not Very Effective",
        ("Electric", "Grass"): "Neutral"
    }

    return effectiveness.get((attacker, defender), "Neutral")

#Effectiveness Against Different Pokemon
print(type_advantage("Water", "Fire"))  # "Super Effective"
print(type_advantage("Fire", "Water"))  # "Not Very Effective"
print(type_advantage("Electric", "Grass"))  # "Neutral"

#4: Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare
#Function
def ferry_fare(age, vehicle):
    if age < 0:
        return "Invalid age"
    elif age <= 18:
        return "Free"
    elif 19 <= age <= 64:
        return 20 if vehicle else 10
    else:  # age >= 65
        return 15 if vehicle else 5

# Example usage
age = 30
vehicle = True
print(f"Age: {age}, Vehicle: {'Yes' if vehicle else 'No'}, Fare: ${ferry_fare(age, vehicle)}")

age = 70
vehicle = False
print(f"Age: {age}, Vehicle: {'Yes' if vehicle else 'No'}, Fare: ${ferry_fare(age, vehicle)}")

age = 10
vehicle = False
print(f"Age: {age}, Vehicle: {'Yes' if vehicle else 'No'}, Fare: ${ferry_fare(age, vehicle)}")

#5: Write a function called level_up(experience)
#Function
def level_up(experience):
    if experience < 100:
        return 1
    elif experience < 200:
        return 2
    else:
        return 3

# Example usage
experience_points = int(input("Enter your experience points: "))
new_level = level_up(experience_points)
print(f"Your new level is: {new_level}")
