def calculate_discount (price, discount_percentage):

    if discount_percentage >= 20:
        discount = (discount_percentage / 100) * price
        final_price = price - discount
        return final_price
    else:
        return price
    
price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the percentage discount: "))

result = calculate_discount(price, discount_percentage)

print(f"The final price is: {result}")