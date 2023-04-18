# Define your functions
def coffee_bot():
    print("Welcome to the cafe!")
    order_drink = 'y'
    drinks_list = []
    while order_drink == 'y':
        size = get_size()
        bev_type = get_drink_type()
        bev_temp = get_drink_temp()
        cup = pick_a_cup()
        bev = '{} {} {}'.format(size, bev_temp, bev_type)
        print("Alright, that's a {} in a {} cup!".format(bev, cup))
        drinks_list.append(bev)
        while True:
            order_drink = input("Would you like to order another drink? \n(y/n) \n> ")
            if order_drink in ['Y', 'yes', 'yeah', 'sure']:
                order_drink = 'y'
            elif order_drink in ['N', 'no', 'nah']:
                order_drink = 'n'
            if order_drink == 'y' or 'n':
                break
    print("Okay, so I have: ")        
    for bev in drinks_list:
        print("- " + bev)
    name = input("Can I get your name please? \n> ")
    if len(drinks_list) == 1:
        print("Thanks, {}! Your drink will be ready shortly.".format(name))
    elif len(drinks_list) > 1:
        print("Thanks, {}! Your drinks will be ready shortly.".format(name))

def get_size(): #using recursion
    res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ")
    if res == 'a':
        return 'small'
    elif res == 'b':
        return 'medium'
    elif res == 'c':
        return 'large'
    else:
        print_message()
        return get_size()

def print_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_drink_type(): #using recursion
    res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ")
    if res == 'a':
        return order_coffee()
    elif res == 'b':
        return order_mocha()
    elif res == 'c':
        return order_latte()
    else:
        print_message()
        return get_drink_type()

def order_latte():  #using recursion
    res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ")
    if res == 'a':
        return 'latte'
    elif res == 'b':
        return 'non-fat latte'
    elif res == 'c':
        return 'soy latte'
    else:
        print_message()
        return order_latte()

def order_coffee(): #using while loop
    while True:
        res = input("Would you like milk or sugar in your coffee? \n[a] Milk \n[b] Sugar \n[c] Both \n[d] Neither \n> ")
        if res == 'a':
            return 'brewed coffee with milk'
        elif res == 'b':
            return 'brewed coffee with sugar'
        elif res == 'c':
            return 'brewed coffee with milk and sugar'
        elif res == 'd':
            return 'black brewed coffee'
        print_message()

def order_mocha(): #using while loop
    while True:
        res = input("Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time! \n> ")
        if res == 'a':
            return 'peppermint mocha'
        elif res == 'b':
            return 'mocha'
        print_message()

def get_drink_temp(): #using while loop
    while True:
        res = input("Would you like that hot or iced? \n[a] Hot \n[b] Iced \n> ")
        if res == 'a':
            return 'hot'
        elif res == 'b':
            return 'iced'
        print_message()

def pick_a_cup(): #using while loop
    while True: 
        res = input("What type of cup would you like for your drink? \n[a] Reusable \n[b] Plastic \n> ")
        if res == 'a':
            return 'reusable'
        elif res == 'b':
            return 'plastic'
        print_message()

# Call coffee_bot()!
coffee_bot()