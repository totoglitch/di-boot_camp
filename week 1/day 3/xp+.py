# -*- coding: utf-8 -*-
"""xp+

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19kOFG582E1hrJnNMv9EKMBZ0wZRmR89f

Exercise 1 : Student Grade Summary
Instructions
You are given a dictionary containing student names as keys and lists of their grades as values. Your task is to create a summary report that calculates the average grade for each student, assigns a letter grade, and determines the class average.



Initial Data:


student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}


Requirements:
Calculate the average grade for each student and store the results in a new dictionary called student_averages.
Assign each student a letter grade (A, B, C, D, F) based on their average grade according to the following scale, and store the results in a dictionary called student_letter_grades:
A: 90 and above
B: 80 to 89
C: 70 to 79
D: 60 to 69
F: Below 60
Calculate the class average (the average of all students’ averages) and print it.
Print the name of each student, their average grade, and their letter grade.
Hints:
"""

# prompt: you are given a dict containing studints names as keys

student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

student_averages = {}
student_letter_grades = {}
all_averages = []

for student, grades in student_grades.items():
  average_grade = sum(grades) / len(grades)
  student_averages[student] = average_grade
  all_averages.append(average_grade)

  if average_grade >= 90:
    student_letter_grades[student] = "A"
  elif average_grade >= 80:
    student_letter_grades[student] = "B"
  elif average_grade >= 70:
    student_letter_grades[student] = "C"
  elif average_grade >= 60:
    student_letter_grades[student] = "D"
  else:
    student_letter_grades[student] = "F"

class_average = sum(all_averages) / len(all_averages)
print(f"Class Average: {class_average:.2f}")

for student, average_grade in student_averages.items():
  print(f"{student}: Average Grade = {average_grade:.2f}, Letter Grade = {student_letter_grades[student]}")

""" Exercise 2 : Advanced Data Manipulation and Analysis
Instructions
In this exercise, you will analyze data from a hypothetical online retail company to gain insights into sales trends and customer behavior. The data is represented as a list of dictionaries, where each dictionary contains information about a single purchase.



sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]


Tasks:
Total Sales Calculation: Calculate the total sales for each product category (i.e., the total revenue generated from each type of product). Use a loop to iterate through the data and a dictionary to store the total sales for each product.

Customer Spending Profile: Determine the total amount spent by each customer. Use a dictionary to maintain the sum of amounts each customer has spent.

Sales Data Enhancement:

Add a new field to each transaction called “total_price” that represents the total price for that transaction (quantity * price).
Use a loop to modify the sales_data list with this new information.
High-Value Transactions:

Using list comprehension, create a list of all transactions where the total price is greater than $500.
Sort this list by the total price in descending order.
Customer Loyalty Identification:

Identify any customer who has made more than one purchase, suggesting potential loyalty.
Use a dictionary to count purchases per customer, then use a loop or comprehension to identify customers meeting the loyalty criterion.
Bonus: Insights and Analysis:

Calculate the average transaction value for each product category.
Identify the most popular product based on the quantity sold.
Provide insights into how these analyses could inform the company’s marketing strategies.

"""

# prompt: analyize data from a hypothetical online retail

sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

# Total Sales Calculation
product_sales = {}
for sale in sales_data:
  product = sale["product"]
  total_price = sale["price"] * sale["quantity"]
  if product not in product_sales:
    product_sales[product] = 0
  product_sales[product] += total_price

print("Total Sales by Product:")
for product, total_sale in product_sales.items():
  print(f"{product}: ${total_sale}")


# Customer Spending Profile
customer_spending = {}
for sale in sales_data:
  customer_id = sale["customer_id"]
  total_price = sale["price"] * sale["quantity"]
  if customer_id not in customer_spending:
    customer_spending[customer_id] = 0
  customer_spending[customer_id] += total_price

print("\nCustomer Spending:")
for customer_id, total_spent in customer_spending.items():
  print(f"Customer {customer_id}: ${total_spent}")


# Sales Data Enhancement
for sale in sales_data:
  sale["total_price"] = sale["price"] * sale["quantity"]


# High-Value Transactions
high_value_transactions = [sale for sale in sales_data if sale["total_price"] > 500]
high_value_transactions.sort(key=lambda sale: sale["total_price"], reverse=True)

print("\nHigh-Value Transactions (sorted by total price):")
for transaction in high_value_transactions:
  print(transaction)


# Customer Loyalty Identification
customer_purchase_counts = {}
for sale in sales_data:
  customer_id = sale["customer_id"]
  if customer_id not in customer_purchase_counts:
    customer_purchase_counts[customer_id] = 0
  customer_purchase_counts[customer_id] += 1

loyal_customers = [customer_id for customer_id, count in customer_purchase_counts.items() if count > 1]

print("\nLoyal Customers (made more than one purchase):")
print(loyal_customers)


# Bonus: Insights and Analysis

# Average transaction value for each product category
product_average_transaction = {}
for product in product_sales:
  transactions_for_product = [sale for sale in sales_data if sale["product"] == product]
  total_transaction_value = sum([sale["total_price"] for sale in transactions_for_product])
  average_transaction_value = total_transaction_value / len(transactions_for_product) if len(transactions_for_product) > 0 else 0
  product_average_transaction[product] = average_transaction_value

print("\nAverage transaction value by product:")
for product, avg_transaction_value in product_average_transaction.items():
  print(f"{product}: ${avg_transaction_value:.2f}")


# Most popular product based on quantity sold
product_quantities = {}
for sale in sales_data:
  product = sale["product"]
  quantity = sale["quantity"]
  if product not in product_quantities:
    product_quantities[product] = 0
  product_quantities[product] += quantity

most_popular_product = max(product_quantities, key=product_quantities.get)

print("\nMost Popular Product:", most_popular_product)

# Insights into how these analyses could inform the company's marketing strategies
#  1. Customer Loyalty: Target loyal customers with promotions and exclusive offers to further increase their spending.
#  2. High-Value Transactions: Further analyze the products within these transactions to identify potential upsell or cross-sell opportunities.
#  3. Product Popularity: Run targeted marketing campaigns for popular products to maximize sales and increase revenue.
#  4. Customer Spending Profiles: Segment customers based on their spending habits to deliver personalized product recommendations.