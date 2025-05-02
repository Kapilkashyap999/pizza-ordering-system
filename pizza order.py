# Input user details
name = input("Please enter your name: ")
location = input("Please enter your location: ")
phone_number = input("Please enter your phone number: ")

print(f"Hello {name}, welcome to Domino's!")
print("We have the following pizzas available:")
print("1. Margherita")
print("2. Pepperoni")
print("3. Farmhouse Cheese Burst")
print("4. Veggie Paradise")
print("5. Paneer Tandoori Pizza")

# Input pizza choice
pizza_choice = input("Please enter your choice of pizza: ")
if pizza_choice in ["Margherita", "Pepperoni", "Farmhouse Cheese Burst", "Veggie Paradise", "Paneer Tandoori Pizza"]:
    print(f"You have ordered {pizza_choice} pizza.")
else:
    print("Invalid choice. Please select a valid pizza from the menu.")
    exit()

# Input pizza size
print("Please choose the size of the pizza:")
print("1. Small")
print("2. Medium")
print("3. Large")
size_choice = input("Please enter your choice of size: ")
if size_choice in ["Small", "Medium", "Large"]:
    print(f"You have ordered a {size_choice} pizza.")
else:
    print("Invalid choice. Please select a valid size.")
    exit()

# Input toppings
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
print("We have the following toppings available:")
for topping in available_toppings:
    print(topping)

topping_choice = input("Please enter your choice of topping: ")
if topping_choice in available_toppings:
    print(f"You have ordered {topping_choice} topping.")
else:
    print("Invalid choice. Please select a valid topping from the menu.")
    exit()

# Input drink choice
print("Please choose your drink:")
print("1. Coke")
print("2. Pepsi")
print("3. Sprite")
drink_choice = input("Please enter your choice of drink: ")
if drink_choice in ["Coke", "Pepsi", "Sprite"]:
    print(f"You have ordered {drink_choice}.")
else:
    print("Invalid choice. Please select a valid drink from the menu.")
    exit()

# Order summary
print("\nYour order has been placed successfully!")
print("Your order will be delivered to your location.")
print("Thank you for choosing Domino's!")
print("\nYour order summary:")
print(f"Name: {name}")
print(f"Location: {location}")
print(f"Phone number: {phone_number}")
print(f"Pizza: {pizza_choice}")
print(f"Size: {size_choice}")
print(f"Toppings: {topping_choice}")
print(f"Drink: {drink_choice}")
print("Total amount: $0 (Placeholder for calculation)")
print("Thank you for choosing Domino's!")