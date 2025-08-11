import json

def load_inventory(filename='inventory.json'):
    with open(filename, 'r') as f:
        return json.load(f)

def save_inventory(data, filename='inventory.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def select_option(options, prompt):
    print(prompt)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    while True:
        choice = input("Enter number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice) - 1
        print("Invalid choice, try again.")

def main():
    data = load_inventory()

    portions = data['mart']['portions']
    portion_names = [p['name'] for p in portions]

    # Select portion
    p_index = select_option(portion_names, "Select a portion:")
    chosen_portion = portions[p_index]

    # Select product
    products = chosen_portion['products']
    product_names = [prod['name'] for prod in products]
    pr_index = select_option(product_names, f"Select a product in '{chosen_portion['name']}':")
    chosen_product = products[pr_index]

    # Select item
    items = chosen_product['items']
    item_names = [item['name'] + f" (Count: {item['count']})" for item in items]
    it_index = select_option(item_names, f"Select an item in '{chosen_product['name']}':")
    chosen_item = items[it_index]

    # Show current count and update
    print(f"\nYou selected: {chosen_item['name']} (Current count: {chosen_item['count']})")
    if chosen_item['count'] > 0:
        chosen_item['count'] -= 1
        print(f"One '{chosen_item['name']}' purchased. New count: {chosen_item['count']}")
    else:
        print("Sorry, this item is out of stock!")
        # After you select the item (chosen_item)
    
 # Save updated inventory
    save_inventory(data)
    print("\nInventory updated and saved.")

if __name__ == "__main__":
    main()
