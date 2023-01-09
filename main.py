name = input("Hello, Welcome to Nathaniel's famous burgers! \nName please? ")
print('\nHi, %s!' % name)

def order_number(user_input):
  numbers = ["1", "2", "3", "4"]

  if user_input in numbers:
    if user_input == "1":
      print("One hamburger coming right up!")
    elif user_input == "2":
      print("One cheeseburger coming right up!")
    elif user_input == "3":
      print("One Double Hamburger coming right up!")
    elif user_input == "4":
      print("One Double Cheeseburger coming right up!")
  else:
    print('?')
user_input = input("We have the following Items: \n \n 1. Hamburger \n 2. Cheeseburger \n 3. Double Hamburger \n 4. Double Cheeseburger \n \nWhat number would you like to order? ")
order_number(user_input)