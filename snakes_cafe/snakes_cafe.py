
def welcome_Msg():
    print('''
        ****************************************
        **    Welcome to the Snakes Cafe!   ****
        **    Please see our menu below.    ****
        **                                  ****
        ** To quit at any time, type "quit()" **
        ****************************************
    ''')

menu = {
    "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "Desserts": ["Ice Cream", "Cake", "Pie"],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"],
}

order = {}

def displayMenu(menu):
    for category in menu:
        print(f"\n{category}\n{'-'*10}\n")
        for item in menu[category]:
            print(item)
            print("")

    print("""
         ***********************************
         ** What would you like to order? **
         ***********************************
        """)


# display Orders and count them 
def displayOrders(order):
    print("\nYour order is:\n")
    for item, count in order.items():
        print(f"{count} order of {item}")
    print("")


def user_input():
    user_input = input("> ")
    word = user_input.split(" ")
    for i in range(len(word)):
        word[i] = word[i].title()
    user_input = " ".join(word)
    return user_input


def main():
    customer_order = user_input()
    while customer_order != "Quit":
        if any(customer_order in values for values in menu.values()):
            if customer_order in order:
                order[customer_order] += 1
            else:
                order[customer_order] = 1
            print(f"** {order[customer_order]} order of {customer_order} has been added to your meal **")
            displayOrders(order)
        else:
            print("Sorry, we don't have this item!")

        customer_order = user_input()

    end_application()


def end_application():
    print("Thanks for using the Snakes Cafe application!")



# Functions # 
welcome_Msg()
displayMenu(menu)
main()
