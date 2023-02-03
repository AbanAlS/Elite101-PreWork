import time

# Asks for the user's name
name = input("Hello, Welcome to Nathaniel's famous burgers! \nName please? ")
print('\nHi, ' + name + '!')

# Displays the menu and fills out order by number
def order_number(menu_order):
  if menu_order == "1":
    print("One hamburger coming right up!\n")
    time.sleep(2)
    print("------------------10 minutes later------------------")
    time.sleep(2)
    
  elif menu_order == "2":
    print("One cheeseburger coming right up!\n")
    time.sleep(2)
    print("------------------10 minutes later------------------")
    time.sleep(2)
    
  elif menu_order == "3":
    print("One Double Burger coming right up!\n")
    time.sleep(2)
    print("------------------10 minutes later------------------")
    time.sleep(2)
    
  elif menu_order == "4":
    print("One Double Cheeseburger coming right up!\n")
    time.sleep(2)
    print("------------------10 minutes later------------------")
    time.sleep(2)
    
  else:
    menu_order = input('Come again? ')
    order_number(menu_order)

# Checks if the order has arrived
def order_check(order_arrival):
  if order_arrival == "yes":
    print("Great! Enjoy your meal!")
  
  elif order_arrival == "no":
    print("Alright, We'll make sure the order arrives on time!\n")
    time.sleep(2)
    print("------------------10 minutes later------------------")
    time.sleep(2)
    order_remind = input("\nHello, did you recieve your order? ")
    order_reminder(order_remind)
    
  else:
    order_arrival = input('Come again? ')
    order_check(order_arrival)

# Checks about the order again
def order_reminder(order_remind):
  if order_remind == "yes":
    print("Good! Sorry for the delay...")
  elif order_remind == "no":
    print("Sorry about this. We'll process a refund as soon as possible.")
  else:
    order_remind = input("Come again? ")
    order_reminder(order_remind)

# Menu list
menu_order = input("We have the following items: \n \n 1. Hamburger \n 2. Cheeseburger \n 3. Double Hamburger \n 4. Double Cheeseburger \n \nWhat number would you like to order? ")
order_number(menu_order)

# Checks if the order has arrived
order_arrival = input("\nHi, " + name + "!\nWe're checking in for your order. Did you recieve it yet? ")
order_check(order_arrival)