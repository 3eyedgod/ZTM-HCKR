
"""Module providing a function printing python version."""
# Lists

li = [1, 2, 3, 4, 5]
li2 = ["a", "b", "c"]
li3 = [1, 2, "a", True]

# Data Structure

amazon_cart = ["notebooks", "sunglasses", "iphone", "knife", "wallet"]
print(amazon_cart[0])
print(amazon_cart[1])

# List Slicing

amazon_cart = ["notebooks", "sunglasses", "iphone", "knife", "wallet"]
print(amazon_cart[0:3:2])
amazon_cart[0] = "laptop"
print(amazon_cart)
new_cart = amazon_cart[:]
new_cart[0] = "gum"
print(new_cart)
print(amazon_cart)
