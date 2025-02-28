# WebSystemsDevelopment(IS601) - Midterm Project

## About This Project: -
This project is designed to process order details from a JSON file and generate two new files:

customers.json – A list of unique customers with their phone numbers.
items.json – A breakdown of items ordered, including their prices and the number of times they were purchased.

## What This Python Script Does
1. Reads order details from example_orders.json file.
2. Extracts customer information while ensuring no duplicates.
3. Collect item data, calculating how often each item was ordered.
4. Saves the processed data into structured JSON files for easy access.

## Requirements: -
1. Python 3.13.2

## How to Use: -
1. Make sure you have an IDE (e.g, VS Code) installed in your system with Python installed.
2. Place the script in your project folder.
3. Ensure the JSON file with order details (e.g., example_orders.json) is in the correct directory.
4. Open a terminal, navigate to the script’s location, and run command: - python main_orders.py example_orders.json

This will generate the customers.json and items.json files based on the order data.
