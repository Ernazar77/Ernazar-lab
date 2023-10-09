package_grams = int(input(" in grams: "))

shipping_cost = 0

if package_grams <= 200:
    shipping_cost = 150
elif package_grams <= 600:
    shipping_cost = 300
elif package_grams <= 1000:
    shipping_cost = 400
else:
    shipping_cost = 475

# Display the calculated shipping cost
print(f"The shipping cost for a {package_grams} gram package is {shipping_cost} tenge.")