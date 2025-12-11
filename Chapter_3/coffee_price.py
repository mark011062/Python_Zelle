
def main():
    pounds_ordered = float(input("How many pounds would you like to order? "))
    coffee_cost = pounds_ordered * 15.5
    cost_to_ship = pounds_ordered * .99 + 4.50
    total_order_cost = round(coffee_cost + cost_to_ship,2)
    print(f"Your total cost is ${total_order_cost}")

main()