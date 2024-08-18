"""This is a reference script for learning python"""

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


# List Unpacking

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)
print(b)
print(c)
print(other)
print(d)
