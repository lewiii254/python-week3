def calculate_discount(price, discount_percent):

    return price - (price * discount_percent / 100) if discount_percent >= 20 else price

# Prompt the user for input
price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount)

# Print the result
print(f"The final price is: ${final_price:.2f}")
