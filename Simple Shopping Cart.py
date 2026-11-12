Customer_name = input("Customer's name: ")

Product1_name = input("Product1 name: ")
Product1_price = float(input(f"price of {Product1_name}: "))

Product2_name = input("Product2 name: ")
Product2_price = float(input(f"price of {Product2_name}: "))

Product3_name = input("Product3 name: ")
Product3_price = float(input(f"price of {Product3_name}: "))

Subtotal = Product1_price + Product2_price + Product3_price


if Subtotal >= 5000:
    discount_rate = 0.20
elif Subtotal >= 3000:
    discount_rate = 0.10
elif Subtotal >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0.0

Discount = Subtotal * discount_rate
Final_total = Subtotal - Discount 

print("Shopping Summary")
print(f"\nCustomer name: {Customer_name}: ")
print(f"\Product purchased: {Product1_name} , {Product2_name}, {Product3_name} ")
print(f"Subtotal: {Subtotal:.2f} ")
print(f"Discount ({int(discount_rate * 100)}%): {Discount:.2f}" )
print(f"Final total: {Final_total:.2f} ")