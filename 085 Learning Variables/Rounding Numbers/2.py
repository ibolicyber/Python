def calculate_discount(price, discount_percentage):
    discount_amount = price * discount_percentage / 100
    final_price = price - discount_amount
    return round(final_price, 2)