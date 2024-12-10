# Bryce Perron
# 12/10/24
# While Loop Practice

# Movie Tickets

visitors = []

while True:
    age = input("What is your age? (707 to quit):\n")

    if age.isdigit():

        age = int(age)
        
        if age == 707:
            break
        elif age < 3:
            visitors.append(0)
        elif age < 13:
            visitors.append(10)
        elif age > 12:
            visitors.append(15)

    else:
        print("Your age must be an integer!")

total_price = sum(visitors)
visitor_count = len(visitors)

print(f'{visitor_count} people purchased tickets for a total of ${total_price:.2f}')
print(visitors)


# Three Exits - Pizza Toppings

toppings = []
active = True

while len(toppings) < 7 and active:
    print(f'You have {len(toppings)} toppings on your pizza\nout of a maximum of 7.')
    print(f'Your toppings are {toppings}')
    topping_to_add = input('What toppings would you like to add to your pizza?\nYou cannot remove toppings so make your choice count.\n"!quit" to quit.\n')
    
    if topping_to_add == '!quit':
        active = False

    elif topping_to_add.isalpha():
        toppings.append(topping_to_add)

    else:
        print("That topping was not a topping!\nIt wasn't even a string!")

print(f'Your toppings are: {toppings}')
print(f'That\'s {len(toppings)} toppings!')
print('Your pizza will arrive in 92.523 Hours. Enjoy!')

