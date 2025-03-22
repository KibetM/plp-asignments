def calculate_discount(price, discount_percent):
    if discount_percent>=20:
        discount_price = price * (discount_percent / 100)
        final_price = price - discount_price
        return f"Discounted price:{final_price}"
    else:
        return f"Original price:{price}"

user_og_price=int(input("Enter the original price:"))
user_discount_percent=int(input("Enter discount percent:"))
print(calculate_discount(user_og_price,user_discount_percent))