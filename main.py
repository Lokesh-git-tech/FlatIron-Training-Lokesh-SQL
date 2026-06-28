# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")


# STEP 2
# Employee Number and Last Name
df_first_five = pd.read_sql("""
SELECT employeeNumber, lastName
FROM employees;
""", conn)


# STEP 3
# Last Name first, then Employee Number
df_five_reverse = pd.read_sql("""
SELECT lastName, employeeNumber
FROM employees;
""", conn)


# STEP 4
# Rename employeeNumber to ID
df_alias = pd.read_sql("""
SELECT lastName, employeeNumber AS ID
FROM employees;
""", conn)


# STEP 5
# Executive or Not Executive
df_executive = pd.read_sql("""
SELECT
CASE
    WHEN jobTitle = 'President'
      OR jobTitle = 'VP Sales'
      OR jobTitle = 'VP Marketing'
    THEN 'Executive'
    ELSE 'Not Executive'
END AS role
FROM employees;
""", conn)


# STEP 6
# Length of last names
df_name_length = pd.read_sql("""
SELECT LENGTH(lastName) AS name_length
FROM employees;
""", conn)


# STEP 7
# First two letters of job title
df_short_title = pd.read_sql("""
SELECT SUBSTR(jobTitle, 1, 2) AS short_title
FROM employees;
""", conn)


# STEP 8
# Total price of all orders
sum_total_price = pd.read_sql("""
SELECT SUM(ROUND(priceEach * quantityOrdered)) AS total_price
FROM orderDetails;
""", conn).iloc[:,0]



# STEP 9
# Day, Month, Year from orderDate
df_day_month_year = pd.read_sql("""
SELECT
    orderDate,
    strftime('%d', orderDate) AS day,
    strftime('%m', orderDate) AS month,
    strftime('%Y', orderDate) AS year
FROM orders;
""", conn)


# Close connection
conn.close()