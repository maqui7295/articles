welcome_message = "Hello welcome to the best restaurant ever"
question = "May we know your name and age please?"

menu = {
    "drinks": ['cokaland', 'fantaland', 'water', 'beer', 'bitters'],
    "food": ['Tuwo Shinkafa', 'Amala and Ewedu', 'Akpu and Ofe nsala', 'eba and egusi', 'rice and stew'],
    "meat": ['chicken', 'beef', 'pork', 'goat', 'turkey']
}

# {1, 2}.


name = input("Your name: ")

while len(name) <= 3:
    print("Your name should be longer than three letters")
    name = input("Your name: ")

print("Welcome {}. It's great to have you here\n".format(name))

age = input("Your age: ")

age_invalid = True

while age_invalid:
    try:
        age = int(age)
        age_invalid = False
    except:
        age = input("Please enter a valid age: ")


if age <= 18:
    print("Ooh it's nice to have a teenager here...")
elif age <= 45:
    print("Hypothetical youth, you must be having the best time of your life...")
else:
    print("Wow, chairman sir, old age is a blessing... are you like 150 years or more?")
# task, you may decide to limit the age that can enter your restaurant
print()

## Let's display the menu

categories = menu.keys()

# spread the items and use zip to transponse
items = zip(*menu.values())

# print('{}\t {}\t {}'.format(*categories))

cats = list(categories)

print('{}\t {}\t\t {}'.format(cats[0].ljust(10), cats[1].ljust(10), cats[2].ljust(1)))

for item in items:
    # print('{}\t {}\t {}'.format(*item))
    print('{}\t {}\t\t {}'.format(item[0].ljust(10), item[1].ljust(10), item[2]))