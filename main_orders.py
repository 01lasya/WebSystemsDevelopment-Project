import json
import sys
import re

def clean_phone(phone_number):
    
    digits = re.sub(r'\D', '', phone_number)
    return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}" if len(digits) == 10 else phone_number

def parse_orders(file_path):
    
    try:
        with open(file_path, 'r') as file:
            orders = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    customer_data = {}
    item_data = {}
    
    for order in orders:
        phone = clean_phone(order.get("phone", ""))
        name = order.get("name", "Unknown")
        
        if phone:
            customer_data[phone] = name
        
        for item in order.get("items", []):
            item_name = item.get("name", "Unknown Item")
            price = item.get("price", 0)
            
            if item_name not in item_data:
                item_data[item_name] = {"price": price, "orders": 0}
            
            item_data[item_name]["orders"] += 1
    
    return customer_data, item_data

def save_to_json(filename, data):
    
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error writing to {filename}: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main_orders.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    customers, items = parse_orders(input_file)
    
    save_to_json("customers.json", customers)
    save_to_json("items.json", items)
    
    print("Both 'customers.json' and 'items.json' are updated now.")

if __name__ == "__main__":
    main()